# SimpleHopt

Source: [`MelvynClark/Freqtrade-Strategy`](https://github.com/MelvynClark/Freqtrade-Strategy) · file `SimpleHopt.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4701 | 11974 |
| expectancy per trade (USDT) | -0.2 | -0.08 |
| mean profit p-value | 1.08e-08 | 0.002292 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -91.83 | -96.82 |
| Sharpe | -10.27 | -2.7 |
| Sortino | -5.0 | -1.17 |
| max drawdown % | 92.12 | 96.97 |
| profit factor | 0.61 | 0.84 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-91.83%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.82%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 12 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
