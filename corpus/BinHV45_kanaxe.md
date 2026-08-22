# BinHV45_kanaxe

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `BinHV45_kanaxe.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 238 | 1560 |
| average profit per trade % | -0.21 | -0.28 |
| win rate % | 77.3 | 76.2 |
| average trade duration, minutes | 154.0 | 75.0 |
| duration measured in own candles | 154.0 | 75.0 |
| expectancy per trade (USDT) | -0.26 | -0.28 |
| mean profit p-value | 0.2116 | 8.326e-06 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -6.21 | -43.27 |
| Sharpe | -0.51 | -1.43 |
| Sortino | -9.37 | -4.57 |
| max drawdown % | 9.97 | 48.25 |
| profit factor | 0.81 | 0.75 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+49.3 pp**, out of sample **-391.2 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.2116 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-6.21%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-43.27%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
