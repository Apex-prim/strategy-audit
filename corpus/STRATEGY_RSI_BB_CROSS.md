# STRATEGY_RSI_BB_CROSS

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `STRATEGY_RSI_BB_CROSS.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4897 | 11930 |
| expectancy per trade (USDT) | -0.15 | -0.08 |
| mean profit p-value | 2.992e-09 | 7.013e-12 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | -71.63 | -96.66 |
| Sharpe | -10.89 | -6.06 |
| Sortino | -8.21 | -4.23 |
| max drawdown % | 71.76 | 96.7 |
| profit factor | 0.74 | 0.75 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-71.63%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.66%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 12.447%, rsi_percent 63.577%, bb_minus_rsi_percent 53.196% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
