# TrixStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `TrixStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2770 | 10784 |
| average profit per trade % | 0.36 | 0.11 |
| win rate % | 45.8 | 40.6 |
| average trade duration, minutes | 1185.0 | 1072.0 |
| duration measured in own candles | 19.75 | 17.87 |
| expectancy per trade (USDT) | 0.7 | 0.13 |
| mean profit p-value | 0.0003718 | 0.5867 |
| market change % (baseline) | -59.13 | 348.67 |
| strategy total % | 193.42 | 141.71 |
| Sharpe | 4.91 | 0.46 |
| Sortino | 8.21 | 0.69 |
| max drawdown % | 31.54 | 81.11 |
| profit factor | 1.25 | 1.02 |

**Retained out of sample: 19%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+252.5 pp**, out of sample **-207.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.13%**; the strategy returned **193.42%**.
Out of sample: buy-and-hold **348.67%** vs strategy **141.71%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
