# LorentzianClassification

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `LorentzianClassification (2).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1815 | 8804 |
| average profit per trade % | -0.53 | -0.27 |
| win rate % | 56.1 | 61.5 |
| average trade duration, minutes | 1367.0 | 1292.0 |
| duration measured in own candles | 22.78 | 21.53 |
| expectancy per trade (USDT) | -0.4 | -0.11 |
| mean profit p-value | 1.902e-08 | 0.01496 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -71.99 | -96.67 |
| Sharpe | -6.29 | -1.85 |
| Sortino | -5.83 | -1.56 |
| max drawdown % | 73.13 | 97.93 |
| profit factor | 0.65 | 0.9 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-13.6 pp**, out of sample **-445.3 pp**.

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

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
