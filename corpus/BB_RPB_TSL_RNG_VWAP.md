# BB_RPB_TSL_RNG_VWAP

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BB_RPB_TSL_RNG_VWAP.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 244 | 1045 |
| expectancy per trade (USDT) | 1.66 | 0.95 |
| mean profit p-value | 7.62e-16 | 0.0002899 |
| market change % (baseline) | -58.87 | 346.34 |
| strategy total % | 40.39 | 99.52 |
| Sharpe | 3.54 | 0.95 |
| Sortino | 4.63 | 0.81 |
| max drawdown % | 2.35 | 19.23 |
| profit factor | 3.99 | 1.57 |

**Retained out of sample: 57%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.87%**; the strategy returned **40.39%**.
Out of sample: buy-and-hold **346.34%** vs strategy **99.52%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: srsi_fk 0.167%, srsi_fd 0.077%, ema_100 0.011%, rsi_slow -0.034%, rsi_84 -2.915% |
| прогрев объявлен | clean | 120 при потребности 112 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
