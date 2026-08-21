# CombinedBinHAndClucHyperV0

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `CombinedBinHAndClucHyperV0.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 733 | 3519 |
| expectancy per trade (USDT) | -0.15 | -0.13 |
| mean profit p-value | 0.119 | 0.004788 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -10.67 | -45.37 |
| Sharpe | -1.11 | -1.35 |
| Sortino | -0.93 | -1.1 |
| max drawdown % | 16.07 | 55.3 |
| profit factor | 0.82 | 0.83 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.119 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-10.67%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-45.37%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
