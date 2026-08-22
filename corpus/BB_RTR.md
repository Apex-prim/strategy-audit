# BB_RTR

Source: [`ShahAnuj2610/my-freqtrade`](https://github.com/ShahAnuj2610/my-freqtrade) · file `BB_RTR.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 178 | 809 |
| average profit per trade % | 1.11 | 1.11 |
| win rate % | 67.4 | 60.8 |
| average trade duration, minutes | 124.0 | 62.0 |
| duration measured in own candles | 24.8 | 12.4 |
| expectancy per trade (USDT) | 1.55 | 2.5 |
| mean profit p-value | 1.982e-08 | 1.82e-21 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 27.52 | 202.1 |
| Sharpe | 2.06 | 2.25 |
| Sortino | 2.03 | 2.16 |
| max drawdown % | 1.91 | 3.06 |
| profit factor | 3.38 | 3.39 |

**Retained out of sample: 161%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+86.8 pp**, out of sample **-144.2 pp**.

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

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
