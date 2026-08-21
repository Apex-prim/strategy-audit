# ElliotV4

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ElliotV4.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 165 | 750 |
| expectancy per trade (USDT) | 0.15 | 3.42 |
| mean profit p-value | 0.8522 | 4.291e-05 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | 2.54 | 256.46 |
| Sharpe | 0.06 | 0.91 |
| Sortino | 0.03 | 0.39 |
| max drawdown % | 17.5 | 24.56 |
| profit factor | 1.12 | 3.21 |

**Retained out of sample: 2280%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.8522 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **2.54%**.
Out of sample: buy-and-hold **346.34%** vs strategy **256.46%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -1.976% |
| прогрев объявлен | clean | 39 при потребности 20 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
