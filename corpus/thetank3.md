# thetank3

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `thetank3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1946 | 6674 |
| expectancy per trade (USDT) | -0.4 | -0.14 |
| mean profit p-value | 7.031e-05 | 0.05311 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -78.4 | -94.14 |
| Sharpe | -4.6 | -1.28 |
| Sortino | -2.76 | -0.76 |
| max drawdown % | 78.49 | 96.77 |
| profit factor | 0.58 | 0.86 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-78.4%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-94.14%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.375%, rsi_ma -0.465%, d8 -0.439%, wave_ci8 0.444% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
