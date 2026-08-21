# ElliotV2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ElliotV2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 43 | 359 |
| expectancy per trade (USDT) | 2.27 | 3.12 |
| mean profit p-value | 0.017 | 1.841e-06 |
| market change % (baseline) | -58.92 | 346.34 |
| strategy total % | 9.74 | 112.05 |
| Sharpe | 0.43 | 0.74 |
| Sortino | 0.23 | 0.7 |
| max drawdown % | 2.22 | 11.01 |
| profit factor | 3.04 | 2.08 |

**Retained out of sample: 137%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.92%**; the strategy returned **9.74%**.
Out of sample: buy-and-hold **346.34%** vs strategy **112.05%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 139 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
