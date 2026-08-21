# stratfib

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `stratfib.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6 | 4 |
| expectancy per trade (USDT) | 1.24 | 1.45 |
| mean profit p-value | 1.379e-13 | 0.006218 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | 0.74 | 0.58 |
| Sharpe | 47.3 | 0.13 |
| Sortino | -100.0 | -100.0 |
| max drawdown % | 0.0 | 0.0 |
| profit factor | 0.0 | 0.0 |

**Retained out of sample: 117%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **0.74%**.
Out of sample: buy-and-hold **348.67%** vs strategy **0.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 4.044% |
| прогрев не объявлен | **found** | самый длинный индикатор 89 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
