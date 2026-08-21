# NFI5MOHO

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NFI5MOHO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 38 | 340 |
| expectancy per trade (USDT) | 1.83 | 2.12 |
| mean profit p-value | 0.0236 | 1.063e-05 |
| market change % (baseline) | -59.35 | 346.34 |
| strategy total % | 6.95 | 72.0 |
| Sharpe | 0.39 | 0.67 |
| Sortino | 7.57 | 1.96 |
| max drawdown % | 1.26 | 13.34 |
| profit factor | 2.78 | 1.81 |

**Retained out of sample: 116%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.35%**; the strategy returned **6.95%**.
Out of sample: buy-and-hold **346.34%** vs strategy **72.0%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
