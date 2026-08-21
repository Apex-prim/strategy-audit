# NFI46

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NFI46.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 21 | 56 |
| expectancy per trade (USDT) | 1.89 | 3.42 |
| mean profit p-value | 0.04489 | 9.85e-16 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 3.97 | 19.14 |
| Sharpe | 0.26 | 0.68 |
| Sortino | 0.39 | 1.21 |
| max drawdown % | 1.46 | 0.24 |
| profit factor | 3.37 | 64.01 |

**Retained out of sample: 181%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **3.97%**.
Out of sample: buy-and-hold **346.34%** vs strategy **19.14%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
