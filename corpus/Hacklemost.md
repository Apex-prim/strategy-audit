# Hacklemost

Source: [`werkkrew/freqtrade-strategies`](https://github.com/werkkrew/freqtrade-strategies) · file `Hacklemost.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 12 | 176 |
| expectancy per trade (USDT) | 2.78 | 1.55 |
| mean profit p-value | 0.00433 | 0.006265 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | 3.33 | 27.37 |
| Sharpe | 0.34 | 0.3 |
| Sortino | -100.0 | 5.74 |
| max drawdown % | 0.0 | 8.45 |
| profit factor | 0.0 | 2.52 |

**Retained out of sample: 56%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **3.33%**.
Out of sample: buy-and-hold **346.34%** vs strategy **27.37%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 48 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
