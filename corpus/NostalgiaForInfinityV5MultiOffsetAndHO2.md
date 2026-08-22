# NostalgiaForInfinityV5MultiOffsetAndHO2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NostalgiaForInfinityV5MultiOffsetAndHO2 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 297 | 1084 |
| average profit per trade % | 0.16 | 0.47 |
| win rate % | 68.4 | 72.1 |
| average trade duration, minutes | 204.0 | 198.0 |
| duration measured in own candles | 40.8 | 39.6 |
| expectancy per trade (USDT) | 0.2 | 0.79 |
| mean profit p-value | 0.1424 | 7.511e-08 |
| market change % (baseline) | -59.35 | 346.34 |
| strategy total % | 5.82 | 85.17 |
| Sharpe | 0.67 | 1.44 |
| Sortino | 0.62 | 1.36 |
| max drawdown % | 6.1 | 7.35 |
| profit factor | 1.28 | 1.76 |

**Retained out of sample: 395%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+65.2 pp**, out of sample **-261.2 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1424 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.35%**; the strategy returned **5.82%**.
Out of sample: buy-and-hold **346.34%** vs strategy **85.17%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317%, kama_offset_buy 0.047% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
