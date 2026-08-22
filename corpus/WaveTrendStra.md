# WaveTrendStra

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `WaveTrendStra.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1885 | 7371 |
| average profit per trade % | 0.21 | 0.11 |
| win rate % | 31.6 | 32.8 |
| average trade duration, minutes | 1709.0 | 1613.0 |
| duration measured in own candles | 7.12 | 6.72 |
| expectancy per trade (USDT) | 0.23 | 0.08 |
| mean profit p-value | 0.1435 | 0.6671 |
| market change % (baseline) | -57.43 | 340.8 |
| strategy total % | 42.79 | 57.64 |
| Sharpe | 1.66 | 0.3 |
| Sortino | 4.69 | 0.67 |
| max drawdown % | 32.97 | 75.71 |
| profit factor | 1.12 | 1.02 |

**Retained out of sample: 35%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+100.2 pp**, out of sample **-283.2 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1435 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-57.43%**; the strategy returned **42.79%**.
Out of sample: buy-and-hold **340.8%** vs strategy **57.64%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
