# AdxStrengthStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `AdxStrengthStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 5560 | 11392 |
| average profit per trade % | -0.24 | -0.24 |
| win rate % | 26.8 | 27.4 |
| average trade duration, minutes | 73.0 | 78.0 |
| duration measured in own candles | 14.6 | 15.6 |
| expectancy per trade (USDT) | -0.15 | -0.08 |
| mean profit p-value | 1.13e-61 | 1.288e-64 |
| market change % (baseline) | -58.52 | 346.34 |
| strategy total % | -81.04 | -96.58 |
| Sharpe | -32.75 | -14.75 |
| Sortino | -55.07 | -22.31 |
| max drawdown % | 81.1 | 96.58 |
| profit factor | 0.52 | 0.56 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-22.5 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.52%**; the strategy returned **-81.04%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: plus_di 3.015%, minus_di 2.061%, rsi 2.684% |
| прогрев занижен | **found** | объявлено 25, нужно не менее 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
