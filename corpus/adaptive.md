# adaptive

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `adaptive.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 94 | 553 |
| expectancy per trade (USDT) | 1.73 | 0.16 |
| mean profit p-value | 3.711e-05 | 0.5226 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | 16.31 | 9.11 |
| Sharpe | 1.1 | 0.12 |
| Sortino | 40.29 | 0.81 |
| max drawdown % | 2.74 | 21.0 |
| profit factor | 3.24 | 1.08 |

**Retained out of sample: 9%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **16.31%**.
Out of sample: buy-and-hold **346.34%** vs strategy **9.11%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 112 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
