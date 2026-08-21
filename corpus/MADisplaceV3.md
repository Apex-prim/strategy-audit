# MADisplaceV3

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `MADisplaceV3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 175 | 543 |
| expectancy per trade (USDT) | 0.22 | 0.83 |
| mean profit p-value | 0.3116 | 9.242e-05 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 3.86 | 45.27 |
| Sharpe | 0.35 | 0.74 |
| Sortino | 0.39 | 0.59 |
| max drawdown % | 8.13 | 7.65 |
| profit factor | 1.23 | 1.66 |

**Retained out of sample: 377%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.3116 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **3.86%**.
Out of sample: buy-and-hold **346.34%** vs strategy **45.27%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
