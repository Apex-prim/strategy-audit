# ElliotV8_original_ichiv2OH

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `ElliotV8_original_ichiv2OH.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 60 | 455 |
| expectancy per trade (USDT) | 1.04 | 1.06 |
| mean profit p-value | 0.06613 | 9.719e-05 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 6.24 | 48.25 |
| Sharpe | 0.38 | 0.68 |
| Sortino | 0.27 | 0.65 |
| max drawdown % | 1.39 | 8.86 |
| profit factor | 2.01 | 1.67 |

**Retained out of sample: 102%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.06613 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **6.24%**.
Out of sample: buy-and-hold **346.34%** vs strategy **48.25%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 400 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
