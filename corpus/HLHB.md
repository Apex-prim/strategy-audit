# hlhb

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `hlhb.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 188 | 673 |
| expectancy per trade (USDT) | -1.14 | -0.24 |
| mean profit p-value | 0.04555 | 0.3125 |
| market change % (baseline) | -58.5 | 340.8 |
| strategy total % | -21.51 | -16.05 |
| Sharpe | -0.73 | -0.21 |
| Sortino | -0.48 | -0.14 |
| max drawdown % | 23.35 | 30.24 |
| profit factor | 0.52 | 0.85 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.5%**; the strategy returned **-21.51%**.
Out of sample: buy-and-hold **340.8%** vs strategy **-16.05%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 3.804%, adx 115.767% |
| прогрев не объявлен | **found** | самый длинный индикатор 10 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
