# ClucFiatSlow

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ClucFiatSlow.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1292 | 4734 |
| expectancy per trade (USDT) | -0.26 | 0.44 |
| mean profit p-value | 0.1486 | 0.08502 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | -33.61 | 206.7 |
| Sharpe | -1.36 | 0.96 |
| Sortino | -0.65 | 0.4 |
| max drawdown % | 38.26 | 60.85 |
| profit factor | 0.77 | 1.19 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1486 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-33.61%**.
Out of sample: buy-and-hold **346.34%** vs strategy **206.7%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_slow 0.012%, rsi 0.110% |
| прогрев не объявлен | **found** | самый длинный индикатор 48 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
