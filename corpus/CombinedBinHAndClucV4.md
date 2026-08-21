# CombinedBinHAndClucV4

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHAndClucV4.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 793 | 2172 |
| expectancy per trade (USDT) | -0.09 | 0.55 |
| mean profit p-value | 0.441 | 7.393e-06 |
| market change % (baseline) | -58.48 | 346.34 |
| strategy total % | -6.81 | 119.13 |
| Sharpe | -0.57 | 1.69 |
| Sortino | -0.65 | 1.52 |
| max drawdown % | 25.05 | 15.68 |
| profit factor | 0.93 | 1.3 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.441 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.48%**; the strategy returned **-6.81%**.
Out of sample: buy-and-hold **346.34%** vs strategy **119.13%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_slow 0.013% |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
