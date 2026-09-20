"""Validate artifacts; this is not an agent-behavior benchmark."""
import argparse
import ipaddress
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "SKILL.md", "INVOKE.md", "CHANGELOG.md", "CONTRIBUTING.md", "UNLICENSE",
    "RELEASE_NOTES.md", "references/core.md", "references/state.md",
    "references/test-cases.md", "references/model-impact.md",
    "references/hypothesis-gate.md", "references/model-staleness.md",
    "references/model-duplication.md", "references/state-ownership.md",
    "references/decision-cost.md", "references/pilot-evidence.md",
    "examples/database-saturation.md", "examples/worker-saturation.md",
    "examples/stale-model.md", "examples/architecture-overfit.md",
    "tests/README.md", "tests/cases.json", "scripts/case_prompt.py",
)
TAGS = {"triggers", "falsification", "staleness", "duplication", "ownership", "decision_cost"}
SKIP = {".git", "__pycache__", ".venv"}
SECRET_PATTERNS = (
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b"),
    re.compile(r"\bAKIA[A-Z0-9]{16}\b"),
    re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?im)^\s*(?:password|api[_-]?key|access[_-]?token)\s*[:=]\s*[\"']?[A-Za-z0-9_+/=-]{12,}"),
)


def sensitive_findings(text):
    """Return categories only, never matched sensitive values."""
    found = set()
    if any(pattern.search(text) for pattern in SECRET_PATTERNS):
        found.add("possible credential")
    if re.search(r"(?i)\b[A-Z]:[\\/]", text) or re.search(r"\\\\[A-Za-z0-9_-]+\\", text):
        found.add("machine-specific absolute path")
    for candidate in re.findall(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])", text):
        try:
            address = ipaddress.ip_address(candidate)
            networks = ((0x0A000000, 8), (0xAC100000, 12), (0xC0A80000, 16),
                        (0x7F000000, 8), (0xA9FE0000, 16))
            if any(address in ipaddress.ip_network(net) for net in networks):
                found.add("private or local network address")
        except ValueError:
            pass
    for candidate in re.findall(r"https?://[^\s<>)\"']+", text):
        try:
            parsed = urlsplit(candidate)
            hostname = parsed.hostname or ""
            if parsed.username is not None or parsed.password is not None:
                found.add("URL credentials")
            if hostname == "localhost" or hostname.endswith((".internal", ".local", ".corp")):
                found.add("internal URL")
            try:
                address = ipaddress.ip_address(hostname)
                if address.version == 6 and (address.is_private or address.is_loopback or address.is_link_local):
                    found.add("private or local network address")
            except ValueError:
                pass
        except ValueError:
            found.add("malformed URL")
    return sorted(found)


def markdown_link_errors(path, root):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"(?ms)^[ \t]*\x60{3}.*?^[ \t]*\x60{3}[ \t]*$", "", text)
    errors = []
    for target in re.findall(r"!?\[[^\]]*\]\(([^)\n]+)\)", text):
        target = target.strip().strip("<>")
        if target.startswith("#"):
            continue
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            if parsed.scheme not in {"http", "https", "mailto"}:
                errors.append(f"{path.relative_to(root)}: unsupported link scheme")
            continue
        destination = (path.parent / unquote(parsed.path)).resolve()
        if not destination.is_relative_to(root.resolve()):
            errors.append(f"{path.relative_to(root)}: relative link escapes package")
        elif not destination.exists():
            errors.append(f"{path.relative_to(root)}: broken local link: {parsed.path}")
    return errors


