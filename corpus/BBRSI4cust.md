# BBRSI4cust

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BBRSI4cust.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 7881 | 15005 |
| expectancy per trade (USDT) | -0.11 | -0.06 |
| mean profit p-value | 1.421e-42 | 2.749e-41 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -85.4 | -96.56 |
| Sharpe | -31.97 | -13.38 |
| Sortino | -23.04 | -9.45 |
| max drawdown % | 85.42 | 96.58 |
| profit factor | 0.45 | 0.52 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-85.4%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.56%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: plus_di 2.181%, rsi -0.375% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
