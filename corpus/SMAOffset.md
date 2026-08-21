# SMAOffset

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `SMAOffset.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 483 | 1625 |
| expectancy per trade (USDT) | 0.1 | 2.45 |
| mean profit p-value | 0.6463 | 6.825e-06 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | 4.77 | 398.09 |
| Sharpe | 0.26 | 1.47 |
| Sortino | 0.33 | 1.35 |
| max drawdown % | 13.03 | 19.27 |
| profit factor | 1.05 | 1.48 |

**Retained out of sample: 2450%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.6463 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **4.77%**.
Out of sample: buy-and-hold **346.34%** vs strategy **398.09%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ma_offset_sell -0.020% |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.0001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
