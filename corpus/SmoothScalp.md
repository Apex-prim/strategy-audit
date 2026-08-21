# SmoothScalp

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `SmoothScalp.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 8950 | 17286 |
| expectancy per trade (USDT) | -0.1 | -0.06 |
| mean profit p-value | 1.502e-55 | 8.174e-29 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -87.59 | -96.57 |
| Sharpe | -39.09 | -11.87 |
| Sortino | -34.33 | -9.51 |
| max drawdown % | 87.71 | 96.57 |
| profit factor | 0.49 | 0.63 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-87.59%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
