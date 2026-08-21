# CombinedBinHAndCluc2021

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHAndCluc2021.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 852 | 2445 |
| expectancy per trade (USDT) | -0.06 | 0.73 |
| mean profit p-value | 0.6192 | 0.0001065 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -4.81 | 177.94 |
| Sharpe | -0.38 | 1.55 |
| Sortino | -0.41 | 1.59 |
| max drawdown % | 18.54 | 25.11 |
| profit factor | 0.95 | 1.26 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.6192 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-4.81%**.
Out of sample: buy-and-hold **346.34%** vs strategy **177.94%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
