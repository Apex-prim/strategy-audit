# FlawlessVictory

Source: [`seannowotny/FlawlessVictoryPort`](https://github.com/seannowotny/FlawlessVictoryPort) · file `flawless_victory_v1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2737 | 9503 |
| expectancy per trade (USDT) | -0.27 | -0.08 |
| mean profit p-value | 8.232e-06 | 0.4918 |
| market change % (baseline) | -58.8 | 345.85 |
| strategy total % | -73.61 | -72.7 |
| Sharpe | -6.12 | -0.54 |
| Sortino | -5.39 | -0.42 |
| max drawdown % | 78.95 | 94.34 |
| profit factor | 0.75 | 0.97 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.8%**; the strategy returned **-73.61%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-72.7%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
