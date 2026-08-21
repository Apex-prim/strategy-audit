# cryptotank

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `cryptotank.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 510 | 1802 |
| expectancy per trade (USDT) | -1.32 | -0.52 |
| mean profit p-value | 0.008512 | 0.001626 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -67.44 | -93.47 |
| Sharpe | -1.56 | -1.08 |
| Sortino | -0.94 | -0.63 |
| max drawdown % | 68.15 | 93.47 |
| profit factor | 0.59 | 0.67 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-67.44%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-93.47%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
