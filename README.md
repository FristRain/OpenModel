# OpenModel — Keep the problem model open until the evidence closes it.

A **falsification-first reasoning protocol for AI agents working under uncertainty**.

AI agents can solve the problem they believe they have while committing to the wrong problem too early. OpenModel helps separate observations from explanations, test competing hypotheses, update stale models, and check who owns new domain state before building around it.

Use it for tasks where an untested explanation could change the next action and existing instructions or checks do not adequately address that risk. It can be supplied directly as guidance or integrated selectively into an agent workflow; harness maturity alone does not determine its fit.

**v0.2.0 · engineering validation release · limited qualitative Pilot evidence**

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

## Who is it for? With or without a harness

A **runtime harness** processes model inputs, coordinates tool calls, and returns results. A **project workflow** adds task-specific practices such as review, evidence collection, tests, and recovery. They overlap, but are not interchangeable: using an agent product can already involve a harness even if you have not designed a project workflow. OpenModel supplies task guidance that can sit within that system; it does not implement the runtime. See the [definition and evidence review](references/audience-evidence.md).

| Decision gap | How OpenModel can fit |
|---|---|
| An uncertain diagnosis with no explicit evidence discipline | Try the compact prompt or relevant skill checks, using only the evidence actually available. This can occur in direct model use or an agent workflow. |
| A structured workflow verifies changes but leaves a causal premise or state owner untested | Add the missing falsification, staleness, or ownership check at that decision boundary. Reuse existing tools and records. |
| The relevant uncertainty is already resolved or the existing workflow covers it | Continue normal execution. Extra OpenModel procedure is unnecessary unless a new gap appears. |

**We have not established that OpenModel is primarily for bare models or more effective without a harness.** Its limited Pilot was reported in an already structured engineering setting, not a controlled comparison of workflow maturity. That does not establish effectiveness in mature harnesses either. Selective integration is a design option to evaluate, not a demonstrated gain for every setup.

**Without an established workflow:** Give the model the task, available evidence, constraints, and a short investigation budget using [INVOKE.md](INVOKE.md). Expect a justified next action, not a full form for every request. The protocol does not create missing tools, persistent memory, isolation, or rollback capabilities; unavailable evidence must remain unknown.

**Inside an existing harness:** Place the relevant check at the decision it protects: uncertain diagnosis before a change, staleness when reusing historical conclusions, or ownership before introducing state. Map the result into your current task or review record. For example, adapt this project instruction:

```text
Use OpenModel when material uncertainty could change our next action.
Reuse the evidence and checks already completed by this workflow.
Add only the missing falsification, staleness, or ownership check.
Do not introduce duplicate records, repeated verification, or new approval steps.
When evidence is sufficient, continue implementation and relevant validation.
```

Keep ordinary CRUD and known fixes on the normal path. Evaluate integration against **your actual existing workflow**, including its costs, rather than against an artificially stripped-down model. The current Pilot does not establish which harness setup benefits most; see the [evaluation method](references/model-impact.md).

## Start in 10 minutes

1. Download the [v0.2.0 skill package](https://github.com/FristRain/OpenModel/releases/download/v0.2.0/openmodel-v0.2.0.zip) and extract its `openmodel/` folder, or clone the release:
   ```sh
   git clone --branch v0.2.0 https://github.com/FristRain/OpenModel.git openmodel
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

Contribute [A/B failure cases, counterexamples, and other agent/domain results](CONTRIBUTING.md), including costs and regressions. See [CHANGELOG.md](CHANGELOG.md) and [release notes](RELEASE_NOTES.md).

## Make it your own

OpenModel's original protocol, documentation, examples, and scripts are available under the [Unlicense](UNLICENSE). Everyone is welcome to use, copy, modify, and redistribute them, including for commercial purposes.

Fork the repository and build a workflow that fits your agent, team, or domain. Adapt the triggers, evidence sources, references, and output style; keep only what improves your decisions. You may keep your customizations private or share them under your own terms. Attribution and publishing your changes are welcome, but are not required by the Unlicense.

The project is provided without warranty. See the [full terms](UNLICENSE) and the [official Unlicense explanation](https://unlicense.org/).
