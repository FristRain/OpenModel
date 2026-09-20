# State ownership

## No New State Without Ownership Proof

Before adding or repurposing durable state, a status, version, snapshot, manifest, or cache, explain its meaning and ownership. This is an engineering contract, not a demand for a new framework or approval.

Reuse existing contracts. A normal CRUD field can use one sentence referencing its established entity owner and lifecycle. A new authority or cross-system boundary requires more evidence.

| Role | Meaning | Boundary |
|---|---|---|
| `AUTHORITATIVE_TRUTH` | Designated owner of a particular domain fact within a declared scope. | Define permitted writers, revision/concurrency rules, and conflicts. One logical authority can have multiple physical replicas. |
| `DERIVED_PROJECTION` | Representation computed from authoritative input for display, search, or another purpose. | Name source identity/revision, derivation, freshness, invalidation, and rebuild. No independent domain edits. |
| `OPERATIONAL_STATE` | Progress/coordination of an attempt: queued, running, retrying, lease ownership. | Name attempt and lifecycle. Worker completion does not prove the intended domain effect. |
| `HISTORICAL_EVIDENCE` | Preserved evidence of what was observed, requested, or accepted at a past boundary. | Define event identity, provenance, integrity, retention, and corrections. It does not assert the latest state. |

Classify by **fact or field**, not blindly by table. A frozen payload and mutable delivery status have different roles. Immutable does not automatically mean historical: an immutable revision can be authoritative for that revision. Historical evidence may be authoritative about a past event without owning present state.

## Proportionate proof

Answer relevant questions using current schema, call paths, tests, and existing contracts:

1. What exact fact does it represent, for which entity/event/revision?
2. Which role applies? Who is the logical authority?
3. Does existing state express it? Why reuse/derive it, or why is another representation necessary?
4. Who creates, reads, changes, and terminates it? Which transitions are valid?
5. How are upstream/downstream identities and versions bound? What rejects stale writes?
6. What happens after partial writes, crashes, retries, and out-of-order delivery? How is success verified?
7. How are projections invalidated/rebuilt, evidence retained/corrected, and attempts retired?
8. What test could show two conflicting current truths?

A verified contract link is better than repeating it. Unknown ownership defers the dependent state addition, not unrelated work; it is not a new user-approval gate.

## Small example

A fictional order's shipping-address field stays under the order's established authority and transaction rules: no separate ceremony is needed.

A "current shipping-address snapshot" independently edited by another service is different. Prove that it owns a distinct fact or make it a revision-bound projection. A dispatch receipt preserving the address actually used can be historical evidence and must not overwrite the current order address on replay.

See [duplication](model-duplication.md) for recovery probes.
