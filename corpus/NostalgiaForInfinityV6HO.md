# NostalgiaForInfinityV6HO

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NostalgiaForInfinityV6HO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 181 | 531 |
| average profit per trade % | 0.24 | 1.18 |
| win rate % | 72.9 | 81.2 |
| average trade duration, minutes | 453.0 | 283.0 |
| duration measured in own candles | 90.6 | 56.6 |
| expectancy per trade (USDT) | 0.29 | 2.19 |
| mean profit p-value | 0.3562 | 2.538e-17 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 5.19 | 116.04 |
| Sharpe | 0.33 | 1.64 |
| Sortino | 0.3 | 1.5 |
| max drawdown % | 10.16 | 3.37 |
| profit factor | 1.25 | 3.05 |

**Retained out of sample: 755%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+64.4 pp**, out of sample **-230.3 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3562 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **5.19%**.
Out of sample: buy-and-hold **346.34%** vs strategy **116.04%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
