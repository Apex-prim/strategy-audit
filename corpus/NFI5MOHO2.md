# NFI5MOHO2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NFI5MOHO2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 283 | 1153 |
| average profit per trade % | 0.14 | 0.75 |
| win rate % | 71.7 | 77.9 |
| average trade duration, minutes | 175.0 | 153.0 |
| duration measured in own candles | 35.0 | 30.6 |
| expectancy per trade (USDT) | 0.17 | 1.61 |
| mean profit p-value | 0.2467 | 9.425e-18 |
| market change % (baseline) | -59.35 | 346.34 |
| strategy total % | 4.88 | 185.86 |
| Sharpe | 0.51 | 2.4 |
| Sortino | 0.44 | 2.73 |
| max drawdown % | 3.81 | 4.69 |
| profit factor | 1.22 | 2.49 |

**Retained out of sample: 947%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+64.2 pp**, out of sample **-160.5 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.2467 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.35%**; the strategy returned **4.88%**.
Out of sample: buy-and-hold **346.34%** vs strategy **185.86%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo 12.108%, kama_offset_buy 0.014% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
