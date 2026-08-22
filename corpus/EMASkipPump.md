# EMASkipPump

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `EMASkipPump.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11468 | 22854 |
| average profit per trade % | -0.23 | -0.11 |
| win rate % | 55.6 | 60.6 |
| average trade duration, minutes | 184.0 | 174.0 |
| duration measured in own candles | 36.8 | 34.8 |
| expectancy per trade (USDT) | -0.08 | -0.04 |
| mean profit p-value | 5.273e-25 | 1.169e-11 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -96.61 | -96.65 |
| Sharpe | -28.97 | -8.3 |
| Sortino | -24.49 | -7.99 |
| max drawdown % | 96.65 | 96.76 |
| profit factor | 0.63 | 0.85 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.4 pp**, out of sample **-443.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-96.61%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.65%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 30 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
