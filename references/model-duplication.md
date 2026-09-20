# Model duplication

Multiple copies are not automatically multiple authorities. A cache, scheduler record, and historical receipt can legitimately answer different questions.

Trigger when new state overlaps existing meaning, readers disagree about which copy wins, or repeated synchronization patches suggest an unclear owner.

## Compare semantics

| Question | Reason |
|---|---|
| What fact, entity, event, and revision does it describe? | Identical words may describe different facts; different words may hide the same fact. |
| Who writes it and decides on conflict? | Independent writers can create competing authorities. |
| What do readers use it to decide? | A display copy can become an accidental authority. |
| Can it be rebuilt, from what source/version? | A projection needs derivation and freshness contracts. |
| What happens on crash, retry, or out-of-order updates? | Individually valid rows can form an invalid combination. |

Compare **necessary separate roles** against **duplicated authority**. Fewer tables is not inherently better.

## Attack the boundary

Try a local failure/recovery scenario: one update commits and a projection fails; an old job retries after a newer revision; historical evidence disagrees with current state. Which fact wins? Is recovery deterministic?

If independent writers assert the same current fact without precedence, withhold another state layer until ownership is clear. Prefer reusing authority or defining derivation over another synchronization patch.

If one copy is immutable past-event evidence and another a rebuildable current projection, preserve both when needed. Historical copies must not silently become current truth; operational completion must not silently prove domain success.

Classify roles and record proportional [ownership proof](state-ownership.md). Investigate only boundaries relevant to the change.
