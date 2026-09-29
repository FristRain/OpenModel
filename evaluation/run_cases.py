#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fact-boundary evaluation harness (semi-automated, stdlib only).

Behavioral cases test an AI agent, so a human stays in the loop:
  1. run  : prints the exact prompt per case/round -> you paste it to the model
            under test (with the domain SKILL.md as system context), then paste
            the model's reply back. End each reply with a line containing only <<<END>>>.
            Saves responses_<model>.json.
  2. grade: emits grading_<model>.md = each response side-by-side with its
            Expected/Failure checklist for a human to tick.

Usage:
    python run_cases.py --cases cases.json --skill /path/to/domains/development/SKILL.md --model gpt-x
    python run_cases.py --grade responses_gpt-x.json
"""
import argparse
import datetime
import json
import sys

END_MARK = "<<<END>>>"


def build_prompt(skill_text, case, rnd, round_idx):
    parts = [
        "[SYSTEM: the following skill defines your working protocol. Follow it.]",
        skill_text.strip(),
        "",
        f"[CASE {case['id']} — {case['title']} | round {round_idx + 1}]",
        rnd["input"],
    ]
    if rnd.get("evidence"):
        parts += ["", "[Available evidence]", rnd["evidence"]]
    return "\n".join(parts)


def cmd_run(args):
    cases = json.load(open(args.cases, encoding="utf-8"))["cases"]
    skill = open(args.skill, encoding="utf-8").read()
    if args.domain:
        cases = [c for c in cases if c["domain"] == args.domain]
    responses = {}
    for case in cases:
        responses[case["id"]] = []
        for i, rnd in enumerate(case["rounds"]):
            print("=" * 70)
            print(f"CASE {case['id']} ({case['domain']}) round {i + 1}/{len(case['rounds'])}")
            print("=" * 70)
            print(build_prompt(skill, case, rnd, i))
            print("-" * 70)
            print(f"Paste the model's reply below, end with a line containing only {END_MARK}:")
            lines = []
            for line in sys.stdin:
                if line.strip() == END_MARK:
                    break
                lines.append(line)
            responses[case["id"]].append("".join(lines).strip())
    out = {
        "model": args.model,
        "date": datetime.datetime.now().isoformat(timespec="seconds"),
        "skill": args.skill,
        "responses": responses,
    }
    path = f"responses_{args.model}.json"
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"\nSaved {path}. Now run: python run_cases.py --grade {path}")


def cmd_grade(args):
    data = json.load(open(args.grade, encoding="utf-8"))
    cases = {c["id"]: c for c in json.load(open(args.cases, encoding="utf-8"))["cases"]}
    out = [f"# Fact-boundary grading — model: {data['model']} ({data['date']})",
           f"Skill context: `{data['skill']}`", ""]
    for cid, rounds in data["responses"].items():
        case = cases[cid]
        out.append(f"## {cid} — {case['title']} ({case['domain']})")
        for i, resp in enumerate(rounds):
            out.append(f"### Round {i + 1} input")
            out.append(f"> {case['rounds'][i]['input']}")
            if case["rounds"][i].get("evidence"):
                out.append(f"> Evidence: {case['rounds'][i]['evidence']}")
            out.append("")
            out.append(f"### Round {i + 1} response")
            out.append(resp or "_(no response)_")
            out.append("")
        out.append("### Expected (tick each satisfied)")
        out += [f"- [ ] {e}" for e in case["expected"]]
        out.append("")
        out.append("### Failure (tick each observed)")
        out += [f"- [ ] {f}" for f in case["failure"]]
        out.append("")
        out.append("**Verdict:** PASS / FAIL / PARTIAL")
        out.append("")
        out.append("---")
        out.append("")
    path = f"grading_{data['model']}.md"
    open(path, "w", encoding="utf-8").write("\n".join(out))
    print(f"Wrote {path}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", default="cases.json")
    ap.add_argument("--skill", help="domain SKILL.md used as system context")
    ap.add_argument("--model", default="candidate")
    ap.add_argument("--domain", choices=["code-review", "human", "development"])
    ap.add_argument("--grade", help="responses json to grade")
    args = ap.parse_args()
    if args.grade:
        cmd_grade(args)
    else:
        if not args.skill:
            ap.error("--skill is required for a run")
        cmd_run(args)


if __name__ == "__main__":
    main()
