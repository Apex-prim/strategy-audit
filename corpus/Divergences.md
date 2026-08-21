# Divergences

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Divergences.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2487 | 7494 |
| expectancy per trade (USDT) | -0.3 | -0.12 |
| mean profit p-value | 3.953e-22 | 6.77e-12 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -74.05 | -91.23 |
| Sharpe | -12.76 | -4.81 |
| Sortino | -15.94 | -5.86 |
| max drawdown % | 74.62 | 91.37 |
| profit factor | 0.48 | 0.7 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-74.05%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-91.23%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: adx 125.955%, rsi 4.044% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
