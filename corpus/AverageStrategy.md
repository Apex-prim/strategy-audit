# AverageStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `AverageStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 600 | 2275 |
| expectancy per trade (USDT) | 0.7 | 1.49 |
| mean profit p-value | 0.1874 | 0.1035 |
| market change % (baseline) | -57.43 | 340.8 |
| strategy total % | 41.95 | 340.05 |
| Sharpe | 0.85 | 0.63 |
| Sortino | 3.75 | 1.95 |
| max drawdown % | 31.11 | 51.57 |
| profit factor | 1.22 | 1.14 |

**Retained out of sample: 213%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1874 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-57.43%**; the strategy returned **41.95%**.
Out of sample: buy-and-hold **340.8%** vs strategy **340.05%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 21 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
