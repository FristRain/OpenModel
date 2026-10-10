---
name: openmodel-development
description: Implement and fix systems by inspecting the real flow, distinguishing patch from design correction, and verifying at a level capable of reproducing the failure.
metadata:
  status: prototype
---

# Development

Apply [Core](../../CORE.md). The goal is justified implementation, not a lengthy diagnosis document.

- **Reconstruct:** Inspect code, actual state ownership, the affected workflow, deployment/config revision and relevant failures. Do not equate an observed symptom with cause.
- **Classify:** Use PATCH for a genuinely local defect; DESIGN CORRECTION for a demonstrated ownership, lifecycle, transaction or interface problem; UNCERTAIN if the distinction changes the action but evidence is insufficient.
- **Choose:** If patch and redesign carry materially different costs or business effects, disclose consequences and obtain an informed choice. An informed temporary patch is valid; record known debt and reopening condition.
- **Implement:** Make authorized changes without repeated permission requests. If evidence contradicts the chosen model, revise it rather than layering patches.
- **Verify:** T0 requires a verifier that could have expressed the original failure. A serial mock does not prove a race fixed; passing unit tests do not prove production throughput. Check affected regressions and report exact verified scope.

For new or repurposed state, establish authority, writers, version, lifecycle and failure recovery; reuse existing structures. Do not create extra durable state solely to support OpenModel.

Prefer concise output: chosen action, decisive evidence, important tradeoff/unknown, observed verification. Do not force templates on small tasks.
