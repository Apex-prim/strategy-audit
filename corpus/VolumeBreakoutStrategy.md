# VolumeBreakoutStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `VolumeBreakoutStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 7556 | 9008 |
| expectancy per trade (USDT) | -0.12 | -0.11 |
| mean profit p-value | 9.619e-37 | 9.159e-39 |
| market change % (baseline) | -58.48 | 346.34 |
| strategy total % | -90.85 | -96.59 |
| Sharpe | -28.96 | -10.04 |
| Sortino | -44.2 | -15.07 |
| max drawdown % | 90.91 | 96.59 |
| profit factor | 0.63 | 0.64 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.48%**; the strategy returned **-90.85%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.59%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.765%, atr -0.109% |
| прогрев объявлен | clean | 50 при потребности 14 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
