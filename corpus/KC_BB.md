# KC_BB

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `KC_BB.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 178 | 517 |
| average profit per trade % | 0.13 | 0.2 |
| win rate % | 62.9 | 68.9 |
| average trade duration, minutes | 348.0 | 307.0 |
| duration measured in own candles | 69.6 | 61.4 |
| expectancy per trade (USDT) | 0.16 | 0.25 |
| mean profit p-value | 0.6211 | 0.2354 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | 2.79 | 12.73 |
| Sharpe | 0.17 | 0.22 |
| Sortino | 0.17 | 0.2 |
| max drawdown % | 5.45 | 6.06 |
| profit factor | 1.11 | 1.16 |

**Retained out of sample: 156%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+61.0 pp**, out of sample **-333.6 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.6211 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **2.79%**.
Out of sample: buy-and-hold **346.34%** vs strategy **12.73%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 28 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
