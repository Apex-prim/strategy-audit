# CBPete9

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `CBPete9.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 752 | 2130 |
| expectancy per trade (USDT) | -0.03 | 0.4 |
| mean profit p-value | 0.7962 | 9.951e-05 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | -2.03 | 84.26 |
| Sharpe | -0.19 | 1.46 |
| Sortino | -0.15 | 1.13 |
| max drawdown % | 16.71 | 13.18 |
| profit factor | 0.97 | 1.3 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.7962 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **-2.03%**.
Out of sample: buy-and-hold **346.34%** vs strategy **84.26%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `2da4e157b88f` · strategy list `dac6309df791d209`*
