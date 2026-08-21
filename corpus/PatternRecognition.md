# PatternRecognition

Source: [`freqtrade/freqtrade-strategies`](https://github.com/freqtrade/freqtrade-strategies) · file `PatternRecognition.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 134 | 520 |
| expectancy per trade (USDT) | -3.56 | -0.48 |
| mean profit p-value | 0.007559 | 0.6741 |
| market change % (baseline) | -59.68 | 352.61 |
| strategy total % | -47.69 | -24.98 |
| Sharpe | -0.82 | -0.08 |
| Sortino | -1.26 | -0.08 |
| max drawdown % | 53.11 | 67.94 |
| profit factor | 0.53 | 0.95 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.68%**; the strategy returned **-47.69%**.
Out of sample: buy-and-hold **352.61%** vs strategy **-24.98%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
