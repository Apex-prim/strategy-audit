# MSO

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `MSO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1752 | 9901 |
| expectancy per trade (USDT) | -0.31 | -0.09 |
| mean profit p-value | 1.264e-07 | 1.482e-08 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -54.71 | -93.33 |
| Sharpe | -5.81 | -4.56 |
| Sortino | -4.29 | -3.05 |
| max drawdown % | 54.96 | 93.68 |
| profit factor | 0.54 | 0.73 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-54.71%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-93.33%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 6, выходов 5 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
