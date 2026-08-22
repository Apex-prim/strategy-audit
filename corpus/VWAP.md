# VWAP

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `VWAP.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 200 | 786 |
| average profit per trade % | 1.06 | 0.62 |
| win rate % | 94.5 | 92.0 |
| average trade duration, minutes | 1082.0 | 374.0 |
| duration measured in own candles | 216.4 | 74.8 |
| expectancy per trade (USDT) | 1.48 | 0.99 |
| mean profit p-value | 0.0001053 | 0.002752 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | 29.61 | 78.13 |
| Sharpe | 1.47 | 0.68 |
| Sortino | 5.29 | 1.36 |
| max drawdown % | 6.33 | 22.26 |
| profit factor | 2.32 | 1.41 |

**Retained out of sample: 67%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+87.8 pp**, out of sample **-268.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **29.61%**.
Out of sample: buy-and-hold **346.34%** vs strategy **78.13%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 112 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
