# ElliotV5HO

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ElliotV5HO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 143 | 667 |
| average profit per trade % | 0.57 | 0.77 |
| win rate % | 70.6 | 75.4 |
| average trade duration, minutes | 50.0 | 44.0 |
| duration measured in own candles | 10.0 | 8.8 |
| expectancy per trade (USDT) | 0.74 | 1.31 |
| mean profit p-value | 0.0001402 | 1.011e-14 |
| market change % (baseline) | -58.45 | 346.34 |
| strategy total % | 10.52 | 87.49 |
| Sharpe | 1.23 | 1.66 |
| Sortino | 1.55 | 1.47 |
| max drawdown % | 1.86 | 5.32 |
| profit factor | 2.24 | 2.38 |

**Retained out of sample: 177%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+69.0 pp**, out of sample **-258.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.45%**; the strategy returned **10.52%**.
Out of sample: buy-and-hold **346.34%** vs strategy **87.49%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.205% |
| прогрев объявлен | clean | 79 при потребности 20 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
