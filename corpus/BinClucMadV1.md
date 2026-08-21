# BinClucMadV1

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BinClucMadV1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 238 | 926 |
| expectancy per trade (USDT) | 0.65 | 2.32 |
| mean profit p-value | 0.001545 | 2.916e-36 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 15.48 | 215.04 |
| Sharpe | 1.3 | 3.23 |
| Sortino | 1.12 | 2.82 |
| max drawdown % | 5.09 | 2.34 |
| profit factor | 1.74 | 3.11 |

**Retained out of sample: 357%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **15.48%**.
Out of sample: buy-and-hold **346.34%** vs strategy **215.04%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `2da4e157b88f` · strategy list `dac6309df791d209`*
