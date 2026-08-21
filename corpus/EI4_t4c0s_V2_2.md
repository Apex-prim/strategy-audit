# EI4_t4c0s_V2_2

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `EI4_t4c0s_V2_2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 968 | — |
| expectancy per trade (USDT) | -0.52 | — |
| mean profit p-value | 0.0009817 | — |
| market change % (baseline) | -59.23 | — |
| strategy total % | -50.63 | — |
| Sharpe | -2.7 | — |
| Sortino | -2.19 | — |
| max drawdown % | 51.22 | — |
| profit factor | 0.69 | — |

**Retained out of sample: —**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **-50.63%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 6, выходов 11 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | could not run | Could not load markets. |
| прогрев объявлен | clean | 400 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
