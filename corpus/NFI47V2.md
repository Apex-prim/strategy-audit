# NFI47V2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NFI47V2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 137 | 387 |
| expectancy per trade (USDT) | 0.78 | 3.01 |
| mean profit p-value | 0.02804 | 5.393e-15 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 10.67 | 116.3 |
| Sharpe | 0.68 | 1.3 |
| Sortino | 0.61 | 0.84 |
| max drawdown % | 8.08 | 4.58 |
| profit factor | 1.7 | 3.77 |

**Retained out of sample: 386%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **10.67%**.
Out of sample: buy-and-hold **346.34%** vs strategy **116.3%** — loses to it.

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
