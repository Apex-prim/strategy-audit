# MACDCrossoverWithTrend

Source: [`paulcpk/freqtrade-strategies-that-work`](https://github.com/paulcpk/freqtrade-strategies-that-work) · file `MACDCrossoverWithTrend.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 303 | 1288 |
| expectancy per trade (USDT) | 0.53 | 0.03 |
| mean profit p-value | 0.1283 | 0.8829 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | 16.0 | 4.26 |
| Sharpe | 0.69 | 0.04 |
| Sortino | 2.87 | 0.19 |
| max drawdown % | 6.99 | 26.26 |
| profit factor | 1.39 | 1.02 |

**Retained out of sample: 6%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1283 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **16.0%**.
Out of sample: buy-and-hold **348.67%** vs strategy **4.26%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.03 задан — читается как работающая защита |
| minimal_roi закомментирован | **found** | правила выхода по прибыли берутся из неопубликованного конфига |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `—`*
