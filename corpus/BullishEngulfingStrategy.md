# BullishEngulfingStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `BullishEngulfingStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 9979 | 14248 |
| average profit per trade % | -0.2 | -0.19 |
| win rate % | 26.4 | 28.1 |
| average trade duration, minutes | 59.0 | 50.0 |
| duration measured in own candles | 11.8 | 10.0 |
| expectancy per trade (USDT) | -0.09 | -0.07 |
| mean profit p-value | 6.047e-71 | 3.896e-85 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | -91.35 | -96.57 |
| Sharpe | -46.93 | -19.01 |
| Sortino | -59.48 | -23.96 |
| max drawdown % | 91.36 | 96.57 |
| profit factor | 0.5 | 0.51 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-32.9 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-91.35%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 12.447% |
| прогрев занижен | **found** | объявлено 20, нужно не менее 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
