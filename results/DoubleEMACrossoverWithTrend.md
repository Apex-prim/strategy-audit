# DoubleEMACrossoverWithTrend

Source: [`paulcpk/freqtrade-strategies-that-work`](https://github.com/paulcpk/freqtrade-strategies-that-work) · file `DoubleEMACrossoverWithTrend.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 861 | 3617 |
| expectancy per trade (USDT) | 0.49 | 0.22 |
| mean profit p-value | 0.04906 | 0.2898 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | 42.43 | 81.08 |
| Sharpe | 1.51 | 0.51 |
| Sortino | 6.56 | 1.97 |
| max drawdown % | 19.74 | 45.37 |
| profit factor | 1.31 | 1.08 |

**Retained out of sample: 45%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **42.43%**.
Out of sample: buy-and-hold **348.67%** vs strategy **81.08%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.03 задан — читается как работающая защита |
| minimal_roi закомментирован | **found** | правила выхода по прибыли берутся из неопубликованного конфига |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `—`*
