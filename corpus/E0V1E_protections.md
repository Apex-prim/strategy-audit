# E0V1E_protections

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `E0V1E_protections.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 39 | 290 |
| expectancy per trade (USDT) | 3.04 | 7.34 |
| mean profit p-value | 0.0001465 | 5.176e-31 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | 11.87 | 212.84 |
| Sharpe | 0.7 | 1.8 |
| Sortino | 0.81 | 1.38 |
| max drawdown % | 1.89 | 3.32 |
| profit factor | 5.21 | 8.03 |

**Retained out of sample: 241%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **11.87%**.
Out of sample: buy-and-hold **346.34%** vs strategy **212.84%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 12.447%, rsi_fast 0.045%, rsi_slow 12.811% |
| прогрев объявлен | clean | 20 при потребности 20 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
