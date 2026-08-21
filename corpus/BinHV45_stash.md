# BinHV45_stash

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `BinHV45_stash.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 224 | 1476 |
| expectancy per trade (USDT) | -0.13 | -0.26 |
| mean profit p-value | 0.5406 | 9.986e-05 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -2.9 | -38.15 |
| Sharpe | -0.24 | -1.21 |
| Sortino | -6.37 | -4.73 |
| max drawdown % | 7.71 | 42.79 |
| profit factor | 0.9 | 0.77 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.5406 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-2.9%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-38.15%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
