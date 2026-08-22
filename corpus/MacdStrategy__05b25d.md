# MacdStrategy

Source: [`DutchCryptoDad/FreqtradeBotStrategyDevelopmentForBeginners`](https://github.com/DutchCryptoDad/FreqtradeBotStrategyDevelopmentForBeginners) · file `MacdStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 103 | 351 |
| average profit per trade % | 0.47 | 3.94 |
| win rate % | 29.1 | 35.0 |
| average trade duration, minutes | 23599.0 | 25013.0 |
| duration measured in own candles | 16.39 | 17.37 |
| expectancy per trade (USDT) | -0.58 | 6.75 |
| mean profit p-value | 0.78 | 0.1268 |
| market change % (baseline) | -51.38 | 352.61 |
| strategy total % | -5.99 | 237.07 |
| Sharpe | -0.08 | 0.23 |
| Sortino | -0.86 | 1.57 |
| max drawdown % | 36.33 | 39.15 |
| profit factor | 0.92 | 1.28 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+45.4 pp**, out of sample **-115.5 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.78 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-51.38%**; the strategy returned **-5.99%**.
Out of sample: buy-and-hold **352.61%** vs strategy **237.07%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
