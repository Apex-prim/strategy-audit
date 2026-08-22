# Cluc4werk

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Cluc4werk.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 522 | 2747 |
| average profit per trade % | -0.42 | -0.63 |
| win rate % | 40.0 | 30.5 |
| average trade duration, minutes | 6.0 | 4.0 |
| duration measured in own candles | 6.0 | 4.0 |
| expectancy per trade (USDT) | -0.46 | -0.32 |
| mean profit p-value | 3.548e-10 | 3.271e-78 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -23.76 | -88.12 |
| Sharpe | -3.82 | -8.2 |
| Sortino | -8.33 | -11.7 |
| max drawdown % | 25.81 | 88.27 |
| profit factor | 0.55 | 0.39 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+31.8 pp**, out of sample **-436.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-23.76%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-88.12%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 168 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
