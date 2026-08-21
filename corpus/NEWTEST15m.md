# NEWTEST15m

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FrayNew-HyperOpt (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 607 | 2037 |
| expectancy per trade (USDT) | -1.14 | -0.33 |
| mean profit p-value | 0.0009625 | 0.3576 |
| market change % (baseline) | -58.34 | 345.85 |
| strategy total % | -69.46 | -66.69 |
| Sharpe | -2.14 | -0.34 |
| Sortino | -2.3 | -0.27 |
| max drawdown % | 71.27 | 86.58 |
| profit factor | 0.63 | 0.93 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.34%**; the strategy returned **-69.46%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-66.69%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: bb_middleband -0.028%, bb_upperband -0.056%, bb_percent 26.782%, bb_width -22.031% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
