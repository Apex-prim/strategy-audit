# KeltnerChannelStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `KeltnerChannelStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6661 | 10059 |
| average profit per trade % | -0.23 | -0.27 |
| win rate % | 29.9 | 30.1 |
| average trade duration, minutes | 54.0 | 57.0 |
| duration measured in own candles | 10.8 | 11.4 |
| expectancy per trade (USDT) | -0.13 | -0.1 |
| mean profit p-value | 1.252e-43 | 3.119e-61 |
| market change % (baseline) | -58.52 | 346.34 |
| strategy total % | -85.52 | -96.57 |
| Sharpe | -29.8 | -13.49 |
| Sortino | -48.92 | -17.49 |
| max drawdown % | 85.52 | 96.57 |
| profit factor | 0.59 | 0.54 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-27.0 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.52%**; the strategy returned **-85.52%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: atr -1.081%, rsi 2.684% |
| прогрев объявлен | clean | 25 при потребности 20 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
