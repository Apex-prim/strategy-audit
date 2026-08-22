# ReinforcedSmoothScalp

Source: [`MelvynClark/Freqtrade-Strategy`](https://github.com/MelvynClark/Freqtrade-Strategy) · file `ReinforcedSmoothScalp.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 121 | 542 |
| average profit per trade % | 0.43 | 0.11 |
| win rate % | 73.6 | 67.5 |
| average trade duration, minutes | 1089.0 | 988.0 |
| duration measured in own candles | 72.6 | 65.87 |
| expectancy per trade (USDT) | 0.55 | 0.13 |
| mean profit p-value | 0.08201 | 0.4299 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | 6.6 | 6.91 |
| Sharpe | 0.51 | 0.15 |
| Sortino | 0.44 | 0.13 |
| max drawdown % | 3.01 | 6.77 |
| profit factor | 1.53 | 1.1 |

**Retained out of sample: 24%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+64.7 pp**, out of sample **-338.9 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.08201 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **6.6%**.
Out of sample: buy-and-hold **345.85%** vs strategy **6.91%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
