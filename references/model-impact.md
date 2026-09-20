# Evaluating OpenModel's net effect

OpenModel changes instructions, not model parameters or domain knowledge. Strong agents may already perform useful checks; extra procedure can make them slower or less effective. Evaluate correctness, completed work, and decision cost together.

## Compare conditions

Keep task, snapshot, tools, permissions, model identifier/settings, and budget identical:

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

The [limited Pilot](pilot-evidence.md) informs evaluation hypotheses, not controlled efficacy results. [Behavioral cases](../tests/README.md) are regressions, not evidence of benefit across models.
