# LorentzianClassification

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `LorentzianClassification (2).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1815 | 8804 |
| expectancy per trade (USDT) | -0.4 | -0.11 |
| mean profit p-value | 1.902e-08 | 0.01496 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -71.99 | -96.67 |
| Sharpe | -6.29 | -1.85 |
| Sortino | -5.83 | -1.56 |
| max drawdown % | 73.13 | 97.93 |
| profit factor | 0.65 | 0.9 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-71.99%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-96.67%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 4, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |
| признак утечки будущего | **found** | сдвиг в будущее .shift(-N) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
