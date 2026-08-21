# TRIWAVE

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `TRIWAVE.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 730 | 2894 |
| expectancy per trade (USDT) | -1.11 | -0.27 |
| mean profit p-value | 4.887e-07 | 0.06018 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -80.95 | -77.47 |
| Sharpe | -3.59 | -0.82 |
| Sortino | -2.84 | -0.48 |
| max drawdown % | 81.04 | 87.98 |
| profit factor | 0.42 | 0.85 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-80.95%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-77.47%** — loses to it.

⚠ **Incomplete coverage:** the engine found no history for ADA/USDT, BTC/USDT, DASH/USDT, ETH/USDT, LTC/USDT, XLM/USDT, XRP/USDT and computed on the rest. Not comparable to a full-coverage result.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: wave_t1 -70.611%, wave_t2 -517.012%, t1_pc 266.228%, rsi -0.375%, rsi_ma -0.515% |
| прогрев занижен | **found** | объявлено 30, нужно не менее 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
