# VolatilitySystem

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `VolatilitySystem.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 156 | 518 |
| average profit per trade % | 1.44 | 4.15 |
| win rate % | 37.8 | 37.6 |
| average trade duration, minutes | 20346.0 | 22494.0 |
| duration measured in own candles | 339.1 | 374.9 |
| expectancy per trade (USDT) | 3.6 | 14.06 |
| mean profit p-value | 0.08096 | 0.04625 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | 56.09 | 728.15 |
| Sharpe | 0.58 | 0.37 |
| Sortino | 1.94 | 0.94 |
| max drawdown % | 27.1 | 29.81 |
| profit factor | 1.63 | 1.49 |

**Retained out of sample: 391%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+114.5 pp**, out of sample **+379.5 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.08096 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **56.09%**.
Out of sample: buy-and-hold **348.67%** vs strategy **728.15%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
