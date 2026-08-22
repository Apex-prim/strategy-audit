# BbandRsiRolling

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `BbandRsiRolling.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3841 | 14075 |
| average profit per trade % | -0.28 | -0.11 |
| win rate % | 71.6 | 73.0 |
| average trade duration, minutes | 1393.0 | 1392.0 |
| duration measured in own candles | 278.6 | 278.4 |
| expectancy per trade (USDT) | -0.21 | -0.07 |
| mean profit p-value | 7.148e-07 | 0.1451 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -79.67 | -93.77 |
| Sharpe | -8.04 | -1.4 |
| Sortino | -7.68 | -1.13 |
| max drawdown % | 83.02 | 97.98 |
| profit factor | 0.79 | 0.96 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-21.4 pp**, out of sample **-440.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-79.67%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-93.77%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
