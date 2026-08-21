# BBRSI3366

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BBRSI3366.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 9643 | 17230 |
| expectancy per trade (USDT) | -0.1 | -0.06 |
| mean profit p-value | 3.751e-28 | 6.842e-07 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -95.6 | -96.61 |
| Sharpe | -28.33 | -5.27 |
| Sortino | -19.67 | -3.48 |
| max drawdown % | 95.62 | 96.73 |
| profit factor | 0.47 | 0.76 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-95.6%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.61%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
