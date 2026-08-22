# BBRSIStrategy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BBRSIStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2666 | 9664 |
| average profit per trade % | -0.36 | -0.1 |
| win rate % | 67.0 | 69.3 |
| average trade duration, minutes | 2142.0 | 2173.0 |
| duration measured in own candles | 142.8 | 144.87 |
| expectancy per trade (USDT) | -0.3 | -0.09 |
| mean profit p-value | 5.774e-05 | 0.1291 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -79.88 | -88.59 |
| Sharpe | -5.44 | -1.21 |
| Sortino | -3.22 | -0.69 |
| max drawdown % | 80.04 | 95.29 |
| profit factor | 0.41 | 0.84 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-21.3 pp**, out of sample **-434.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-79.88%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-88.59%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.375% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
