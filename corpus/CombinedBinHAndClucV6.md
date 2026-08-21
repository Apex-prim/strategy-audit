# CombinedBinHAndClucV6

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHAndClucV6.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 405 | 1319 |
| expectancy per trade (USDT) | 0.71 | 0.31 |
| mean profit p-value | 0.0005298 | 0.01678 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 28.58 | 40.31 |
| Sharpe | 1.84 | 0.7 |
| Sortino | 2.67 | 0.97 |
| max drawdown % | 6.58 | 10.98 |
| profit factor | 1.6 | 1.18 |

**Retained out of sample: 44%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **28.58%**.
Out of sample: buy-and-hold **346.34%** vs strategy **40.31%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `2da4e157b88f` · strategy list `dac6309df791d209`*
