# StochasticCciStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `StochasticCciStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 243 | 1082 |
| average profit per trade % | -0.36 | -0.03 |
| win rate % | 56.0 | 56.7 |
| average trade duration, minutes | 1674.0 | 1428.0 |
| duration measured in own candles | 27.9 | 23.8 |
| expectancy per trade (USDT) | -0.45 | -0.06 |
| mean profit p-value | 0.2302 | 0.7332 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -10.97 | -6.37 |
| Sharpe | -0.49 | -0.09 |
| Sortino | -0.51 | -0.09 |
| max drawdown % | 18.01 | 28.03 |
| profit factor | 0.78 | 0.97 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+48.3 pp**, out of sample **-355.0 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.2302 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-10.97%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-6.37%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
