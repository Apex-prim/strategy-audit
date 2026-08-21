# CombinedBinHAndCluc2021Bull

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHAndCluc2021Bull.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 946 | 2930 |
| expectancy per trade (USDT) | -0.1 | -0.02 |
| mean profit p-value | 0.1989 | 0.7675 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -9.18 | -4.85 |
| Sharpe | -1.03 | -0.13 |
| Sortino | -0.85 | -0.09 |
| max drawdown % | 19.27 | 31.4 |
| profit factor | 0.88 | 0.98 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1989 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-9.18%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-4.85%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
