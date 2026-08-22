# UziChan2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `UziChan2 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11400 | 12961 |
| average profit per trade % | -0.24 | -0.21 |
| win rate % | 20.2 | 20.6 |
| average trade duration, minutes | 14.0 | 16.0 |
| duration measured in own candles | 14.0 | 16.0 |
| expectancy per trade (USDT) | -0.08 | -0.07 |
| mean profit p-value | 4.577e-226 | 6.08e-120 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -96.57 | -96.57 |
| Sharpe | -91.64 | -21.67 |
| Sortino | -88.3 | -20.6 |
| max drawdown % | 96.57 | 96.57 |
| profit factor | 0.16 | 0.21 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-41.0 pp**, out of sample **-444.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
