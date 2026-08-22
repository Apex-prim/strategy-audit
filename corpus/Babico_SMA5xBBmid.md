# Babico_SMA5xBBmid

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `Babico_SMA5xBBmid.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 15 | 64 |
| average profit per trade % | -16.74 | 33.16 |
| win rate % | 53.3 | 89.1 |
| average trade duration, minutes | 386496.0 | 350168.0 |
| duration measured in own candles | 268.4 | 243.17 |
| expectancy per trade (USDT) | -23.23 | 67.47 |
| mean profit p-value | 0.1316 | 0.2134 |
| market change % (baseline) | -59.68 | 352.61 |
| strategy total % | -34.85 | 431.84 |
| Sharpe | -0.17 | 0.08 |
| Sortino | -0.35 | 0.23 |
| max drawdown % | 45.22 | 52.46 |
| profit factor | 0.35 | 1.74 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+24.8 pp**, out of sample **+79.2 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1316 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.68%**; the strategy returned **-34.85%**.
Out of sample: buy-and-hold **352.61%** vs strategy **431.84%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
