# Slowbro

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Slowbro.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 21 | 74 |
| expectancy per trade (USDT) | -11.63 | 5.24 |
| mean profit p-value | 0.3226 | 0.4581 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -24.43 | 38.78 |
| Sharpe | -0.12 | 0.05 |
| Sortino | -0.18 | 0.1 |
| max drawdown % | 41.1 | 45.97 |
| profit factor | 0.54 | 1.33 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.3226 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-24.43%**.
Out of sample: buy-and-hold **348.67%** vs strategy **38.78%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
