# Architecture overfit

**Fictional teaching case.** A minimal inventory example, not a renamed private architecture.

**Problem:** A stock display sometimes disagrees with a reservation operation. The proposed fix adds another mutable "availability snapshot."

**Competing explanations:** Existing layers serve necessary separate purposes; or two components independently own the same current availability fact. More tables alone do not prove duplication.

| Existing representation | Role | Contract to verify |
|---|---|---|
| Inventory ledger and its current revision | AUTHORITATIVE_TRUTH | Owns stock movements and valid reservations for an item. |
| Search availability view | DERIVED_PROJECTION | Derived from ledger revisions; bounded freshness and rebuild rules. |
| Projection job attempt | OPERATIONAL_STATE | Records lease/retry progress, not permission to reserve stock. |
| Reservation receipt | HISTORICAL_EVIDENCE | Preserves the revision and decision used for that reservation. |

These roles are stipulated for the example; an agent must verify them in a real system.

**Ownership proof:** The proposed snapshot has no distinct fact, writer precedence, or recovery rule. Before adding it, identify existing readers/writers, revision binding, and the authoritative reservation decision.

**Attack:** In a local fixture, commit a ledger change, interrupt projection update, and retry an older projection job after a newer one. Check whether stock decisions can use stale display state and whether recovery rejects stale writes.

**Two possible updates:**

- If reservations consult an independently editable display copy, duplicated authority is supported. Route decisions to the established authority and repair projection semantics.
- If reservations already use the ledger and the view follows an explicit freshness contract, separate layers may be legitimate. Investigate whether the symptom is expected lag or a contract violation.

**Act and stop:** Defer the unproven extra snapshot; test the relevant contract. Keep the immutable receipt if historical evidence is required, and do not replay it as current stock truth. Stop once the ownership boundary and recovery action are justified; do not redesign every state in the system.

This is **No New State Without Ownership Proof**, not "no duplication of bytes" or "delete every snapshot."
