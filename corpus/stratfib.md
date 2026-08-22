# stratfib

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `stratfib.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6 | 4 |
| average profit per trade % | 1.0 | 1.17 |
| win rate % | 100.0 | 100.0 |
| average trade duration, minutes | 2480.0 | 1065.0 |
| duration measured in own candles | 41.33 | 17.75 |
| expectancy per trade (USDT) | 1.24 | 1.45 |
| mean profit p-value | 1.379e-13 | 0.006218 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | 0.74 | 0.58 |
| Sharpe | 47.3 | 0.13 |
| Sortino | -100.0 | -100.0 |
| max drawdown % | 0.0 | 0.0 |
| profit factor | 0.0 | 0.0 |

**Retained out of sample: 117%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+60.0 pp**, out of sample **-348.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **0.74%**.
Out of sample: buy-and-hold **348.67%** vs strategy **0.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 4.044% |
| прогрев не объявлен | **found** | самый длинный индикатор 89 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
