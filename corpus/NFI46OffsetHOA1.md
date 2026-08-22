# NFI46OffsetHOA1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NFI46OffsetHOA1 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 187 | 850 |
| average profit per trade % | 0.63 | 1.05 |
| win rate % | 80.2 | 83.1 |
| average trade duration, minutes | 57.0 | 57.0 |
| duration measured in own candles | 11.4 | 11.4 |
| expectancy per trade (USDT) | 0.83 | 2.31 |
| mean profit p-value | 5.717e-05 | 1.939e-17 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 15.46 | 196.43 |
| Sharpe | 1.48 | 2.05 |
| Sortino | 1.21 | 1.73 |
| max drawdown % | 4.05 | 5.61 |
| profit factor | 2.17 | 2.78 |

**Retained out of sample: 278%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+74.7 pp**, out of sample **-149.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **15.46%**.
Out of sample: buy-and-hold **346.34%** vs strategy **196.43%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317%, kama_offset_buy 0.053% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
