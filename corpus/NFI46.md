# NFI46

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NFI46.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 21 | 56 |
| average profit per trade % | 1.51 | 2.53 |
| win rate % | 85.7 | 96.4 |
| average trade duration, minutes | 274.0 | 87.0 |
| duration measured in own candles | 54.8 | 17.4 |
| expectancy per trade (USDT) | 1.89 | 3.42 |
| mean profit p-value | 0.04489 | 9.85e-16 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 3.97 | 19.14 |
| Sharpe | 0.26 | 0.68 |
| Sortino | 0.39 | 1.21 |
| max drawdown % | 1.46 | 0.24 |
| profit factor | 3.37 | 64.01 |

**Retained out of sample: 181%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+63.2 pp**, out of sample **-327.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **3.97%**.
Out of sample: buy-and-hold **346.34%** vs strategy **19.14%** — loses to it.

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
