# Thirteen strategies pass every statistical test. None beats holding the coins.

**Interim result — the corpus sweep is about one quarter complete.** The
denominator is stated everywhere below and will change. The finding is published
now because it does not depend on the remaining three quarters: it is a statement
about what happens to strategies that pass, not about how many pass.

## The funnel, applied as pre-registered

Stages and thresholds were fixed in [CORPUS_PLAN.md](CORPUS_PLAN.md) before any
of these numbers existed. `git log` shows that file committed first.

```
corpus strategies that ran, >= 30 in-sample trades        68
  in-sample expectancy > 0                                25
     of those, no look-ahead bias detected                23   (2 excluded, named below)
  and significant in-sample (p < 0.05)                    16
     of those, also ran out of sample                     15
  and out-of-sample expectancy > 0                        15
  and significant out of sample (p < 0.05)                13
```

Thirteen strategies clear every statistical gate this repository applies. Most
do not merely survive — they *improve* out of sample, some by a factor of three.

That improvement is the tell.

## The baseline column

```
strategy                          strategy %   market %   beat it?
BB_RPB_TSL_RNG                       124.67     346.34       no
BB_RPB_TSL_RNG_TBS                   124.67     346.34       no
ClucHAnix_5m                         111.99     346.34       no
ClucHAnix_hhll                        87.57     346.34       no
Combined_NFIv6_SMA                   187.48     346.34       no
Combined_NFIv7_SMA                   188.00     346.34       no
ElliotV7                              51.53     346.34       no
Elliotv8                              80.17     346.34       no
ElliotV8_original_ichiv3             159.87     346.34       no
NASOSv5_mod1                         289.68     346.34       no
NostalgiaForInfinityV7_SMA           188.00     346.34       no
NotAnotherSMAOffsetStrategy          139.57     346.34       no
NotAnotherSMAOffsetStrategy_uzi       32.47     346.34       no

beat buy-and-hold:  0 of 13
```

All thirteen are 5-minute strategies. All thirteen returned less than the eight
coins returned by sitting still. Their statistics are not wrong — the p-values
are real, the out-of-sample improvement is real. They were measuring the market
going up, and capturing between 9% and 84% of it.

Two pairs are the same strategy under different names — `BB_RPB_TSL_RNG` /
`_TBS` and `Combined_NFIv7_SMA` / `NostalgiaForInfinityV7_SMA` are numerically
identical — so the thirteen are **eleven distinct**, in perhaps six families.
Counting them as thirteen independent findings would overstate the evidence in
both directions.

## Why this is the whole point

An earlier version of this repository reported no baseline at all. An external
critic said so, and was right. Had the baseline column not been added,
**this page would be announcing thirteen winners.**

That is the entire value of the check: it is cheap, it is one column freqtrade
already prints, and it inverts the conclusion.

> `Market change` is in every backtest summary. Most people scroll past it.

## What this does not say

**It does not say these strategies are worthless.** On risk they look very
different: `Combined_NFIv6_SMA` returns 187% with a 2.13% maximum drawdown and a
Sharpe of 2.47, against a buy-and-hold drawdown of roughly 75–80% in 2022. Return
is not the only axis, and a strategy that captures half the upside with a
thirtieth of the pain is a real object, not a fraud.

Two hypotheses that the low drawdown was hiding risk were tested and **both
failed**:

- *"It never closes losers."* Checked: zero trades left open at the end of the
  backtest; losing trades close in 13h46m on average; worst trade −22.31%.
- *"It compounds a rare blow-up outside the window."* Checked: 84.8% win rate
  with a real stoploss path and a maximum drawdown arithmetically consistent
  with 7 concurrent positions each risking ~22%.

The suspicions were stated, tested, and withdrawn. They are recorded here
because a check that only ever confirms the auditor is not a check.

**It does not clear these strategies for use.** Backtests fill at the candle
open with no spread and no slippage. On 5-minute bars, that omission is the
dominant unmodelled cost, and none of these has been tested against it. Nor has
any multiple-comparison correction been applied across the 68 — that comes with
the completed sweep.

## Look-ahead bias, found and named

Five strategies in the corpus so far have look-ahead bias confirmed by
freqtrade's own `lookahead-analysis`, and are excluded from every calculation
above rather than quietly dropped:

```
ichiV1                 bias detected: 7 entries of 20 signals
Ichi
CCIStrategy
FrayLIVEBTC15m
BuyAllSellAllStrategy
```

`ichiV1` reports **+18,701,080%** out of sample. A number that large is not a
finding; it is a receipt for a broken measurement.

---

*Reproduce: `python corpus.py --shard k/5`, then `python stats.py`. Cards for
every strategy, including the ones that could not be measured and why, are in
[corpus/](corpus/).*
