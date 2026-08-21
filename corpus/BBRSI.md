# bbrsi

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BBRSI.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1201 | 4306 |
| expectancy per trade (USDT) | -0.73 | -0.22 |
| mean profit p-value | 1.533e-07 | 1.093e-06 |
| market change % (baseline) | -58.5 | 340.8 |
| strategy total % | -87.36 | -96.8 |
| Sharpe | -4.82 | -2.59 |
| Sortino | -3.21 | -1.68 |
| max drawdown % | 87.36 | 96.81 |
| profit factor | 0.11 | 0.33 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.5%**; the strategy returned **-87.36%**.
Out of sample: buy-and-hold **340.8%** vs strategy **-96.8%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 4.632% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
