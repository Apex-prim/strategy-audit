# UltimateMomentumIndicator

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `UltimateMomentumIndicator.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1765 | 6382 |
| expectancy per trade (USDT) | -0.39 | -0.01 |
| mean profit p-value | 0.0002804 | 0.9665 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -69.69 | -8.43 |
| Sharpe | -4.0 | -0.03 |
| Sortino | -4.73 | -0.04 |
| max drawdown % | 78.83 | 86.37 |
| profit factor | 0.76 | 1.0 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-69.69%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-8.43%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
