# BinHV45_werkkrew

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `BinHV45_werkkrew.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 129 | 631 |
| average profit per trade % | 0.36 | 1.02 |
| win rate % | 79.1 | 77.5 |
| average trade duration, minutes | 661.0 | 214.0 |
| duration measured in own candles | 661.0 | 214.0 |
| expectancy per trade (USDT) | 0.43 | 1.75 |
| mean profit p-value | 0.3735 | 0.0009339 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | 5.58 | 110.45 |
| Sharpe | 0.27 | 0.68 |
| Sortino | 0.19 | 0.69 |
| max drawdown % | 6.16 | 18.91 |
| profit factor | 1.3 | 1.45 |

**Retained out of sample: 407%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+61.1 pp**, out of sample **-237.5 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3735 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **5.58%**.
Out of sample: buy-and-hold **347.94%** vs strategy **110.45%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
