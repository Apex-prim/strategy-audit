# XtraThicc

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `XtraThicc.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1981 | 7186 |
| expectancy per trade (USDT) | -0.31 | -0.12 |
| mean profit p-value | 0.0001176 | 0.01333 |
| market change % (baseline) | -58.42 | 346.34 |
| strategy total % | -62.21 | -85.46 |
| Sharpe | -4.5 | -1.7 |
| Sortino | -8.67 | -1.67 |
| max drawdown % | 63.77 | 89.65 |
| profit factor | 0.77 | 0.91 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.42%**; the strategy returned **-62.21%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-85.46%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 6 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.002 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
