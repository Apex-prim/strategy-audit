# SMA_BBRSI

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `SMA_BBRSI.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 102 | 604 |
| average profit per trade % | 0.1 | 0.11 |
| win rate % | 77.5 | 74.5 |
| average trade duration, minutes | 66.0 | 60.0 |
| duration measured in own candles | 13.2 | 12.0 |
| expectancy per trade (USDT) | 0.12 | 0.14 |
| mean profit p-value | 0.6714 | 0.3287 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 1.21 | 8.18 |
| Sharpe | 0.11 | 0.19 |
| Sortino | 0.08 | 0.16 |
| max drawdown % | 2.9 | 6.57 |
| profit factor | 1.16 | 1.13 |

**Retained out of sample: 117%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+60.3 pp**, out of sample **-338.2 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.6714 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **1.21%**.
Out of sample: buy-and-hold **346.34%** vs strategy **8.18%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: basis_65 0.249%, EWO -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
