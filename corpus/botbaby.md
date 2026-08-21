# botbaby

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `botbaby.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2552 | 9786 |
| expectancy per trade (USDT) | -0.23 | -0.1 |
| mean profit p-value | 4.426e-56 | 1.039e-90 |
| market change % (baseline) | -58.41 | 343.26 |
| strategy total % | -58.38 | -93.66 |
| Sharpe | -21.39 | -16.33 |
| Sortino | -73.28 | -26.87 |
| max drawdown % | 58.61 | 93.73 |
| profit factor | 0.52 | 0.59 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-58.38%**.
Out of sample: buy-and-hold **343.26%** vs strategy **-93.66%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **30m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
