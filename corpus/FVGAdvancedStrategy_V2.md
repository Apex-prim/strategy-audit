# FVGAdvancedStrategy_V2

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `FVGAdvancedStrategy_V2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 473 | 1553 |
| expectancy per trade (USDT) | -0.17 | -0.29 |
| mean profit p-value | 0.8574 | 0.6353 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -7.9 | -45.6 |
| Sharpe | -0.1 | -0.15 |
| Sortino | -0.09 | -0.13 |
| max drawdown % | 40.57 | 74.92 |
| profit factor | 0.95 | 0.92 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.8574 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-7.9%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-45.6%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
