# Evidence Core (experimental, opt-in)

REA-inspired **ideas**, not REA code: explicit provenance, content-addressed immutable records, unknowns and honest verification limits. See [CORE](../CORE.md) and [Development](../domains/development/SKILL.md). OpenModel is still primarily a reasoning protocol, not a universal MCP server.

## Integration invariant

Do not replace Shared Reality, Hypothesis Gate, Change Conflict Gate, State Ownership Gate, Loud Patch or T0. Evidence Core supplies machine-checkable *receipts* to those rules where the cost is justified. Level 0 work does not require a ledger.

1. Identify project target and revision. The same source path at different revisions is not the same target.
2. Record provenance and confidence separately: observed / derived / inferred; label human report as such.
3. Store claims independently from observations. A hash proves record integrity, not fact truth, provider honesty, or source independence.
4. Record rival explanations and discriminating falsifiers only when they change the decision.
5. Mark missing coverage as unknown, not as evidence of absence.
6. A passing test proves only a claim that the test can express (T0). Mock-only tests must not prove real concurrency or production behavior.
7. If a provider is unavailable, report limitations; never silently substitute inferred results for runtime observations.
8. New durable state requires the existing ownership proof; this reference does not authorize extra database tables, background tasks or deployments.

## Prototype interface

`openmodel_evidence.py` exports `seal`, `verify`, `EvidenceLedger`, `Claim`, `Verification`, `assess`. The ledger is intentionally **session-local**, not durable or concurrent. IDs use a domain-separated SHA-256 over canonical JSON; mutation-safe copy-in/copy-out applies. The prototype validates structural identity and reference existence but does not prove provider authenticity, independent observations, real target identity, or test adequacy. `assess(...)=supported` is **not** an authorization to merge or deploy.

## Provider adoption

Existing GitNexus/CodeGraph or trace/test tools remain independent. Wrap their outputs only at a decision boundary requiring traceability. A provider record should declare provider name/version, supported actions, target/revision, side effects, source scope, and partial failures. Prefer existing tool calls. Do not declare a new MCP server until the host has a demonstrated need.

## Verification gates

- **Evidence Gate:** Which observations support the claim? Which are inference or user reports? Are version, time, and scope comparable?
- **Causal Gate:** Which competing mechanism predicts a different outcome? What would falsify the preferred explanation?
- **Change Gate:** Is the proposed action PATCH / DESIGN CORRECTION / UNCERTAIN? Existing material trade-off confirmation remains authoritative.
- **T0 Gate:** Could the verifier actually exhibit the original failure? If not, report a narrower claim.
- **Release Gate:** State what is verified and what remains unknown; do not infer a production fix from a unit-test pass.

## Evaluation

Compare main/v0.2, the fact-boundary prototype, and evidence-enabled prototype on identical held-out prompts, fixtures and scoring rubrics. Blind grade root-cause accuracy, unsupported claims, omitted constraints, regression, tool/time/token cost. Do not call documentation checks an agent-behavior benchmark.

## Security / privacy

Avoid writing raw private logs, credentials, machine paths and internal addresses to public fixtures, Git history, or exports. Content hashes do not anonymize sensitive payloads. Redact before sealing, explicitly recording resulting limitations.
