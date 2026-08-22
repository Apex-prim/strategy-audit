# NFI46FrogZ

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NFI46FrogZ.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3303 | 12970 |
| average profit per trade % | -0.24 | -0.14 |
| win rate % | 79.2 | 79.0 |
| average trade duration, minutes | 220.0 | 185.0 |
| duration measured in own candles | 44.0 | 37.0 |
| expectancy per trade (USDT) | -0.19 | -0.07 |
| mean profit p-value | 7.469e-11 | 9.791e-07 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | -63.26 | -90.89 |
| Sharpe | -9.84 | -4.51 |
| Sortino | -5.55 | -2.24 |
| max drawdown % | 65.54 | 91.06 |
| profit factor | 0.53 | 0.68 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-4.0 pp**, out of sample **-437.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **-63.26%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-90.89%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
