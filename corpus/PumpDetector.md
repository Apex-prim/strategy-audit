# PumpDetector

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `PumpDetector.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 13347 | 18911 |
| expectancy per trade (USDT) | -0.07 | -0.05 |
| mean profit p-value | 2.106e-31 | 3.294e-22 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -96.58 | -96.75 |
| Sharpe | -35.34 | -10.79 |
| Sortino | -29.68 | -8.11 |
| max drawdown % | 96.6 | 96.76 |
| profit factor | 0.6 | 0.67 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-96.58%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.75%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: k -1.582%, d -5.693%, j 17.992% |
| прогрев не объявлен | **found** | самый длинный индикатор 3 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
