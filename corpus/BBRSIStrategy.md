# BBRSIStrategy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BBRSIStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2666 | 9664 |
| expectancy per trade (USDT) | -0.3 | -0.09 |
| mean profit p-value | 5.774e-05 | 0.1291 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -79.88 | -88.59 |
| Sharpe | -5.44 | -1.21 |
| Sortino | -3.22 | -0.69 |
| max drawdown % | 80.04 | 95.29 |
| profit factor | 0.41 | 0.84 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-79.88%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-88.59%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.375% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
