# GodCard

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `GodCard.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 185 | 291 |
| expectancy per trade (USDT) | -0.98 | 0.65 |
| mean profit p-value | 0.0009233 | 0.0009482 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -18.17 | 19.0 |
| Sharpe | -1.2 | 0.46 |
| Sortino | -1.06 | 0.26 |
| max drawdown % | 19.64 | 5.38 |
| profit factor | 0.37 | 2.05 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-18.17%**.
Out of sample: buy-and-hold **346.34%** vs strategy **19.0%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
