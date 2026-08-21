# TrendFollowingStrategy

Source: [`freqtrade/freqtrade-strategies`](https://github.com/freqtrade/freqtrade-strategies) · file `TrendFollowingStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 660 | 2561 |
| expectancy per trade (USDT) | -0.97 | 0.16 |
| mean profit p-value | 0.006103 | 0.8363 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -63.76 | 41.9 |
| Sharpe | -1.85 | 0.08 |
| Sortino | -2.52 | 0.09 |
| max drawdown % | 71.17 | 75.49 |
| profit factor | 0.73 | 1.01 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-63.76%**.
Out of sample: buy-and-hold **346.34%** vs strategy **41.9%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
