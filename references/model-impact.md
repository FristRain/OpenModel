# Evaluating OpenModel's net effect

OpenModel changes instructions, not model parameters or domain knowledge. Strong agents may already perform useful checks; extra procedure can make them slower or less effective. Evaluate correctness, completed work, and decision cost together.

## Compare conditions

Keep task, snapshot, tools, permissions, model identifier/settings, and budget identical:

Keep the surrounding harness constant too: orchestration, context or memory, existing evidence checks, verification, and recovery. For a mature workflow, A is that workflow as it actually runs, not a stripped-down model. For direct model use, preserve the same available tools and context across conditions. Otherwise, gains from changing the harness can be mistaken for gains from OpenModel.

- **A — Baseline:** Normal competent prompt with goal and constraints.
- **B — Compact discipline:** A plus the short prompt in [INVOKE.md](../INVOKE.md).
- **C — Full skill:** A plus [SKILL.md](../SKILL.md), with references available on demand.

Do not weaken the baseline or feed it the intended answer. Use isolated sessions, repeated runs, and tasks not used to write rules. Record actual model/version and configuration.

Provide round-specific artifacts only as each round begins. Keep reviewer rubrics/reference answers away from the evaluated agent. Randomize/anonymize results for an independent reviewer where feasible; disclose missing blinding.

| Outcome | Evaluate |
|---|---|
| Correctness and completion | Original task completed within authorization and evidence? |
| Falsification and updating | Does counterevidence change conclusions? Is a correct initial model retained? |
| Action quality | Do checks distinguish hypotheses? Executed or merely proposed? |
| State semantics | Are authority, projection, progress, and historical evidence distinct? |
| Cost | Time, tokens if available, tool calls, unnecessary questions/rechecks. |
| Trigger precision | Do ordinary CRUD and known fixes avoid needless investigation? |

Predefine quality/cost boundaries. Include null/adverse cases. Headings, hypothesis count, length, and confidence wording are not success metrics.

If A is equally sound and cheaper, use A. If B matches C more cheaply, prefer B. Retain the full protocol where it gives useful repeatable gains.

Assess only the gaps an integration is intended to fill. If the existing workflow already satisfies the protocol's relevant checks, no extra integration is needed. Report harness setup alongside results; the limited Pilot does not establish that bare model use benefits more than a mature workflow, or that every mature workflow benefits at all.

## Testing an audience claim

To test whether OpenModel helps more in minimally structured use than in an established workflow, use four conditions: minimal workflow without/with OpenModel, and established workflow without/with OpenModel. Define the actual instructions, tools, evidence access, and verification in each setup; avoid treating "complete harness" as a measurable binary property without that definition.

Within each pair, hold model, task, tools, context, and budget constant. Use unseen tasks, isolated repeated trials, and independent outcome assessment. Compare the change from adding OpenModel within each setup, including completion and cost, before comparing those changes across setups. Comparing only a bare baseline against a full workflow plus OpenModel confounds the two interventions.

This is a proposed study, not an executed result. The [audience evidence review](audience-evidence.md) separates definitions, reported experience, design inferences, and untested effectiveness claims.

The [limited Pilot](pilot-evidence.md) informs evaluation hypotheses, not controlled efficacy results. [Behavioral cases](../tests/README.md) are regressions, not evidence of benefit across models.
