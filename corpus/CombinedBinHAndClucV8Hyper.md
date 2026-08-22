# CombinedBinHAndClucV8Hyper

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHAndClucV8Hyper.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 287 | 956 |
| average profit per trade % | 0.51 | 0.42 |
| win rate % | 78.7 | 77.7 |
| average trade duration, minutes | 107.0 | 121.0 |
| duration measured in own candles | 21.4 | 24.2 |
| expectancy per trade (USDT) | 0.68 | 0.66 |
| mean profit p-value | 6.253e-06 | 1.149e-09 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 19.59 | 62.89 |
| Sharpe | 2.04 | 1.54 |
| Sortino | 1.41 | 1.15 |
| max drawdown % | 5.55 | 6.36 |
| profit factor | 2.45 | 1.87 |

**Retained out of sample: 97%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+78.6 pp**, out of sample **-283.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **19.59%**.
Out of sample: buy-and-hold **346.34%** vs strategy **62.89%** — loses to it.

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
