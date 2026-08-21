# BBRSIv2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BBRSIv2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 90 | 494 |
| expectancy per trade (USDT) | -2.51 | 1.35 |
| mean profit p-value | 0.2726 | 0.1909 |
| market change % (baseline) | -58.99 | 345.85 |
| strategy total % | -22.58 | 66.71 |
| Sharpe | -0.28 | 0.24 |
| Sortino | -0.15 | 0.06 |
| max drawdown % | 38.03 | 43.5 |
| profit factor | 0.53 | 1.52 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.2726 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.99%**; the strategy returned **-22.58%**.
Out of sample: buy-and-hold **345.85%** vs strategy **66.71%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 60 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
