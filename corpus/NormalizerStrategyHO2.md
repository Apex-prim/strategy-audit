# NormalizerStrategyHO2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NormalizerStrategyHO2 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 819 | 2330 |
| expectancy per trade (USDT) | -0.48 | -0.15 |
| mean profit p-value | 0.0008315 | 0.1775 |
| market change % (baseline) | -51.25 | 348.67 |
| strategy total % | -39.02 | -35.85 |
| Sharpe | -2.6 | -0.53 |
| Sortino | -4.94 | -0.99 |
| max drawdown % | 43.14 | 54.68 |
| profit factor | 0.73 | 0.92 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-51.25%**; the strategy returned **-39.02%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-35.85%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: pct_sum -33.617% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
