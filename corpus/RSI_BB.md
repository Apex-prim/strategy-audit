# RSI_BB

Source: [`mikedigriz/freqtrade-strategy-mikedigriz`](https://github.com/mikedigriz/freqtrade-strategy-mikedigriz) · file `RSI_BB.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3471 | 11460 |
| expectancy per trade (USDT) | -0.23 | -0.06 |
| mean profit p-value | 8.836e-08 | 0.6599 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -81.22 | -67.93 |
| Sharpe | -8.26 | -0.38 |
| Sortino | -7.04 | -0.32 |
| max drawdown % | 85.31 | 94.81 |
| profit factor | 0.71 | 0.98 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-81.22%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-67.93%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
