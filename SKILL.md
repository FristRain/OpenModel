---
name: openmodel
description: Test whether the current observation and problem frame are adequate before committing to explanations or actions when material uncertainty, projection loss, conflicting evidence, recurring failures, stale assumptions, unclear state ownership, or irreversible decisions could change the next step. Use when explicitly requested; do not expand ordinary CRUD, known local fixes, or simple execution into an investigation.
metadata:
  version: "0.3.0-dev"
---

# OpenModel

A projection-aware, falsification-first decision protocol for AI agents working under uncertainty.

**Keep the problem model open until the evidence closes it.**

OpenModel is organized around three different error surfaces:

1. **Reality Interface** — are we seeing a partial projection and mistaking it for the problem itself?
2. **Model Space** — are we committing too early to one explanation?
3. **Decision Space** — are we confusing understanding with the action that should follow?

> Do not confuse the projection with reality, the model with fact, or understanding with action.

"Model" means an explanation of the problem. Preserve the user's goal, authorization, and host instructions. This skill adds no permission to mutate systems, send messages, or run experiments. It does not replace profiling, tracing, tests, static analysis, architecture tools, domain expertise, or missing evidence.

## Route by the decision, not keywords

| Level | Trigger | Enough work |
|---|---|---|
| 0 — Flow | Ordinary CRUD with established ownership, formatting, a demonstrated local fix, creation/listening, or alternatives leading to the same low-risk action | Execute directly; no protocol table. |
| 1 — Check | One local uncertainty, projection boundary, or frame assumption could change an action | Bind the observation to its conditions, separate observation from explanation, check one relevant counterexample or missing dimension, then act. |
| 2 — Explore | Plausible frames or competing causes imply different actions | Rotate the observation if needed, compare discriminating evidence, and complete the relevant loop functions. |
| 3 — Critical | A mistaken decision is costly, hard to reverse, or materially affects other agents/systems | Independently verify material evidence, frame, failure/recovery, intervention effects, and rollback or waiting conditions. |

Consider Level 2 for performance/concurrency incidents, intermittent or cross-module failures, repeated unsuccessful fixes, disagreement with historical explanations, untested architectural premises, ambiguous requirements, or cases where a user description already embeds a causal claim. These are signals, not automatic mandates; known causes and adequate current evidence can stay at Level 0 or 1.

**Level and Layer are orthogonal:** choose one Level for the whole decision; use Layers only to locate where the material uncertainty lives. A Level 1 check may stop in Reality Interface, Model Space, or Decision Space. Do not assign separate Level scores to each Layer.

For new or repurposed domain state, use the proportionate ownership check below. An ordinary field under an existing authority is not automatically an architecture investigation. Explicit invocation still permits Level 0.

## Layer 0 — Reality Interface

Before deepening an explanation, ask whether the available input is a projection of a higher-dimensional situation.

**In human–AI or multi-agent collaboration, the task description is itself a projection.** Treat another agent's wording as evidence about reality and about that observer's viewpoint, not as reality itself. Ask boundary questions only when a missing dimension could change the action. The agent's response is also a projection and should remain open to correction against reality.

### Projection check

Bind important observations to the conditions under which they were produced when relevant:

- **Position:** whose viewpoint or system boundary produced the observation?
- **State:** what operating/human/system state may affect the projection?
- **Context:** what constraints and surrounding conditions were present?
- **Time / revision:** when and under which version/configuration did it occur?
- **Granularity:** function, request, workflow, organization, relationship, market, or other scale?
- **Instrument:** log, metric, screenshot, summary, user report, OCR, query, model output, language description?
- **Missing dimensions:** what material variables may never have entered the sample?
- **Intervention:** did the act of measuring, asking, prompting, testing, or probing change the observed system?

A partial projection is not invalid evidence. It is evidence with boundaries.

### Problem-frame audit

Before solving a consequential problem, ask:

- Who defined the current problem?
- Which nouns or labels already contain an explanation?
- If rewritten as observations only, does the same problem still exist?
- Would another viewpoint, time window, scale, or stakeholder produce a different shape?
- Are all current hypotheses trapped inside the same frame?

Use **Rotate** as a technique, not a peer of Branch or Generate: change viewpoint, scale, time, stakeholder, representation, or system boundary when another projection can reveal a missing dimension.

Quick rule:
- **Branch = change explanation** inside the current frame when rivals make different predictions.
- **Generate = change coordinate system/frame** when current candidates share the same limiting frame.
- **Rotate = change observation angle** to obtain a projection that can support Generate or reframe the problem.

