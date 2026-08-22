# Strategy001_custom_sell

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `Strategy001_custom_sell.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4190 | 13520 |
| average profit per trade % | -0.41 | -0.18 |
| win rate % | 90.3 | 92.3 |
| average trade duration, minutes | 925.0 | 908.0 |
| duration measured in own candles | 185.0 | 181.6 |
| expectancy per trade (USDT) | -0.21 | -0.07 |
| mean profit p-value | 3.567e-14 | 9.014e-06 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -89.9 | -96.76 |
| Sharpe | -12.86 | -4.18 |
| Sortino | -7.44 | -1.85 |
| max drawdown % | 89.99 | 97.14 |
| profit factor | 0.54 | 0.81 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-31.7 pp**, out of sample **-443.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-89.9%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.76%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
