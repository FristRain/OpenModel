# Audience and harness claims: evidence review

Reviewed 2026-09-20. This is a definition and evidence audit, not a new controlled experiment.

## Finding

The available evidence does **not** establish that OpenModel is primarily for bare models, that having a complete workflow removes the need for it, or that either setup benefits more. The defensible design scope is tasks where an uncertain problem explanation can change the action and the current process leaves that risk insufficiently checked.

A direct prompt and a selectively loaded skill are possible delivery modes. Neither delivery mode proves an effect.

## What the sources establish

| Evidence | Supported point | Limit |
|---|---|---|
| Anthropic's [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), Jan 9, 2026 | An agent harness processes inputs and tool calls; evaluating an agent evaluates model and harness together. The article identifies Claude Code as a harness. | Not having a custom project workflow does not imply the absence of a runtime harness. The article does not evaluate OpenModel. |
| Anthropic's [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), Oct 16, 2025 | Skills package instructions and resources for existing agents, with relevant content loaded on demand. The authors recommend starting from observed capability gaps. | This supports composability, not the efficacy of this particular skill. |
| Anthropic's [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps), Mar 24, 2026 | The authors test components by removal and report that some scaffolding becomes unnecessary as model capability changes, while other checks still help particular tasks. | This is task- and model-specific experience, not an OpenModel benchmark or a universal rule about workflow completeness. |
| OpenModel's [reported Pilot](pilot-evidence.md) | The original narrative describes diagnostic comparisons within an already structured engineering environment and reports both evidence-discipline benefits and overhead. | Same-session ablation, self-evaluation, one project/model family, and no comparison across harness setups. Private raw findings have not been independently reproduced. |

The external sources explain architecture and evaluation principles. They are not endorsements or independent validation of OpenModel.

## Practical interpretation

The following are **design inferences**, not measured effectiveness claims:

- Missing evidence discipline can motivate trying compact OpenModel guidance, whether the model is called directly or through an agent.
- A workflow may have tools, memory, tests, and recovery without explicitly challenging a particular causal premise. Conversely, its existing checks may already do that adequately.
- Where a relevant check is already satisfied, duplicating it adds procedure without filling a gap. Inspect actual coverage rather than labeling a workflow simply "complete" or "incomplete."
- If the problem is missing tools, unavailable observations, or unreliable execution infrastructure, this Markdown protocol does not supply those capabilities.
- Simple execution and demonstrated local fixes do not become hypothesis investigations merely because the user lacks a custom workflow.

Use task uncertainty, actual gaps, and observed decision cost to select the relevant checks. Reuse existing records and authorization boundaries.

## What remains untested

Relative benefit requires comparing the effect of adding OpenModel within each well-defined workflow setup, not comparing an unassisted model against a differently equipped agent. See the proposed four-condition study in [model-impact.md](model-impact.md#testing-an-audience-claim).

Current artifact tests verify repository integrity. Prior decision smoke tests check selected behaviors. Neither establishes an audience ranking or a general performance benefit.
