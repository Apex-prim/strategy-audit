# ElliotV5HO

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ElliotV5HO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 143 | 667 |
| expectancy per trade (USDT) | 0.74 | 1.31 |
| mean profit p-value | 0.0001402 | 1.011e-14 |
| market change % (baseline) | -58.45 | 346.34 |
| strategy total % | 10.52 | 87.49 |
| Sharpe | 1.23 | 1.66 |
| Sortino | 1.55 | 1.47 |
| max drawdown % | 1.86 | 5.32 |
| profit factor | 2.24 | 2.38 |

**Retained out of sample: 177%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.45%**; the strategy returned **10.52%**.
Out of sample: buy-and-hold **346.34%** vs strategy **87.49%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.205% |
| прогрев объявлен | clean | 79 при потребности 20 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
