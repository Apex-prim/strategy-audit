# FiveMinCrossAbove

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FiveMinCrossAbove.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 172 | 1679 |
| expectancy per trade (USDT) | -2.67 | 0.62 |
| mean profit p-value | 0.06019 | 0.3158 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -45.96 | 104.67 |
| Sharpe | -0.65 | 0.33 |
| Sortino | -0.57 | 0.12 |
| max drawdown % | 53.8 | 56.89 |
| profit factor | 0.27 | 1.39 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.06019 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-45.96%**.
Out of sample: buy-and-hold **346.34%** vs strategy **104.67%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
