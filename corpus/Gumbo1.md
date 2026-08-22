# Gumbo1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `gumbo1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 10024 | 13558 |
| average profit per trade % | -0.26 | -0.19 |
| win rate % | 52.0 | 60.1 |
| average trade duration, minutes | 136.0 | 125.0 |
| duration measured in own candles | 27.2 | 25.0 |
| expectancy per trade (USDT) | -0.1 | -0.07 |
| mean profit p-value | 3.633e-40 | 1.943e-16 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | -96.56 | -96.64 |
| Sharpe | -34.92 | -7.76 |
| Sortino | -28.27 | -5.37 |
| max drawdown % | 96.57 | 96.68 |
| profit factor | 0.48 | 0.59 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-37.5 pp**, out of sample **-443.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **-96.56%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.64%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 200 при потребности 80 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
