# BigZ04_TSL4

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `BigZ04_TSL4.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 479 | 1277 |
| expectancy per trade (USDT) | -0.72 | -0.56 |
| mean profit p-value | 6.899e-05 | 2.162e-16 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | -34.67 | -71.49 |
| Sharpe | -2.31 | -2.41 |
| Sortino | -2.38 | -2.3 |
| max drawdown % | 39.93 | 72.01 |
| profit factor | 0.58 | 0.48 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **-34.67%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-71.49%** — loses to it.

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
