# bestV2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `bestV2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 41 | 304 |
| expectancy per trade (USDT) | 1.47 | 2.28 |
| mean profit p-value | 0.007141 | 6.892e-07 |
| market change % (baseline) | -58.87 | 346.34 |
| strategy total % | 6.04 | 69.2 |
| Sharpe | 0.48 | 0.72 |
| Sortino | 0.61 | 0.58 |
| max drawdown % | 0.87 | 5.48 |
| profit factor | 2.78 | 2.28 |

**Retained out of sample: 155%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.87%**; the strategy returned **6.04%**.
Out of sample: buy-and-hold **346.34%** vs strategy **69.2%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 120 при потребности 14 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
