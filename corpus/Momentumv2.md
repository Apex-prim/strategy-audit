# Momentumv2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `Momentumv2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 414 | 1849 |
| expectancy per trade (USDT) | 0.89 | 0.24 |
| mean profit p-value | 0.01987 | 0.3744 |
| market change % (baseline) | -50.13 | 340.8 |
| strategy total % | 37.0 | 44.9 |
| Sharpe | 1.27 | 0.31 |
| Sortino | 4.26 | 0.86 |
| max drawdown % | 9.11 | 38.09 |
| profit factor | 1.4 | 1.06 |

**Retained out of sample: 27%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-50.13%**; the strategy returned **37.0%**.
Out of sample: buy-and-hold **340.8%** vs strategy **44.9%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: macd -0.093%, macdsignal -0.134%, rsi 0.023%, ema 0.223% |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
