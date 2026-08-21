# tbtest

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `tbedit (2).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1164 | 3720 |
| expectancy per trade (USDT) | 0.04 | 0.26 |
| mean profit p-value | 0.7794 | 0.1192 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | 4.94 | 94.87 |
| Sharpe | 0.25 | 0.77 |
| Sortino | 0.31 | 1.04 |
| max drawdown % | 24.91 | 55.9 |
| profit factor | 1.02 | 1.06 |

**Retained out of sample: 650%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.7794 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **4.94%**.
Out of sample: buy-and-hold **346.34%** vs strategy **94.87%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 30 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
