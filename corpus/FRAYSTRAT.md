# FRAYSTRAT

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FRAYSTRAT (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 5668 | 6778 |
| expectancy per trade (USDT) | -0.17 | -0.14 |
| mean profit p-value | 5.687e-17 | 1.18e-11 |
| market change % (baseline) | -58.34 | 345.85 |
| strategy total % | -96.7 | -96.64 |
| Sharpe | -16.55 | -4.52 |
| Sortino | -13.4 | -3.84 |
| max drawdown % | 96.73 | 96.7 |
| profit factor | 0.59 | 0.73 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.34%**; the strategy returned **-96.7%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.64%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 3.688% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
