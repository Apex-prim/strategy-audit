# bbandrsi

Source: [`phuchust/freqtrade_strategy`](https://github.com/phuchust/freqtrade_strategy) · file `bbandrsi.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1528 | 5230 |
| average profit per trade % | -0.56 | -0.08 |
| win rate % | 57.9 | 62.1 |
| average trade duration, minutes | 2133.0 | 2230.0 |
| duration measured in own candles | 142.2 | 148.67 |
| expectancy per trade (USDT) | -0.46 | -0.13 |
| mean profit p-value | 8.472e-07 | 0.1679 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -70.41 | -67.81 |
| Sharpe | -5.05 | -0.81 |
| Sortino | -4.69 | -0.67 |
| max drawdown % | 72.22 | 84.9 |
| profit factor | 0.66 | 0.93 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-12.3 pp**, out of sample **-413.7 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-70.41%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-67.81%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
