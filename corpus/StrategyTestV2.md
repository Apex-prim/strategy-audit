# StrategyTestV2

Source: [`markdregan/FreqAI-Marcos-Lopez-De-Prado`](https://github.com/markdregan/FreqAI-Marcos-Lopez-De-Prado) · file `strategy_test_v2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6303 | 19767 |
| expectancy per trade (USDT) | -0.12 | -0.05 |
| mean profit p-value | 7.396e-12 | 0.0004201 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | -77.37 | -96.59 |
| Sharpe | -14.26 | -4.01 |
| Sortino | -8.64 | -2.5 |
| max drawdown % | 79.59 | 97.65 |
| profit factor | 0.54 | 0.84 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-77.37%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.59%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: minus_di -4.063%, plus_di 29.287%, rsi 12.447% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
