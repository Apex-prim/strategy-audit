# RSIDirectionalWithTrendSlow

Source: [`paulcpk/freqtrade-strategies-that-work`](https://github.com/paulcpk/freqtrade-strategies-that-work) · file `RSIDirectionalWithTrendSlow.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 132 | 498 |
| expectancy per trade (USDT) | 1.13 | 0.06 |
| mean profit p-value | 0.3807 | 0.9244 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | 14.96 | 3.21 |
| Sharpe | 0.27 | 0.02 |
| Sortino | 1.1 | 0.05 |
| max drawdown % | 12.37 | 26.01 |
| profit factor | 1.33 | 1.02 |

**Retained out of sample: 5%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.3807 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **14.96%**.
Out of sample: buy-and-hold **348.67%** vs strategy **3.21%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 600 свечей, startup_candle_count не задан (по умолчанию 0) |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |
| minimal_roi закомментирован | **found** | правила выхода по прибыли берутся из неопубликованного конфига |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `—`*
