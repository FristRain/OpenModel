# Working state — Core v0.1, retained in v0.2

Use for multi-turn updates and handoff, not as a required form. Record evidence and decisions, not private reasoning.

| Field | Content and boundary |
|---|---|
| Observed | Original measurement/report; ID, source, time, scope, units, conditions. A report is not automatically verified. |
| Known | Verified facts or explicit constraints, with evidence IDs and applicability. User explanations are not facts by default. |
| Experienced | Explicitly reported experience; do not invent motives or feelings. |
| Hypotheses | Mechanism, scope, distinct prediction, falsifier, status: candidate/leading/downgraded/unresolved. |
| Evidence For | Linked observation and hypothesis; why discriminating, quality and independence. Compatibility alone is labeled. |
| Evidence Against | Linked contradiction, scope and quality. No support is not automatically disproof. |
| Unknown | Missing facts, whether they change action, and possible source. |
| Observer Bias | Specific concern, evidence, likely effect, and remedy; no personality claims. |
| Current Best Model | Leading or unresolved explanation, scope, and latest update reason. |
| Confidence | Claim-specific low/medium/high with reasons/limits; avoid uncalibrated percentages. |
| Reversible Next Test | Action, target distinction, predictions, observations, budget, stop/rollback, authorization, execution status and actual result. |

## Update discipline

Preserve original evidence IDs. Append corrections with reason and linkage. Reusing evidence across hypotheses does not make it independent.

Record only meaningful changes: old → new judgment, new evidence, changed action. Retain disproven models and reopening conditions during compaction. If raw sources are unavailable, disclose that.

Working state may remain in conversation. Do not claim persistence unless it was actually saved. Unknown, unavailable, and not applicable are valid values.

## Optional compact handoff

```text
Goal / decision:
Level / scope / revision / time:
Budget:
Observed / Known: [sources and boundaries]
Hypotheses: [leading, material rival, distinct predictions and falsifiers]
Evidence For / Against: [linked records, independence]
Unknown: [which gaps change the action]
Current Best Model / Confidence: [scope and reasons]
Reversible Next Test: [action; observations; update criteria; budget; rollback]
Execution status: [planned / executed / result unverified, with actual evidence]
Update: [old → new; why; action change]
Exit / reopen: [why stop now; what would change the decision]
```

Use Experienced and Observer Bias only when relevant. For new domain state, link the existing [ownership contract](state-ownership.md) rather than creating a second representation.
