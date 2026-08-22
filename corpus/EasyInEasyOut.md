# EasyInEasyOut

Source: [`mikedigriz/freqtrade-strategy-mikedigriz`](https://github.com/mikedigriz/freqtrade-strategy-mikedigriz) · file `EasyInEasyOut.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 83 | — |
| average profit per trade % | -4.23 | — |
| win rate % | 91.6 | — |
| average trade duration, minutes | 78437.0 | — |
| duration measured in own candles | 78437.0 | — |
| expectancy per trade (USDT) | -5.57 | — |
| mean profit p-value | 0.06388 | — |
| market change % (baseline) | -55.54 | — |
| strategy total % | -46.27 | — |
| Sharpe | -0.45 | — |
| Sortino | -0.66 | — |
| max drawdown % | 54.6 | — |
| profit factor | 0.28 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+9.3 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.06388 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-46.27%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
