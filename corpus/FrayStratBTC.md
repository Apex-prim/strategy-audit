# FrayStratBTC

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FRAYSTRAT-BTCUSDT-1H.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2045 | 7044 |
| average profit per trade % | -0.64 | -0.27 |
| win rate % | 92.3 | 94.2 |
| average trade duration, minutes | 3063.0 | 2522.0 |
| duration measured in own candles | 204.2 | 168.13 |
| expectancy per trade (USDT) | -0.42 | -0.14 |
| mean profit p-value | 5.085e-07 | 0.009515 |
| market change % (baseline) | -58.34 | 345.85 |
| strategy total % | -86.89 | -96.67 |
| Sharpe | -5.97 | -1.76 |
| Sortino | -3.2 | -0.66 |
| max drawdown % | 87.99 | 97.49 |
| profit factor | 0.52 | 0.82 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-28.5 pp**, out of sample **-442.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.34%**; the strategy returned **-86.89%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.67%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: bb_middleband -0.028%, bb_upperband -0.056%, bb_percent 26.782%, bb_width -22.031% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
