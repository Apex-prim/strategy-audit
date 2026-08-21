# BBRSI21

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BBRSI21.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1375 | 4470 |
| expectancy per trade (USDT) | -0.45 | -0.06 |
| mean profit p-value | 0.0003669 | 0.5272 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -62.37 | -28.44 |
| Sharpe | -3.46 | -0.34 |
| Sortino | -1.97 | -0.19 |
| max drawdown % | 63.59 | 58.77 |
| profit factor | 0.46 | 0.93 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-62.37%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-28.44%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
