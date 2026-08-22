# CombinedBinHAndClucHyperV0

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `CombinedBinHAndClucHyperV0.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 733 | 3519 |
| average profit per trade % | -0.12 | -0.12 |
| win rate % | 58.3 | 55.7 |
| average trade duration, minutes | 26.0 | 13.0 |
| duration measured in own candles | 26.0 | 13.0 |
| expectancy per trade (USDT) | -0.15 | -0.13 |
| mean profit p-value | 0.119 | 0.004788 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -10.67 | -45.37 |
| Sharpe | -1.11 | -1.35 |
| Sortino | -0.93 | -1.1 |
| max drawdown % | 16.07 | 55.3 |
| profit factor | 0.82 | 0.83 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+44.9 pp**, out of sample **-393.3 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.119 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-10.67%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-45.37%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
