# TheForce

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `TheForce.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11971 | 12117 |
| average profit per trade % | -0.23 | -0.22 |
| win rate % | 32.7 | 29.8 |
| average trade duration, minutes | 44.0 | 42.0 |
| duration measured in own candles | 2.93 | 2.8 |
| expectancy per trade (USDT) | -0.08 | -0.08 |
| mean profit p-value | 3.222e-116 | 3.398e-112 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -96.57 | -96.57 |
| Sharpe | -66.35 | -20.25 |
| Sortino | -78.84 | -24.04 |
| max drawdown % | 96.58 | 96.58 |
| profit factor | 0.51 | 0.5 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.0 pp**, out of sample **-442.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: fastd_rsi 8.725%, macd -45000.555%, macdsignal -45000.555% |
| прогрев не объявлен | **found** | самый длинный индикатор 5 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
