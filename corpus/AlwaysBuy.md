# AlwaysBuy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `AlwaysBuy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11069 | 21290 |
| average profit per trade % | -0.23 | -0.1 |
| win rate % | 41.0 | 45.6 |
| average trade duration, minutes | 300.0 | 300.0 |
| duration measured in own candles | 60.0 | 60.0 |
| expectancy per trade (USDT) | -0.09 | -0.05 |
| mean profit p-value | 2.111e-18 | 4.148e-11 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -96.63 | -96.88 |
| Sharpe | -24.11 | -7.79 |
| Sortino | -27.59 | -8.5 |
| max drawdown % | 96.74 | 96.96 |
| profit factor | 0.7 | 0.84 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.4 pp**, out of sample **-443.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-96.63%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.88%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.005 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
