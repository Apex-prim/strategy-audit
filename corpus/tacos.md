# tacos

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `tacos.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 198 | 683 |
| expectancy per trade (USDT) | -1.26 | -0.93 |
| mean profit p-value | 0.3464 | 0.3352 |
| market change % (baseline) | -45.75 | 352.61 |
| strategy total % | -25.02 | -63.71 |
| Sharpe | -0.36 | -0.2 |
| Sortino | -0.6 | -0.2 |
| max drawdown % | 45.42 | 87.27 |
| profit factor | 0.84 | 0.9 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.3464 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-45.75%**; the strategy returned **-25.02%**.
Out of sample: buy-and-hold **352.61%** vs strategy **-63.71%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: wave_ci -0.282%, OBV -52.426%, rsi 1.778%, rsi_slope 3.253%, rsi_ma 1.709% |
| прогрев не объявлен | **found** | самый длинный индикатор 21 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
