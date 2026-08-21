# BB_RPB_TSL_RNG_2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BB_RPB_TSL_RNG_2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 101 | 675 |
| expectancy per trade (USDT) | 1.51 | 1.88 |
| mean profit p-value | 3.911e-05 | 1.279e-08 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | 15.23 | 126.98 |
| Sharpe | 1.14 | 1.21 |
| Sortino | 1.3 | 1.24 |
| max drawdown % | 2.69 | 9.01 |
| profit factor | 3.25 | 2.39 |

**Retained out of sample: 125%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **15.23%**.
Out of sample: buy-and-hold **346.34%** vs strategy **126.98%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
