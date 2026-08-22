# PpoMomentumStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `PpoMomentumStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 7012 | 13525 |
| average profit per trade % | -0.18 | -0.2 |
| win rate % | 30.3 | 31.5 |
| average trade duration, minutes | 91.0 | 95.0 |
| duration measured in own candles | 18.2 | 19.0 |
| expectancy per trade (USDT) | -0.11 | -0.07 |
| mean profit p-value | 1.25e-36 | 1.71e-33 |
| market change % (baseline) | -58.3 | 346.34 |
| strategy total % | -79.91 | -96.57 |
| Sharpe | -27.87 | -11.38 |
| Sortino | -43.01 | -17.02 |
| max drawdown % | 79.97 | 96.61 |
| profit factor | 0.63 | 0.69 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-21.6 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.3%**; the strategy returned **-79.91%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -4.207% |
| прогрев занижен | **found** | объявлено 35, нужно не менее 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
