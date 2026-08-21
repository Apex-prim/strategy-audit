# CCIStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CCIStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2468 | 9880 |
| expectancy per trade (USDT) | -0.19 | -0.09 |
| mean profit p-value | 1.854e-06 | 4.777e-07 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -48.03 | -88.51 |
| Sharpe | -6.21 | -4.05 |
| Sortino | -21.13 | -8.14 |
| max drawdown % | 51.75 | 89.92 |
| profit factor | 0.79 | 0.86 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-48.03%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-88.51%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
