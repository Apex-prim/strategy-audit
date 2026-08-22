# PolymarketPortfolio

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `polymarket_portfolio.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 47 | 358 |
| average profit per trade % | 0.46 | 0.89 |
| win rate % | 68.1 | 75.1 |
| average trade duration, minutes | 3140.0 | 2615.0 |
| duration measured in own candles | 13.08 | 10.9 |
| expectancy per trade (USDT) | -0.13 | 0.29 |
| mean profit p-value | 0.5922 | 0.1358 |
| market change % (baseline) | -57.43 | 340.8 |
| strategy total % | -0.59 | 10.27 |
| Sharpe | -0.1 | 0.23 |
| Sortino | -0.08 | 0.16 |
| max drawdown % | 1.36 | 3.0 |
| profit factor | 0.74 | 1.5 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+56.8 pp**, out of sample **-330.5 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.5922 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-57.43%**; the strategy returned **-0.59%**.
Out of sample: buy-and-hold **340.8%** vs strategy **10.27%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
