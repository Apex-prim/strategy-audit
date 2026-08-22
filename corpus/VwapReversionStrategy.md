# VwapReversionStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `VwapReversionStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 8047 | 14269 |
| average profit per trade % | -0.3 | -0.18 |
| win rate % | 60.8 | 63.9 |
| average trade duration, minutes | 534.0 | 500.0 |
| duration measured in own candles | 106.8 | 100.0 |
| expectancy per trade (USDT) | -0.12 | -0.07 |
| mean profit p-value | 5.262e-22 | 2.884e-09 |
| market change % (baseline) | -58.52 | 346.34 |
| strategy total % | -95.37 | -96.61 |
| Sharpe | -22.71 | -5.74 |
| Sortino | -21.13 | -5.93 |
| max drawdown % | 95.4 | 96.71 |
| profit factor | 0.69 | 0.86 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-36.9 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.52%**; the strategy returned **-95.37%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.61%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 2.684%, atr -1.081% |
| прогрев занижен | **found** | объявлено 25, нужно не менее 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
