---
name: openmodel
description: Test problem explanations before committing to changes when material uncertainty, conflicting evidence, recurring failures, stale assumptions, or unclear state ownership changes the next action. Use when explicitly requested; do not expand ordinary CRUD, known local fixes, or simple execution into an investigation.
metadata:
  version: "0.2.0-rc.1"
---

# OpenModel

A falsification-first reasoning protocol for AI agents working under uncertainty.
Keep the problem model open until the evidence closes it.

"Model" means an explanation of the problem. Preserve the user's goal, authorization, and host instructions. This skill adds no permission to mutate systems, send messages, or run experiments. It does not replace profiling, tracing, tests, static analysis, or architecture tools.

## Route by the decision, not keywords

| Level | Trigger | Enough work |
|---|---|---|
| 0 — Flow | Ordinary CRUD with established ownership, formatting, a demonstrated local fix, creation/listening, or alternatives leading to the same low-risk action | Execute directly; no hypothesis table. |
| 1 — Check | One local uncertainty could change an action | Separate observation from explanation; check a relevant counterexample. |
| 2 — Explore | Plausible competing causes imply different actions | Compare discriminating evidence and complete relevant loop functions. |
| 3 — Critical | A mistaken decision is costly or hard to reverse | Independently verify material evidence and check failure/recovery and rollback. |

Consider Level 2 for performance/concurrency incidents, intermittent or cross-module failures, a repeated unsuccessful fix, disagreement with historical explanations, or an untested architectural premise. These are signals, not automatic mandates; known causes and adequate current evidence can stay at Level 0 or 1.

For new or repurposed domain state, use the proportionate ownership check below. An ordinary field under an existing authority is not automatically an architecture investigation. Explicit invocation still permits Level 0.

## Core loop

**Observe → Separate → Branch → Attack → Update → Act**

These are combinable functions, not a required output format or instructions to expose private reasoning.

1. **Observe:** Preserve reports and measurements with source, time, scope, and revision when relevant. A reported symptom is not a measured cause. Attribute unverified external claims and make conclusions that depend on them conditional.
2. **Separate:** Distinguish observed/known facts, experiences, interpretations, hypotheses, and decisions. User and agent explanations are not automatically facts.
3. **Branch:** Keep only plausible alternatives that could change action, plus material unknowns. No hypothesis quota; do not manufacture doubt about established evidence.
4. **Attack:** For consequential hypotheses, state feasible observations that would lower confidence or narrow scope. Prefer evidence that predicts different outcomes under competing explanations. Define the update before obtaining the result.
5. **Update:** Revise the current best model when warranted; preserve superseded explanations and why they failed. Repeated summaries and agreement are not independent evidence. An unrun test is a plan.
6. **Act:** Obtain the smallest useful discriminator within authorization and budget, or execute the justified solution. Continue the requested work and relevant validation.

Read [core](references/core.md) for deeper definitions. Reuse checks already satisfied by the host workflow.

## Conditional engineering checks

Read only what affects the decision:

- [Hypothesis gate](references/hypothesis-gate.md): before an uncertain cause becomes a change. Record the leading explanation, relevant rival, falsifier, evidence, and next action.
- [Model staleness](references/model-staleness.md): when history conflicts with present behavior. Verify current revision, configuration, deployment, and active path; source alone does not prove deployment.
- [Model duplication](references/model-duplication.md): when records may encode the same fact. Compare meaning and writers, not names alone.
- [State ownership](references/state-ownership.md): **No New State Without Ownership Proof.** Classify new/repurposed state as `AUTHORITATIVE_TRUTH`, `DERIVED_PROJECTION`, `OPERATIONAL_STATE`, or `HISTORICAL_EVIDENCE`; identify authority, writers, identity/version, lifecycle, and recovery. Reuse existing contracts. Missing proof withholds the dependent state change while independent work continues; it does not require another approval for an authorized action.
- [Decision cost](references/decision-cost.md): when investigation grows. Limit checks to those that can change action and account for delay.

**Observer Audit:** Check sampling, measurement coverage, source independence, and anchoring when material. Do not invent personal motives.

**Overfit Detector:** If contradictions are repeatedly explained away or confidence grows without new evidence, narrow the claim and seek a real falsifier. Do not oppose a sound model merely to show skepticism.

## Stop and continue

End analysis when evidence is sufficient, alternatives lead to the same low-risk action, a pass adds no evidence/prediction/action change, the budget expires, or useful information requires execution.

Exit with the current best model (possibly unresolved), material unknowns, an authorized action or concrete waiting condition, and evidence that would reopen it. A spent budget neither proves a cause nor authorizes risky implementation. Urgent authorized containment can precede root-cause analysis. Stop analyzing, then continue the task.

Use [working state](references/state.md) for updates/handoff, not a mandatory form. Normally present only the judgment, decisive evidence/unknowns, and action. [Tests](tests/README.md) and [Pilot evidence](references/pilot-evidence.md) are evaluation material, not default task context.
