# SMAOffsetProtectOptV1_kkeue_20210619

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `SMAOffsetProtectOptV1_kkeue_20210619.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 27 | 179 |
| expectancy per trade (USDT) | 1.43 | 1.37 |
| mean profit p-value | 0.0002127 | 0.0002101 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | 3.86 | 24.51 |
| Sharpe | 0.6 | 0.41 |
| Sortino | 0.51 | 0.16 |
| max drawdown % | 0.46 | 4.61 |
| profit factor | 6.67 | 2.88 |

**Retained out of sample: 96%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **3.86%**.
Out of sample: buy-and-hold **346.34%** vs strategy **24.51%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.935% |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
