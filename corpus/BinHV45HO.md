# BinHV45HO

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BinHV45HO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 32 | 357 |
| expectancy per trade (USDT) | 1.58 | -0.14 |
| mean profit p-value | 4.195e-58 | 0.7039 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | 5.07 | -5.08 |
| Sharpe | 55.7 | -0.06 |
| Sortino | -100.0 | -0.19 |
| max drawdown % | 0.0 | 24.36 |
| profit factor | 0.0 | 0.92 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **5.07%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-5.08%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
