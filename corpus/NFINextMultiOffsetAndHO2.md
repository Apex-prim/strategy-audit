# NFINextMultiOffsetAndHO2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NFINextMultiOffsetAndHO2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 186 | 519 |
| expectancy per trade (USDT) | -0.32 | 1.04 |
| mean profit p-value | 0.3492 | 6.644e-07 |
| market change % (baseline) | -58.96 | 346.34 |
| strategy total % | -6.0 | 53.81 |
| Sharpe | -0.34 | 0.93 |
| Sortino | -0.26 | 0.62 |
| max drawdown % | 11.4 | 8.01 |
| profit factor | 0.79 | 2.09 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.3492 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.96%**; the strategy returned **-6.0%**.
Out of sample: buy-and-hold **346.34%** vs strategy **53.81%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317%, stochrsi_fastd_96 -0.557% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
