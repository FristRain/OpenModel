---
name: openmodel-development
description: Develop new systems, implement requirements, and fix bugs by building a sufficiently complete shared model of the system before changing code. Expand only material perspectives, investigate observable facts independently, ask only for load-bearing external reality, distinguish local patches from design corrections with evidence, make architectural debt explicit, then implement and verify at the strongest reachable evidence level.
metadata:
  status: prototype
---

# OpenModel — Development

Development turns an idea, requirement, or observed failure into a verified system change without silently converting an incomplete system model into code.

It specializes the Core flow as:

| Core | Development |
|---|---|
| Expand | Expand |
| Observe | Reconstruct |
| Align | Align |
| Decide | Classify + Confirm when needed |
| Act | Implement |
| Verify | Verify |

The development flow is:

**Expand → Reconstruct → Align → Classify → Confirm → Implement → Verify**

Not every task needs every step. Local work stays local unless evidence shows it crosses an existing contract, state boundary, lifecycle, failure boundary, or other material system boundary.

## Materiality rule

A perspective, question, or investigation is material only if it could change at least one of:

- the chosen implementation or action;
- PATCH vs DESIGN CORRECTION;
- acceptance criteria;
- severity or urgency;
- compatibility or migration requirements;
- whether implementation should proceed.

When unsure, state in one sentence:

> **If this fact were different, which development decision would change?**

If no decision would change, do not expand the investigation.

## Entry modes

### 1. New project

For a new system, do not begin by freezing the idea into tables, APIs, services, or classes.

First establish the important overall workflow and system skeleton.

Identify only the material parts of:

- primary actors;
- entry and exit points;
- main end-to-end workflow;
- important states and transitions;
- authoritative facts and owners;
- external systems and dependencies;
- failure/retry/recovery paths that affect the design;
- business completion and acceptance conditions;
- major operational constraints.

A useful skeleton often looks like:

**Actor → Trigger → Workflow step → State change → Authority → Failure path → Outcome**

The goal is not exhaustive requirements capture. It is to expose missing load-bearing structure before implementation choices harden it.

### 2. New requirement

Treat the requested behavior as an outcome to locate inside the existing system.

Before implementing, reconstruct enough to determine:

1. where the requirement enters the current workflow;
2. which responsibilities, state, contracts, callers, consumers, and lifecycle it affects;
3. which external business boundaries materially change implementation;
4. whether it fits the current design or conflicts with it;
5. whether the change is PATCH, DESIGN CORRECTION, or UNCERTAIN.

A user's suggested implementation is a proposal unless explicitly required as a constraint.

### 3. Bug

Treat the reported symptom as evidence, not as the proven cause.

Before fixing:

1. reconstruct the affected end-to-end path;
2. identify the observed failure and its scope;
3. inspect code, logs, tests, state, configuration, deployment/revision, and relevant runtime evidence;
4. widen the view only to other layers or perspectives that could change the diagnosis or fix;
5. determine whether the failure is local or exposes a design conflict;
6. classify the fix as PATCH, DESIGN CORRECTION, or UNCERTAIN.

Do not stop at “the symptom disappeared” if the mechanism that created the failure is still present.

## Reconstruct before changing

For an existing system, reconstruct enough of the current path to answer the material questions:

- what happens now;
- where the reported requirement or failure sits;
- which components participate;
- which state changes;
- which facts are authoritative;
- who reads and writes them;
- what happens on failure/retry;
- what downstream behavior depends on the path.

Do not ask the user for code facts that can be inspected.

Do not infer production behavior from source alone when deployment identity, configuration, workload, data shape, or runtime evidence could change the conclusion.

## Align reality boundaries

Ask the user only when a fact:

1. cannot be established from available code/tools/evidence; and
2. could materially change the design, diagnosis, acceptance criteria, or action.

Prefer narrow boundary questions.

Examples:

- “Does ‘approved’ mean the business transaction is complete, or must the PDF already exist?”
- “May this workflow complete asynchronously after the user receives success?”
- “Can two operators legitimately update this state concurrently?”
- “Does an external system outside the accessible repositories consume this field?”

When a user-provided constraint becomes load-bearing, clarify its status if that distinction changes the design:

- mandatory policy or contract;
- business requirement;
- current practice;
- preference;
- assumption.

For example, “the API cannot change” should not silently become an immutable design constraint until it is clear whether this is an external contract or a preference for compatibility.

The model should discover which question matters. The user should not have to perform the architectural analysis first.

## Evidence-backed challenge

When the user's explanation, design assumption, or proposed fix conflicts with observable evidence, state the conflict.

A useful challenge identifies:

- the claim or implied assumption;
- the conflicting evidence;
- the scope and limits of that evidence;
- the consequence for the current diagnosis or design;
- what evidence would resolve the disagreement if still material.

Evidence must match the claim's scope and time horizon.

Examples:

- Current query latency can challenge a claim that the database is the present bottleneck, but does not by itself refute a future peak-capacity requirement.
- Source code can challenge an explanation of what the code path does, but does not prove which revision is deployed.
- A user can report “the page feels slow”; measurement may challenge the proposed technical cause without invalidating the reported experience.

Do not challenge merely to appear independent.

## Change Conflict Gate

Before materially changing code, classify the change.

### PATCH

Use PATCH when:

- the existing design remains sound;
- the defect or requirement is local and bounded;
- the change does not create a new authority, competing writer, hidden lifecycle, or structural exception;
- the fix addresses the mechanism creating the failure or satisfies the requirement within the established contract.

Examples may include a wrong condition, mapping bug, missing validation, incorrect query predicate, or a bounded compatibility fix.

### DESIGN CORRECTION

