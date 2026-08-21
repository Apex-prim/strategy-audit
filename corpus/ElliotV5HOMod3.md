# ElliotV5HOMod3

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ElliotV5HOMod3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 88 | 459 |
| expectancy per trade (USDT) | -0.11 | 2.68 |
| mean profit p-value | 0.9003 | 3.493e-05 |
| market change % (baseline) | -58.45 | 346.34 |
| strategy total % | -0.95 | 123.16 |
| Sharpe | -0.03 | 0.73 |
| Sortino | -1.48 | 3.12 |
| max drawdown % | 7.96 | 9.75 |
| profit factor | 0.97 | 1.53 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.9003 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.45%**; the strategy returned **-0.95%**.
Out of sample: buy-and-hold **346.34%** vs strategy **123.16%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.205% |
| прогрев объявлен | clean | 79 при потребности 14 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.005 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
