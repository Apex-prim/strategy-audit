# BigZ04_TSL3

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `BigZ04_TSL3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 456 | 1187 |
| expectancy per trade (USDT) | -0.8 | -0.6 |
| mean profit p-value | 1.687e-05 | 1.231e-16 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | -36.6 | -70.77 |
| Sharpe | -2.43 | -2.34 |
| Sortino | -2.53 | -2.25 |
| max drawdown % | 40.3 | 71.28 |
| profit factor | 0.55 | 0.47 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **-36.6%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-70.77%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
