# PRICEFOLLOWINGX

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `PRICEFOLLOWINGX (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 273 | 899 |
| average profit per trade % | -1.91 | 0.23 |
| win rate % | 93.0 | 97.4 |
| average trade duration, minutes | 10320.0 | 10308.0 |
| duration measured in own candles | 688.0 | 687.2 |
| expectancy per trade (USDT) | -2.03 | 0.14 |
| mean profit p-value | 0.008674 | 0.7712 |
| market change % (baseline) | -58.34 | 345.85 |
| strategy total % | -55.47 | 12.75 |
| Sharpe | -1.15 | 0.07 |
| Sortino | -1.04 | 0.04 |
| max drawdown % | 56.05 | 42.19 |
| profit factor | 0.37 | 1.06 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+2.9 pp**, out of sample **-333.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.34%**; the strategy returned **-55.47%**.
Out of sample: buy-and-hold **345.85%** vs strategy **12.75%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 3.688%, frsi -34.863% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
