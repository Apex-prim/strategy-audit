# PRICEFOLLOWING

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `PRICEFOLLOWING (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 74 | 198 |
| expectancy per trade (USDT) | -0.64 | -0.03 |
| mean profit p-value | 0.1793 | 0.9012 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | -4.71 | -0.61 |
| Sharpe | -0.31 | -0.01 |
| Sortino | -0.69 | -0.34 |
| max drawdown % | 5.61 | 5.26 |
| profit factor | 0.5 | 0.96 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1793 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-4.71%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-0.61%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 1.408%, sar 0.021% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
