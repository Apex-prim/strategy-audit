# Inverse

Source: [`Foxel05/freqtrade-stuff`](https://github.com/Foxel05/freqtrade-stuff) · file `Inverse.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 449 | 2021 |
| average profit per trade % | 0.18 | 0.14 |
| win rate % | 27.8 | 29.1 |
| average trade duration, minutes | 1321.0 | 1241.0 |
| duration measured in own candles | 22.02 | 20.68 |
| expectancy per trade (USDT) | 0.18 | 0.15 |
| mean profit p-value | 0.5077 | 0.4343 |
| market change % (baseline) | -54.03 | 348.67 |
| strategy total % | 8.21 | 30.78 |
| Sharpe | 0.37 | 0.28 |
| Sortino | 0.92 | 0.69 |
| max drawdown % | 15.21 | 37.39 |
| profit factor | 1.11 | 1.06 |

**Retained out of sample: 83%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+62.2 pp**, out of sample **-317.9 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.5077 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-54.03%**; the strategy returned **8.21%**.
Out of sample: buy-and-hold **348.67%** vs strategy **30.78%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_4h -0.020%, ema_200 -0.448% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
