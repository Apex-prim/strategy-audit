# RSIv2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `RSIv2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1327 | 4581 |
| expectancy per trade (USDT) | -0.45 | -0.16 |
| mean profit p-value | 3.191e-05 | 0.003419 |
| market change % (baseline) | -58.34 | 345.85 |
| strategy total % | -59.13 | -72.29 |
| Sharpe | -3.98 | -1.6 |
| Sortino | -2.22 | -0.79 |
| max drawdown % | 60.94 | 76.34 |
| profit factor | 0.58 | 0.8 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.34%**; the strategy returned **-59.13%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-72.29%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi_30m -10.757%, rsi 3.688% |
| прогрев объявлен | clean | 20 при потребности 14 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
