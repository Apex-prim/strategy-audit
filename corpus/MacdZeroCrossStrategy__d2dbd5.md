# MacdZeroCrossStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `MacdZeroCrossStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 14163 | 15746 |
| average profit per trade % | -0.19 | -0.17 |
| win rate % | 27.0 | 28.5 |
| average trade duration, minutes | 85.0 | 89.0 |
| duration measured in own candles | 17.0 | 17.8 |
| expectancy per trade (USDT) | -0.07 | -0.06 |
| mean profit p-value | 1.712e-62 | 5.9e-34 |
| market change % (baseline) | -58.3 | 346.34 |
| strategy total % | -96.57 | -96.6 |
| Sharpe | -52.22 | -12.36 |
| Sortino | -79.18 | -20.81 |
| max drawdown % | 96.58 | 96.75 |
| profit factor | 0.61 | 0.66 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.3 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.3%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.6%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: macd -112.524%, macd_prev 28.928%, macd_signal 17.388%, rsi -4.207% |
| прогрев занижен | **found** | объявлено 35, нужно не менее 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
