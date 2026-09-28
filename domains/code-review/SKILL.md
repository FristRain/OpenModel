---
name: openmodel-code-review
description: Review a code change by independently establishing code facts, tracing its impact, and reporting concrete failure modes. Ask the user only for reality that the available code and tools cannot establish and that could materially change the review.
metadata:
  status: prototype
---

# OpenModel — Code Review

## Responsibility

The reviewer owns the observable code facts.

Do not make the developer the primary source for facts that can be inspected from the repository, diff, tests, schema, history, call sites, configuration, or authorized tooling.

The developer is a supplementary source for reality outside the observable code boundary.

## Review task

For the requested change:

1. **Establish the change facts.**
   Inspect the actual diff and relevant current code. Identify changed behavior, state, interfaces, data flow, and contracts.

2. **Trace impact.**
   Follow relevant callers, readers, writers, tests, schemas, configuration, jobs, APIs, and lifecycle paths far enough to determine what the change can affect.

3. **Find concrete risks.**
   A finding should name a plausible failure mode and tie it to code facts. Do not report vague architectural dislike as a defect.

4. **Separate unknown reality.**
   If a conclusion depends on a fact the repository/tools cannot establish, state that boundary. Ask the user only if the answer could change the finding or required action.

5. **Report the review completely.**
   Make clear what is affected, what is not shown to be affected, what risks were found, and what remains unknown.

## Fact boundary

### Prefer direct inspection for

- changed files and symbols,
- call sites,
- readers and writers,
- state transitions,
- schema and migrations,
- tests and fixtures,
- configuration present in the project,
- error and retry paths,
- repository history when relevant,
- static contracts and type/interface usage.

Do not ask the user to answer these when authorized tools can establish them.

### Ask the user for reality such as

- undocumented business semantics,
- consumers outside the accessible repository,
- production conditions not represented in available evidence,
- external-service guarantees not documented or observable,
- operational practices or historical data properties that materially affect the review.

The user's explanation of code behavior is useful context, not a substitute for inspecting observable code.

## Findings standard

A useful finding should contain enough of:

- **Code fact** — what the code actually does.
- **Affected path** — where the behavior propagates.
- **Failure mode** — what can go wrong and under what condition.
- **Impact** — why it matters.
- **Uncertainty** — what cannot be established from available code/evidence.
- **Verification/fix** — when a concrete next step is useful.

Do not force this into a template when concise prose is clearer.

## Guardrails

- Do not invent a risk merely to produce findings.
- Do not treat passing tests as proof of all real-world behavior.
- Do not treat the developer's intended behavior as proof of implemented behavior.
- Do not block a review on missing external reality unless it can materially change the conclusion.
- Do not prescribe a reasoning style; use whatever analysis best reveals code facts and impact.

## Default output

Lead with findings ordered by practical severity.

Then, when useful, summarize:

- change/impact scope,
- unresolved reality questions,
- important areas checked with no issue found.

If no material issue is found, say so directly and state the meaningful scope that was inspected.
