# Divergences

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Divergences.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2487 | 7494 |
| average profit per trade % | -0.43 | -0.25 |
| win rate % | 31.4 | 35.4 |
| average trade duration, minutes | 243.0 | 278.0 |
| duration measured in own candles | 4.05 | 4.63 |
| expectancy per trade (USDT) | -0.3 | -0.12 |
| mean profit p-value | 3.953e-22 | 6.77e-12 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -74.05 | -91.23 |
| Sharpe | -12.76 | -4.81 |
| Sortino | -15.94 | -5.86 |
| max drawdown % | 74.62 | 91.37 |
| profit factor | 0.48 | 0.7 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-14.8 pp**, out of sample **-439.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-74.05%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-91.23%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: adx 125.955%, rsi 4.044% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
