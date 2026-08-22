# Macd

Source: [`Foxel05/freqtrade-stuff`](https://github.com/Foxel05/freqtrade-stuff) · file `macd.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 243 | 825 |
| average profit per trade % | 1.56 | 2.68 |
| win rate % | 35.0 | 31.8 |
| average trade duration, minutes | 14088.0 | 14897.0 |
| duration measured in own candles | 234.8 | 248.28 |
| expectancy per trade (USDT) | 1.18 | 3.94 |
| mean profit p-value | 0.4275 | 0.3306 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | 28.71 | 325.35 |
| Sharpe | 0.32 | 0.23 |
| Sortino | 1.44 | 1.08 |
| max drawdown % | 46.34 | 52.5 |
| profit factor | 1.18 | 1.16 |

**Retained out of sample: 334%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+87.1 pp**, out of sample **-23.3 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.4275 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **28.71%**.
Out of sample: buy-and-hold **348.67%** vs strategy **325.35%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
