# OmaGann

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `OmaGann (2).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2208 | 8827 |
| average profit per trade % | -0.13 | -0.12 |
| win rate % | 27.4 | 28.7 |
| average trade duration, minutes | 1261.0 | 1208.0 |
| duration measured in own candles | 21.02 | 20.13 |
| expectancy per trade (USDT) | -0.16 | -0.09 |
| mean profit p-value | 0.02567 | 0.01089 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -35.27 | -80.96 |
| Sharpe | -2.74 | -1.93 |
| Sortino | -7.18 | -4.05 |
| max drawdown % | 51.71 | 85.59 |
| profit factor | 0.87 | 0.92 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+23.1 pp**, out of sample **-429.6 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-35.27%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-80.96%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
