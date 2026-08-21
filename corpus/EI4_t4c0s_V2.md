# EI4_t4c0s_V2

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `EI4_t4c0s_V2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 968 | 3400 |
| expectancy per trade (USDT) | -0.52 | -0.04 |
| mean profit p-value | 0.0009817 | 0.7495 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | -50.63 | -15.16 |
| Sharpe | -2.7 | -0.15 |
| Sortino | -2.19 | -0.1 |
| max drawdown % | 51.22 | 57.31 |
| profit factor | 0.69 | 0.98 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **-50.63%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-15.16%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 6, выходов 11 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: HMA_SQZ -0.972%, EWO -12.317%, EWO_UP -12.317%, EWO_MEAN_UP -87.199%, EWO_UP_FIB -87.199% |
| прогрев объявлен | clean | 400 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
