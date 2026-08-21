# NostalgiaForInfinityX7

Source: [`iterativv/NostalgiaForInfinity`](https://github.com/iterativv/NostalgiaForInfinity) · file `NostalgiaForInfinityX7.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 60 | 329 |
| expectancy per trade (USDT) | 2.23 | 4.49 |
| mean profit p-value | 9.531e-20 | 7.27e-49 |
| market change % (baseline) | -59.75 | 346.34 |
| strategy total % | 13.37 | 147.63 |
| Sharpe | 2.77 | 2.57 |
| Sortino | -100.0 | -100.0 |
| max drawdown % | 0.0 | 0.0 |
| profit factor | 0.0 | 0.0 |

**Retained out of sample: 201%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.75%**; the strategy returned **13.37%**.
Out of sample: buy-and-hold **346.34%** vs strategy **147.63%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: OBV_change_pct_15m 15751.239%, EMA_100_4h -0.020%, OBV_change_pct 2111.273% |
| прогрев не объявлен | **found** | самый длинный индикатор 480 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
