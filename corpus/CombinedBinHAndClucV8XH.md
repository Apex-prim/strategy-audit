# CombinedBinHAndClucV8XH

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHAndClucV8XH.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 165 | 477 |
| average profit per trade % | 0.54 | 0.56 |
| win rate % | 80.0 | 77.8 |
| average trade duration, minutes | 156.0 | 169.0 |
| duration measured in own candles | 31.2 | 33.8 |
| expectancy per trade (USDT) | 0.7 | 0.81 |
| mean profit p-value | 0.004944 | 3.408e-09 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 11.48 | 38.78 |
| Sharpe | 0.96 | 1.07 |
| Sortino | 0.9 | 1.22 |
| max drawdown % | 3.75 | 4.32 |
| profit factor | 1.8 | 1.98 |

**Retained out of sample: 116%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+70.5 pp**, out of sample **-307.6 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **11.48%**.
Out of sample: buy-and-hold **346.34%** vs strategy **38.78%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
