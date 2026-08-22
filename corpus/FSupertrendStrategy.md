# FSupertrendStrategy

Source: [`freqtrade/freqtrade-strategies`](https://github.com/freqtrade/freqtrade-strategies) · file `FSupertrendStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1760 | 6492 |
| average profit per trade % | -0.06 | 0.01 |
| win rate % | 61.8 | 59.2 |
| average trade duration, minutes | 1009.0 | 987.0 |
| duration measured in own candles | 16.82 | 16.45 |
| expectancy per trade (USDT) | -0.1 | -0.02 |
| mean profit p-value | 0.3202 | 0.763 |
| market change % (baseline) | -59.19 | 348.67 |
| strategy total % | -17.89 | -14.49 |
| Sharpe | -1.09 | -0.2 |
| Sortino | -1.51 | -0.24 |
| max drawdown % | 39.75 | 62.76 |
| profit factor | 0.95 | 0.99 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+41.3 pp**, out of sample **-363.2 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3202 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.19%**; the strategy returned **-17.89%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-14.49%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
