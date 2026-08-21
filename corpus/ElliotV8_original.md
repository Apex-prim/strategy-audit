# ElliotV8_original

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ElliotV8_original.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 118 | 478 |
| expectancy per trade (USDT) | 1.74 | 2.89 |
| mean profit p-value | 0.0001429 | 2.707e-15 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 20.49 | 137.9 |
| Sharpe | 1.12 | 1.45 |
| Sortino | 0.39 | 0.45 |
| max drawdown % | 3.98 | 3.98 |
| profit factor | 5.29 | 5.72 |

**Retained out of sample: 166%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **20.49%**.
Out of sample: buy-and-hold **346.34%** vs strategy **137.9%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 400 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
