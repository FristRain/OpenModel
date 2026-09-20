# v0.2 candidate validation record

Date: 2026-09-20. Scope: repository artifacts and qualitative decision smoke tests; **not a controlled A/B efficacy study**.

## Automated validation

- 29 standard-library unit tests passed locally.
- Package resources, relative Markdown links, skill metadata, and behavioral-case schema/coverage passed.
- The skill-creator frontmatter validator passed in UTF-8 mode.
- Git whitespace checks passed.
- Heuristic credential/private-address/machine-path checks passed on candidate files and reachable history.
- An additional local, unpublished denylist check for source-project identifiers passed. The denylist itself is excluded to avoid publishing private identifiers.
- A manual semantic review checked the four fictional cases for private workflow, naming, configuration, business data, and architecture leakage. No such material was found; neither review nor scanning proves complete absence.

The original five cross-domain case specifications are unchanged from the imported baseline. There was no preexisting executable test suite. CI repeats artifact validation and the 29 unit tests; CI does not run an agent.

Reproduce:

```sh
python scripts/validate.py --history
python -m unittest discover -s tests -v
git diff --check
```

## Forward decision smoke tests

A separate evaluator session loaded the skill and selected protocol references. It did not receive the Pilot conversation, public examples, test rubrics, or intended answers. The editing agent subsequently assessed its outputs. Later evidence for the five legacy cases and the initially supported capacity model was supplied after first-round answers.

The evaluator had no tools for the simulated business actions. Results below concern action selection, evidence handling, and declared scope; no implementation, production probe, actual trace capture, or business outcome is claimed.

| Scenario theme | Observed decision |
|---|---|
| Ordinary CRUD / established owner | Proceed using existing ownership, validation, and transaction rules without a full hypothesis investigation. |
| Demonstrated delimiter defect | Use the proven local cause and relevant regression test, without inventing rivals. |
| Database saturation / falsification | Compare correlated timing boundaries; downgrade capacity when post-execute work dominates; propose local profiling. |
| Initial capacity hypothesis supported | Strengthen the hypothesis after repeated controlled local results; limit the conclusion to tested conditions. |
| Source updated, deployment unknown | Avoid duplicating the async refactor; leave production applicability unresolved. |
| Current deployed path verified | Downgrade direct blocking and target the measured request stage. |
| Competing current stock writers | Defer another snapshot; clarify authority and recovery while continuing read-only work. |
| Legitimate state copies | Preserve all four distinct ownership roles; receipt is not present truth and job completion is not domain success. |
| Exhausted analysis budget / shared safe action | Stop speculation and choose the authorized trace capture; cause remains unresolved. |
| Deadline / unsupported destructive migration | Withhold destructive production action and prepare reviewable independent local work. |
| Existing host checks completed | Reuse evidence and verification; no repeated ceremony. |
| Emergency containment | Prefer the explicitly authorized reversible mitigation before exhaustive diagnosis. |
| Legacy software performance | Shift investigation to browser main-thread work after correlated timing evidence. |
| Legacy market inference | Correct the target-population inference, prepare clearer scope wording, and avoid extrapolating a stable conversion rate. |
| Legacy collaboration | Update from missing chat reply to documented participation and the agreed feedback deadline. |
| Legacy learning | Account for test-content differences and deliver a practical study plan without diagnosing decline. |
| Legacy unfamiliar-image inference | Downgrade physical expansion, but the initial response did not explicitly condition the new source claim on its accuracy. |

The final row exposed a source-attribution gap. A narrow clarification was added to Observe in the skill and core: attribute unverified external claims and make dependent conclusions conditional.

A **fresh evaluator** then received that image case in two rounds, without the rubric or prior result. Its updated response explicitly said the display-scaling explanation applies **if the publication note is accurate and applies to those images**; it rejected the expansion inference without asserting no physical change. This satisfied the affected source-boundary check. Other scenarios were not rerun after this narrow wording change.

## Limits

These are manually assessed smoke tests across the 12 engineering scenario themes and five preserved cross-domain cases, not automatic behavioral tests or a claim that every fixture was run verbatim. Some engineering prompts were condensed; the database pre-evidence prediction was also checked separately from its post-evidence decision.

There was one evaluator for the initial pass and a fresh evaluator only for the affected retest. They used the runtime-selected model; exact build/settings, wall time, and token accounting were not independently captured. There was no baseline comparison, randomization, repeated sampling, independent human judge, host-integration test, or end-to-end implementation test. The editing agent's assessment can itself be biased.

These results support a reviewable candidate and identify one corrected behavior gap. They do not establish universal benefit, production improvement, or compatibility/performance across agents. The historical [Pilot limitations](../references/pilot-evidence.md) remain separate from these packaging and decision checks.
