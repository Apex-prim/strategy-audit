# AwesomeMacd

Source: [`MelvynClark/Freqtrade-Strategy`](https://github.com/MelvynClark/Freqtrade-Strategy) · file `AwesomeMacd.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 831 | 3158 |
| average profit per trade % | -0.13 | -0.08 |
| win rate % | 31.4 | 29.8 |
| average trade duration, minutes | 3166.0 | 3047.0 |
| duration measured in own candles | 52.77 | 50.78 |
| expectancy per trade (USDT) | -0.23 | -0.14 |
| mean profit p-value | 0.3116 | 0.3865 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -18.78 | -42.77 |
| Sharpe | -0.76 | -0.39 |
| Sortino | -1.23 | -0.64 |
| max drawdown % | 32.41 | 73.65 |
| profit factor | 0.91 | 0.96 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+39.6 pp**, out of sample **-391.4 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3116 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-18.78%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-42.77%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
