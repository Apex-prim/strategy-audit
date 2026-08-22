# FrostAuraM115mStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FrostAuraM115mStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 7461 | 23390 |
| average profit per trade % | -0.22 | -0.1 |
| win rate % | 62.2 | 64.5 |
| average trade duration, minutes | 324.0 | 299.0 |
| duration measured in own candles | 21.6 | 19.93 |
| expectancy per trade (USDT) | -0.12 | -0.04 |
| mean profit p-value | 3.149e-17 | 0.001517 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -88.9 | -96.58 |
| Sharpe | -19.13 | -3.92 |
| Sortino | -14.45 | -2.71 |
| max drawdown % | 89.07 | 97.31 |
| profit factor | 0.64 | 0.88 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-30.4 pp**, out of sample **-442.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-88.9%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.375% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
