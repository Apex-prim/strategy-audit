# FrayLIVEBTC15m

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FrayLIVEBTC15m.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1015 | 3732 |
| expectancy per trade (USDT) | -0.72 | -0.24 |
| mean profit p-value | 0.0002412 | 0.04952 |
| market change % (baseline) | -58.84 | 345.85 |
| strategy total % | -73.09 | -88.51 |
| Sharpe | -3.07 | -0.97 |
| Sortino | -1.56 | -0.36 |
| max drawdown % | 73.26 | 93.31 |
| profit factor | 0.5 | 0.82 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.84%**; the strategy returned **-73.09%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-88.51%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 1 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -1.584%, frsi 13.618%, macd 25828.480%, macdsignal -308.147%, macdn 16.676% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
