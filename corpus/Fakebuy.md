# Fakebuy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `Fakebuy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 36 | 335 |
| expectancy per trade (USDT) | -0.75 | 0.1 |
| mean profit p-value | 0.3316 | 0.6904 |
| market change % (baseline) | -59.11 | 346.34 |
| strategy total % | -2.71 | 3.28 |
| Sharpe | -0.16 | 0.06 |
| Sortino | -8.91 | 1.1 |
| max drawdown % | 3.22 | 8.4 |
| profit factor | 0.58 | 1.07 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.3316 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.11%**; the strategy returned **-2.71%**.
Out of sample: buy-and-hold **346.34%** vs strategy **3.28%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 168 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
