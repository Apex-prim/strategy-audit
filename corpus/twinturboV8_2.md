# twinturboV8_2

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `twinturboV8_2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 23 | 96 |
| expectancy per trade (USDT) | -0.06 | 1.02 |
| mean profit p-value | 0.9665 | 0.2505 |
| market change % (baseline) | -58.3 | 346.34 |
| strategy total % | -0.15 | 9.84 |
| Sharpe | -0.01 | 0.09 |
| Sortino | -0.01 | 0.06 |
| max drawdown % | 3.34 | 5.84 |
| profit factor | 0.97 | 1.55 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.9665 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.3%**; the strategy returned **-0.15%**.
Out of sample: buy-and-hold **346.34%** vs strategy **9.84%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: BTC_EWO_Fast_1h 13.218%, rsi -4.207%, rsi_slow -7.999% |
| прогрев занижен | **found** | объявлено 35, нужно не менее 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
