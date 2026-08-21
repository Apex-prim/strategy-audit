# ADXMomentum

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ADXMomentum.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 20 | 63 |
| expectancy per trade (USDT) | 0.16 | -0.61 |
| mean profit p-value | 0.7087 | 0.1589 |
| market change % (baseline) | -59.31 | 348.67 |
| strategy total % | 0.33 | -3.84 |
| Sharpe | 0.05 | -0.09 |
| Sortino | 0.14 | -0.09 |
| max drawdown % | 0.74 | 4.74 |
| profit factor | 1.21 | 0.58 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.7087 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.31%**; the strategy returned **0.33%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-3.84%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 25 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
