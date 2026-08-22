# MSO

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `MSO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1752 | 9901 |
| average profit per trade % | -0.35 | -0.21 |
| win rate % | 61.3 | 67.4 |
| average trade duration, minutes | 431.0 | 601.0 |
| duration measured in own candles | 7.18 | 10.02 |
| expectancy per trade (USDT) | -0.31 | -0.09 |
| mean profit p-value | 1.264e-07 | 1.482e-08 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -54.71 | -93.33 |
| Sharpe | -5.81 | -4.56 |
| Sortino | -4.29 | -3.05 |
| max drawdown % | 54.96 | 93.68 |
| profit factor | 0.54 | 0.73 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+3.7 pp**, out of sample **-442.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-54.71%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-93.33%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 6, выходов 5 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
