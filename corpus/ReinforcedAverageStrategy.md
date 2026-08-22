# ReinforcedAverageStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ReinforcedAverageStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 164 | 999 |
| average profit per trade % | 1.46 | 1.22 |
| win rate % | 27.4 | 30.2 |
| average trade duration, minutes | 5216.0 | 4911.0 |
| duration measured in own candles | 21.73 | 20.46 |
| expectancy per trade (USDT) | 1.81 | 2.49 |
| mean profit p-value | 0.1147 | 0.02526 |
| market change % (baseline) | -57.43 | 340.8 |
| strategy total % | 29.65 | 248.67 |
| Sharpe | 0.53 | 0.57 |
| Sortino | 2.61 | 1.8 |
| max drawdown % | 7.07 | 31.82 |
| profit factor | 1.58 | 1.3 |

**Retained out of sample: 138%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+87.1 pp**, out of sample **-92.1 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1147 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-57.43%**; the strategy returned **29.65%**.
Out of sample: buy-and-hold **340.8%** vs strategy **248.67%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
