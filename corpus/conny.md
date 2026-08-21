# conny

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `conny.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1484 | 4341 |
| expectancy per trade (USDT) | -0.22 | -0.11 |
| mean profit p-value | 1.218e-08 | 5.475e-06 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -32.36 | -48.3 |
| Sharpe | -5.78 | -2.43 |
| Sortino | -10.7 | -4.07 |
| max drawdown % | 33.33 | 49.73 |
| profit factor | 0.69 | 0.81 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-32.36%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-48.3%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: consensus_sell -42.857% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
