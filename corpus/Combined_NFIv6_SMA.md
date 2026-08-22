# Combined_NFIv6_SMA

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Combined_NFIv6_SMA.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 239 | 712 |
| average profit per trade % | 0.61 | 1.21 |
| win rate % | 79.1 | 84.8 |
| average trade duration, minutes | 328.0 | 205.0 |
| duration measured in own candles | 65.6 | 41.0 |
| expectancy per trade (USDT) | 0.82 | 2.63 |
| mean profit p-value | 0.0002381 | 6.907e-28 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 19.51 | 187.48 |
| Sharpe | 1.52 | 2.47 |
| Sortino | 1.25 | 1.79 |
| max drawdown % | 9.77 | 2.13 |
| profit factor | 1.97 | 3.35 |

**Retained out of sample: 321%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+78.7 pp**, out of sample **-158.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **19.51%**.
Out of sample: buy-and-hold **346.34%** vs strategy **187.48%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
