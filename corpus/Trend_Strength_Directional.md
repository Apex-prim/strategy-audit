# Trend_Strength_Directional

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `Trend_Strength_Directional.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1624 | 6060 |
| expectancy per trade (USDT) | -0.42 | -0.02 |
| mean profit p-value | 0.003714 | 0.9564 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -68.44 | -9.26 |
| Sharpe | -3.06 | -0.03 |
| Sortino | -1.89 | -0.02 |
| max drawdown % | 72.4 | 84.78 |
| profit factor | 0.66 | 1.0 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-68.44%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-9.26%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
