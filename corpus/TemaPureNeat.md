# TemaPureNeat

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `TemaPureNeat.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2806 | 9596 |
| average profit per trade % | -0.18 | -0.15 |
| win rate % | 41.6 | 46.2 |
| average trade duration, minutes | 1372.0 | 1544.0 |
| duration measured in own candles | 274.4 | 308.8 |
| expectancy per trade (USDT) | -0.19 | -0.09 |
| mean profit p-value | 0.02368 | 0.07608 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -52.36 | -90.19 |
| Sharpe | -3.13 | -1.41 |
| Sortino | -5.58 | -1.72 |
| max drawdown % | 59.15 | 95.45 |
| profit factor | 0.9 | 0.94 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+5.9 pp**, out of sample **-436.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-52.36%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-90.19%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 25 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
