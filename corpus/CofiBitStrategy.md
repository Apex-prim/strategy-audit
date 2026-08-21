# CofiBitStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CofiBitStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 7429 | 20015 |
| expectancy per trade (USDT) | -0.11 | -0.05 |
| mean profit p-value | 1.463e-54 | 1.374e-21 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -79.75 | -96.68 |
| Sharpe | -35.33 | -10.93 |
| Sortino | -33.49 | -10.67 |
| max drawdown % | 80.11 | 96.69 |
| profit factor | 0.47 | 0.7 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-79.75%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.68%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 5 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
