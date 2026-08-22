# NostalgiaForInfinityX2

Source: [`ShahAnuj2610/my-freqtrade-nfi-nextgen`](https://github.com/ShahAnuj2610/my-freqtrade-nfi-nextgen) · file `NostalgiaForInfinityX2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2 | — |
| average profit per trade % | 0.77 | — |
| win rate % | 100.0 | — |
| average trade duration, minutes | 675.0 | — |
| duration measured in own candles | 135.0 | — |
| expectancy per trade (USDT) | 1.13 | — |
| mean profit p-value | 0.3229 | — |
| market change % (baseline) | -59.75 | — |
| strategy total % | 0.23 | — |
| Sharpe | 0.09 | — |
| Sortino | -100.0 | — |
| max drawdown % | 0.0 | — |
| profit factor | 0.0 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+60.0 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3229 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.75%**; the strategy returned **0.23%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ema_100_4h -0.020% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |
| признак утечки будущего | **found** | центрированное окно center=True |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
