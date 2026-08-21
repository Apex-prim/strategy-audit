# NFINextMultiOffsetAndHO

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NFINextMultiOffsetAndHO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 219 | 875 |
| expectancy per trade (USDT) | 0.68 | 3.03 |
| mean profit p-value | 0.00379 | 2.62e-17 |
| market change % (baseline) | -58.96 | 346.34 |
| strategy total % | 14.97 | 265.18 |
| Sharpe | 1.14 | 2.07 |
| Sortino | 1.23 | 1.78 |
| max drawdown % | 5.31 | 7.22 |
| profit factor | 1.73 | 2.54 |

**Retained out of sample: 446%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.96%**; the strategy returned **14.97%**.
Out of sample: buy-and-hold **346.34%** vs strategy **265.18%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317%, stochrsi_fastd_96 -0.557%, kama_offset_buy 0.029% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
