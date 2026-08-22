# EmaRibbonStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `EmaRibbonStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 8479 | 14273 |
| average profit per trade % | -0.18 | -0.19 |
| win rate % | 24.5 | 25.7 |
| average trade duration, minutes | 64.0 | 67.0 |
| duration measured in own candles | 12.8 | 13.4 |
| expectancy per trade (USDT) | -0.1 | -0.07 |
| mean profit p-value | 1.154e-49 | 5.17e-44 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -84.52 | -96.57 |
| Sharpe | -35.94 | -13.49 |
| Sortino | -70.03 | -25.35 |
| max drawdown % | 84.55 | 96.66 |
| profit factor | 0.61 | 0.66 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-26.1 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-84.52%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -2.484% |
| прогрев занижен | **found** | объявлено 40, нужно не менее 55 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
