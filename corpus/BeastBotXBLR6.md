# BeastBotXBLR6

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `BeastBotXBLR6.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 116 | 519 |
| expectancy per trade (USDT) | 1.48 | 1.95 |
| mean profit p-value | 3.136e-06 | 0.0001986 |
| market change % (baseline) | -59.35 | 346.34 |
| strategy total % | 17.18 | 101.29 |
| Sharpe | 1.39 | 0.69 |
| Sortino | 1.71 | 0.52 |
| max drawdown % | 1.26 | 14.13 |
| profit factor | 3.53 | 1.76 |

**Retained out of sample: 132%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.35%**; the strategy returned **17.18%**.
Out of sample: buy-and-hold **346.34%** vs strategy **101.29%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `2da4e157b88f` · strategy list `dac6309df791d209`*
