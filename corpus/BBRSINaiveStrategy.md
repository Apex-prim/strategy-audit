# BBRSINaiveStrategy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BBRSINaiveStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4539 | 15483 |
| expectancy per trade (USDT) | -0.19 | -0.06 |
| mean profit p-value | 8.016e-13 | 0.0003645 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -87.79 | -96.84 |
| Sharpe | -12.66 | -3.59 |
| Sortino | -8.23 | -2.11 |
| max drawdown % | 87.96 | 97.05 |
| profit factor | 0.65 | 0.88 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-87.79%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.84%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.375% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
