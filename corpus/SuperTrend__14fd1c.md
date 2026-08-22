# SuperTrend

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `SuperTrend (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2353 | — |
| average profit per trade % | -0.3 | — |
| win rate % | 57.5 | — |
| average trade duration, minutes | 376.0 | — |
| duration measured in own candles | 376.0 | — |
| expectancy per trade (USDT) | -0.25 | — |
| mean profit p-value | 7.729e-18 | — |
| market change % (baseline) | -55.55 | — |
| strategy total % | -58.39 | — |
| Sharpe | -11.01 | — |
| Sortino | -35.8 | — |
| max drawdown % | 58.5 | — |
| profit factor | 0.68 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-2.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.55%**; the strategy returned **-58.39%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 2.525% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
