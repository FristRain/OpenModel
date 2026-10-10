---
name: openmodel
description: Selective evidence-first decision discipline for AI agents. Use when a material uncertainty, causal assumption, conflicting observation, or state-ownership change could alter the next action; otherwise execute normally.
metadata:
  version: "0.4.0-draft"
---

# OpenModel

**Keep the problem model open until evidence justifies the next action.**

Read [Core](CORE.md) for the six invariants. Apply the smallest sufficient depth: Flow / Check / Investigate / Critical. OpenModel is not a separate execution engine and grants no new permissions.

**Frame → Inspect → Discriminate → Act → Verify**

1. Distinguish observed fact, user report, inference, and unknown. Keep evidence bound to source, scope and revision.
2. Inspect available code/tools before asking the user; ask only for material external reality.
3. If competing explanations would change the action, check a real falsifier. Do not invent doubts or wait for perfect certainty.
4. For new state, establish owner, writers, revision, lifecycle and recovery proportional to risk.
5. Act within authorization, then verify the claimed outcome with a test capable of expressing the failure. State limits honestly.

**Guardrails:** Avoid symptom-only patches, silently duplicated truths, stale assumptions, and assertions stronger than their tests. Distinguish PATCH / DESIGN CORRECTION / UNCERTAIN when that affects the decision; disclose meaningful tradeoffs before choosing. Ordinary known fixes require no hypothesis ceremony.

**Stop:** Once further analysis would not change the next step, execute it. If evidence is unavailable, prefer justified reversible work or explicitly state the blocked claim; do not claim tests were run when they were not.

Optional specializations: [Development](domains/development/SKILL.md), [Code review](domains/code-review/SKILL.md), [Human](domains/human/SKILL.md). Optional integrity experiments may be evaluated independently; they are not mandatory runtime dependencies. Do not load every reference by default.
