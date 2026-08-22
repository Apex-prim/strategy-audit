# TrixSignalStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `TrixSignalStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 5071 | 12814 |
| average profit per trade % | -0.2 | -0.21 |
| win rate % | 32.2 | 32.9 |
| average trade duration, minutes | 134.0 | 140.0 |
| duration measured in own candles | 26.8 | 28.0 |
| expectancy per trade (USDT) | -0.14 | -0.08 |
| mean profit p-value | 1.095e-24 | 4.91e-24 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -71.12 | -96.57 |
| Sharpe | -19.22 | -9.28 |
| Sortino | -32.65 | -13.86 |
| max drawdown % | 71.32 | 96.73 |
| profit factor | 0.67 | 0.72 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-12.8 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-71.12%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -2.484% |
| прогрев занижен | **found** | объявлено 40, нужно не менее 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
