---
name: openmodel-development
description: Implement bug fixes and requirements by separating the user's observable reality and business intent from the code facts the agent can investigate. For bugs, treat the reported symptom as the entry point rather than a proven root cause. For requirements, treat the requested outcome and business semantics as authoritative constraints while independently investigating the current implementation.
metadata:
  status: prototype
---

# OpenModel — Development

Development turns a real symptom or requested outcome into a verified code change.

It has two entry modes:

- **Bug:** symptom → investigate → locate failure path → change → verify.
- **Requirement:** desired behavior → inspect current system → change → verify.

The model owns investigation of observable code facts. The user supplies reality the code cannot establish.

## Shared rules

1. **Investigate available code facts yourself.**
   Inspect relevant source, callers, readers/writers, tests, schema, configuration, history, logs, and authorized tools instead of asking the user to restate facts the model can obtain.

2. **Separate user reality from suggested implementation.**
   A user's symptom, desired behavior, or business rule can be authoritative for that reality. A proposed root cause or implementation remains a candidate until supported by code/evidence.

3. **Trace enough impact to make the change safely.**
   Follow affected behavior and state until the implementation and material regression surface can be judged. Expand further only when new investigation could change the implementation, risk, or verification.

4. **Check evidence coverage.**
   Before relying on a log, metric, test, or code path, ask what part of the claimed failure/behavior it actually covers and what material part it omits.

5. **Ask only across the reality boundary.**
   Ask the user when code/tools cannot establish a fact and the answer could materially change implementation or acceptance.

6. **Verify observable behavior, not only code shape.**
   A successful edit or passing narrow test is not by itself proof that the reported bug is fixed or the requested behavior is delivered.

## Bug mode

### User owns

- the symptom they actually observed;
- relevant production/user-visible conditions they can report;
- business meaning not represented in accessible code.

The user's proposed root cause is context, not proof.

### Agent owns

- locating the relevant implementation;
- reproducing or otherwise grounding the failure when feasible;
- tracing the failure path;
- distinguishing cause from correlated symptoms;
- implementing the smallest correct change that addresses the failure;
- checking affected regression paths.

### Bug completion

A bug task is complete when the failure path is understood well enough to justify the change, the original failure case is no longer reproduced or an equivalent observable verification succeeds, and material affected behavior has been checked.

Do not require a metaphysically final root cause when a bounded, verified fix is sufficient.

If the original symptom cannot be reproduced or observed, state that boundary and verify the strongest available proxy without pretending it proves production resolution.

## Requirement mode

### User owns

- the desired observable outcome;
- business semantics they explicitly define;
- acceptance constraints outside the codebase.

A user's suggested implementation is a proposal unless they explicitly require it as a constraint.

### Agent owns

- understanding current behavior;
- identifying the implementation and affected contracts;
- reusing existing mechanisms where appropriate;
- choosing and implementing a technically sound solution within the stated constraints;
- verifying the requested observable behavior and relevant regressions.

### Requirement completion

A requirement task is complete when the requested observable behavior is implemented, relevant existing behavior has not suffered unacceptable regression, and no unresolved code-external fact blocks acceptance.

## When to ask the user

Good questions concern reality the model cannot establish, for example:

- "Does approved mean the document must already exist, or may generation finish asynchronously?"
- "Does this external consumer exist outside the repositories I can inspect?"
- "When you say the UI freezes, is the request timing out, the browser becoming unresponsive, or the background task remaining pending?"

Do not ask:

- where a symbol is used when code search can answer;
- whether tests exist when the repository can answer;
- what a field currently does when its readers/writers can be inspected.

## Handoff to Code Review

After Development produces a change, Code Review should independently inspect the resulting code facts and impact.

Provide the reviewer the requirement or observed symptom and necessary external business facts. Treat Development's root-cause explanation and implementation rationale as context, not as facts the reviewer must inherit.

> **Development creates the change; Code Review independently tests what the change actually means.**
