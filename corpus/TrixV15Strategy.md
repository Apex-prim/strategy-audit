# TrixV15Strategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `TrixV15Strategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 316 | 1128 |
| average profit per trade % | -0.98 | -0.23 |
| win rate % | 77.8 | 76.2 |
| average trade duration, minutes | 6260.0 | 6706.0 |
| duration measured in own candles | 104.33 | 111.77 |
| expectancy per trade (USDT) | -1.15 | -0.31 |
| mean profit p-value | 0.03201 | 0.2411 |
| market change % (baseline) | -59.12 | 348.67 |
| strategy total % | -36.44 | -35.47 |
| Sharpe | -1.0 | -0.32 |
| Sortino | -0.59 | -0.19 |
| max drawdown % | 39.27 | 51.68 |
| profit factor | 0.53 | 0.83 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+22.7 pp**, out of sample **-384.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.12%**; the strategy returned **-36.44%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-35.47%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
