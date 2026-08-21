# TheRealPullbackV2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `TheRealPullbackV2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 229 | 689 |
| expectancy per trade (USDT) | 0.47 | 0.97 |
| mean profit p-value | 0.05565 | 0.0002219 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 10.76 | 67.0 |
| Sharpe | 0.76 | 0.79 |
| Sortino | 1.49 | 2.37 |
| max drawdown % | 3.34 | 8.94 |
| profit factor | 1.38 | 1.47 |

**Retained out of sample: 206%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.05565 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **10.76%**.
Out of sample: buy-and-hold **346.34%** vs strategy **67.0%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 200 при потребности 26 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
