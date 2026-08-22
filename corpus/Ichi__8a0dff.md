# Ichi

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Example_Strat_With_FileLogging.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3630 | 11067 |
| average profit per trade % | -0.38 | -0.23 |
| win rate % | 74.6 | 76.1 |
| average trade duration, minutes | 784.0 | 887.0 |
| duration measured in own candles | 52.27 | 59.13 |
| expectancy per trade (USDT) | -0.23 | -0.09 |
| mean profit p-value | 1.03e-10 | 4.84e-09 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -84.17 | -96.71 |
| Sharpe | -10.21 | -4.98 |
| Sortino | -5.36 | -2.5 |
| max drawdown % | 84.22 | 96.75 |
| profit factor | 0.27 | 0.47 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-26.1 pp**, out of sample **-442.6 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-84.17%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.71%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 55 свечей, startup_candle_count не задан (по умолчанию 0) |
| признак утечки будущего | **found** | сдвиг в будущее .shift(-N) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
