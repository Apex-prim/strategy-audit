# JuicyTrend

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `JuicyTrend.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 10455 | 13681 |
| expectancy per trade (USDT) | -0.09 | -0.07 |
| mean profit p-value | 7.047e-19 | 1.256e-13 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -95.77 | -96.58 |
| Sharpe | -23.76 | -7.02 |
| Sortino | -40.72 | -13.14 |
| max drawdown % | 95.92 | 96.71 |
| profit factor | 0.71 | 0.79 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-95.77%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
