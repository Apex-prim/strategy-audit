# ElliotV5_SMA

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `ElliotV5_SMA.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 112 | 611 |
| expectancy per trade (USDT) | 1.69 | 2.56 |
| mean profit p-value | 0.0001274 | 3.861e-13 |
| market change % (baseline) | -57.18 | 346.34 |
| strategy total % | 18.88 | 156.64 |
| Sharpe | 1.11 | 1.49 |
| Sortino | 0.8 | 1.03 |
| max drawdown % | 2.65 | 3.42 |
| profit factor | 2.7 | 2.33 |

**Retained out of sample: 151%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-57.18%**; the strategy returned **18.88%**.
Out of sample: buy-and-hold **346.34%** vs strategy **156.64%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 2000 при потребности 20 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
