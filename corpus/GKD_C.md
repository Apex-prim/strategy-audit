# GKD_C

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `GKD_C.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4 | — |
| average profit per trade % | -3.47 | — |
| win rate % | 25.0 | — |
| average trade duration, minutes | 285.0 | — |
| duration measured in own candles | 4.75 | — |
| expectancy per trade (USDT) | -4.28 | — |
| mean profit p-value | 0.2372 | — |
| market change % (baseline) | -58.4 | — |
| strategy total % | -1.71 | — |
| Sharpe | -0.09 | — |
| Sortino | -0.1 | — |
| max drawdown % | 1.71 | — |
| profit factor | 0.07 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+56.7 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.2372 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-1.71%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
