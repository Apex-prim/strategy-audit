# Schism3

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Schism-v1.3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1800 | — |
| average profit per trade % | -0.45 | — |
| win rate % | 87.2 | — |
| average trade duration, minutes | 2901.0 | — |
| duration measured in own candles | 580.2 | — |
| expectancy per trade (USDT) | -0.41 | — |
| mean profit p-value | 0.0001751 | — |
| market change % (baseline) | -58.42 | — |
| strategy total % | -73.21 | — |
| Sharpe | -4.18 | — |
| Sortino | -1.77 | — |
| max drawdown % | 73.85 | — |
| profit factor | 0.54 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-14.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.42%**; the strategy returned **-73.21%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi_1h 0.367% |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
