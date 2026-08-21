# SmaRsiStrategy

Source: [`DutchCryptoDad/FreqtradeBotStrategyDevelopmentForBeginners`](https://github.com/DutchCryptoDad/FreqtradeBotStrategyDevelopmentForBeginners) · file `SmaRsiStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 85 | 490 |
| expectancy per trade (USDT) | 4.3 | 7.38 |
| mean profit p-value | 0.2055 | 0.09025 |
| market change % (baseline) | -51.38 | 352.61 |
| strategy total % | 36.51 | 361.48 |
| Sharpe | 0.32 | 0.3 |
| Sortino | 1.84 | 1.51 |
| max drawdown % | 17.67 | 35.37 |
| profit factor | 1.68 | 1.33 |

**Retained out of sample: 172%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.2055 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-51.38%**; the strategy returned **36.51%**.
Out of sample: buy-and-hold **352.61%** vs strategy **361.48%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 4.262% |
| прогрев не объявлен | **found** | самый длинный индикатор 21 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
