# Lean redesign decision record (draft)

Base: PR #5 `fact-boundary-prototype`. This branch competes with, and does **not** merge, PR #7's optional Evidence Core experiment.

## Delete from runtime context, retain as optional documentation

- Duplicated philosophy and long checklists in each domain: collapsed into six Core invariants.
- Mandatory phase names and fixed-length outputs: replaced by adaptive decision depth.
- Default loading of pilot studies, examples, A/B scoring material, and evaluation fixtures: these remain offline review resources.
- Mandatory Evidence/Claim/Unknown persistence: rejected for a prompt-first reasoning protocol. Evidence Core remains an optional separate experiment, not a prerequisite.

## Retain, not simplify away

- User first-person truth and material external fact boundaries.
- Independent inspection, rival explanations, falsifiers and model updates.
- State authority/ownership and explicit material patch-vs-design choice.
- T0 verification adequacy; honest scope and unknowns.
- Tool/action authorization, privacy, and stop conditions.

## Proposed acceptance criteria

1. Simple local edit yields immediate execution, no new forms.
2. Performance incident with competing causes demands discriminating evidence, not resource-size guessing.
3. Reviewer independently inspects actual diff and explains concrete impact, or reports limited scope.
4. Development decision differentiates a local patch from lifecycle-level defect.
5. A mocked serial test never proves real concurrency behavior.
6. Personal reflection does not turn inferred motives into facts.
7. Existing `scripts/validate.py` tests and evaluation harness remain usable; future release version and README must be synchronized before publication.

## Architectural choice

One minimal SKILL entry point, one Core, three small domain adaptors, and optional references. No new persistent state or MCP runtime in the lean baseline. A/B validation must measure reasoning quality *and* token/time cost, not count instructions.
