# Pilot evidence: provenance and limitations

## Source and status

The v0.2 design draws on a maintainer-provided conversation record describing diagnostic work on one private production software project with one main model family. It covered resource saturation, a historical blocking-path explanation, worker scaling, and a later architecture review.

The first comparison explicitly described **same-session behavioral ablation**: the same assistant produced and evaluated alternatives. It was not two isolated, blinded runs. Later reports are qualitative diagnostic comparisons; the available record does not establish independent replication or stronger controls.

The reported setting already included a structured engineering workflow and verification tools. It was not a comparison between bare model use and a mature harness, so it cannot establish a preferred audience or relative benefit across those setups.

This release treats that record as reported experience. It does not independently reproduce private source inspections, traces, findings, or production outcomes. Raw private artifacts are excluded. Merely replacing names would not adequately anonymize a private architecture, so the public examples are newly written fictional scenarios retaining only general reasoning patterns.

## Lessons used

| Reported pattern | Product change | Unproven |
|---|---|---|
| Baseline and protocol both found several plausible causes; failure conditions became more explicit. | Hypothesis gate with discriminating predictions. | General improvement in cause discovery or accuracy. |
| Historical explanation no longer fully matched current code. | Staleness check separating source from deployment. | All production paths fixed or latency improved. |
| Resource occupancy risked being read as inadequate capacity. | Saturation examples and bounded measurement before tuning. | Measured performance benefit from the protocol. |
| New layers raised duplicated-authority and recovery questions. | Ownership and duplication references. | That the design was defective or fewer layers are always better. |
| Explicit analysis added overhead. | Conditional activation and stopping rules. | Overhead is small or worthwhile for ordinary tasks. |

## Limits and non-claims

- One project and one main model family, not a representative agent/domain sample.
- Same-session context leakage, prompting, and self-evaluation can influence comparisons.
- Diagnostic quality is not successful implementation or measured production outcome.
- No independently reviewed raw evidence or reproducible numerical effect size is published.
- The baseline already showed useful skepticism; marginal benefit may be small.
- Extra process can reduce completion or waste resources; negative and null results matter.

No universal effectiveness, statistically significant uplift, cross-agent superiority, verified production speedup, or certified root-cause finding is claimed. "Engineering validation release" describes phase and focus, not completed validation.

Next evidence should use preregistered, repeated, isolated comparisons on unseen cases with independent assessment and reported costs. See [evaluation method](model-impact.md) and [contributing](../CONTRIBUTING.md).
