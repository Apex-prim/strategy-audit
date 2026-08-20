# Pre-registration of the corpus sweep

**Written before the results exist.** Git timestamps this file; the results
commit will come after it. That ordering is the only thing that makes the
headline number worth reading, and it is cheap to verify — `git log` the two.

The five hand-picked audits in this repository were chosen by me. A corpus is
different: it can be steered by which strategies I keep, which window I use, and
when I decide to stop. So those decisions are fixed here, in advance.

## The question

> Of the strategies people were confident enough to publish, how many still show
> a statistically significant per-trade edge on data the author never saw?

## Population

571 unique classes inheriting `IStrategy`, deduplicated by class name from 1,055
occurrences across 10 public repositories. 484 are copies — `Schism` appears in
16 repositories, `ClucHAnix` in 9.

Of the 571, **568 define an entry method**. Three (`MasterMoniGoManiHyperStrategy`,
`ThreeCommasStrategy`, `YourStrat`) are base or template classes with no entry
logic and are excluded. The denominator is 568.

## Fixed before running

| | |
|---|---|
| Engine | freqtrade 2026.7, the strategies' own code, no re-implementation |
| Timeframe | **whatever each strategy declares** — never overridden by config |
| Pairs | BTC, ETH, LTC, XRP, ADA, XLM, XMR, DASH — all vs USDT |
| In-sample | 2018-03-01 … 2020-03-01 |
| Out-of-sample | 2020-03-01 … 2026-08-20 |
| Cost | 0.1% per side headline; 0.3% reported as sensitivity |
| Minimum trades | **30 in-sample**, declared now, not after seeing the distribution |
| Significance | `Mean profit p-value` < 0.05, freqtrade's own figure |

## The funnel — stages fixed in advance

The headline is the last stage; every stage is published, so a reader can see
where the attrition happened rather than trusting one number.

1. loaded and ran in-sample
2. also ran out-of-sample
3. at least 30 in-sample trades
4. in-sample expectancy > 0
5. **and** in-sample p < 0.05
6. **and** out-of-sample expectancy > 0
7. **and** out-of-sample p < 0.05 ← the headline

## What will not be done

- **No threshold moves after seeing data.** 30 trades and p < 0.05 are set above.
- **No dropping strategies that fail to load.** They are counted and their error
  is published. "Could not measure" is a category, never folded into "clean".
- **No stopping when the number looks good.** The sweep ends when the corpus ends
  or when a stated cap is reached.

## Declared caps

A 5-minute strategy over 8.5 years is roughly 12× the candles of an hourly one,
and 351 of the 571 declare 5m. If the full sweep does not fit in available
compute, the cap will be **stated as a number in the results** — how many
strategies ran, how many did not, and the rule that selected them. A silently
truncated sweep reads as complete coverage; that is precisely the failure this
repository documents in its own README.

Timeframes without downloaded data are a cap of the same kind: those strategies
fail loudly, are counted, and are named.

## What would embarrass this project

If the surviving fraction comes out high, that is the answer and it gets
published — this is not an exercise in showing that public strategies are bad. A
low number in a sample authors pre-selected for good in-sample results is a
strong claim; a high number would be a stronger and more surprising one.

The result this project cannot survive is a number that looked fine and was not.
One of those has already been found here, and is documented in the README.