Use DESIGN CORRECTION when evidence shows the existing design is part of the problem.

Signals include:

- duplicate current truth;
- new competing writers;
- responsibility leakage across layers;
- one workflow owning unrelated lifecycle work;
- repeated special-case branches;
- retries or partial failure revealing missing lifecycle semantics;
- a requirement that must bypass an established contract;
- recurring failures caused by the same structural boundary;
- a patch that removes the symptom while preserving the mechanism;
- state that cannot be rebuilt, reconciled, or authoritatively owned;
- synchronous coupling that conflicts with the actual business completion boundary.

A design correction is not “cleaner code.” It must be tied to concrete failure, inconsistency, lifecycle, ownership, coupling, or change-impact evidence.

### UNCERTAIN

Use UNCERTAIN when evidence is insufficient to distinguish a local defect from a design problem.

Obtain the smallest additional evidence that could change the classification.

Stop the UNCERTAIN loop when the Core stop condition applies: if the next evidence is unlikely to change the classification, is unavailable, requires execution/time, or costs more than its decision value, stop and choose the safest justified reversible action or explicitly defer the classification.

Do not invent certainty to escape UNCERTAIN.

## Confirm material conflicts

When PATCH and DESIGN CORRECTION are both viable and materially different paths, present both before implementation.

For each path, explain:

- what changes;
- what evidence supports it;
- what it fixes;
- what it leaves unresolved;
- blast radius and maintenance consequences;
- business urgency and delay cost;
- migration or compatibility impact;
- rollback/recovery considerations when relevant.

Then obtain the user's decision.

The model performs the analysis; the user chooses among materially different business/engineering tradeoffs.

### Loud Patch

A user may knowingly choose PATCH even when DESIGN CORRECTION is better structurally.

That is a valid terminal decision when the requested patch is authorized and acceptable.

Execute it, but make the debt explicit:

- what structural problem remains;
- what the patch does and does not solve;
- expected consequences or risk;
- rollback point when relevant;
- the condition that should reopen DESIGN CORRECTION.

> **The protocol prevents silent debt, not informed debt.**

Do not keep re-arguing for redesign after the user has made an informed choice unless new material evidence appears.

## Implementation contract

Before coding, have enough shared understanding to state, as needed:

- desired observable outcome;
- affected workflow;
- important business semantics;
- relevant state/ownership;
- chosen PATCH / DESIGN CORRECTION / bounded UNCERTAIN path;
- compatibility constraints;
- acceptance criteria;
- meaningful failure/recovery expectations.

This need not be a formal document for every task.

For a small task it may be one or two sentences. For a substantial change it should be explicit enough that implementation and review can verify the same target.

## Implementation

Once the path is justified and confirmed when required, implement with high autonomy.

The model owns:

- code changes;
- reuse of existing mechanisms;
- schema/API changes within the agreed contract;
- tests;
- migration logic when required;
- observability needed to verify the change;
- regression checks;
- local refactoring needed to keep the implementation coherent.

Do not keep asking the user questions that code or engineering judgment can answer.

If implementation reveals evidence that invalidates the shared model, stop patching around it and return to Reconstruct / Align / Classify.

Sunk implementation cost is not evidence that the current model is correct.

## Verification

Verification must test the real goal at the strongest reachable evidence level.

### T0 — The verifier must be capable of expressing the failure

For a bug, a passing test is not evidence of a fix if the test environment cannot reproduce or represent the original failure mode.

Before claiming the bug is verified, establish that the baseline/control can express the relevant failure or that the chosen proxy actually exercises the mechanism under test.

Examples:

- a serial mock cannot verify elimination of a concurrency race;
- an in-memory stub that bypasses transaction behavior cannot verify a database deadlock fix;
- a unit test that never executes the deployment-specific branch cannot verify that production path.

If T0 is not met, label the result as a narrower check rather than bug resolution.

### Verification strength and graceful degradation

Use the strongest reachable evidence. Do not block useful work merely because production verification is unavailable, and do not claim more than the evidence supports.

Possible evidence levels include:

- static/source reasoning;
- focused unit or local test;
- integration or representative local/staging test;
- representative runtime measurement;
- observed production outcome.

These are not mandatory labels or a universal hierarchy. State the strongest evidence actually obtained and the material gap that remains.

A local pass may justify merging a bounded fix while leaving production resolution unverified.

### For a bug

Verify:

- T0 is satisfied for the claimed level of verification, or the limitation is explicit;
- the original failure or strongest valid reproduction no longer occurs;
- the failure mechanism addressed by the chosen fix is actually changed;
- materially affected regression paths still work;
- remaining uncertainty is explicit;
- a PATCH is not falsely reported as a DESIGN CORRECTION.

### For a requirement

Verify:

- the requested observable outcome exists at the strongest reachable level;
- the affected workflow behaves consistently;
- important prior behavior has not regressed;
- acceptance boundaries are satisfied;
- new state, contracts, or lifecycle behavior match the agreed model.

### For a new project

Verify incrementally against the system skeleton:

- implemented flows still match the intended end-to-end workflow;
- state ownership remains coherent;
- feature implementations do not silently redefine core business semantics;
- newly discovered reality is folded back into the shared model.

Passing tests are evidence, not proof of all real-world behavior.

## Completion

A development task is complete when:

- the relevant system model is sufficient for the decision;
- material external reality has been aligned;
- any material patch-versus-design conflict has been made explicit and resolved or intentionally deferred;
- the implementation matches the agreed path;
- verification supports the strongest claim actually made;
- known remaining uncertainty or debt is stated rather than hidden.

> **Do not optimize for satisfying the current request at the expense of silently damaging the system that must carry it.**
