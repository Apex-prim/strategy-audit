# gettinMoist

Source: [`werkkrew/freqtrade-strategies`](https://github.com/werkkrew/freqtrade-strategies) · file `gettinMoist.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 5122 | 14914 |
| expectancy per trade (USDT) | -0.16 | -0.06 |
| mean profit p-value | 9.266e-10 | 5.386e-05 |
| market change % (baseline) | -58.42 | 346.34 |
| strategy total % | -83.24 | -96.66 |
| Sharpe | -11.49 | -3.99 |
| Sortino | -16.88 | -4.04 |
| max drawdown % | 84.25 | 96.81 |
| profit factor | 0.8 | 0.9 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.42%**; the strategy returned **-83.24%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.66%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: macd -15.308%, macdsignal 8.398%, macdhist 1.915% |
| прогрев не объявлен | **found** | самый длинный индикатор 7 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
