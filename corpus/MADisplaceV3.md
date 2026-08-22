# MADisplaceV3

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `MADisplaceV3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 175 | 543 |
| average profit per trade % | 0.18 | 0.56 |
| win rate % | 58.9 | 69.8 |
| average trade duration, minutes | 69.0 | 49.0 |
| duration measured in own candles | 13.8 | 9.8 |
| expectancy per trade (USDT) | 0.22 | 0.83 |
| mean profit p-value | 0.3116 | 9.242e-05 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 3.86 | 45.27 |
| Sharpe | 0.35 | 0.74 |
| Sortino | 0.39 | 0.59 |
| max drawdown % | 8.13 | 7.65 |
| profit factor | 1.23 | 1.66 |

**Retained out of sample: 377%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+62.9 pp**, out of sample **-301.1 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3116 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **3.86%**.
Out of sample: buy-and-hold **346.34%** vs strategy **45.27%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
