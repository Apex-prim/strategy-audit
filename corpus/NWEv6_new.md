# NWEv6_new

Source: [`anakein/beastbotXB`](https://github.com/anakein/beastbotXB) · file `NWEv6_new.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1869 | 6239 |
| expectancy per trade (USDT) | -0.38 | -0.15 |
| mean profit p-value | 2.66e-16 | 2.109e-16 |
| market change % (baseline) | -56.37 | 347.44 |
| strategy total % | -70.27 | -95.02 |
| Sharpe | -9.35 | -5.26 |
| Sortino | -11.21 | -4.66 |
| max drawdown % | 70.66 | 95.13 |
| profit factor | 0.59 | 0.71 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-56.37%**; the strategy returned **-70.27%**.
Out of sample: buy-and-hold **347.44%** vs strategy **-95.02%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 500 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.005 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **3m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
