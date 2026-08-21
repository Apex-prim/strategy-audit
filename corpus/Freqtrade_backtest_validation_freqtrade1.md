# Freqtrade_backtest_validation_freqtrade1

Source: [`freqtrade/freqtrade-strategies`](https://github.com/freqtrade/freqtrade-strategies) · file `Freqtrade_backtest_validation_freqtrade1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2128 | 8036 |
| expectancy per trade (USDT) | 0.04 | 0.01 |
| mean profit p-value | 0.7433 | 0.9594 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | 8.34 | 5.43 |
| Sharpe | 0.39 | 0.04 |
| Sortino | 1.03 | 0.08 |
| max drawdown % | 36.09 | 80.21 |
| profit factor | 1.03 | 1.0 |

**Retained out of sample: 25%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.7433 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **8.34%**.
Out of sample: buy-and-hold **348.67%** vs strategy **5.43%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 28 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
