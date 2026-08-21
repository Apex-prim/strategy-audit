# GKD_Baseline

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `GKD_Baseline.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 7411 | 10927 |
| expectancy per trade (USDT) | -0.12 | -0.09 |
| mean profit p-value | 5.884e-47 | 1.231e-43 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -92.64 | -96.58 |
| Sharpe | -32.61 | -11.76 |
| Sortino | -44.63 | -15.86 |
| max drawdown % | 92.65 | 96.61 |
| profit factor | 0.58 | 0.65 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-92.64%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-96.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
