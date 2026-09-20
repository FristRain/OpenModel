# OpenModel — Keep the problem model open until the evidence closes it.

A **falsification-first reasoning protocol for AI agents working under uncertainty**.

AI agents can solve the problem they believe they have while committing to the wrong problem too early. OpenModel helps separate observations from explanations, test competing hypotheses, update stale models, and check who owns new domain state before building around it.

**v0.2 release candidate · engineering validation release · limited qualitative Pilot evidence**

## Understand it in 30 seconds

> **Symptom:** "The database pool is saturated."
>
> **Premature commitment:** "Increase the pool size."
>
> **OpenModel:** Saturation is an observation. Insufficient capacity is one hypothesis. Slow queries, long transactions, or connection-held work can produce the same symptom. What measurement would distinguish them and disprove the preferred explanation?

| Failure | What OpenModel changes |
|---|---|
| Premature commitment | Keep a plausible explanation as a hypothesis until relevant evidence supports action. |
| Symptom patching | Test the causal link before tuning the resource that happens to be busy. |
| Stale models | Check whether a historical explanation still applies to the current revision and deployed path. |
| Duplicated domain state | Identify authority, projections, operational state, and historical evidence before adding another mutable copy. |

OpenModel does **not replace profiling, tracing, tests, static analysis, or architecture tools**. Those produce evidence and validate changes; this protocol helps decide what to investigate and what the evidence supports. It is Markdown guidance, not a trained model, enforcement engine, or source of missing facts.

## Understand the value in 3 minutes

**Observe → Separate → Branch → Attack → Update → Act**

The steps are combinable functions, not six mandatory headings. Ask what would change the decision; obtain that evidence; act when the remaining uncertainty no longer changes the next step.

| Example | Tempting conclusion | Discriminating check |
|---|---|---|
| [Database saturation](examples/database-saturation.md) | A full pool must be too small. | Compare acquisition wait, execution, fetch, and connection hold time on the same requests. |
| [Worker saturation](examples/worker-saturation.md) | Busy workers require more workers. | Separate queue wait from service time and downstream contention. |
| [Stale model](examples/stale-model.md) | A previously synchronous operation still blocks requests. | Check current paths, deployment identity, and request traces. |
| [Architecture overfit](examples/architecture-overfit.md) | Another snapshot or status layer will fix consistency. | Prove ownership and recovery semantics; try to produce disagreeing copies. |

These are **fictional teaching examples inspired by anonymized diagnostic patterns**, not production traces, reproduced incidents, or measured outcomes.

## Start in 10 minutes

1. Download this candidate branch or clone the repository:
   ```sh
   git clone --branch release/v0.2-rc https://github.com/FristRain/OpenModel.git openmodel
   ```
2. Give your agent access to [SKILL.md](SKILL.md) and `references/`. For a directory-skill host, install the `openmodel/` folder through its documented mechanism; discovery paths and syntax depend on the host.
3. For any agent that can read files, paste:
   ```text
   Read openmodel/SKILL.md and apply it to this task.
   Symptom: Searches slow down as result size increases.
   Goal: Identify the next justified change.
   Materials: Current source, representative traces, and a local test environment.
   Constraints: Read-only production access; one diagnostic pass before a local experiment.
   Use the lowest sufficient level. Execute authorized work when evidence is sufficient.
   ```
   In chat without file access, attach/paste `SKILL.md` and only the references it needs. Relative links alone do not load their content.
4. Expect a concise decision record: observations versus explanations, the leading hypothesis and its failure condition, missing evidence, and an action with a stopping condition. A full table is optional.
5. Check the boundary: ask for a simple title change. The agent should do it directly. Then try the two-round [behavioral cases](tests/README.md).

For Codex, Claude Code, and other skill-capable agents, keep the complete folder and use the host's current installation documentation. This repository provides a portable prompt/file route, not host-specific adapters or a claim of tested compatibility with every host. See [INVOKE.md](INVOKE.md).

## Use only as much protocol as needed

- **Level 0 — Flow:** Ordinary CRUD with an established owner, formatting, clear local fixes, creation, or listening: do the task.
- **Level 1 — Check:** One material uncertainty: a short evidence check.
- **Level 2 — Explore:** Competing explanations change the action: compare predictions and run a discriminating check.
- **Level 3 — Critical:** A costly or hard-to-reverse decision: independently verify material claims and failure/recovery boundaries.

Performance incidents, intermittent failures, repeated unsuccessful fixes, stale assumptions, and architecture/state changes are useful triggers **when uncertainty affects the decision**. Complexity, the word "database," or adding an ordinary field is not sufficient.

Stop when evidence supports action, more discussion adds no information, the agreed budget expires, or the next information requires execution. A time limit does not justify an unsafe guess. Reuse existing evidence and workflows. Stop analyzing, then continue authorized work or state the specific missing input.

## Protocol and engineering references

The [core epistemic loop](references/core.md) remains general. Load these only when relevant:

| Reference | When to read |
|---|---|
| [Hypothesis gate](references/hypothesis-gate.md) | An uncertain cause is about to become an implementation premise. |
| [Model staleness](references/model-staleness.md) | Old explanations conflict with current code or evidence. |
| [Model duplication](references/model-duplication.md) | Several records appear to describe the same fact. |
| [State ownership](references/state-ownership.md) | Introducing or repurposing durable state, statuses, snapshots, or caches. |
| [Decision cost](references/decision-cost.md) | Investigation is growing or delay matters. |
| [Working state](references/state.md) | Evidence-preserving updates or handoff. |

**No New State Without Ownership Proof** means a proportionate explanation of fact, authority, writers, lifecycle, identity, and recovery. A normal field on an established entity can satisfy it in one sentence. It does not require a new approval process or ban legitimate projections and historical copies.

## What the evidence supports

v0.1 established the **core epistemic loop**. v0.2 is an **engineering validation release**: lessons and falsifiable evaluation criteria, not a declaration that validation is complete.

A limited real-engineering Pilot reported stronger fact/inference separation, clearer falsification conditions, detection of stale assumptions, and scrutiny of duplicated state. It also reported analysis overhead; the baseline already found several of the same candidate causes.

The evidence is a maintainer-provided conversation record from one project and one main model family. The first comparison explicitly used same-session behavioral ablation and self-evaluation, not independent blinded runs. Later diagnostic comparisons do not establish stronger controls. Private artifacts are not published, and this release has not independently reproduced the findings.

**No claim of universal effectiveness, statistically significant uplift, measured production speedup, independently verified root causes, or cross-agent superiority is made.** See [Pilot provenance and limits](references/pilot-evidence.md) and the [evaluation method](references/model-impact.md).

## Validate and contribute

Python 3.10+; standard library only:

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

These check packaging, local links, case schemas, and obvious public-data hazards. They do **not** measure agent reasoning. The original five [cross-domain cases](references/test-cases.md) are retained; engineering cases and manual evaluation are in [tests/README.md](tests/README.md).

Contribute [A/B failure cases, counterexamples, and other agent/domain results](CONTRIBUTING.md), including costs and regressions. See [CHANGELOG.md](CHANGELOG.md) and [candidate notes](RELEASE_NOTES.md).

A license has not yet been selected by the maintainer. Public visibility alone does not grant an open-source license.
