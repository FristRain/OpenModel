---
name: openmodel-development
description: Develop new systems, implement requirements, and fix bugs by building a sufficiently complete shared model of reality before changing code. The model should expand the user's initial view, investigate observable system facts independently, ask only for material external reality, expose patch-versus-design conflicts with evidence, obtain user confirmation for materially different design paths, then implement and verify against the end-to-end outcome.
metadata:
  status: prototype
---

# OpenModel — Development

Development turns an idea, requirement, or observed failure into a verified system change without silently converting an incomplete problem model into code.

The shared development flow is:

**Expand → Reconstruct → Align → Classify → Confirm → Implement → Verify**

Not every task needs every step. Simple, local, low-risk work should remain simple.

## Core responsibility

The user's description is the entry point, not the full system model.

The model is responsible for:

- finding missing perspectives that could change the design or fix;
- inspecting observable code/runtime facts itself;
- identifying which real-world boundary questions actually matter;
- challenging unsupported explanations when evidence conflicts;
- distinguishing a local patch from a design correction;
- explaining architectural consequences before implementation;
- and verifying the final result against the real outcome, not only the edited code.

The user is responsible for reality the model cannot directly establish, such as business meaning, desired outcomes, external actors, operational practice, priorities, and acceptance boundaries.

## Entry modes

### 1. New project

For a new system, do not begin by freezing the idea into tables, APIs, services, or classes.

First establish the important overall workflow and system skeleton.

At minimum, identify the material parts of:

- primary actors;
- entry and exit points;
- main end-to-end workflow;
- important states and transitions;
- who owns authoritative facts;
- external systems and dependencies;
- failure/retry/recovery paths that affect the design;
- business completion/acceptance conditions;
- major operational constraints.

The goal is not exhaustive requirements capture. The goal is to expose missing structure before implementation choices harden it.

A useful project skeleton often looks like:

**Actor → Trigger → Workflow step → State change → Authority → Failure path → Outcome**

Ask the user only for business or real-world facts that cannot be established elsewhere and that would materially change the skeleton.

### 2. New requirement

Treat the requested behavior as an outcome to locate inside the existing system.

Before implementing:

1. reconstruct the relevant current workflow;
2. identify affected responsibilities, state, contracts, callers, consumers, and lifecycle;
3. identify any missing business boundary that changes implementation;
4. determine whether the request fits the current design or conflicts with it;
5. classify the change as PATCH, DESIGN CORRECTION, or UNCERTAIN.

A user's suggested implementation is a proposal unless explicitly required as a constraint.

### 3. Bug

Treat the reported symptom as evidence, not as the proven cause.

Before fixing:

1. reconstruct the affected end-to-end path;
2. identify the observed failure and its scope;
3. inspect code, logs, tests, state, configuration, deployment/revision, and relevant runtime evidence;
4. widen the view to other plausible system layers or perspectives when they could change the diagnosis;
5. determine whether the failure is local or exposes a design conflict;
6. classify the fix as PATCH, DESIGN CORRECTION, or UNCERTAIN.

Do not stop at “the symptom disappeared” if the mechanism that created the failure is still present.

## Expand the view

The model should actively look for perspectives the initial request may omit.

Relevant perspectives may include:

- user-visible behavior;
- business workflow;
- frontend/browser behavior;
- API/request lifecycle;
- background jobs;
- database/query/transaction behavior;
- resource ownership and hold time;
- state ownership and competing writers;
- retries, partial failure, recovery, idempotency, and concurrency;
- external consumers;
- configuration and deployed revision;
- observability coverage;
- future maintenance and repeated special cases.

Do not enumerate perspectives mechanically.

Only expand when another viewpoint could materially change the diagnosis, implementation, or acceptance criteria.

## Reconstruct before changing

For an existing system, reconstruct enough of the current path to answer:

- what happens now;
- where the reported requirement or failure sits;
- which components participate;
- which state changes;
- which facts are authoritative;
- who reads and writes them;
- what happens on failure/retry;
- what downstream behavior depends on the current path.

