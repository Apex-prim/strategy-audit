# NOTankAi_15_Cleaned

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `NOTankAi_15_Cleaned.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2853 | 6773 |
| expectancy per trade (USDT) | 174.76 | 43922.02 |
| mean profit p-value | 1.015e-54 | 1.179e-182 |
| market change % (baseline) | -59.49 | 345.85 |
| strategy total % | 49858.99 | 29748386.38 |
| Sharpe | 22.32 | 19.79 |
| Sortino | -100.0 | 1.6 |
| max drawdown % | 3.99 | 4.06 |
| profit factor | 24.98 | 24.61 |

**Retained out of sample: 25133%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.49%**; the strategy returned **49858.99%**.
Out of sample: buy-and-hold **345.85%** vs strategy **29748386.38%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: min_threshold_mean 9.210%, max_threshold_mean 9.000% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
