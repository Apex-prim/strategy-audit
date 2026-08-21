# ReinforcedQuickie

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ReinforcedQuickie.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 5080 | 18998 |
| expectancy per trade (USDT) | -0.15 | -0.05 |
| mean profit p-value | 3.172e-14 | 3.331e-09 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -73.77 | -95.91 |
| Sharpe | -14.18 | -6.6 |
| Sortino | -11.86 | -4.8 |
| max drawdown % | 74.7 | 96.25 |
| profit factor | 0.71 | 0.85 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-73.77%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-95.91%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 30 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
