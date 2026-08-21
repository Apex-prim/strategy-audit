# CombinedBinHAndClucV3

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `CombinedBinHAndClucV3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 687 | 1902 |
| expectancy per trade (USDT) | 0.1 | 1.17 |
| mean profit p-value | 0.5701 | 6.407e-07 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | 6.59 | 222.87 |
| Sharpe | 0.39 | 1.76 |
| Sortino | 0.32 | 0.92 |
| max drawdown % | 16.63 | 24.1 |
| profit factor | 1.07 | 1.53 |

**Retained out of sample: 1170%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.5701 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **6.59%**.
Out of sample: buy-and-hold **346.34%** vs strategy **222.87%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
