# strato

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `strato.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 12251 | 12158 |
| expectancy per trade (USDT) | -0.08 | -0.08 |
| mean profit p-value | 1.94e-113 | 1.372e-91 |
| market change % (baseline) | -55.53 | 347.94 |
| strategy total % | -96.57 | -96.59 |
| Sharpe | -66.26 | -18.26 |
| Sortino | -64.83 | -16.53 |
| max drawdown % | 96.57 | 96.59 |
| profit factor | 0.41 | 0.38 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-55.53%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-96.59%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -1.353% |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
