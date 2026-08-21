# ZScoreMeanReversionStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `ZScoreMeanReversionStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 5 | 32 |
| expectancy per trade (USDT) | 2.99 | 1.03 |
| mean profit p-value | 0.3344 | 0.3519 |
| market change % (baseline) | -43.53 | 340.8 |
| strategy total % | 1.49 | 3.31 |
| Sharpe | 0.08 | 0.04 |
| Sortino | -100.0 | 0.17 |
| max drawdown % | 0.64 | 1.98 |
| profit factor | 3.33 | 1.47 |

**Retained out of sample: 34%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.3344 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-43.53%**; the strategy returned **1.49%**.
Out of sample: buy-and-hold **340.8%** vs strategy **3.31%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_trend -0.267% |
| прогрев объявлен | clean | 210 при потребности 14 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
