# LinearRegressionStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `LinearRegressionStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11184 | 13386 |
| average profit per trade % | -0.16 | -0.2 |
| win rate % | 27.8 | 29.0 |
| average trade duration, minutes | 57.0 | 58.0 |
| duration measured in own candles | 11.4 | 11.6 |
| expectancy per trade (USDT) | -0.08 | -0.07 |
| mean profit p-value | 3.738e-56 | 1.435e-56 |
| market change % (baseline) | -58.52 | 346.34 |
| strategy total % | -89.87 | -96.58 |
| Sharpe | -43.95 | -14.9 |
| Sortino | -69.26 | -22.6 |
| max drawdown % | 89.89 | 96.6 |
| profit factor | 0.61 | 0.61 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-31.4 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.52%**; the strategy returned **-89.87%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 2.684% |
| прогрев занижен | **found** | объявлено 25, нужно не менее 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
