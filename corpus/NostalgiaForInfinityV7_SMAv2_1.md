# NostalgiaForInfinityV7_SMAv2_1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NostalgiaForInfinityV7_SMAv2_1 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 123 | 422 |
| expectancy per trade (USDT) | 0.88 | 3.46 |
| mean profit p-value | 0.04119 | 2.18e-12 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 10.86 | 146.04 |
| Sharpe | 0.6 | 1.2 |
| Sortino | 0.49 | 0.45 |
| max drawdown % | 9.06 | 6.37 |
| profit factor | 1.66 | 3.57 |

**Retained out of sample: 393%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **10.86%**.
Out of sample: buy-and-hold **346.34%** vs strategy **146.04%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, rsi_slow 0.071%, ewo -12.317%, rsi 0.530% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
