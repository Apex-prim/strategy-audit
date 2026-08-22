# MomentumRegimeBasket

Source: [`nateemma/strategies`](https://github.com/nateemma/strategies) · file `MomentumRegimeBasket.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 52 | 293 |
| average profit per trade % | 4.88 | 5.06 |
| win rate % | 32.7 | 37.9 |
| average trade duration, minutes | 22071.0 | 19447.0 |
| duration measured in own candles | 15.33 | 13.5 |
| expectancy per trade (USDT) | 5.67 | 11.78 |
| mean profit p-value | 0.2192 | 0.008619 |
| market change % (baseline) | -47.82 | 352.61 |
| strategy total % | 29.47 | 345.26 |
| Sharpe | 0.27 | 0.37 |
| Sortino | 1.0 | 1.38 |
| max drawdown % | 8.9 | 13.08 |
| profit factor | 2.17 | 2.03 |

**Retained out of sample: 208%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+77.3 pp**, out of sample **-7.4 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.2192 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-47.82%**; the strategy returned **29.47%**.
Out of sample: buy-and-hold **352.61%** vs strategy **345.26%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
