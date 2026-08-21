# FSupertrendStrategy

Source: [`freqtrade/freqtrade-strategies`](https://github.com/freqtrade/freqtrade-strategies) · file `FSupertrendStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1760 | 6492 |
| expectancy per trade (USDT) | -0.1 | -0.02 |
| mean profit p-value | 0.3202 | 0.763 |
| market change % (baseline) | -59.19 | 348.67 |
| strategy total % | -17.89 | -14.49 |
| Sharpe | -1.09 | -0.2 |
| Sortino | -1.51 | -0.24 |
| max drawdown % | 39.75 | 62.76 |
| profit factor | 0.95 | 0.99 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.3202 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.19%**; the strategy returned **-17.89%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-14.49%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
