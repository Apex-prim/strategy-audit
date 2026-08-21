# PRICEFOLLOWINGX

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `PRICEFOLLOWINGX (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 273 | 899 |
| expectancy per trade (USDT) | -2.03 | 0.14 |
| mean profit p-value | 0.008674 | 0.7712 |
| market change % (baseline) | -58.34 | 345.85 |
| strategy total % | -55.47 | 12.75 |
| Sharpe | -1.15 | 0.07 |
| Sortino | -1.04 | 0.04 |
| max drawdown % | 56.05 | 42.19 |
| profit factor | 0.37 | 1.06 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.34%**; the strategy returned **-55.47%**.
Out of sample: buy-and-hold **345.85%** vs strategy **12.75%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 3.688%, frsi -34.863% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
