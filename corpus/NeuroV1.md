# NeuroV1

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `NeuroV1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1860 | 7511 |
| expectancy per trade (USDT) | 0.02 | -0.07 |
| mean profit p-value | 0.9053 | 0.4789 |
| market change % (baseline) | -52.66 | 348.67 |
| strategy total % | 3.05 | -51.65 |
| Sharpe | 0.14 | -0.5 |
| Sortino | 0.35 | -1.09 |
| max drawdown % | 40.12 | 85.95 |
| profit factor | 1.01 | 0.96 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.9053 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-52.66%**; the strategy returned **3.05%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-51.65%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
