# CombinedBinHAndClucHyper

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `CombinedBinHAndClucHyper.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 653 | 3164 |
| expectancy per trade (USDT) | 0.1 | 0.48 |
| mean profit p-value | 0.5822 | 1.373e-14 |
| market change % (baseline) | -55.69 | 347.94 |
| strategy total % | 6.41 | 152.66 |
| Sharpe | 0.37 | 3.52 |
| Sortino | 0.21 | 2.25 |
| max drawdown % | 8.73 | 6.87 |
| profit factor | 1.33 | 8.85 |

**Retained out of sample: 480%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.5822 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.69%**; the strategy returned **6.41%**.
Out of sample: buy-and-hold **347.94%** vs strategy **152.66%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
