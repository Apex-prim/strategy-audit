# BBRSIOptimStrategy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BBRSIOptimStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2425 | 8272 |
| expectancy per trade (USDT) | -0.29 | -0.05 |
| mean profit p-value | 0.001221 | 0.8198 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -71.51 | -37.99 |
| Sharpe | -4.17 | -0.17 |
| Sortino | -2.5 | -0.1 |
| max drawdown % | 75.59 | 88.71 |
| profit factor | 0.59 | 0.98 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-71.51%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-37.99%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.935% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
