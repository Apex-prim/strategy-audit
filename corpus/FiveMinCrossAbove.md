# FiveMinCrossAbove

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FiveMinCrossAbove.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 172 | 1679 |
| average profit per trade % | -2.03 | 0.44 |
| win rate % | 95.9 | 99.6 |
| average trade duration, minutes | 37517.0 | 13861.0 |
| duration measured in own candles | 7503.4 | 2772.2 |
| expectancy per trade (USDT) | -2.67 | 0.62 |
| mean profit p-value | 0.06019 | 0.3158 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -45.96 | 104.67 |
| Sharpe | -0.65 | 0.33 |
| Sortino | -0.57 | 0.12 |
| max drawdown % | 53.8 | 56.89 |
| profit factor | 0.27 | 1.39 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+12.3 pp**, out of sample **-241.7 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.06019 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-45.96%**.
Out of sample: buy-and-hold **346.34%** vs strategy **104.67%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
