# WaveTrendStra

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `WaveTrendStra.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1885 | 7371 |
| expectancy per trade (USDT) | 0.23 | 0.08 |
| mean profit p-value | 0.1435 | 0.6671 |
| market change % (baseline) | -57.43 | 340.8 |
| strategy total % | 42.79 | 57.64 |
| Sharpe | 1.66 | 0.3 |
| Sortino | 4.69 | 0.67 |
| max drawdown % | 32.97 | 75.71 |
| profit factor | 1.12 | 1.02 |

**Retained out of sample: 35%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1435 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-57.43%**; the strategy returned **42.79%**.
Out of sample: buy-and-hold **340.8%** vs strategy **57.64%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
