# MACDStrategy_crossed

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `MACDStrategy_crossed.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1075 | 3990 |
| expectancy per trade (USDT) | -0.51 | -0.21 |
| mean profit p-value | 0.001216 | 0.0006579 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -55.1 | -83.98 |
| Sharpe | -2.78 | -1.74 |
| Sortino | -1.42 | -0.75 |
| max drawdown % | 58.12 | 86.59 |
| profit factor | 0.6 | 0.72 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-55.1%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-83.98%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
