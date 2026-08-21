# SMAIP3

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `SMAIP3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 74 | 290 |
| expectancy per trade (USDT) | 1.07 | 1.74 |
| mean profit p-value | 0.1503 | 0.001549 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | 7.94 | 50.4 |
| Sharpe | 0.33 | 0.44 |
| Sortino | 0.16 | 0.24 |
| max drawdown % | 4.11 | 4.65 |
| profit factor | 2.02 | 2.35 |

**Retained out of sample: 163%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1503 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **7.94%**.
Out of sample: buy-and-hold **346.34%** vs strategy **50.4%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев занижен | **found** | объявлено 30, нужно не менее 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
