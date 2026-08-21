# GKD_PFE

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `GKD_PFE.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6530 | 10583 |
| expectancy per trade (USDT) | -0.14 | -0.09 |
| mean profit p-value | 2.587e-24 | 1.447e-16 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -88.76 | -96.59 |
| Sharpe | -21.58 | -6.88 |
| Sortino | -22.88 | -6.88 |
| max drawdown % | 88.78 | 96.69 |
| profit factor | 0.67 | 0.77 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-88.76%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-96.59%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
