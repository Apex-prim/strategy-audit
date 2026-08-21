# FVGChannel

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `FVGChannel.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4761 | 11838 |
| expectancy per trade (USDT) | -0.19 | -0.08 |
| mean profit p-value | 8.852e-17 | 2.13e-13 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -89.9 | -96.57 |
| Sharpe | -15.06 | -6.46 |
| Sortino | -12.98 | -5.89 |
| max drawdown % | 89.9 | 96.61 |
| profit factor | 0.61 | 0.76 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-89.9%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
