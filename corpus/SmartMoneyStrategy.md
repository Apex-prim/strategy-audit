# SmartMoneyStrategy

Source: [`mikedigriz/freqtrade-strategy-mikedigriz`](https://github.com/mikedigriz/freqtrade-strategy-mikedigriz) · file `smart_money_strategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 23 | 262 |
| expectancy per trade (USDT) | -20.68 | 7.39 |
| mean profit p-value | 0.03823 | 0.1117 |
| market change % (baseline) | -57.83 | 343.26 |
| strategy total % | -47.56 | 193.69 |
| Sharpe | -0.28 | 0.21 |
| Sortino | -0.52 | 0.25 |
| max drawdown % | 52.86 | 49.24 |
| profit factor | 0.19 | 1.68 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-57.83%**; the strategy returned **-47.56%**.
Out of sample: buy-and-hold **343.26%** vs strategy **193.69%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **30m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
