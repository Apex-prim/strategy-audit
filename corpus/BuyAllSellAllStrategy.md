# BuyAllSellAllStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `BuyAllSellAllStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 13533 | 13509 |
| expectancy per trade (USDT) | -0.07 | -0.07 |
| mean profit p-value | 0.0 | 0.0 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -96.57 | -96.57 |
| Sharpe | -397.29 | -122.9 |
| Sortino | -397.29 | -122.9 |
| max drawdown % | 96.57 | 96.57 |
| profit factor | 0.0 | 0.0 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 14, выходов 9 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
