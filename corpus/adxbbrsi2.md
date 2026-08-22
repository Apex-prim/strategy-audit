# adxbbrsi2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `adxbbrsi2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 179 | 562 |
| average profit per trade % | 0.36 | -0.09 |
| win rate % | 78.2 | 74.9 |
| average trade duration, minutes | 2406.0 | 3819.0 |
| duration measured in own candles | 40.1 | 63.65 |
| expectancy per trade (USDT) | 0.46 | -0.21 |
| mean profit p-value | 0.2955 | 0.4843 |
| market change % (baseline) | -59.31 | 348.67 |
| strategy total % | 8.21 | -11.98 |
| Sharpe | 0.37 | -0.13 |
| Sortino | 0.19 | -0.07 |
| max drawdown % | 4.01 | 27.45 |
| profit factor | 1.61 | 0.82 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+67.5 pp**, out of sample **-360.7 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.2955 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.31%**; the strategy returned **8.21%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-11.98%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 1.247% |
| прогрев не объявлен | **found** | самый длинный индикатор 25 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
