# CombinedBinHClucAndMADV9

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHClucAndMADV9.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 748 | 2094 |
| average profit per trade % | 0.1 | 0.32 |
| win rate % | 80.5 | 82.0 |
| average trade duration, minutes | 169.0 | 199.0 |
| duration measured in own candles | 33.8 | 39.8 |
| expectancy per trade (USDT) | 0.13 | 0.59 |
| mean profit p-value | 0.1968 | 1.959e-07 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 9.48 | 124.23 |
| Sharpe | 0.93 | 1.93 |
| Sortino | 0.81 | 1.52 |
| max drawdown % | 11.9 | 11.83 |
| profit factor | 1.15 | 1.41 |

**Retained out of sample: 454%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+68.5 pp**, out of sample **-222.1 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1968 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **9.48%**.
Out of sample: buy-and-hold **346.34%** vs strategy **124.23%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
