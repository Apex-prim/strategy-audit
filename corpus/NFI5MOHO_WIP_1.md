# NFI5MOHO_WIP_1

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NFI5MOHO_WIP_1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 208 | 768 |
| expectancy per trade (USDT) | 0.48 | 3.58 |
| mean profit p-value | 0.0864 | 1.296e-37 |
| market change % (baseline) | -59.35 | 346.34 |
| strategy total % | 9.99 | 275.03 |
| Sharpe | 0.65 | 3.04 |
| Sortino | 0.4 | 1.66 |
| max drawdown % | 5.85 | 4.76 |
| profit factor | 1.5 | 4.56 |

**Retained out of sample: 746%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.0864 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.35%**; the strategy returned **9.99%**.
Out of sample: buy-and-hold **346.34%** vs strategy **275.03%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
