# FrayLIVEBTC15m

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FrayLIVEBTC15m.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1015 | 3732 |
| average profit per trade % | -0.82 | -0.29 |
| win rate % | 92.2 | 94.0 |
| average trade duration, minutes | 4478.0 | 5089.0 |
| duration measured in own candles | 298.53 | 339.27 |
| expectancy per trade (USDT) | -0.72 | -0.24 |
| mean profit p-value | 0.0002412 | 0.04952 |
| market change % (baseline) | -58.84 | 345.85 |
| strategy total % | -73.09 | -88.51 |
| Sharpe | -3.07 | -0.97 |
| Sortino | -1.56 | -0.36 |
| max drawdown % | 73.26 | 93.31 |
| profit factor | 0.5 | 0.82 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-14.2 pp**, out of sample **-434.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.84%**; the strategy returned **-73.09%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-88.51%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 1 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -1.584%, frsi 13.618%, macd 25828.480%, macdsignal -308.147%, macdn 16.676% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
