# MomStrategy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `MomStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 8604 | 13003 |
| expectancy per trade (USDT) | -0.11 | -0.07 |
| mean profit p-value | 1.796e-33 | 4.718e-34 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -92.36 | -96.57 |
| Sharpe | -29.35 | -11.25 |
| Sortino | -34.74 | -11.94 |
| max drawdown % | 92.46 | 96.66 |
| profit factor | 0.65 | 0.68 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-92.36%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
