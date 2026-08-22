# CombinedBinHAndClucV3

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `CombinedBinHAndClucV3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 687 | 1902 |
| average profit per trade % | 0.1 | 0.52 |
| win rate % | 78.6 | 84.8 |
| average trade duration, minutes | 681.0 | 452.0 |
| duration measured in own candles | 136.2 | 90.4 |
| expectancy per trade (USDT) | 0.1 | 1.17 |
| mean profit p-value | 0.5701 | 6.407e-07 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | 6.59 | 222.87 |
| Sharpe | 0.39 | 1.76 |
| Sortino | 0.32 | 0.92 |
| max drawdown % | 16.63 | 24.1 |
| profit factor | 1.07 | 1.53 |

**Retained out of sample: 1170%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+65.0 pp**, out of sample **-123.5 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.5701 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **6.59%**.
Out of sample: buy-and-hold **346.34%** vs strategy **222.87%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
