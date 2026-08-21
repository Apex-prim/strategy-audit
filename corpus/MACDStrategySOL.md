# MACDStrategySOL

Source: [`MelvynClark/Freqtrade-Strategy`](https://github.com/MelvynClark/Freqtrade-Strategy) · file `MACDStrategy - SOL.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1677 | 5779 |
| expectancy per trade (USDT) | -0.42 | -0.12 |
| mean profit p-value | 0.000823 | 0.2858 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -70.45 | -67.49 |
| Sharpe | -3.59 | -0.66 |
| Sortino | -2.0 | -0.32 |
| max drawdown % | 72.37 | 84.48 |
| profit factor | 0.6 | 0.92 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-70.45%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-67.49%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
