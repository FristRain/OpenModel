# Evidence Core migration and non-goals

Base: `fact-boundary-prototype` (PR #5), not `main` (v0.2). This branch is additive to avoid discarding the established Shared Reality and domain boundaries.

## Decision record

Problem: claims, verification receipts and unknowns are presently mostly prose. Proposed change: optional integrity envelope and precise verification limitations. Not proposed: replacing the domain protocol, forcing Evidence on trivial work, auto-authorizing mutations, rewriting git tools, or embedding REA's binary adapters.

State ownership:
- Evidence belongs to the transient investigation/session; the ledger is authoritative only for what has been *recorded*, not reality.
- Claims belong to the agent investigation model, remain hypotheses until justified, and can be superseded without changing evidence.
- Runtime source systems (Git, traces, tests) remain authoritative for their respective factual observations.
- No new persistent state is introduced. Export, storage, provenance attestation and retention are deferred until requirements justify them.

## Progressive adoption

P0: Use the lightweight Evidence Core only for consequential debugging and change review.
P1: Attach real provider adapters with stable target/revision identity and explicit capability limitations.
P2: Feed evidence IDs into the existing PATCH / DESIGN CORRECTION and T0 decisions.
P3: Run matched A/B cases; remove or simplify features if they increase cost without improving decisions.

## Known limitations

Prototype `assess` checks existence, T0 flag, and pass status. It does not semantically judge whether a test expresses a claimed failure, nor whether test scope equals claim scope. Human/domain validation remains mandatory. `confidence` values are assertions by the source, not calibrated probabilities. No MCP runtime implementation has been added.
