# BeastBotXBLR7

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `BeastBotXBLR7.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 111 | 458 |
| expectancy per trade (USDT) | 0.59 | 3.13 |
| mean profit p-value | 0.1902 | 1.77e-05 |
| market change % (baseline) | -59.35 | 346.34 |
| strategy total % | 6.6 | 143.37 |
| Sharpe | 0.37 | 0.75 |
| Sortino | 0.55 | 0.59 |
| max drawdown % | 3.15 | 14.83 |
| profit factor | 1.38 | 1.94 |

**Retained out of sample: 531%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1902 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.35%**; the strategy returned **6.6%**.
Out of sample: buy-and-hold **346.34%** vs strategy **143.37%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `2da4e157b88f` · strategy list `dac6309df791d209`*
