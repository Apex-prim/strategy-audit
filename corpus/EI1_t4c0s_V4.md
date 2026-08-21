# EI1_t4c0s_V4

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `EI1_t4c0s_V4.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 177 | 544 |
| expectancy per trade (USDT) | -1.9 | -1.05 |
| mean profit p-value | 0.0002499 | 0.0005834 |
| market change % (baseline) | -51.52 | 348.67 |
| strategy total % | -33.63 | -56.9 |
| Sharpe | -1.33 | -0.65 |
| Sortino | -1.6 | -0.47 |
| max drawdown % | 33.63 | 60.5 |
| profit factor | 0.44 | 0.55 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-51.52%**; the strategy returned **-33.63%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-56.9%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 6, выходов 7 из 14 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: move_mean -39.562%, move_mean_x -39.562%, exit_mean -1.425%, exit_mean_x -2.232%, enter_mean 1.536% |
| прогрев объявлен | clean | 400 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
