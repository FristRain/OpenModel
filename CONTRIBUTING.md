# Contributing

Help discover where OpenModel fails, adds cost, or does not generalize. A/B failure cases, counterexamples, null results, and different agents/domains are especially useful.

## An evaluable case

Include a minimal fictional or safely anonymized task, intended decision, permitted actions, current evidence, and later evidence as a separate round. Distinguish observed behavior from proposed tests.

For comparisons, record model/version, settings, skill revision, tools, context, budget, isolation/blinding, repeated-run count, and assessment. Share only publishable information; disclose withheld details without inventing experimental controls.

Use identical inputs and budgets. Predefine success, failure, and acceptable overhead. Include a competent baseline, failures and unchanged outcomes, and whether actions were actually executed.

Report correctness, completion, evidence updates, time/cost, unnecessary questions, and regressions. Length and hypothesis count are not wins. See [evaluation method](references/model-impact.md).

## Privacy

Remove company/project identities, internal addresses/paths, credentials, business records, private links, and private architecture. Prefer a fictional minimal reproduction over renaming a detailed incident. Check logs, screenshots, archives, and chat transcripts before sharing.

The scanner catches only obvious patterns; human review must check semantic leakage and identifying combinations of ordinary details.

## Keep changes proportionate

Explain the demonstrated failure a rule fixes. General rules belong in [core](references/core.md); engineering details in focused references. Do not turn one incident into a universal gate.

Preserve Level 0, authorization boundaries, and stop rules. Avoid mandatory approval, fixed hypothesis counts, and exhaustive forms without a demonstrated need.

Before a PR:

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

For behavior changes, evaluate relevant [cases](tests/README.md) in an actual agent session. Distinguish executed results from specifications; static checks are not an agent benchmark.

## Contribution terms

OpenModel uses the [Unlicense](UNLICENSE), including for its original protocol, documentation, examples, and scripts. By submitting original contributions for inclusion, you agree to make them available under the same terms. Submit only material you have the right to contribute on that basis.

You are welcome to maintain your own public or private workflow without contributing it back. If you choose to share improvements here, explain what they change and the evidence behind them.
