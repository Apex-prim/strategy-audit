# Apollo11

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Apollo11 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1495 | 4883 |
| expectancy per trade (USDT) | -0.51 | -0.2 |
| mean profit p-value | 1.494e-05 | 0.01694 |
| market change % (baseline) | -59.37 | 345.85 |
| strategy total % | -75.63 | -96.67 |
| Sharpe | -4.42 | -1.35 |
| Sortino | -4.72 | -0.97 |
| max drawdown % | 78.84 | 97.75 |
| profit factor | 0.71 | 0.89 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.37%**; the strategy returned **-75.63%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.67%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: s2_ema_xxl_off 0.123%, s2_ema_xxl 0.123%, vwmacd 0.030%, signal -0.033% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
