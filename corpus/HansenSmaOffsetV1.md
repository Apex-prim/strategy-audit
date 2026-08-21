# HansenSmaOffsetV1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `HansenSmaOffsetV1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 27 | 92 |
| expectancy per trade (USDT) | -6.71 | 36.87 |
| mean profit p-value | 0.2359 | 0.09532 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -18.11 | 339.17 |
| Sharpe | -0.17 | 0.13 |
| Sortino | -0.26 | 0.18 |
| max drawdown % | 21.88 | 53.3 |
| profit factor | 0.53 | 1.66 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.2359 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-18.11%**.
Out of sample: buy-and-hold **345.85%** vs strategy **339.17%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
