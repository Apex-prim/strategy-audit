# twinturboV8

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `twinturboV8.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 253 | 847 |
| expectancy per trade (USDT) | -0.23 | 0.39 |
| mean profit p-value | 0.5715 | 0.1498 |
| market change % (baseline) | -58.3 | 346.34 |
| strategy total % | -5.94 | 33.1 |
| Sharpe | -0.24 | 0.34 |
| Sortino | -0.11 | 0.15 |
| max drawdown % | 14.28 | 12.25 |
| profit factor | 0.82 | 1.27 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.5715 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.3%**; the strategy returned **-5.94%**.
Out of sample: buy-and-hold **346.34%** vs strategy **33.1%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: BTC_EWO_Fast_1h 13.218%, rsi -4.207%, rsi_slow -7.999% |
| прогрев занижен | **found** | объявлено 35, нужно не менее 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
