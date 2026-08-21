# custom

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `custom.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4 | 16 |
| expectancy per trade (USDT) | 1.05 | 1.06 |
| mean profit p-value | 0.09184 | 0.3203 |
| market change % (baseline) | -58.85 | 346.34 |
| strategy total % | 0.42 | 1.7 |
| Sharpe | 0.15 | 0.03 |
| Sortino | -100.0 | -100.0 |
| max drawdown % | 0.0 | 1.38 |
| profit factor | 0.0 | 2.23 |

**Retained out of sample: 101%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.09184 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.85%**; the strategy returned **0.42%**.
Out of sample: buy-and-hold **346.34%** vs strategy **1.7%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: osc -0.033%, min -0.033%, prevMin -0.033%, max -0.058%, prevMax -0.075% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
