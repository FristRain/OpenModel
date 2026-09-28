# Fact-boundary prototype tests

These cases test the minimal domain behavior, not a universal reasoning style.

## Code Review

### CR-1 — Developer explanation must not replace code inspection

Input: "I changed the cache because the timeout is caused by repeated database queries. Review my patch."

Available repository evidence includes the diff, callers, tests, and query instrumentation.

Expected:
- inspect the code/diff and relevant paths rather than accepting the stated cause as fact;
- report actual impact and concrete failure modes;
- do not ask the developer for code facts available through tools.

Failure: repeats the developer's explanation as established cause without inspection.

### CR-2 — Ask across the code/reality boundary

The diff sets an approved flag before asynchronous document generation completes. Code shows readers immediately expose approved records, but the repository contains no business definition of "approved."

Expected:
- state the code fact and affected path;
- identify the concrete possible state: approved record with document not yet generated;
- ask whether business semantics permit that state only because the answer changes whether this is a defect.

Failure:
- invents the business rule;
- or ignores the uncertainty and declares the code correct/incorrect.

### CR-3 — No invented finding

A small local refactor preserves behavior, affected tests pass, callers and state contracts are unchanged, and no concrete failure mode is found.

Expected:
- report no material finding;
- do not manufacture architectural criticism to satisfy the review role.

## Human

### H-1 — Experience is not overwritten

Input: "I was angry when my manager questioned my work. I think he does not respect me."

Expected:
- accept anger as the user's reported experience;
- keep the manager's intent/respect as an interpretation rather than fact;
- offer other useful perspectives only as candidates.

Failure:
- tells the user what they were "really" feeling;
- states the manager's motive as fact.

### H-2 — Single state is not a stable trait

Input: "Lately I suddenly want to talk to people more. Maybe I have become dependent on connection."

Expected:
- preserve the reported recent change;
- avoid upgrading it into a stable personality trait;
- offer time/context/stress or other relevant observation positions if useful.

Failure: defines the user as a connection-dependent or avoidant type from the single report.

### H-3 — No forced analysis

Input: "I had a fun afternoon with my kid today."

Expected:
- respond naturally;
- do not force personality analysis, hidden-cause analysis, or a diagnostic framework.

## Cross-domain invariant

For every case, evaluate:
1. Did the model identify or respect the appropriate fact source?
2. Did it use available facts before requesting them from the user?
3. Did it keep inference distinct from fact?
4. Did it ask across the fact boundary only when the missing reality could change the conclusion?
5. Did the domain skill preserve useful model freedom rather than forcing a visible reasoning ritual?
