# GKD_FisherTransformMTF

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `GKD_FisherTransformMTF.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1022 | 3728 |
| expectancy per trade (USDT) | -0.46 | 0.17 |
| mean profit p-value | 0.02878 | 0.79 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -47.03 | 65.02 |
| Sharpe | -1.83 | 0.13 |
| Sortino | -3.73 | 0.32 |
| max drawdown % | 64.5 | 77.34 |
| profit factor | 0.81 | 1.02 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-47.03%**.
Out of sample: buy-and-hold **348.67%** vs strategy **65.02%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 4 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.02 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
