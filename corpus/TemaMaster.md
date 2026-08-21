# TemaMaster

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `TemaMaster.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1417 | 5077 |
| expectancy per trade (USDT) | -0.44 | -0.15 |
| mean profit p-value | 0.003677 | 0.4405 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -62.43 | -75.56 |
| Sharpe | -2.86 | -0.44 |
| Sortino | -2.67 | -0.36 |
| max drawdown % | 69.39 | 94.37 |
| profit factor | 0.79 | 0.96 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-62.43%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-75.56%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 26 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
