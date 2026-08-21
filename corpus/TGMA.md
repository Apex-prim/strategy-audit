# TGMA

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `TGMA.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1766 | 6907 |
| expectancy per trade (USDT) | -0.24 | -0.14 |
| mean profit p-value | 2.334e-08 | 2.536e-19 |
| market change % (baseline) | -59.31 | 348.67 |
| strategy total % | -42.39 | -94.09 |
| Sharpe | -6.17 | -6.06 |
| Sortino | -8.91 | -8.06 |
| max drawdown % | 42.39 | 94.13 |
| profit factor | 0.65 | 0.66 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.31%**; the strategy returned **-42.39%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-94.09%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | could not run | Fatal exception! |
| прогрев объявлен | clean | 20 при потребности 3 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.035 задан — читается как работающая защита |
| признак утечки будущего | **found** | центрированное окно center=True |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
