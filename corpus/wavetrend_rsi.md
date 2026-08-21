# wavetrend_rsi

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `wavetrend_rsi.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1196 | 4044 |
| expectancy per trade (USDT) | -0.16 | -0.07 |
| mean profit p-value | 0.0001369 | 0.001212 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -19.6 | -28.75 |
| Sharpe | -3.47 | -1.67 |
| Sortino | -2.31 | -1.06 |
| max drawdown % | 20.14 | 34.58 |
| profit factor | 0.62 | 0.81 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-19.6%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-28.75%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 4.044%, rsi_ma 5.719%, d -3.198%, wave_ci 5.266% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
