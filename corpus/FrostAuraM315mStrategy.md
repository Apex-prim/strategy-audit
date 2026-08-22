# FrostAuraM315mStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FrostAuraM315mStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1892 | 7229 |
| average profit per trade % | -0.52 | -0.11 |
| win rate % | 62.8 | 66.8 |
| average trade duration, minutes | 1388.0 | 1329.0 |
| duration measured in own candles | 92.53 | 88.6 |
| expectancy per trade (USDT) | -0.39 | -0.1 |
| mean profit p-value | 3.135e-09 | 0.05951 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -73.32 | -74.57 |
| Sharpe | -6.78 | -1.3 |
| Sortino | -4.64 | -0.85 |
| max drawdown % | 75.15 | 84.29 |
| profit factor | 0.45 | 0.88 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-14.8 pp**, out of sample **-420.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-73.32%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-74.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.375% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
