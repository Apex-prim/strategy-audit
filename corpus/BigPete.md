# BigPete

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BigPete.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4439 | 13236 |
| expectancy per trade (USDT) | -0.18 | -0.07 |
| mean profit p-value | 2.996e-08 | 0.0004976 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | -79.34 | -96.63 |
| Sharpe | -9.68 | -3.24 |
| Sortino | -9.67 | -2.37 |
| max drawdown % | 83.61 | 96.78 |
| profit factor | 0.78 | 0.9 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **-79.34%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.63%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
