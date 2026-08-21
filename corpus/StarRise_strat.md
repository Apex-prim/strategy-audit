# StarRise_strat

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `StarRise_V2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 73 | 182 |
| expectancy per trade (USDT) | -0.1 | 0.05 |
| mean profit p-value | 0.8106 | 0.8751 |
| market change % (baseline) | -59.11 | 346.34 |
| strategy total % | -0.72 | 0.92 |
| Sharpe | -0.05 | 0.02 |
| Sortino | -0.03 | 0.01 |
| max drawdown % | 2.79 | 4.15 |
| profit factor | 0.88 | 1.06 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.8106 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.11%**; the strategy returned **-0.72%**.
Out of sample: buy-and-hold **346.34%** vs strategy **0.92%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: mama_diff_1h -0.774%, rsi_84 1.930%, rsi_112 1.913%, mama_diff -0.047% |
| прогрев занижен | **found** | объявлено 168, нужно не менее 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
