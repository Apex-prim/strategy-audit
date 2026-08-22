# BigZ03

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BigZ03.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 225 | 700 |
| average profit per trade % | -0.3 | 0.96 |
| win rate % | 95.1 | 95.6 |
| average trade duration, minutes | 8375.0 | 5204.0 |
| duration measured in own candles | 1675.0 | 1040.8 |
| expectancy per trade (USDT) | -0.42 | 1.84 |
| mean profit p-value | 0.5465 | 4.438e-06 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | -9.43 | 128.97 |
| Sharpe | -0.24 | 0.99 |
| Sortino | -0.09 | 0.26 |
| max drawdown % | 25.43 | 10.19 |
| profit factor | 0.77 | 2.63 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+49.6 pp**, out of sample **-217.4 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.5465 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **-9.43%**.
Out of sample: buy-and-hold **346.34%** vs strategy **128.97%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
