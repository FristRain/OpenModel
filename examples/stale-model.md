# Stale model

**Fictional teaching case.** No private service, deployment, or task flow is reproduced.

**Historical explanation:** "Generating a preview blocks document submission."

**Current report:** Submission is still slow. A proposed refactor moves preview generation to background work.

**Competing models:** The old synchronous path remains active; the fix exists in source but is not deployed; or background generation is active and latency arises elsewhere, possibly shared-resource contention.

**Discriminator:** Inspect the current call path/configuration, verify deployment identity, and correlate request completion with generation start. An enqueue function name alone cannot settle the question.

**Round-one evidence:** Current source queues preview generation; deployed revision is unknown.

**Update:** The old explanation is weaker for this source path. Production applicability remains unresolved; do not declare the issue fixed.

**Round-two stipulated evidence:** A matching deployed revision and trace show request completion before generation starts, with most request time in a separate validation stage.

**Update:** Direct blocking is downgraded for those requests. Background resource contention is still possible. Validation becomes the next measured path; its root cause is not yet established.

**Act and stop:** Investigate the validation span instead of rebuilding an existing asynchronous boundary. Retain the old explanation with its historical scope. Reopen if another active path executes generation inline or representative traces contradict the model.
