# SwingHighToSky

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `SwingHighToSky.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1303 | 4802 |
| expectancy per trade (USDT) | -0.6 | -0.15 |
| mean profit p-value | 8.978e-06 | 0.0944 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -78.47 | -72.82 |
| Sharpe | -4.21 | -0.94 |
| Sortino | -2.49 | -0.56 |
| max drawdown % | 78.51 | 85.86 |
| profit factor | 0.31 | 0.81 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-78.47%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-72.82%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
