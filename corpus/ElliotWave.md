# ElliotWave

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `ElliotWave.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 535 | — |
| average profit per trade % | -0.18 | — |
| win rate % | 49.9 | — |
| average trade duration, minutes | 5459.0 | — |
| duration measured in own candles | 22.75 | — |
| expectancy per trade (USDT) | -0.36 | — |
| mean profit p-value | 0.3363 | — |
| market change % (baseline) | -45.47 | — |
| strategy total % | -19.14 | — |
| Sharpe | -0.61 | — |
| Sortino | -0.92 | — |
| max drawdown % | 40.93 | — |
| profit factor | 0.9 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+26.3 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3363 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-45.47%**; the strategy returned **-19.14%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 5, выходов 6 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
