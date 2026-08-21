# Ichess

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Ichess.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 62 | 293 |
| expectancy per trade (USDT) | 0.23 | 2.4 |
| mean profit p-value | 0.9539 | 0.4566 |
| market change % (baseline) | -59.68 | 352.61 |
| strategy total % | 1.45 | 70.22 |
| Sharpe | 0.01 | 0.1 |
| Sortino | 0.03 | 0.19 |
| max drawdown % | 34.24 | 44.61 |
| profit factor | 1.02 | 1.12 |

**Retained out of sample: 1043%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.9539 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.68%**; the strategy returned **1.45%**.
Out of sample: buy-and-hold **352.61%** vs strategy **70.22%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