Do not rely on the user's explanation for code facts that can be inspected.

Do not infer production behavior from source alone when deployment identity, configuration, data shape, or runtime evidence materially matters.

## Align reality boundaries

Ask the user when a fact:

1. cannot be established from available code/tools/evidence; and
2. could materially change the design, diagnosis, acceptance criteria, or action.

Prefer narrow boundary questions.

Good examples:

- “Does ‘approved’ mean the business transaction is complete, or must the PDF already exist?”
- “May this workflow complete asynchronously after the user receives success?”
- “Can two operators legitimately update this state concurrently?”
- “Does an external system outside the accessible repositories consume this field?”
- “Is preserving the current API contract mandatory, or may it change?”

Avoid broad questions such as:

- “Can you describe all edge cases?”
- “Can you explain the whole architecture?”
- “Where is this function used?” when code search can answer it.

The model should discover which question matters. The user should not have to perform the architectural analysis first.

## Evidence-backed challenge

When the user's explanation, design assumption, or proposed fix conflicts with observable evidence, state the conflict.

A useful challenge should identify:

- the user's claim or implied assumption;
- the conflicting evidence;
- the scope and limits of that evidence;
- the consequence for the current diagnosis or design;
- what evidence would resolve the disagreement if still uncertain.

Examples:

- “The request is described as database-bound, but the measured query stage is short and the connection is held during serialization; the current evidence does not support database capacity as the primary bottleneck.”
- “This is described as a local field addition, but the proposed writer creates a second mutable source for current status; that crosses the existing state-ownership boundary.”

Do not challenge merely to appear independent.

## Change Conflict Gate

Before materially changing code, classify the change.

### PATCH

Use PATCH when:

- the existing design remains sound;
- the defect or requirement is local and bounded;
- the change does not create a new authority, competing writer, hidden lifecycle, or structural exception;
- the fix addresses the mechanism creating the failure or satisfies the requirement within the established contract.

Examples may include a wrong condition, mapping bug, missing validation, bounded retry defect, incorrect query predicate, or a clearly local compatibility fix.

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

Do not default to patching simply because it is easier.

Obtain the smallest additional evidence that could change the classification.

## User confirmation for material conflict

When PATCH and DESIGN CORRECTION are both viable but materially different paths, present both before implementation.

For each path, explain:

- what changes;
- what evidence supports it;
- what it fixes;
- what it leaves unresolved;
- architecture/maintenance consequences;
- migration or compatibility impact;
- rollback/recovery considerations when relevant.

Then obtain the user's decision.

The goal is not to make the user choose architecture unaided. The model should perform the analysis and present the tradeoff clearly.

Do not silently choose a patch that creates architectural debt.

Do not force redesign when a local fix is genuinely sufficient.

## Implementation contract

Before coding, the model should have enough shared understanding to state, as needed:

- desired observable outcome;
- affected workflow;
- important business semantics;
- relevant state/ownership;
- chosen PATCH or DESIGN CORRECTION path;
- known compatibility constraints;
- acceptance criteria;
- meaningful failure/recovery expectations.

This need not be a formal document for every task.

For a small task it may be one or two sentences.

For a substantial change it should be explicit enough that implementation and review can verify the same target.

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

## Verification

Verification must test the real goal, not only the code shape.

### For a bug

Verify:

- the original failure or strongest available reproduction no longer occurs;
- the failure mechanism addressed by the chosen fix is actually changed;
- materially affected regression paths still work;
- any remaining uncertainty is explicit;
- a patch is not falsely reported as a structural fix.

### For a requirement

Verify:

- the requested observable outcome exists;
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

- the relevant reality and system model is sufficient for the decision;
- any material patch-versus-design conflict has been made explicit and confirmed;
- the implementation matches the agreed path;
- verification supports the real outcome;
- known remaining uncertainty or debt is stated rather than hidden.

> **Do not optimize for satisfying the current request at the expense of silently damaging the system that must carry it.**
