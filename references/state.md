# Working state — OpenModel v0.3 draft

Use for multi-turn updates and handoff, not as a required form. Record evidence, projection boundaries, and decisions, not private reasoning.

| Field | Content and boundary |
|---|---|
| Goal | The decision, understanding, or outcome this analysis serves. |
| Projection Conditions | Position, state, context, time/revision, instrument, and material observation boundaries. |
| Problem Frame | How the situation is currently defined and any embedded assumptions. |
| Granularity | Relevant scale: function/request/workflow/system/organization/person/relationship/market/etc. |
| Observed | Original measurement/report; ID, source, time, scope, units, conditions. A report is not automatically verified. |
| Known | Verified facts or explicit constraints, with evidence IDs and applicability. User explanations are not facts by default. |
| Experienced | Explicitly reported experience; do not invent motives or feelings. |
| Hypotheses | Mechanism, scope, distinct prediction, falsifier, status: candidate/leading/downgraded/unresolved. |
| Evidence For | Linked observation and hypothesis; why discriminating, quality and independence. Compatibility alone is labeled. |
| Evidence Against | Linked contradiction, scope and quality. No support is not automatically disproof. |
| Unknown | Missing facts, whether they change action, and possible source. |
| Observer Effects | Sampling, anchoring, state, position, scale, projection loss, or intervention effects relevant to the decision. |
| Current Best Model | Leading or unresolved explanation, scope, frame, and latest update reason. |
| Confidence | Claim-specific low/medium/high with reasons/limits; avoid uncalibrated percentages. |
| Agency | What can be changed, observed, probed, delegated, delayed, or is outside control. |
| Reversibility | Which candidate actions can restore prior state and which create difficult-to-reverse effects. |
| Value of Information | Whether another pass could plausibly change the next action and at what cost. |
| Next Action | `ACT`, `PROBE`, or `WAIT`, with target distinction, authorization, budget, and execution status. |
| Wait Condition | If waiting: why time is the discriminator, observation window/condition, and what will be sampled. |
| Exit / Reopen | Why analysis stops now and what evidence/context/risk/goal change would reopen it. |

## Update discipline

Preserve original evidence IDs and projection conditions. Append corrections with reason and linkage.

Do not rewrite a historical observation merely because the interpretation changed.

Reusing evidence across hypotheses does not make it independent.

Record only meaningful changes:

- old → new frame,
- old → new judgment,
- new evidence,
- changed confidence,
- changed action,
- or changed reopening condition.

Retain disproven or superseded models and why they failed during compaction when their reappearance would matter.

If raw sources are unavailable, disclose that.

Working state may remain in conversation. Do not claim persistence unless it was actually saved.

Unknown, unavailable, state-dependent, projection-limited, and not applicable are valid values.

## Optional compact handoff

```text
Goal / decision:
Level / scope / revision / time:
Budget:

Reality Interface
- Projection conditions:
- Problem frame:
- Granularity:
- Observed / Known:
- Experienced (if relevant):
- Missing dimensions / observer effects:

Model Space
- Hypotheses:
- Evidence For / Against:
- Unknown:
- Current Best Model / Confidence:

Decision Space
- Agency / Reversibility:
- Value of Information:
- Next Action: ACT / PROBE / WAIT
- Wait condition (if any):
- Execution status:

Update:
- old → new; why; action change

Exit / reopen:
- why stop now
- what would change the decision
```

Use only the sections needed for the task.

For new domain state, link the existing [ownership contract](state-ownership.md) rather than creating a second representation.
