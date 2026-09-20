# Database saturation

**Fictional teaching case.** General reasoning pattern inspired by limited Pilot experience; all measurements below are invented for illustration.

**Symptom:** A catalog search slows under concurrent use. Some requests wait for a database connection. The proposed fix is to increase the pool.

**Separate:** Connection wait is an observation; "too few connections" is a hypothesis. Larger result sets also appear slower, but correlation does not identify the mechanism.

| Hypothesis | Distinguishing prediction | Evidence that lowers it |
|---|---|---|
| Capacity limits otherwise short work | Acquisition dominates; hold time stays short and stable. | Acquisition is tiny while hold time dominates. |
| Database execution is slow | Execution occupies most hold time. | Execution is short for the same slow request. |
| Fetch/materialization or application work holds connections | Hold time greatly exceeds execution; later spans explain the gap. | Connection is returned before that work, or execution explains the duration. |

**Bounded test:** Compare small/large result sets in the same environment. Correlate acquisition, execute, fetch/materialization, hold time, and request duration. Verify whether the driver includes fetch in execute timing; do not subtract incompatible spans.

**Illustrative new evidence:** In a representative trace acquisition is 3 ms, execution 90 ms, connection hold 1,900 ms, and measured post-execute work 1,750 ms.

**Update:** Capacity shortage loses rank as the dominant explanation for this trace. The post-execute path becomes the next target; exact function/cause remains unproven. These numbers do not establish behavior for all requests.

**Act and stop:** Inspect/profile that span, then run a bounded local comparison of the justified fix. Stop debating pool size now. Reopen if representative traces instead show acquisition dominating with short holds and downstream headroom. A temporary capacity change, if separately justified, is mitigation rather than a demonstrated root-cause fix.
