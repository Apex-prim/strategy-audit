# BigZ07

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BigZ07.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 409 | 1184 |
| expectancy per trade (USDT) | -0.47 | 0.64 |
| mean profit p-value | 0.1123 | 0.006003 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | -19.26 | 76.23 |
| Sharpe | -0.84 | 0.77 |
| Sortino | -0.71 | 0.62 |
| max drawdown % | 28.49 | 18.53 |
| profit factor | 0.72 | 1.35 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1123 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **-19.26%**.
Out of sample: buy-and-hold **346.34%** vs strategy **76.23%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: bb_lowerband_1h 3.629%, bb_middleband_1h 3.126%, bb_upperband_1h 2.629% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
