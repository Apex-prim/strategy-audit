# MAC

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `MAC.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 10 | 42 |
| expectancy per trade (USDT) | -11.04 | 6.18 |
| mean profit p-value | 0.1276 | 0.5446 |
| market change % (baseline) | -54.78 | 352.61 |
| strategy total % | -11.04 | 25.96 |
| Sharpe | -0.16 | 0.03 |
| Sortino | -1.31 | 0.57 |
| max drawdown % | 11.04 | 32.67 |
| profit factor | 0.3 | 1.44 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1276 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-54.78%**; the strategy returned **-11.04%**.
Out of sample: buy-and-hold **352.61%** vs strategy **25.96%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.661%, macd -1.351%, macdsignal -1.749%, macdhist 1.156%, ema50 -0.581% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
