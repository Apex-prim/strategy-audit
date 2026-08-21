# Combined_NFIv7_SMA_bAdBoY_20211204

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `Combined_NFIv7_SMA_bAdBoY_20211204.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 229 | 698 |
| expectancy per trade (USDT) | 0.67 | 2.69 |
| mean profit p-value | 0.005881 | 3.005e-29 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 15.37 | 188.0 |
| Sharpe | 1.11 | 2.51 |
| Sortino | 0.92 | 1.73 |
| max drawdown % | 10.68 | 2.14 |
| profit factor | 1.69 | 3.55 |

**Retained out of sample: 401%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **15.37%**.
Out of sample: buy-and-hold **346.34%** vs strategy **188.0%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
