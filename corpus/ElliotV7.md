# ElliotV7

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ElliotV7.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 112 | 442 |
| expectancy per trade (USDT) | 0.87 | 1.17 |
| mean profit p-value | 4.546e-05 | 6.238e-10 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | 9.77 | 51.53 |
| Sharpe | 1.18 | 1.08 |
| Sortino | 1.44 | 0.78 |
| max drawdown % | 1.46 | 4.78 |
| profit factor | 2.72 | 2.46 |

**Retained out of sample: 134%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **9.77%**.
Out of sample: buy-and-hold **346.34%** vs strategy **51.53%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: macd 98.725%, macdsignal -63.003%, rsi -1.976%, rsi_slow -4.174% |
| прогрев занижен | **found** | объявлено 39, нужно не менее 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
