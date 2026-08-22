# The column that decides everything, and nobody prints it

A strategy that survives every statistical test in this repository has shown
one thing: that its measurement is not obviously broken. It has not shown that
it makes money, and it has not shown that it beats doing nothing.

The second question needs one more column — the one freqtrade prints in every
backtest summary, for free, immediately under the profit line:

```
Absolute profit    ...
Total profit %     ...
Market change      ...   <- this one
```

`Market change` is buy-and-hold on the same pairs over the same window. It costs
nothing to read and it is scrolled past in nearly every published backtest,
because a large positive `Total profit %` already feels like an answer.

**This page carries no counts of its own.** Every number lives in
**[LEDGER.md](LEDGER.md)**, generated from [LEDGER.csv](LEDGER.csv) by
`ledger.py`, and a pre-commit hook rejects a commit in which the published
figures no longer reproduce. That arrangement exists because this file used to
open with a count in its own title, and that count went stale within a day of
being published while still reading as authoritative. A document that repeats
numbers is a document that will eventually contradict them.

## What the ladder is for

Each gate in the ledger removes strategies for a different reason, and the order
matters, because a reader who sees only the last number cannot tell which stage
did the work:

- The **largest** single drop is not a bias detector. It is in-sample
  expectancy: strategies that lose money in the window their own author chose.
- The **statistical** gates — significance in both windows — are the ones most
  audits stop at. By those alone a substantial fraction survives, and that
  fraction is what a reader would call a finding.
- The **baseline** question is asked after all of them, and it is the one that
  changes the conclusion.

Had the baseline column not been added — it was added because an outside critic
pointed out its absence — this page would be announcing every one of those
survivors as a winner.

## Why survivors are not winners

The out-of-sample window covers a market that rose a great deal. A strategy that
is long most of the time will show a large positive return, a good p-value, and
a genuine improvement over its own in-sample period — while capturing a fraction
of a rise it did not predict. All of those numbers are real. None of them is
edge.

This also cuts against the strategies in the other direction: the *in-sample*
window was largely a bear market, so a strategy that merely stayed out of
trouble there looks selective rather than lucky. Any measure of "how much of the
edge was retained" mixes the two regimes together and should not be read as a
measure of robustness. That confound is stated rather than corrected, because
correcting it would require regime-matched windows that the authors' own
published window does not provide.

## Duplicates

A meaningful share of the corpus is the same strategy under different names —
identical trade counts, identical results. They are kept in the ledger, marked,
and counted once when the question is *how many distinct things survive*.
Counting name-duplicates as independent findings would overstate the evidence in
both directions: it inflates the survivor count, and it inflates the number of
independent tests in the multiplicity correction.

## What this does not say

- It does not say these strategies do not work. It says that on this data, with
  these costs, in this window, none of them beat holding the same coins.
- It does not say the authors were wrong. Most publish code that does exactly
  what they describe. The question is what a reader takes from a results table.
- It does not say buy-and-hold is a good strategy. It says it is the number an
  active strategy has to beat before "profitable" means anything.

## The honest reading

The survivors are not frauds and their statistics are not fake. They are
strategies whose authors measured the right quantity and never compared it to
the obvious alternative. That is not a rare mistake, and it is not a
sophisticated one — it is the default outcome of reading a backtest summary from
the top down and stopping when the number is large enough to be satisfying.
