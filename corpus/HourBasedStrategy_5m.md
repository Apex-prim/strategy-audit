# HourBasedStrategy_5m

Source: [`eovie/freqtrade_strs`](https://github.com/eovie/freqtrade_strs) · file `HourBasedStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2473 | 9311 |
| expectancy per trade (USDT) | -0.33 | -0.08 |
| mean profit p-value | 2.157e-06 | 0.5246 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -81.88 | -75.05 |
| Sharpe | -6.17 | -0.5 |
| Sortino | -6.51 | -0.54 |
| max drawdown % | 86.62 | 93.12 |
| profit factor | 0.73 | 0.98 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-81.88%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-75.05%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
