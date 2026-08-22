# UziChan

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `UziChan.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 10667 | 14372 |
| average profit per trade % | -0.25 | -0.19 |
| win rate % | 35.5 | 46.3 |
| average trade duration, minutes | 65.0 | 60.0 |
| duration measured in own candles | 13.0 | 12.0 |
| expectancy per trade (USDT) | -0.09 | -0.07 |
| mean profit p-value | 7.214e-69 | 6.479e-47 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -96.57 | -96.6 |
| Sharpe | -47.69 | -14.0 |
| Sortino | -43.5 | -11.5 |
| max drawdown % | 96.57 | 96.61 |
| profit factor | 0.36 | 0.48 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.3 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.6%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
