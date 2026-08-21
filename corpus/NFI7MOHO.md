# NFI7MOHO

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NFI7MOHO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 402 | 1564 |
| expectancy per trade (USDT) | 0.21 | 0.86 |
| mean profit p-value | 0.07765 | 1.875e-11 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 8.64 | 134.92 |
| Sharpe | 0.93 | 2.16 |
| Sortino | 0.73 | 1.85 |
| max drawdown % | 4.85 | 6.23 |
| profit factor | 1.3 | 1.77 |

**Retained out of sample: 410%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.07765 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **8.64%**.
Out of sample: buy-and-hold **346.34%** vs strategy **134.92%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
