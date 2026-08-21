# StarRise

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `StarRise.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 64 | 156 |
| expectancy per trade (USDT) | 1.25 | 1.41 |
| mean profit p-value | 1.047e-19 | 2.164e-43 |
| market change % (baseline) | -59.11 | 346.34 |
| strategy total % | 8.03 | 22.01 |
| Sharpe | 2.77 | 1.97 |
| Sortino | 2198.78 | 37.4 |
| max drawdown % | 0.02 | 0.05 |
| profit factor | 155.03 | 90.38 |

**Retained out of sample: 113%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.11%**; the strategy returned **8.03%**.
Out of sample: buy-and-hold **346.34%** vs strategy **22.01%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: mama_diff_1h -0.774%, rsi_84 1.930%, rsi_112 1.913%, mama_diff -0.047% |
| прогрев занижен | **found** | объявлено 168, нужно не менее 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
