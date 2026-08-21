# MacdZeroCrossStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `MacdZeroCrossStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 14163 | 15746 |
| expectancy per trade (USDT) | -0.07 | -0.06 |
| mean profit p-value | 1.712e-62 | 5.9e-34 |
| market change % (baseline) | -58.3 | 346.34 |
| strategy total % | -96.57 | -96.6 |
| Sharpe | -52.22 | -12.36 |
| Sortino | -79.18 | -20.81 |
| max drawdown % | 96.58 | 96.75 |
| profit factor | 0.61 | 0.66 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

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

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
