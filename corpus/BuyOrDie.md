# BuyOrDie

Source: [`mikedigriz/freqtrade-strategy-mikedigriz`](https://github.com/mikedigriz/freqtrade-strategy-mikedigriz) · file `BuyOrDie.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 911 | 2336 |
| expectancy per trade (USDT) | -0.59 | 0.62 |
| mean profit p-value | 0.004883 | 0.617 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -53.64 | 143.79 |
| Sharpe | -2.23 | 0.2 |
| Sortino | -28.0 | 3.14 |
| max drawdown % | 72.75 | 78.29 |
| profit factor | 0.56 | 1.08 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-53.64%**.
Out of sample: buy-and-hold **346.34%** vs strategy **143.79%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
