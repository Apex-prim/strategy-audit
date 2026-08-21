# StarRise_strat3

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `StarRise_V3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 295 | 966 |
| expectancy per trade (USDT) | -0.15 | 0.42 |
| mean profit p-value | 0.588 | 0.0338 |
| market change % (baseline) | -59.11 | 346.34 |
| strategy total % | -4.46 | 40.14 |
| Sharpe | -0.24 | 0.53 |
| Sortino | -0.22 | 0.38 |
| max drawdown % | 9.91 | 13.33 |
| profit factor | 0.91 | 1.25 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.588 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.11%**; the strategy returned **-4.46%**.
Out of sample: buy-and-hold **346.34%** vs strategy **40.14%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 3, выходов 3 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: mama_diff_1h -0.774%, move_mean -50.938%, move_mean_x -50.938%, move_mean_2x -50.938%, threshold_mean -0.208% |
| прогрев занижен | **found** | объявлено 168, нужно не менее 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
