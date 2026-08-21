# Martin

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Martin.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3105 | 9619 |
| expectancy per trade (USDT) | -0.25 | -0.1 |
| mean profit p-value | 8.058e-09 | 1.498e-06 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -76.96 | -96.76 |
| Sharpe | -8.44 | -3.82 |
| Sortino | -7.24 | -2.13 |
| max drawdown % | 78.6 | 96.94 |
| profit factor | 0.68 | 0.8 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-76.96%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.76%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.935% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
