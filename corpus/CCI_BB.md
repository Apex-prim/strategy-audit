# CCI_BB

Source: [`mikedigriz/freqtrade-strategy-mikedigriz`](https://github.com/mikedigriz/freqtrade-strategy-mikedigriz) · file `CCI_BB.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 81 | 845 |
| expectancy per trade (USDT) | -5.42 | 3.17 |
| mean profit p-value | 0.08116 | 0.149 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -43.92 | 268.22 |
| Sharpe | -0.42 | 0.34 |
| Sortino | -0.61 | 0.18 |
| max drawdown % | 53.68 | 56.48 |
| profit factor | 0.32 | 1.56 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.08116 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-43.92%**.
Out of sample: buy-and-hold **346.34%** vs strategy **268.22%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
