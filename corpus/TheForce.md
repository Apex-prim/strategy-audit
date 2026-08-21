# TheForce

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `TheForce.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11971 | 12117 |
| expectancy per trade (USDT) | -0.08 | -0.08 |
| mean profit p-value | 3.222e-116 | 3.398e-112 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -96.57 | -96.57 |
| Sharpe | -66.35 | -20.25 |
| Sortino | -78.84 | -24.04 |
| max drawdown % | 96.58 | 96.58 |
| profit factor | 0.51 | 0.5 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: fastd_rsi 8.725%, macd -45000.555%, macdsignal -45000.555% |
| прогрев не объявлен | **found** | самый длинный индикатор 5 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
