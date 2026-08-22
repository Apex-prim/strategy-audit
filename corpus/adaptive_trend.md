# adaptive_trend

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `adaptive_trend.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 65 | 257 |
| average profit per trade % | 0.45 | 11.06 |
| win rate % | 38.5 | 52.1 |
| average trade duration, minutes | 84768.0 | 85677.0 |
| duration measured in own candles | 353.2 | 356.99 |
| expectancy per trade (USDT) | -2.72 | 23.62 |
| mean profit p-value | 0.4783 | 0.2202 |
| market change % (baseline) | -44.46 | 340.8 |
| strategy total % | -17.7 | 607.08 |
| Sharpe | -0.16 | 0.16 |
| Sortino | -0.33 | 0.34 |
| max drawdown % | 44.98 | 41.51 |
| profit factor | 0.81 | 1.31 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+26.8 pp**, out of sample **+266.3 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.4783 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-44.46%**; the strategy returned **-17.7%**.
Out of sample: buy-and-hold **340.8%** vs strategy **607.08%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
