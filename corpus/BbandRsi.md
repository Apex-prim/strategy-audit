# bbandrsi

Source: [`phuchust/freqtrade_strategy`](https://github.com/phuchust/freqtrade_strategy) · file `bbandrsi.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1528 | 5230 |
| expectancy per trade (USDT) | -0.46 | -0.13 |
| mean profit p-value | 8.472e-07 | 0.1679 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -70.41 | -67.81 |
| Sharpe | -5.05 | -0.81 |
| Sortino | -4.69 | -0.67 |
| max drawdown % | 72.22 | 84.9 |
| profit factor | 0.66 | 0.93 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-70.41%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-67.81%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