Read [core](references/core.md) for deeper definitions and examples.

## Layer 1 — Model Space

**Observe → Separate → Branch / Generate → Attack → Update**

These are combinable functions, not a required output format or instructions to expose private reasoning.

1. **Observe:** Preserve reports and measurements with source and projection conditions when material. A reported symptom is not a measured cause.
2. **Separate:** Distinguish observations, experiences, frames, interpretations, hypotheses, and decisions. Example: `no message for three days` (Observation) → `I feel disappointed` (Experience) → `is the relationship becoming distant?` (Frame) → `they may be pulling away` (Interpretation) → `their investment may have decreased` (Hypothesis) → `I will not increase contact yet` (Decision). User and agent explanations are not automatically facts.
3. **Branch:** Keep only plausible alternatives that could change action, plus material unknowns. No hypothesis quota.
4. **Generate:** When current hypotheses share the same frame or predictions, consider a different coordinate system, scale, stakeholder, or mechanism rather than manufacturing more variants of the same model.
5. **Attack:** For consequential models, state feasible observations that would lower confidence, narrow scope, or reveal the frame as wrong. Prefer discriminating evidence.
6. **Update:** Revise the current best model or frame when warranted; preserve superseded explanations and why they failed. Repeated summaries and agreement are not independent evidence. An unrun test is a plan.

**Observer Audit:** Check sampling, measurement coverage, source independence, anchoring, observer state, observation position, scale, projection loss, and intervention effects when material. Do not invent personal motives.

**Overfit Detector:** If contradictions are repeatedly explained away, a theory explains every scale and outcome, or confidence grows without new independent evidence, narrow the claim, rotate the frame, and seek a real falsifier. Do not oppose a sound model merely to show skepticism.

## Layer 2 — Decision Space

Understanding does not determine action by itself.

Before expanding investigation or acting, identify:

- **Goal:** what decision, understanding, or outcome is this analysis for?
- **Agency:** what can actually be changed, observed, delayed, or delegated?
- **Reversibility:** which actions can be rolled back, and which alter the state space or other people/systems?
- **Intervention effect:** will the test itself change the system being measured?
- **Value of information:** would more evidence plausibly change the next action? Example: one 2-minute `EXPLAIN` could decide whether an index change is justified → high enough value to run it; a fourth equivalent `EXPLAIN` after three consistent runs is unlikely to change the action → stop.
- **Cost of delay:** what is lost by waiting?
- **Authorization:** what actions are already permitted?

Choose among three legitimate outputs:

- **Act** — evidence supports the effective authorized action.
- **Probe** — run the smallest useful discriminator that can change the decision.
- **Wait** — deliberately allow time or natural system evolution to generate information that cannot be obtained cheaply by intervention.

Prefer reversible informative action when evidence is insufficient, but do not fragment a justified solution into endless probes.

## Conditional engineering checks

Read only what affects the decision:

- [Hypothesis gate](references/hypothesis-gate.md): before an uncertain cause becomes a change.
- [Model staleness](references/model-staleness.md): when history conflicts with present behavior.
- [Model duplication](references/model-duplication.md): when records may encode the same fact.
- [State ownership](references/state-ownership.md): **No New State Without Ownership Proof.** Classify new/repurposed state as `AUTHORITATIVE_TRUTH`, `DERIVED_PROJECTION`, `OPERATIONAL_STATE`, or `HISTORICAL_EVIDENCE`; identify authority, writers, identity/version, lifecycle, and recovery.
- [Decision cost](references/decision-cost.md): when investigation grows. Limit checks to those that can change action and account for delay.

## Stop and continue

End analysis when evidence supports action, all plausible frames lead to the same low-risk action, another pass adds no evidence/prediction/action change, the expected value of information is below its cost, the agreed budget expires, or useful information requires execution or time.

Exit with the current best model or unresolved frame, material unknowns, and one of: authorized action, discriminating probe, or concrete waiting condition. State what evidence would reopen the model.

A spent budget neither proves a cause nor authorizes risky implementation. Urgent authorized containment can precede root-cause analysis. Stopping analysis is not stopping the task.

Use [working state](references/state.md) for updates/handoff, not as a mandatory form. Normally present only the judgment, decisive evidence/unknowns, and action. [Tests](tests/README.md) and Pilot evidence are evaluation material, not default task context.
