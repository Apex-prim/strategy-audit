# FRAYSTRAT

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FRAYSTRAT (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 5668 | 6778 |
| average profit per trade % | -0.45 | -0.37 |
| win rate % | 53.5 | 57.7 |
| average trade duration, minutes | 778.0 | 591.0 |
| duration measured in own candles | 51.87 | 39.4 |
| expectancy per trade (USDT) | -0.17 | -0.14 |
| mean profit p-value | 5.687e-17 | 1.18e-11 |
| market change % (baseline) | -58.34 | 345.85 |
| strategy total % | -96.7 | -96.64 |
| Sharpe | -16.55 | -4.52 |
| Sortino | -13.4 | -3.84 |
| max drawdown % | 96.73 | 96.7 |
| profit factor | 0.59 | 0.73 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.4 pp**, out of sample **-442.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.34%**; the strategy returned **-96.7%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.64%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 3.688% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
