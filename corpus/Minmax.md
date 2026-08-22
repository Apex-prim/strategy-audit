# Minmax

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `MinmaxF.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 898 | 2984 |
| average profit per trade % | -1.03 | -0.03 |
| win rate % | 32.3 | 39.5 |
| average trade duration, minutes | 3517.0 | 3775.0 |
| duration measured in own candles | 58.62 | 62.92 |
| expectancy per trade (USDT) | -0.8 | -0.16 |
| mean profit p-value | 3.103e-08 | 0.3454 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -71.98 | -46.64 |
| Sharpe | -4.38 | -0.42 |
| Sortino | -15.21 | -2.37 |
| max drawdown % | 71.98 | 66.89 |
| profit factor | 0.65 | 0.96 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-13.6 pp**, out of sample **-395.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-71.98%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-46.64%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
