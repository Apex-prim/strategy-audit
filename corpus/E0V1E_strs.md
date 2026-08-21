# E0V1E_strs

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `E0V1E_strs.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 14 | 120 |
| expectancy per trade (USDT) | 2.11 | 1.98 |
| mean profit p-value | 0.0001183 | 2.388e-10 |
| market change % (baseline) | -58.87 | 346.34 |
| strategy total % | 2.95 | 23.76 |
| Sharpe | 0.55 | 0.62 |
| Sortino | -100.0 | 0.87 |
| max drawdown % | 0.0 | 1.47 |
| profit factor | 0.0 | 6.18 |

**Retained out of sample: 94%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.87%**; the strategy returned **2.95%**.
Out of sample: buy-and-hold **346.34%** vs strategy **23.76%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi_slow -0.034% |
| прогрев объявлен | clean | 120 при потребности 20 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
