# Cluc7werk

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Cluc7werk.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 303 | 2018 |
| expectancy per trade (USDT) | -0.71 | -0.44 |
| mean profit p-value | 5.648e-15 | 1.21e-106 |
| market change % (baseline) | -55.61 | 347.94 |
| strategy total % | -21.39 | -89.79 |
| Sharpe | -3.76 | -8.47 |
| Sortino | -6.85 | -11.9 |
| max drawdown % | 21.81 | 89.81 |
| profit factor | 0.33 | 0.19 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-55.61%**; the strategy returned **-21.39%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-89.79%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 48 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
