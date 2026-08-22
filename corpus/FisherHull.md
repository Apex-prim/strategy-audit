# FisherHull

Source: [`mikedigriz/freqtrade-strategy-mikedigriz`](https://github.com/mikedigriz/freqtrade-strategy-mikedigriz) · file `FisherHull.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 82 | — |
| average profit per trade % | -2.25 | — |
| win rate % | 25.6 | — |
| average trade duration, minutes | 79405.0 | — |
| duration measured in own candles | 79405.0 | — |
| expectancy per trade (USDT) | -5.89 | — |
| mean profit p-value | 0.04737 | — |
| market change % (baseline) | -55.54 | — |
| strategy total % | -48.32 | — |
| Sharpe | -0.48 | — |
| Sortino | -1.34 | — |
| max drawdown % | 67.32 | — |
| profit factor | 0.55 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+7.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-48.32%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
