# YOLO

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `YOLO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 133 | 427 |
| average profit per trade % | -0.4 | -0.43 |
| win rate % | 23.3 | 26.0 |
| average trade duration, minutes | 57.0 | 85.0 |
| duration measured in own candles | 57.0 | 85.0 |
| expectancy per trade (USDT) | -0.48 | -0.48 |
| mean profit p-value | 3.52e-08 | 1.29e-30 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -6.38 | -20.39 |
| Sharpe | -1.77 | -2.09 |
| Sortino | -4.0 | -4.47 |
| max drawdown % | 6.39 | 20.63 |
| profit factor | 0.32 | 0.27 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+49.2 pp**, out of sample **-368.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-6.38%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-20.39%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 90 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
