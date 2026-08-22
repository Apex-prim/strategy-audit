# E0V1E_ewo

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `E0V1E_ewo.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 40 | 269 |
| average profit per trade % | 2.06 | 2.3 |
| win rate % | 97.5 | 93.3 |
| average trade duration, minutes | 92.0 | 41.0 |
| duration measured in own candles | 18.4 | 8.2 |
| expectancy per trade (USDT) | 2.67 | 4.17 |
| mean profit p-value | 2.319e-05 | 3.867e-09 |
| market change % (baseline) | -58.87 | 346.34 |
| strategy total % | 10.67 | 112.12 |
| Sharpe | 0.81 | 0.81 |
| Sortino | -100.0 | 0.49 |
| max drawdown % | 1.22 | 12.76 |
| profit factor | 9.53 | 3.27 |

**Retained out of sample: 156%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+69.5 pp**, out of sample **-234.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.87%**; the strategy returned **10.67%**.
Out of sample: buy-and-hold **346.34%** vs strategy **112.12%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi_slow -0.034% |
| прогрев объявлен | clean | 120 при потребности 20 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
