# OpenModel Core v0.1

The core epistemic loop is retained in v0.2; engineering extensions live in separate references. Its goal is to reduce premature commitment to a wrong explanation when evidence is incomplete. This is a reasoning protocol, not a trained model or guarantee of correctness.

## Three disciplines

1. **Facts must not be overwritten by explanations.** Preserve original evidence and provenance. Corrections link back to what changed.
2. **Consequential models must be allowed to fail.** Identify observable evidence that would downgrade, narrow, or reject them.
3. **When information is insufficient, prefer informative reversible action.** Consider the goal, cost, risk, and existing authorization.

The protocol supports the user's task. It does not substitute a research project for an execution request or grant permission for tools, external messages, experiments, or mutations.

## Activation and levels

Start only when material uncertainty can change the action and a check, question, or experiment can help. Explicit invocation still permits Level 0.

| Level | Situation | Sufficient response |
|---|---|---|
| 0 — Flow | Simple execution, calculation, translation, ordinary CRUD, creation, listening, established evidence, or alternatives implying the same low-risk action | Do the task without a protocol table. |
| 1 — Check | Local uncertainty | Briefly separate observation/explanation, check a relevant counterexample, act. |
| 2 — Explore | Competing explanations imply different actions | Cover the relevant loop functions and obtain discriminating evidence. |
| 3 — Critical | High cost or hard-to-reverse decision | Independently verify material claims, falsifiers, failure/recovery, and rollback. |

Complexity or domain name alone does not set the level. No hypothesis quotas. Reuse completed checks and reliable applicable evidence; do not manufacture doubt. Urgent authorized containment may precede diagnosis.

If Level 3 evidence is inaccessible, state the gap and feasible work; do not claim verification. External evidence can be a primary document, measurement, source inspection, or log, not necessarily a web search.

## Observe → Separate → Branch → Attack → Update → Act

These are judgment functions, not prescribed private reasoning or mandatory headings. Combine, reorder, and skip already satisfied checks; do not hide a material gap.

### Observe

Preserve source, time, scope, conditions, and type: direct measurement, report, summary, or generated material. "The page feels slow" is a report, not a measured latency or database diagnosis. Attribute unverified external claims and make conclusions that depend on them conditional; a newly found explanation is not independently corroborated merely because it fits. Record units and measurement boundaries. Screenshots, OCR, transcripts, and summaries can lose context. Multiple representations of the same event are not independent observations.

### Separate

| Layer | Meaning |
|---|---|
| Observation | What was recorded or measured? |
| Experience | What did someone report feeling or experiencing? |
| Interpretation | How was the observation understood? |
| Hypothesis | What proposed mechanism could explain it? |
| Decision | What action follows given goals and constraints? |

A feeling deserves acknowledgment without proving another person's motives. Neither the user's nor the agent's preferred cause is automatically Known. Preferences and value choices are not causal facts.

### Branch

Retain the leading explanation, plausible rivals that change action, and material unknowns. Do not give remote possibilities equal weight to strong evidence. Merge hypotheses with identical predictions. A leading model can remain unresolved.

For consequential hypotheses, identify scope, supporting and opposing evidence, and distinct predictions. Do not add candidates just to fill a table.

### Attack

Ask: **If this explanation is wrong, what observable result would change the decision?** Apply comparable evidence standards to rivals. Mere compatibility is weaker than evidence favoring one model over another.

Before a meaningful test, define how different results will update the model. An explanation with no feasible falsifier is an untestable narrative for this task, not a basis for strong causal claims. Attack explanations, not people.

### Update

Upgrade with discriminating support; downgrade or narrow with conflict. Branch again only for important new evidence or unexplained observations. Lack of information remains unknown.

Check measurement validity, scope, and source independence first. Repetition, paraphrase, or agreement does not add independent evidence. Preserve superseded hypotheses and reasons so they are not reintroduced without cause.

Use low/medium/high confidence with reasons and scope rather than invented probabilities. Low confidence in a cause can coexist with strong justification for a low-risk next action.

### Act

Return to the requested outcome. With a material gap, choose affordable discriminating evidence or an authorized reversible probe. With sufficient evidence, execute the effective solution, not endlessly smaller steps. Independent useful checks may be combined.

For tests that affect decisions, specify observations, update criteria, budget, stop, and rollback. Label plans as unexecuted; tool success alone is not proof of real-world benefit.

If no reversible option exists, state uncertainty, delay cost, and consequences. Proceed only within existing authorization; missing authorization is handled by the host's rules, not a new protocol-specific approval gate.

## Observer Audit

Check only biases relevant to the decision:

- Missing normal/successful/contradictory samples, selection, and time windows.
- Measurement coverage, filtering, crop, summary, and provenance.
- Anchoring to the user's description, an earlier answer, or the agent's favorite theory.
- Concrete context affecting reliability, without inventing motives or personality judgments.

Possible bias does not invalidate all evidence. State its likely effect and a practical remedy; do not claim an independent viewpoint that was never obtained.

## Overfit Detector

Check when a model explains every outcome without boundaries, absorbs contradictions as support, accumulates ad hoc exceptions, or gains confidence without independent evidence. Agreement alone proves neither truth nor overfit.

Identify the specific contradiction, narrow the claim, and seek a falsifier. If none is accessible, reduce confidence and stop under the exit rules. Contrarianism is not a success criterion.

## Analysis Loop exit

Stop when expected decision value of another pass is lower than its cost. No numerical score is required. Exit when:

1. Evidence supports the next action and remaining uncertainty does not change it.
2. New information requires execution rather than discussion.
3. No new evidence, prediction, or action change emerged.
4. The agreed time, cost, evidence budget, or deadline has arrived.
5. Key evidence is inaccessible and further inference is unhelpful.

Exit with current judgment, material unknowns, action/waiting condition, and reopening evidence. A budget does not prove truth or authorize unsafe action.

**Stopping analysis is not stopping the task.** Continue authorized implementation and relevant validation. Reopen for material new evidence, context, risk, or goals, not repetition.

## State and domain adaptation

The [working-state fields](state.md) remain:
`Observed / Known / Experienced / Hypotheses / Evidence For / Evidence Against / Unknown / Observer Bias / Current Best Model / Confidence / Reversible Next Test`.

Use only needed fields, especially on handoff; no mandatory full form. Missing facts remain unknown. Report decisions and supporting evidence, not private chain-of-thought.

Domains supply observation units, evidence standards, plausible mechanisms, feasible tests, and risk/rollback constraints. Do not transplant thresholds or assume a familiar analogy supplies missing expertise. In unfamiliar domains check definitions, units, measurement, and primary evidence. No mind-reading or invented diagnoses.

The five [original cross-domain cases](test-cases.md) test transfer, updates, and exits; they do not establish universal benefit. Engineering references in [SKILL.md](../SKILL.md) add targeted guidance without replacing this core.
