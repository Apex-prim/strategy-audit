# BB_RTR

Source: [`ShahAnuj2610/my-freqtrade`](https://github.com/ShahAnuj2610/my-freqtrade) · file `BB_RTR.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 178 | 809 |
| expectancy per trade (USDT) | 1.55 | 2.5 |
| mean profit p-value | 1.982e-08 | 1.82e-21 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 27.52 | 202.1 |
| Sharpe | 2.06 | 2.25 |
| Sortino | 2.03 | 2.16 |
| max drawdown % | 1.91 | 3.06 |
| profit factor | 3.38 | 3.39 |

**Retained out of sample: 161%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **27.52%**.
Out of sample: buy-and-hold **346.34%** vs strategy **202.1%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi_84 2.859%, rsi_112 3.913%, EWO -12.317%, ema_vwap_diff_50 -0.717%, rsi_42_1h 0.055% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
