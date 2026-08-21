# eltoro1_4_simple

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `eltoro1_4_simple.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 496 | 1921 |
| expectancy per trade (USDT) | -1.29 | -0.27 |
| mean profit p-value | 0.0006008 | 0.2491 |
| market change % (baseline) | -59.09 | 345.85 |
| strategy total % | -64.13 | -51.7 |
| Sharpe | -2.01 | -0.41 |
| Sortino | -2.62 | -0.47 |
| max drawdown % | 64.45 | 63.65 |
| profit factor | 0.62 | 0.92 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.09%**; the strategy returned **-64.13%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-51.7%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: INFEWO_4h -1.742%, BTC_EWO_Fast_4h -1.742%, rsi -0.238%, rsi_ma -0.280%, rsi_ma_pcnt -7.901% |
| прогрев занижен | **found** | объявлено 79, нужно не менее 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
