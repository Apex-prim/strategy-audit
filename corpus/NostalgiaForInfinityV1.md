# NostalgiaForInfinityV1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NostalgiaForInfinityV1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 769 | 2688 |
| expectancy per trade (USDT) | 0.47 | 0.59 |
| mean profit p-value | 0.0002134 | 0.0001009 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 36.15 | 159.61 |
| Sharpe | 2.7 | 1.63 |
| Sortino | 3.02 | 1.85 |
| max drawdown % | 7.61 | 15.66 |
| profit factor | 1.49 | 1.27 |

**Retained out of sample: 126%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **36.15%**.
Out of sample: buy-and-hold **346.34%** vs strategy **159.61%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `2da4e157b88f` · strategy list `dac6309df791d209`*
