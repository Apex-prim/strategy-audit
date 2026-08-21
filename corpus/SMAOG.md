# SMAOG

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `SMAOG.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 105 | 433 |
| expectancy per trade (USDT) | 0.95 | 0.89 |
| mean profit p-value | 0.0001089 | 2.809e-10 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 10.02 | 38.56 |
| Sharpe | 1.09 | 1.09 |
| Sortino | 0.86 | 0.79 |
| max drawdown % | 1.48 | 2.86 |
| profit factor | 2.88 | 2.45 |

**Retained out of sample: 94%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **10.02%**.
Out of sample: buy-and-hold **346.34%** vs strategy **38.56%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 400 при потребности 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
