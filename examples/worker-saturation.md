# Worker saturation

**Fictional teaching case.** Generic scenario, not a reproduction of any private queue or configuration.

**Symptom:** A thumbnail service's queue grows and all workers are busy. The suggested answer is "add workers."

**Hypotheses:** Insufficient execution slots; slower work per item; downstream contention; or intentional serialization. Busy workers fit all four.

**Falsification:** The slot-shortage model predicts stable service time, spare downstream capacity, and throughput improvement as a safe local concurrency probe increases slots. If service time or contention rises while throughput stays flat, adding slots is not supported.

**Bounded test:** On fixed inputs, compare queue wait, service time by stage, throughput, and downstream wait at two modest concurrency settings in an isolated environment. Preserve any per-key ordering/correctness constraints. Define a stop if errors or contention increase.

**Illustrative new evidence:** Larger images take disproportionately longer in one transform stage. A local concurrency increase does not improve throughput and increases downstream wait. These are stipulated scenario facts, not measured project results.

**Update:** Per-item work and contention now outrank slot shortage. More workers could amplify the symptom.

**Act and stop:** Profile the transform with varying image sizes and validate the resulting bounded fix. Stop capacity speculation while that measurable path is available. Reopen if service time stabilizes, spare capacity is demonstrated, and a controlled probe shows scaling. Do not claim a production speedup from this fictional exercise.
