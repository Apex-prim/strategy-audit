# ElliotV5HOMod2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ElliotV5HOMod2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 81 | 413 |
| average profit per trade % | 2.11 | 2.05 |
| win rate % | 100.0 | 99.5 |
| average trade duration, minutes | 4546.0 | 4895.0 |
| duration measured in own candles | 909.2 | 979.0 |
| expectancy per trade (USDT) | 2.89 | 4.48 |
| mean profit p-value | 5.428e-39 | 1.462e-07 |
| market change % (baseline) | -58.45 | 346.34 |
| strategy total % | 23.42 | 185.18 |
| Sharpe | 5.82 | 0.88 |
| Sortino | -100.0 | 0.23 |
| max drawdown % | 0.0 | 13.67 |
| profit factor | 0.0 | 5.1 |

**Retained out of sample: 155%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+81.9 pp**, out of sample **-161.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.45%**; the strategy returned **23.42%**.
Out of sample: buy-and-hold **346.34%** vs strategy **185.18%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.205%, rsi_slow 0.977% |
| прогрев объявлен | clean | 79 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