def validate_cases(cases):
    errors = []
    if not isinstance(cases, list) or not cases:
        return ["cases must be a nonempty list"]
    ids, coverage = set(), set()
    for index, case in enumerate(cases):
        prefix = f"case {index + 1}"
        if not isinstance(case, dict):
            errors.append(f"{prefix}: expected object")
            continue
        identifier = case.get("id")
        if not isinstance(identifier, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", identifier):
            errors.append(f"{prefix}: invalid ID")
        elif identifier in ids:
            errors.append(f"{prefix}: duplicate ID")
        else:
            ids.add(identifier)
        tags = case.get("tags")
        if not isinstance(tags, list) or not tags or any(not isinstance(t, str) or t not in TAGS for t in tags):
            errors.append(f"{prefix}: invalid tags")
        else:
            coverage.update(tags)
        rounds = case.get("rounds")
        if not isinstance(rounds, list) or not rounds:
            errors.append(f"{prefix}: missing rounds")
        else:
            for round_data in rounds:
                if (not isinstance(round_data, dict) or set(round_data) != {"input"}
                        or not isinstance(round_data.get("input"), str) or not round_data["input"].strip()):
                    errors.append(f"{prefix}: round must contain only nonempty input")
        rubric = case.get("rubric")
        if not isinstance(rubric, dict):
            errors.append(f"{prefix}: missing rubric")
        else:
            for key in ("must", "must_not"):
                values = rubric.get(key)
                if not isinstance(values, list) or not values or any(not isinstance(v, str) or not v.strip() for v in values):
                    errors.append(f"{prefix}: invalid {key} criteria")
    if coverage != TAGS:
        errors.append("missing behavioral coverage: " + ", ".join(sorted(TAGS - coverage)))
    return errors


def history_errors(root):
    """Scan all locally reachable Git blobs, including baseline history."""
    result = subprocess.run(["git", "rev-list", "--objects", "--all"], cwd=root,
                            text=True, capture_output=True, check=False)
    if result.returncode:
        return ["history scan unavailable: git rev-list failed"]
    errors = []
    for record in result.stdout.splitlines():
        oid = record.split(" ", 1)[0]
        kind = subprocess.run(["git", "cat-file", "-t", oid], cwd=root,
                              text=True, capture_output=True, check=True).stdout.strip()
        if kind != "blob":
            continue
        data = subprocess.run(["git", "cat-file", "blob", oid], cwd=root,
                              capture_output=True, check=True).stdout
        try:
            content = data.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"history {oid[:12]}: non-text artifact requires review")
            continue
        for finding in sensitive_findings(content):
            errors.append(f"history {oid[:12]}: {finding}")
    return errors


def validate(root=ROOT):
    root = Path(root).resolve()
    errors = [f"missing required file: {name}" for name in REQUIRED if not (root / name).is_file()]
    for path in sorted(root.rglob("*")):
        if not path.is_file() or any(part in SKIP for part in path.relative_to(root).parts):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"{path.relative_to(root)}: non-text artifact requires review")
            continue
        for finding in sensitive_findings(content):
            errors.append(f"{path.relative_to(root)}: {finding}")
        if path.suffix == ".md":
            errors.extend(markdown_link_errors(path, root))
    skill = root / "SKILL.md"
    if skill.exists():
        content = skill.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.S)
        if not frontmatter:
            errors.append("SKILL.md: missing YAML frontmatter")
        else:
            fields = frontmatter.group(1)
            if not re.search(r"(?m)^name: openmodel$", fields):
                errors.append("SKILL.md: wrong skill name")
            if not re.search(r"(?m)^description: .+", fields):
                errors.append("SKILL.md: missing description")
            if not re.search(r'(?m)^  version: "0\.2\.0"$', fields):
                errors.append("SKILL.md: unexpected release version")
    cases_path = root / "tests/cases.json"
    if cases_path.exists():
        try:
            errors.extend(validate_cases(json.loads(cases_path.read_text(encoding="utf-8"))))
        except (ValueError, TypeError) as exc:
            errors.append(f"case data invalid: {type(exc).__name__}")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--history", action="store_true", help="also scan all reachable Git blobs")
    args = parser.parse_args()
    problems = validate()
    if args.history:
        problems.extend(history_errors(ROOT))
    for problem in problems:
        print(problem)
    if problems:
        raise SystemExit(1)
    print("PASS: package, local links, case schema/coverage, and heuristic privacy checks.")
    if args.history:
        print("PASS: reachable Git history heuristic scan.")
    print("Not an agent benchmark or a guarantee of no sensitive information.")
