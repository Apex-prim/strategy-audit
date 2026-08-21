# MomentumRegimeBasket

Source: [`nateemma/strategies`](https://github.com/nateemma/strategies) · file `MomentumRegimeBasket.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 52 | 293 |
| expectancy per trade (USDT) | 5.67 | 11.78 |
| mean profit p-value | 0.2192 | 0.008619 |
| market change % (baseline) | -47.82 | 352.61 |
| strategy total % | 29.47 | 345.26 |
| Sharpe | 0.27 | 0.37 |
| Sortino | 1.0 | 1.38 |
| max drawdown % | 8.9 | 13.08 |
| profit factor | 2.17 | 2.03 |

**Retained out of sample: 208%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.2192 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-47.82%**; the strategy returned **29.47%**.
Out of sample: buy-and-hold **352.61%** vs strategy **345.26%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
