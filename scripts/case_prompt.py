"""Print one behavioral test round without leaking its grading rubric."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def prepare(case_id, round_number=1):
    cases = json.loads((ROOT / "tests/cases.json").read_text(encoding="utf-8"))
    case = next((item for item in cases if item["id"] == case_id), None)
    if case is None:
        raise ValueError("Unknown case ID")
    if round_number < 1 or round_number > len(case["rounds"]):
        raise ValueError("Round outside this case")
    return case["rounds"][round_number - 1]["input"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case")
    parser.add_argument("--round", type=int, default=1)
    args = parser.parse_args()
    try:
        print(prepare(args.case, args.round))
    except ValueError as exc:
        parser.error(str(exc))
