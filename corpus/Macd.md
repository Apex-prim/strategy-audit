# Macd

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `macd.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 243 | 825 |
| expectancy per trade (USDT) | 1.18 | 3.94 |
| mean profit p-value | 0.4275 | 0.3306 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | 28.71 | 325.35 |
| Sharpe | 0.32 | 0.23 |
| Sortino | 1.44 | 1.08 |
| max drawdown % | 46.34 | 52.5 |
| profit factor | 1.18 | 1.16 |

**Retained out of sample: 334%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.4275 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **28.71%**.
Out of sample: buy-and-hold **348.67%** vs strategy **325.35%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
