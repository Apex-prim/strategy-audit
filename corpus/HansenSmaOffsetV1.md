# HansenSmaOffsetV1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `HansenSmaOffsetV1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 27 | 92 |
| average profit per trade % | -5.11 | 25.06 |
| win rate % | 44.4 | 66.3 |
| average trade duration, minutes | 126654.0 | 145422.0 |
| duration measured in own candles | 8443.6 | 9694.8 |
| expectancy per trade (USDT) | -6.71 | 36.87 |
| mean profit p-value | 0.2359 | 0.09532 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -18.11 | 339.17 |
| Sharpe | -0.17 | 0.13 |
| Sortino | -0.26 | 0.18 |
| max drawdown % | 21.88 | 53.3 |
| profit factor | 0.53 | 1.66 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+40.0 pp**, out of sample **-6.7 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.2359 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-18.11%**.
Out of sample: buy-and-hold **345.85%** vs strategy **339.17%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
