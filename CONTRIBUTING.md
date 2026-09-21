# Contributing

Three kinds of contribution are useful here, in this order.

## 1. Tell me a number is wrong

Every number in the README is regenerated from [LEDGER.csv](LEDGER.csv) by
`ledger.py`, and `verify_ledger.py` fails CI if they disagree. So if a number
looks wrong, one of three things is true: the ledger row is wrong, the harness
that produced the row is wrong, or the prose around the number misreads it.
Open an issue naming the strategy and the column. Errors found in this
repository are published *in* it — see [CORRECTIONS.md](CORRECTIONS.md) — not
quietly patched.

## 2. Add a strategy or a repository

The corpus is defined by [corpus_sources.json](corpus_sources.json) and grown
with `expand.py`. Send the repository URL in an issue, or a pull request that
adds it to the sources file. Do **not** add the strategy files themselves: the
corpus is fetched, not vendored, so that what was measured is what the author
published.

A strategy is measured only if it loads under freqtrade 2026.7 — 94 of the
895 did not, and [loadcheck.py](loadcheck.py) says why for each.

## 3. Add a check

A new gate goes into `harness.py` (dynamic, runs the code) or
`foreign_strategy_audit.py` (static, reads it). Either way the rules are:

- **A lived case, not a hypothetical.** The selftest takes the exact line, the
  exact name, the exact number on which something actually broke. The
  repository's own defects are in [anatman.py](anatman.py) as executable cases.
- **Every silence is paired with a boundary.** If your check stops flagging
  something, the selftest must also contain the nearest line that it *must
  still* flag. Silencing a check and blinding it look identical on screen.
- **Declare it.** `sync_repo.py --orphans` refuses a published module that is
  not listed in the pipeline. CI stayed red for a month because three modules
  were added without this; the gate was right.
- **Total, not partial.** `totality.py` refuses a check that has an input for
  which it has no defined answer. A partial function with a flattering default
  was three of the first four defects found here.

## Before you push

```bash
git config core.hooksPath .githooks     # the same gates CI runs
python foreign_strategy_audit.py --selftest
python sync_repo.py --orphans
```

The pre-commit hook runs the secret gate, the ledger check, the freeze guard
and the totality check, and refuses the commit on any of them. That is the
whole review process; there is no other.

## What is not accepted

- A change to a published number without a change to the code or data that
  produced it.
- A strategy verdict written by hand. Verdicts come from `harness.py` or they
  do not exist.
- Anything containing a credential. `tools/secret_gate.py` will refuse it, and
  it self-tests by planting one, so a green run means the gate works.
