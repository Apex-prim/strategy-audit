# RSI

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `RSI.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 35 | 365 |
| average profit per trade % | -10.34 | 2.29 |
| win rate % | 80.0 | 98.1 |
| average trade duration, minutes | 183665.0 | 62372.0 |
| duration measured in own candles | 12244.33 | 4158.13 |
| expectancy per trade (USDT) | -13.41 | 3.82 |
| mean profit p-value | 0.05053 | 0.2054 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -46.93 | 139.61 |
| Sharpe | -0.32 | 0.2 |
| Sortino | -0.57 | 0.17 |
| max drawdown % | 53.66 | 53.51 |
| profit factor | 0.24 | 1.51 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+11.2 pp**, out of sample **-206.2 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.05053 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-46.93%**.
Out of sample: buy-and-hold **345.85%** vs strategy **139.61%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
