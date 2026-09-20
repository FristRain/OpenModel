# OpenModel v0.2.0 — Engineering validation release

**Keep the problem model open until the evidence closes it.**

OpenModel is a falsification-first reasoning protocol for AI agents working under uncertainty. This release helps agents avoid premature commitment, symptom patching, stale explanations, and duplicated domain state.

## What changed

- A README organized around understanding the purpose in 30 seconds, the value in 3 minutes, and starting an agent workflow in 10 minutes.
- The same Observe → Separate → Branch → Attack → Update → Act core loop, with proportionate triggers and stopping rules that spare ordinary CRUD and known fixes.
- Focused references for hypothesis gates, model staleness, model duplication, state ownership, and decision cost.
- Four state roles: AUTHORITATIVE_TRUTH, DERIVED_PROJECTION, OPERATIONAL_STATE, and HISTORICAL_EVIDENCE, plus **No New State Without Ownership Proof**.
- Four fictional engineering examples, the five original cross-domain cases, 12 additional engineering case specifications, artifact checks, and CI.
- The [Unlicense](UNLICENSE) for original project materials, supporting freely customized personal or team workflows, private modifications, redistribution, and commercial use.

## Get started

Download the `openmodel-v0.2.0.zip` release asset and extract the `openmodel/` folder. Give your agent access to [SKILL.md](SKILL.md) and its references, then follow the [quick start](README.md#start-in-10-minutes). The release also includes `SHA256SUMS.txt` for checking the downloaded package.

## Validation and evidence limits

All 29 automated tests pass, alongside package, frontmatter, local-link, whitespace, and heuristic privacy checks. The [validation record](tests/VALIDATION.md) documents qualitative forward decision checks, one corrected source-attribution gap, and their limitations. These checks do not constitute a controlled A/B efficacy benchmark or end-to-end business execution.

The design draws on [limited qualitative Pilot experience](references/pilot-evidence.md) from one private project and one main model family, including same-session ablation and self-evaluation. Private artifacts are excluded; public examples are fictional general patterns.

"Engineering validation release" describes this release's focus, not proof of universal effectiveness. No statistical uplift, production speedup, independently verified root causes, or cross-agent superiority is claimed. OpenModel does not replace profiling, tracing, tests, static analysis, or architecture tools.

## What comes next

External A/B failure cases, counterexamples, null results, decision costs, and other agent/domain results are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).
