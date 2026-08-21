# MacdStrategy

Source: [`DutchCryptoDad/FreqtradeBotStrategyDevelopmentForBeginners`](https://github.com/DutchCryptoDad/FreqtradeBotStrategyDevelopmentForBeginners) · file `MacdStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 103 | 351 |
| expectancy per trade (USDT) | -0.58 | 6.75 |
| mean profit p-value | 0.78 | 0.1268 |
| market change % (baseline) | -51.38 | 352.61 |
| strategy total % | -5.99 | 237.07 |
| Sharpe | -0.08 | 0.23 |
| Sortino | -0.86 | 1.57 |
| max drawdown % | 36.33 | 39.15 |
| profit factor | 0.92 | 1.28 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.78 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-51.38%**; the strategy returned **-5.99%**.
Out of sample: buy-and-hold **352.61%** vs strategy **237.07%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
