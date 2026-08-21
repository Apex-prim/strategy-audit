# Fifty-five strategies pass every statistical test. None beats holding the coins.

The sweep is complete: **571 unique strategies** from 10 public repositories, each
run by freqtrade itself on its own declared timeframe, in-sample and out-of-sample,
with two of freqtrade's own bias detectors.

Every stage and threshold below was fixed in [CORPUS_PLAN.md](CORPUS_PLAN.md)
**before** any of these numbers existed. `git log` shows that file committed first.

## The funnel

```
corpus strategies                                        571
  loaded and ran in the authors' window                  344
  also ran out of sample                                 336
  at least 30 in-sample trades                           314
  in-sample expectancy > 0                               126
  and significant in-sample (p < 0.05)                    64
  and out-of-sample expectancy > 0                        62
  and significant out of sample (p < 0.05)                57
```

By the statistics almost everyone uses, **57 of 336 survive — 17%**. That reads
like a finding. Then one more column is applied: a column freqtrade prints in
every backtest summary, free, that most people scroll past.

## The baseline column

```
of the 57 survivors
  look-ahead bias detected by freqtrade's own analyser     2   excluded
  clean                                                   55

  BEAT BUY-AND-HOLD OUT OF SAMPLE                          0   of 55
```

**Zero.** Fifty-five strategies clear in-sample significance, positive
out-of-sample expectancy, and out-of-sample significance — and not one returns
more than sitting still in the same eight coins over the same period.

```
market, 2020-03-01 .. 2026-08-19                      +346.3%
best survivor        NASOSv5_mod1                     +289.7%
worst survivor                                         +24.1%
all 55 are 5-minute strategies
```

Five of the 55 are the same strategies under different names — identical trade
counts and identical results — so **50 are distinct**. Counting name-duplicates
as independent findings would overstate the evidence in both directions.

Their p-values are real. Their out-of-sample improvement is real. They were
measuring the market going up and capturing a fraction of it.

> Had the baseline column not been added — it was added because an external
> critic pointed out its absence — **this page would be announcing fifty-five
> winners.**

## What this does not say

**It does not say these strategies are worthless.** Their median maximum
drawdown is **5.5%**, against roughly 75–80% for holding through 2022. Capturing
70% of a bull market with a fifteenth of the pain is a real object, and someone
who cannot stomach an 80% drawdown may reasonably prefer it. What it is not is
an edge over the asset.

Two hypotheses that such low drawdowns were hiding risk were tested and **both
failed** — no trades left open at the end of the backtest, losing trades closing
in under 14 hours, worst trade −22.3%, drawdown arithmetically consistent with
position sizing. Both are recorded as withdrawn, because a check that only ever
confirms the auditor is not a check.

**It does not clear any strategy for use.** Backtests fill at the candle open
with no spread and no slippage. All 55 survivors are 5-minute strategies, where
that omission is the dominant unmodelled cost. And no multiple-comparison
correction is applied across 314 tested strategies — at p < 0.05, roughly 16
would clear each significance gate by chance alone.

**It does not say an edge cannot exist.** It says that among 571 strategies their
own authors were confident enough to publish, the ones surviving every
statistical test still lose to doing nothing.

## Look-ahead bias

**17 strategies in the corpus** have look-ahead bias confirmed by freqtrade's own
`lookahead-analysis`. They are excluded from the funnel and named in their cards
rather than quietly dropped.

The most striking is `ichiV1`, bias confirmed at 7 entries out of 20 signals,
reporting **+18,701,080%** out of sample. A number that large is not a finding;
it is a receipt for a broken measurement.

## What could not be measured — and whose fault each bucket is

227 strategies produced no numbers. "Could not measure" is a category with a
named cause, never folded into "clean":

```
 41  no timeframe declared anywhere; the engine refuses to guess
 22  numpy.exceptions.DTypePromotionError — np.where mixing str and float,
     which numpy 1.x allowed and 2.0 rejects
  9  exceeded the 20-minute run limit (a declared cap, not a silent skip)
  8  engine exited 0 with no summary table
  7  ImportError: short strategies cannot run in spot markets
  7  TypeError: fillna(method=...) removed in pandas 2
  5  TypeError: invalid value for dtype 'bool'
  4  cannot determine parameter space for a hyperopt variable
  3  'stoploss' is a required property
```

Most of the remainder are version incompatibilities: these strategies were
written for numpy 1.x and pandas 1.x. That is a fact about their age, stated
plainly, not a verdict on their logic.

## Four defects in this sweep, found and fixed before publication

Every one of them made a bucket of strategies look worse than it was, and none
announced itself.

**Short strategies in a spot market.** 78 strategies declare `can_short` and this
sweep ran spot mode. They were counted as failures of the strategies. They were
failures of our configuration.

**A removed numpy alias.** 38 strategies died on `np.NAN`, which was an alias for
`np.nan` deleted in numpy 2.0 — the same object under an old name. Restoring the
alias (`np.NAN is np.nan` → `True`, no behaviour changed) returned 21 strategies
to the measured set and added 11 more survivors. None of them beat the baseline
either.

**A label instead of a cause.** About a hundred cards read `Fatal exception!` or
`Impossible to load Strategy` — the first line of a traceback and a wrapper
message. Neither is a reason. A category with no cause is indistinguishable from
a category nobody looked at.

**Six strategies lost silently.** Six pairs of class names differ only in case —
`Ichi`/`ichi`, `SAR`/`Sar`, and four more. On a case-insensitive filesystem the
two cards are one file, so the resumable sweep saw "already done" and skipped the
second of each pair. One percent of the corpus, without a word — the exact
failure [CORPUS_PLAN.md](CORPUS_PLAN.md) forbids.

The pattern is worth naming: **every large "these strategies do not work" bucket,
when opened, turned out to be "we could not run them".** The asymmetry is not
accidental — an unexplained failure flatters the auditor, so it is exactly the
place where an auditor should look hardest.

---

*Reproduce: `python corpus.py --shard k/5`, then `python funnel.py`. Cards for
every strategy — including all 227 that could not be measured, each with its
reason — are in [corpus/](corpus/).*
