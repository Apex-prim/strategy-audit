# wtc

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `wtc.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 321 | 1919 |
| average profit per trade % | -0.34 | -0.21 |
| win rate % | 58.9 | 59.5 |
| average trade duration, minutes | 6861.0 | 7027.0 |
| duration measured in own candles | 228.7 | 234.23 |
| expectancy per trade (USDT) | -0.53 | -0.31 |
| mean profit p-value | 0.3234 | 0.2223 |
| market change % (baseline) | -57.83 | 343.26 |
| strategy total % | -16.88 | -59.64 |
| Sharpe | -0.46 | -0.43 |
| Sortino | -0.74 | -0.58 |
| max drawdown % | 35.21 | 78.43 |
| profit factor | 0.87 | 0.93 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+41.0 pp**, out of sample **-402.9 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3234 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-57.83%**; the strategy returned **-16.88%**.
Out of sample: buy-and-hold **343.26%** vs strategy **-59.64%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 12, выходов 8 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **30m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
