# NFINextMOHO2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NFINextMOHO2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 357 | 1427 |
| expectancy per trade (USDT) | 0.14 | 0.76 |
| mean profit p-value | 0.489 | 3.395e-05 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 4.84 | 108.76 |
| Sharpe | 0.34 | 1.27 |
| Sortino | 0.19 | 0.73 |
| max drawdown % | 7.67 | 18.35 |
| profit factor | 1.15 | 1.54 |

**Retained out of sample: 543%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.489 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **4.84%**.
Out of sample: buy-and-hold **346.34%** vs strategy **108.76%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317%, kama_offset_buy 0.014% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
