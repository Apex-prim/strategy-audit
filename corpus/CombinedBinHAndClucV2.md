# CombinedBinHAndClucV2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHAndClucV2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 207 | 521 |
| expectancy per trade (USDT) | 0.08 | 0.71 |
| mean profit p-value | 0.765 | 0.00276 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 1.6 | 37.03 |
| Sharpe | 0.11 | 0.56 |
| Sortino | 0.16 | 1.11 |
| max drawdown % | 8.02 | 5.79 |
| profit factor | 1.05 | 1.36 |

**Retained out of sample: 888%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.765 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **1.6%**.
Out of sample: buy-and-hold **346.34%** vs strategy **37.03%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: srsi_fk -0.144%, srsi_fd -0.134% |
| прогрев объявлен | clean | 200 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `2da4e157b88f` · strategy list `dac6309df791d209`*
