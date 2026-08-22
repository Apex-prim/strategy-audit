# BinHV27

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `BinHV27.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2571 | 8932 |
| average profit per trade % | -0.15 | -0.1 |
| win rate % | 55.8 | 57.1 |
| average trade duration, minutes | 315.0 | 298.0 |
| duration measured in own candles | 63.0 | 59.6 |
| expectancy per trade (USDT) | -0.15 | -0.08 |
| mean profit p-value | 0.0001062 | 0.007594 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -39.84 | -73.94 |
| Sharpe | -5.15 | -2.04 |
| Sortino | -5.18 | -1.93 |
| max drawdown % | 46.73 | 84.17 |
| profit factor | 0.78 | 0.88 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+18.4 pp**, out of sample **-420.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-39.84%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-73.94%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 240 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
