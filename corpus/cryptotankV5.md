# cryptotankV5

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `cryptotankV5.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 946 | 3836 |
| expectancy per trade (USDT) | -0.82 | -0.23 |
| mean profit p-value | 2.459e-05 | 0.02872 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -77.27 | -87.32 |
| Sharpe | -3.41 | -1.1 |
| Sortino | -2.47 | -0.56 |
| max drawdown % | 77.37 | 92.29 |
| profit factor | 0.55 | 0.85 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-77.27%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-87.32%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 32 свечей, startup_candle_count не задан (по умолчанию 0) |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
