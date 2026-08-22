# RiskParityPortfolio

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `risk_parity.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6 | 17 |
| average profit per trade % | -37.07 | 73.4 |
| win rate % | 33.3 | 64.7 |
| average trade duration, minutes | 904560.0 | 1358936.0 |
| duration measured in own candles | 628.17 | 943.71 |
| expectancy per trade (USDT) | -68.6 | 413.04 |
| mean profit p-value | 0.06361 | 0.2285 |
| market change % (baseline) | -55.75 | 352.61 |
| strategy total % | -41.16 | 702.17 |
| Sharpe | -0.18 | 0.04 |
| Sortino | -0.43 | 0.07 |
| max drawdown % | 42.73 | 39.46 |
| profit factor | 0.08 | 2.17 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+14.6 pp**, out of sample **+349.6 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.06361 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.75%**; the strategy returned **-41.16%**.
Out of sample: buy-and-hold **352.61%** vs strategy **702.17%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
