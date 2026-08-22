# StochasticOversoldStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `StochasticOversoldStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 8474 | 15236 |
| average profit per trade % | -0.21 | -0.18 |
| win rate % | 48.4 | 52.2 |
| average trade duration, minutes | 117.0 | 110.0 |
| duration measured in own candles | 23.4 | 22.0 |
| expectancy per trade (USDT) | -0.11 | -0.06 |
| mean profit p-value | 1.953e-42 | 4.817e-36 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | -89.05 | -96.59 |
| Sharpe | -33.08 | -12.55 |
| Sortino | -29.75 | -11.28 |
| max drawdown % | 89.11 | 96.69 |
| profit factor | 0.53 | 0.65 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-30.6 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-89.05%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.59%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 12.447% |
| прогрев занижен | **found** | объявлено 20, нужно не менее 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
