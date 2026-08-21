# Renko

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Renko.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11 | 113 |
| expectancy per trade (USDT) | -3.09 | 50.17 |
| mean profit p-value | 0.8385 | 3.329e-05 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -3.4 | 566.89 |
| Sharpe | -0.02 | 0.37 |
| Sortino | -0.1 | 0.37 |
| max drawdown % | 17.34 | 21.9 |
| profit factor | 0.83 | 4.03 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.8385 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-3.4%**.
Out of sample: buy-and-hold **345.85%** vs strategy **566.89%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 13, выходов 0 из 13 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 5 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
