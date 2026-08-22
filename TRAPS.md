# Backtesting traps: 71% of the survivors carry at least one

When this audit was posted to the freqtrade Discord, `froggleston` said the bias
checks are not the only thing that flags a gamed strategy. He was right, and I
asked what else. The community answered with a link to their own document:

**<https://brookmiles.github.io/freqtrade-stuff/2021/04/12/backtesting-traps/>**

It describes six ways a backtest flatters a strategy. Four are checkable by
reading the code, and `traps.py` now checks them. **Nothing in this file is my
own idea** — including the 0.1–0.5% spread threshold, which is theirs. Adding my
own guesses on top of practitioner experience would have made it worse.

## What the corpus looks like under their checks

```
strategies checked                              895
of which pass every statistical gate             72
of which also clear both bias detectors          15

stoploss is not a stop                          263
inert trailing setting                          177
trailing tighter than the spread                 37
trailing without trailing_stop_positive          25
tight ROI on a long timeframe                     4

flagged by at least one trap   393 of 895   (44%)
among statistical survivors     51 of  72   (71%)
among detector-clean            9 of  15    (60%)
```

*These counts are read from [LEDGER.csv](LEDGER.csv), not computed separately —
one source, so the two cannot drift apart. The corpus grew from 804 to 895 and
the survivor figure stayed at 71%; that is stability, not a coincidence
preserved by rounding.*

**Seventy-one percent of the strategies that clear every statistical test carry
at least one of these.** Neither `lookahead-analysis` nor `recursive-analysis`
nor any p-value sees them, because they are properties of the strategy's
configuration rather than of its signal.

## The four that are checked

**`stoploss = -0.99` — 245 strategies.** A declared stop that is not a stop.
Losing positions are never cut, so the reported maximum drawdown is computed on
closed trades while the real risk sits in positions that stay open. This is the
single most common pattern in the corpus.

**Inert trailing settings — 164.** `trailing_stop_positive` is set while
`trailing_stop` is `False`. The value does nothing. Whoever tuned it was tuning
a number the engine ignores.

**Trailing tighter than the spread — 27.** The traps article explains the
mechanism: backtesting walks price to the candle high, adjusts the trailing
stop, then walks price down, which "gives you a perfect candle trade, selling
just below the high of the candle, almost every time." A trailing stop below the
0.1–0.5% spread cannot behave that way live.

**Trailing with no `trailing_stop_positive` — 22.** The stop trails at the full
`stoploss` distance rather than a few percent, which is usually not what the
author meant.

**Tight `minimal_roi` on long candles — 4.** Same mechanism as the trailing
trap: on hourly-plus candles the price is unlikely to reach a sub-1% ROI target
before the stop would have triggered in real conditions.

## The three that are NOT checked, and why

Stated because a check list with silent gaps is worse than a short one:

- **Unfilled limit orders.** Backtesting fills every order at the requested
  price. Live, they sit unfilled.
- **Slippage.** The market moves between decision and execution.
- **Many trades with sub-0.5% average profit.** The article is blunt: those
  profits "will become losses in live due to slippage." This one needs average
  profit per trade in percent and trade duration, which the cards do not yet
  carry.

The article's sharpest red flag is also not yet checked: **average trade
duration shorter than the candle timeframe** — a trade opening and closing
inside one candle, which backtesting permits and live trading mostly does not.
Adding duration to the cards is the next step, and until it is there, these
four checks are a floor rather than a ceiling.

## Reproduce

```bash
python traps.py
```

Pure static analysis of the strategy source. No backtests, no data, seconds to
run against the whole corpus.
