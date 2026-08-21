# SMAOffset_Hippocritical_dca

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `SMAOffset_Hippocritical_dca.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 27 | 191 |
| expectancy per trade (USDT) | 0.5 | 0.51 |
| mean profit p-value | 2.385e-10 | 8.432e-17 |
| market change % (baseline) | -59.3 | 346.34 |
| strategy total % | 1.35 | 9.72 |
| Sharpe | 1.38 | 1.03 |
| Sortino | -100.0 | 0.29 |
| max drawdown % | 0.03 | 0.63 |
| profit factor | 50.9 | 8.74 |

**Retained out of sample: 102%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.3%**; the strategy returned **1.35%**.
Out of sample: buy-and-hold **346.34%** vs strategy **9.72%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
