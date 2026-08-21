# Forty-four strategies pass every statistical test. None beats holding the coins.

The sweep is complete: **571 unique strategies** from 10 public repositories, each
run by freqtrade itself on its own declared timeframe, in-sample and out-of-sample,
with two of freqtrade's own bias detectors.

Every stage and threshold below was fixed in [CORPUS_PLAN.md](CORPUS_PLAN.md)
**before** any of these numbers existed. `git log` shows that file committed first.

## The funnel

```
corpus strategies                                        571
  loaded and ran in the authors' window                  319
  also ran out of sample                                 311
  at least 30 in-sample trades                           289
  in-sample expectancy > 0                               108
  and significant in-sample (p < 0.05)                    52
  and out-of-sample expectancy > 0                        50
  and significant out of sample (p < 0.05)                46   <- 14.8%
```

By the statistics almost everyone uses, **14.8% survive**. That reads like a
finding. Then one more column is applied — a column freqtrade prints in every
backtest summary, free, that most people scroll past.

## The baseline column

```
of the 46 survivors
  look-ahead bias detected by freqtrade's own analyser     2   excluded
  clean                                                   44

  BEAT BUY-AND-HOLD OUT OF SAMPLE                          0   of 44
```

**Zero.** Forty-four strategies clear in-sample significance, positive
out-of-sample expectancy, and out-of-sample significance — and not one of them
returns more than sitting still in the same eight coins over the same period.

Five of the 44 are the same strategies under different names (identical trade
counts and identical results), so **39 are distinct**. Counting name-duplicates
as independent findings would overstate the evidence in both directions.

The market returned **+346%** out of sample. The survivors returned between 32%
and 290%. Their p-values are real; their out-of-sample improvement is real. They
were measuring the market going up, and capturing a fraction of it.

> Had the baseline column not been added — it was added because an external
> critic pointed out its absence — **this page would be announcing forty-four
> winners.**

## Look-ahead bias

**17 strategies in the corpus** have look-ahead bias confirmed by freqtrade's own
`lookahead-analysis`. They are excluded from the funnel and named in their cards
rather than quietly dropped.

The most striking is `ichiV1`, which reports **+18,701,080%** out of sample with
bias confirmed at 7 entries out of 20 signals. A number that large is not a
finding; it is a receipt for a broken measurement.

## What could not be measured — and whose fault it is

246 strategies produced no numbers. "Could not measure" is a category with a
named cause, never folded into "clean":

```
 76  ImportError: short strategies cannot run in spot markets   <- OUR config
 41  timeframe declared nowhere; the engine refuses to guess
  9  exceeded the 20-minute run limit
  8  engine exited 0 with no summary table
  4  cannot determine parameter space for a hyperopt variable
  3  'stoploss' is a required property
```

The largest bucket is **ours, not theirs**. Those 76 declare `can_short = True`
and this sweep ran in spot mode; they are perfectly measurable on futures data
and were excluded by a configuration choice. Until that run happens, the honest
denominator for "how many public strategies hold up" excludes them, and the
reason is stated here rather than buried.

Until this was traced, all 76 were reported as `Fatal exception!` — which is the
first line of a traceback, not a reason. A category with no cause is
indistinguishable from a category that was never looked at.

## Two defects in this sweep, found and fixed before publication

**Six strategies were lost silently.** Six pairs of class names differ only in
case — `Ichi`/`ichi`, `SAR`/`Sar`, `BBRSI`/`bbrsi`, `HLHB`/`hlhb`,
`mabStra`/`MabStra`, `SuperTrend`/`Supertrend`. On a case-insensitive filesystem
`results/ichi.json` and `results/Ichi.json` are one file, so the resumable sweep
saw "already done" and skipped the second of each pair. One percent of the
corpus, silently. Card filenames are now disambiguated by a hash of the exact
name, and the six were recomputed.

**The largest failure class had no cause.** See above: 76 strategies reported
with a traceback header instead of the exception. Fixed by reading the end of
the traceback rather than the label at its start.

## What this does not say

**It does not say these strategies are worthless.** On risk they look different
from buy-and-hold: several return 100–190% with maximum drawdowns under 5%,
against roughly 75–80% for holding through 2022. Return is not the only axis, and
capturing half the upside with a fifteenth of the pain is a real object.

Two hypotheses that such low drawdowns were hiding risk were tested and **both
failed** — no trades left open at the end, losers closing in under 14 hours,
worst trade −22.31%, drawdown arithmetically consistent with position sizing.
Both are recorded as withdrawn, because a check that only ever confirms the
auditor is not a check.

**It does not clear any strategy for use.** Backtests fill at the candle open
with no spread and no slippage. Most survivors are 5-minute strategies, where
that omission is the dominant unmodelled cost. And no multiple-comparison
correction is applied across 289 tested strategies — at p < 0.05, roughly 14
would clear each significance gate by chance alone.

**It does not say an edge cannot exist.** It says that among 571 strategies their
own authors were confident enough to publish, the ones that survive every
statistical test still lose to doing nothing.

---

*Reproduce: `python corpus.py --shard k/5`, then `python stats.py`. Cards for
every strategy — including all 246 that could not be measured, each with its
reason — are in [corpus/](corpus/).*
