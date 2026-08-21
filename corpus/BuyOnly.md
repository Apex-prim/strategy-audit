# BuyOnly

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BuyOnly.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 608 | 2171 |
| expectancy per trade (USDT) | -0.25 | -0.12 |
| mean profit p-value | 0.1449 | 0.1842 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -15.17 | -25.22 |
| Sharpe | -0.94 | -0.5 |
| Sortino | -3.45 | -1.91 |
| max drawdown % | 21.16 | 33.67 |
| profit factor | 0.82 | 0.91 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1449 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-15.17%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-25.22%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.375% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
