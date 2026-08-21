# NormalizerStrategy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NormalizerStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 970 | 2777 |
| expectancy per trade (USDT) | -0.65 | -0.33 |
| mean profit p-value | 8.168e-18 | 4.409e-24 |
| market change % (baseline) | -51.25 | 348.67 |
| strategy total % | -63.39 | -92.16 |
| Sharpe | -7.4 | -4.35 |
| Sortino | -8.66 | -4.48 |
| max drawdown % | 63.66 | 92.25 |
| profit factor | 0.44 | 0.4 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-51.25%**; the strategy returned **-63.39%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-92.16%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: pct_sum -33.617% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
