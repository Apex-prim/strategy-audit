# CombinedBinHAndClucV5Hyperoptable

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `CombinedBinHAndClucV5Hyperoptable.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 702 | 2003 |
| average profit per trade % | -0.05 | 0.32 |
| win rate % | 65.5 | 73.7 |
| average trade duration, minutes | 173.0 | 122.0 |
| duration measured in own candles | 34.6 | 24.4 |
| expectancy per trade (USDT) | -0.07 | 0.57 |
| mean profit p-value | 0.5293 | 8.577e-06 |
| market change % (baseline) | -58.48 | 346.34 |
| strategy total % | -5.13 | 114.39 |
| Sharpe | -0.44 | 1.62 |
| Sortino | -0.47 | 1.32 |
| max drawdown % | 25.57 | 23.16 |
| profit factor | 0.94 | 1.32 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+53.3 pp**, out of sample **-231.9 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.5293 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.48%**; the strategy returned **-5.13%**.
Out of sample: buy-and-hold **346.34%** vs strategy **114.39%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_slow 0.013% |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
