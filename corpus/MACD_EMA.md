# MACD_EMA

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `MACD_EMA.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 10460 | 15195 |
| expectancy per trade (USDT) | -0.09 | -0.06 |
| mean profit p-value | 2.151e-27 | 5.342e-18 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -95.03 | -96.58 |
| Sharpe | -29.07 | -8.63 |
| Sortino | -28.65 | -8.85 |
| max drawdown % | 95.04 | 96.68 |
| profit factor | 0.68 | 0.79 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-95.03%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
