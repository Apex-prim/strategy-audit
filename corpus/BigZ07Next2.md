# BigZ07Next2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BigZ07Next2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 443 | 1273 |
| average profit per trade % | -0.26 | 0.28 |
| win rate % | 81.9 | 86.4 |
| average trade duration, minutes | 532.0 | 377.0 |
| duration measured in own candles | 106.4 | 75.4 |
| expectancy per trade (USDT) | -0.32 | 0.41 |
| mean profit p-value | 0.08808 | 0.006744 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | -14.27 | 52.61 |
| Sharpe | -0.94 | 0.78 |
| Sortino | -0.74 | 0.42 |
| max drawdown % | 23.33 | 16.68 |
| profit factor | 0.75 | 1.33 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+45.0 pp**, out of sample **-293.7 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.08808 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **-14.27%**.
Out of sample: buy-and-hold **346.34%** vs strategy **52.61%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
