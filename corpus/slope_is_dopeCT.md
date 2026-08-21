# slope_is_dopeCT

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `slope_is_dopeCT.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 114 | 707 |
| expectancy per trade (USDT) | -3.07 | 3.69 |
| mean profit p-value | 0.2154 | 0.2175 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -35.0 | 260.54 |
| Sharpe | -0.35 | 0.27 |
| Sortino | -0.28 | 0.09 |
| max drawdown % | 47.25 | 52.58 |
| profit factor | 0.57 | 1.38 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.2154 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-35.0%**.
Out of sample: buy-and-hold **345.85%** vs strategy **260.54%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.111%, rsi_11 -0.283% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
