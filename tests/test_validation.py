"""Regression tests for artifact validation, not simulated agent reasoning."""
import copy
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from scripts import case_prompt, validate

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_current_package(self):
        self.assertEqual(validate.validate(ROOT), [])

    def test_missing_resource_is_reported(self):
        with tempfile.TemporaryDirectory() as folder:
            errors = validate.validate(Path(folder))
            self.assertIn("missing required file: SKILL.md", errors)

    def test_bad_frontmatter_is_reported(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "SKILL.md").write_text("# No metadata\n", encoding="utf-8")
            self.assertIn("SKILL.md: missing YAML frontmatter", validate.validate(root))


class LinkTests(unittest.TestCase):
    def check(self, content, files=()):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in files:
                (root / name).write_text("ok", encoding="utf-8")
            document = root / "doc.md"
            document.write_text(content, encoding="utf-8")
            return validate.markdown_link_errors(document, root)

    def test_valid_local_and_external_links(self):
        self.assertEqual(self.check("[local](target.md) [web](https://example.com/)", ["target.md"]), [])

    def test_missing_link_is_rejected(self):
        self.assertTrue(self.check("[missing](missing.md)"))

    def test_escape_is_rejected(self):
        self.assertTrue(self.check("[outside](../outside.md)"))

    def test_encoded_filename_is_resolved(self):
        self.assertEqual(self.check("[space](some%20file.md)", ["some file.md"]), [])

    def test_fenced_examples_are_not_links(self):
        fence = chr(96) * 3
        self.assertEqual(self.check(f"{fence}text\n[example](not-a-file)\n{fence}\n"), [])

    def test_local_machine_scheme_is_rejected(self):
        self.assertTrue(self.check("[bad](file:///private/doc.md)"))


class PrivacyTests(unittest.TestCase):
    def test_public_prose_is_allowed(self):
        self.assertEqual(validate.sensitive_findings("https://example.com API keys must not be published."), [])

    def test_private_addresses_are_caught(self):
        address = ".".join(map(str, (192, 168, 5, 9)))
        self.assertIn("private or local network address", validate.sensitive_findings(address))

    def test_documentation_address_is_allowed(self):
        address = ".".join(map(str, (203, 0, 113, 5)))
        self.assertEqual(validate.sensitive_findings(address), [])

    def test_url_credentials_are_caught(self):
        url = "https://" + "test:example@" + "example.com/"
        self.assertIn("URL credentials", validate.sensitive_findings(url))

    def test_internal_host_is_caught(self):
        url = "https://" + "service" + ".internal/"
        self.assertIn("internal URL", validate.sensitive_findings(url))

    def test_ipv6_local_host_is_caught(self):
        url = "http://" + "[::1]/"
        self.assertIn("private or local network address", validate.sensitive_findings(url))

    def test_machine_path_is_caught(self):
        path = "Q:" + chr(92) + "private" + chr(92) + "artifact"
        self.assertIn("machine-specific absolute path", validate.sensitive_findings(path))

    def test_credential_is_redacted(self):
        credential = "gh" + "p_" + "x" * 36
        findings = validate.sensitive_findings(credential)
        self.assertEqual(findings, ["possible credential"])
        self.assertNotIn(credential, str(findings))


class CaseTests(unittest.TestCase):
    def setUp(self):
        self.cases = json.loads((ROOT / "tests/cases.json").read_text(encoding="utf-8"))

    def test_complete_cases(self):
        self.assertEqual(validate.validate_cases(self.cases), [])

    def test_duplicate_id_is_rejected(self):
        self.cases.append(copy.deepcopy(self.cases[0]))
        self.assertTrue(any("duplicate ID" in error for error in validate.validate_cases(self.cases)))

    def test_empty_input_is_rejected(self):
        self.cases[0]["rounds"][0]["input"] = ""
        self.assertTrue(any("nonempty input" in error for error in validate.validate_cases(self.cases)))

    def test_rubric_leak_in_round_is_rejected(self):
        self.cases[0]["rounds"][0]["expected_answer"] = "leaked"
        self.assertTrue(any("only nonempty input" in error for error in validate.validate_cases(self.cases)))

    def test_missing_counterexample_criteria_are_rejected(self):
        self.cases[0]["rubric"]["must_not"] = []
        self.assertTrue(any("must_not" in error for error in validate.validate_cases(self.cases)))

    def test_missing_coverage_is_rejected(self):
        self.cases = [case for case in self.cases if "staleness" not in case["tags"]]
        self.assertTrue(any("missing behavioral coverage" in error for error in validate.validate_cases(self.cases)))

    def test_invalid_case_shape_is_rejected(self):
        self.assertTrue(validate.validate_cases({"not": "a list"}))
        self.assertTrue(validate.validate_cases([None]))

    def test_unknown_tag_is_rejected(self):
        self.cases[0]["tags"] = ["unsupported"]
        self.assertTrue(any("invalid tags" in error for error in validate.validate_cases(self.cases)))

    def test_round_prompt_has_no_rubric_or_future_evidence(self):
        case = next(case for case in self.cases if case["id"] == "pool-falsifier")
        self.assertEqual(case_prompt.prepare(case["id"], 1), case["rounds"][0]["input"])
        self.assertNotIn(case["rounds"][1]["input"], case_prompt.prepare(case["id"], 1))
        for criterion in case["rubric"]["must"]:
            self.assertNotIn(criterion, case_prompt.prepare(case["id"], 1))

    def test_invalid_prompt_request_is_rejected(self):
        for case, number in (("absent", 1), ("pool-falsifier", 0), ("pool-falsifier", 3)):
            with self.assertRaises(ValueError):
                case_prompt.prepare(case, number)


class HistoryTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("git"), "Git unavailable")
    def test_removed_sensitive_blob_is_still_detected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            def git(*args):
                return subprocess.run(["git", "-c", "user.name=Fixture",
                                       "-c", "user.email=fixture@example.com", *args],
                                      cwd=root, capture_output=True, check=True)
            git("init")
            target = root / "fixture.txt"
            target.write_text("gh" + "p_" + "x" * 36, encoding="utf-8")
            git("add", "fixture.txt")
            git("commit", "-m", "Fixture baseline")
            target.write_text("clean current content", encoding="utf-8")
            git("add", "fixture.txt")
            git("commit", "-m", "Fixture cleanup")
            self.assertTrue(any("possible credential" in error
                                for error in validate.history_errors(root)))

    @unittest.skipUnless(shutil.which("git"), "Git unavailable")
    def test_history_requires_repository(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(validate.history_errors(folder),
                             ["history scan unavailable: git rev-list failed"])


if __name__ == "__main__":
    unittest.main()
