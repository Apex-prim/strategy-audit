# SlowPotato

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `SlowPotato.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 104 | 1578 |
| expectancy per trade (USDT) | -4.76 | 0.29 |
| mean profit p-value | 0.03195 | 0.501 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -49.55 | 45.31 |
| Sharpe | -0.58 | 0.22 |
| Sortino | -0.55 | 0.03 |
| max drawdown % | 53.89 | 54.45 |
| profit factor | 0.16 | 1.26 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-49.55%**.
Out of sample: buy-and-hold **346.34%** vs strategy **45.31%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
