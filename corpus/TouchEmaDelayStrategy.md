# TouchEmaDelayStrategy

Source: [`flaviosiotto/freqtrade-strategy`](https://github.com/flaviosiotto/freqtrade-strategy) · file `touchemadelay-strategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 474 | 1857 |
| expectancy per trade (USDT) | -0.85 | -0.32 |
| mean profit p-value | 4.91e-08 | 3.666e-08 |
| market change % (baseline) | -55.61 | 347.44 |
| strategy total % | -40.35 | -58.9 |
| Sharpe | -3.16 | -1.93 |
| Sortino | -2.3 | -1.35 |
| max drawdown % | 41.17 | 59.01 |
| profit factor | 0.28 | 0.51 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-55.61%**; the strategy returned **-40.35%**.
Out of sample: buy-and-hold **347.44%** vs strategy **-58.9%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **3m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
