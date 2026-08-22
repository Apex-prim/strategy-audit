# INSIDEUP

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `INSIDEUP.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 70 | 484 |
| average profit per trade % | -3.73 | 1.44 |
| win rate % | 81.4 | 90.3 |
| average trade duration, minutes | 85351.0 | 44039.0 |
| duration measured in own candles | 59.27 | 30.58 |
| expectancy per trade (USDT) | -5.17 | 2.08 |
| mean profit p-value | 0.1258 | 0.29 |
| market change % (baseline) | -59.68 | 352.61 |
| strategy total % | -36.18 | 100.85 |
| Sharpe | -0.34 | 0.19 |
| Sortino | -0.21 | 0.07 |
| max drawdown % | 48.18 | 54.48 |
| profit factor | 0.39 | 1.42 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+23.5 pp**, out of sample **-251.8 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1258 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.68%**; the strategy returned **-36.18%**.
Out of sample: buy-and-hold **352.61%** vs strategy **100.85%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
