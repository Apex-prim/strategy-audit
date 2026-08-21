# HurstCycle3

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `HurstCycle3 (2).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 10088 | 10019 |
| expectancy per trade (USDT) | -0.1 | -0.1 |
| mean profit p-value | 5.45e-53 | 8.501e-47 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -96.57 | -96.6 |
| Sharpe | -40.46 | -11.69 |
| Sortino | -49.47 | -15.83 |
| max drawdown % | 96.57 | 96.6 |
| profit factor | 0.58 | 0.65 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.6%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| признак утечки будущего | **found** | центрированное окно center=True |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
