# E0V1E_ewo

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `E0V1E_ewo.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 40 | 269 |
| expectancy per trade (USDT) | 2.67 | 4.17 |
| mean profit p-value | 2.319e-05 | 3.867e-09 |
| market change % (baseline) | -58.87 | 346.34 |
| strategy total % | 10.67 | 112.12 |
| Sharpe | 0.81 | 0.81 |
| Sortino | -100.0 | 0.49 |
| max drawdown % | 1.22 | 12.76 |
| profit factor | 9.53 | 3.27 |

**Retained out of sample: 156%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.87%**; the strategy returned **10.67%**.
Out of sample: buy-and-hold **346.34%** vs strategy **112.12%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi_slow -0.034% |
| прогрев объявлен | clean | 120 при потребности 20 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
