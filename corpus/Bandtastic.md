# Bandtastic

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `Bandtastic.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 7384 | 21361 |
| average profit per trade % | -0.26 | -0.1 |
| win rate % | 59.0 | 61.7 |
| average trade duration, minutes | 555.0 | 525.0 |
| duration measured in own candles | 37.0 | 35.0 |
| expectancy per trade (USDT) | -0.12 | -0.05 |
| mean profit p-value | 5.092e-14 | 0.0254 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -92.14 | -96.81 |
| Sharpe | -16.94 | -2.64 |
| Sortino | -13.44 | -1.95 |
| max drawdown % | 92.22 | 98.17 |
| profit factor | 0.67 | 0.92 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-34.0 pp**, out of sample **-442.7 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-92.14%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.81%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
