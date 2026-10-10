---
name: openmodel-code-review
description: Review code using inspected diff and impact evidence, with concrete failure paths and scope-limited findings.
metadata:
  status: prototype
---

# Code Review

Apply [Core](../../CORE.md). Inspection, not the author's explanation, owns code facts.

1. Inspect actual diff, current callers/readers/writers, interfaces, persistence and relevant tests.
2. Trace only far enough to establish plausible affected paths and material failures.
3. For a finding, name **code fact → affected path → failure condition → impact**; cite code evidence and uncertainty.
4. Treat missing runtime coverage as unknown; do not infer production safety from static or mocked tests.
5. Ask about external contracts or business requirements only when material and not inspectable.

Return findings by severity, or say no material issue was found within the checked scope. Do not invent issues to meet a quota.
