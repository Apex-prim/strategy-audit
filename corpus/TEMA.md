# TEMA

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `TEMA.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 12845 | 12313 |
| expectancy per trade (USDT) | -0.08 | -0.08 |
| mean profit p-value | 6.579e-141 | 3.804e-110 |
| market change % (baseline) | -55.55 | 347.94 |
| strategy total % | -96.57 | -96.57 |
| Sharpe | -75.9 | -20.22 |
| Sortino | -76.98 | -20.15 |
| max drawdown % | 96.58 | 96.58 |
| profit factor | 0.33 | 0.33 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-55.55%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: adx 15.936%, rsi 2.525% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
