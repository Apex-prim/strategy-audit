# ForexSignal

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ForexSignal.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 13660 | 12656 |
| expectancy per trade (USDT) | -0.07 | -0.08 |
| mean profit p-value | 8.04e-76 | 6.5e-69 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -96.57 | -96.57 |
| Sharpe | -56.72 | -16.06 |
| Sortino | -85.53 | -23.38 |
| max drawdown % | 96.57 | 96.59 |
| profit factor | 0.58 | 0.56 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 21 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
