# TouchEmaStrategy

Source: [`flaviosiotto/freqtrade-strategy`](https://github.com/flaviosiotto/freqtrade-strategy) · file `touchema-strategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1072 | 4121 |
| expectancy per trade (USDT) | -0.61 | -0.19 |
| mean profit p-value | 1.399e-05 | 0.0004046 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -65.15 | -76.83 |
| Sharpe | -3.74 | -1.84 |
| Sortino | -2.31 | -1.09 |
| max drawdown % | 65.22 | 77.37 |
| profit factor | 0.3 | 0.6 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-65.15%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-76.83%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
