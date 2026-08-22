# Trend_Strength_Directional

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `Trend_Strength_Directional.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1624 | 6060 |
| average profit per trade % | -0.34 | 0.17 |
| win rate % | 70.9 | 70.9 |
| average trade duration, minutes | 3993.0 | 3915.0 |
| duration measured in own candles | 266.2 | 261.0 |
| expectancy per trade (USDT) | -0.42 | -0.02 |
| mean profit p-value | 0.003714 | 0.9564 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -68.44 | -9.26 |
| Sharpe | -3.06 | -0.03 |
| Sortino | -1.89 | -0.02 |
| max drawdown % | 72.4 | 84.78 |
| profit factor | 0.66 | 1.0 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-10.3 pp**, out of sample **-355.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-68.44%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-9.26%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
