# Obelisk_TradePro_Ichi_v1_1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Obelisk_TradePro_Ichi_v1_1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 992 | 4067 |
| expectancy per trade (USDT) | 0.23 | 0.07 |
| mean profit p-value | 0.232 | 0.5473 |
| market change % (baseline) | -59.31 | 348.67 |
| strategy total % | 22.6 | 28.57 |
| Sharpe | 0.99 | 0.31 |
| Sortino | 9.21 | 2.82 |
| max drawdown % | 12.42 | 42.7 |
| profit factor | 1.17 | 1.05 |

**Retained out of sample: 30%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.232 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.31%**; the strategy returned **22.6%**.
Out of sample: buy-and-hold **348.67%** vs strategy **28.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
