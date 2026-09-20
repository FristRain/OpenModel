# Testing OpenModel

There are two different kinds of verification. Do not report one as the other.

See the [candidate validation record](VALIDATION.md) for what was actually executed and its limits.

## Automated artifact checks

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

Python 3.10+; no third-party runtime dependency. Checks cover relative Markdown links, frontmatter, expected package resources, behavioral-case structure/coverage, and obvious sensitive-data patterns. Unit tests exercise the validator with broken links, malformed cases, missing files, and sensitive fixtures. These are packaging checks, not agent-behavior pass rates.

The scanner is a heuristic. It cannot prove absence of secrets, private architecture, or identifying business details. Review the final diff and history before publication.

## Behavioral regressions

The five original fictional [cross-domain cases](../references/test-cases.md) are retained. [cases.json](cases.json) adds engineering regressions for trigger boundaries, falsification (including a supported initial model), staleness, duplication/ownership, and decision cost/analysis paralysis.

1. Start a clean agent session with [SKILL.md](../SKILL.md) and references accessible.
2. Give it only the selected round's input. Prepare a prompt without the rubric using:
   ```sh
   python scripts/case_prompt.py pool-falsifier --round 1
   ```
3. Capture the actual output and tool actions, then supply the next round in the same session. Do not reveal later evidence early.
4. A separate reviewer reads the case rubric after the run. Judge observable decisions and evidence use, not wording or headings.
5. Record case, round, exact model/settings, skill revision, tool permissions, output, elapsed time/cost if available, and pass/fail/unresolved with evidence. Missing tools can make execution unresolved; do not fabricate it.
6. Mark explicitly which cases were executed. Adding fixtures does not mean they passed behaviorally.

For a change, select affected cases plus neighboring boundaries. For efficacy claims, use the isolated/repeated comparison method in [model-impact.md](../references/model-impact.md), not these familiar regression prompts alone.

No API key or model runner is bundled, and CI does not call an agent. A manually assessed smoke test is not a controlled A/B benchmark.
