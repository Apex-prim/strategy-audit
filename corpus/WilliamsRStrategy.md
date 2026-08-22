# WilliamsRStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `WilliamsRStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11547 | 15377 |
| average profit per trade % | -0.23 | -0.17 |
| win rate % | 44.8 | 51.6 |
| average trade duration, minutes | 85.0 | 76.0 |
| duration measured in own candles | 17.0 | 15.2 |
| expectancy per trade (USDT) | -0.08 | -0.06 |
| mean profit p-value | 2.324e-69 | 3.559e-53 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | -96.57 | -96.58 |
| Sharpe | -49.84 | -15.46 |
| Sortino | -43.27 | -13.52 |
| max drawdown % | 96.57 | 96.6 |
| profit factor | 0.43 | 0.57 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.2 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 12.447% |
| прогрев занижен | **found** | объявлено 20, нужно не менее 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
