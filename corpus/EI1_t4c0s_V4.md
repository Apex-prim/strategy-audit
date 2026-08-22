# EI1_t4c0s_V4

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `EI1_t4c0s_V4.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 177 | 544 |
| average profit per trade % | -1.78 | -1.07 |
| win rate % | 63.3 | 73.7 |
| average trade duration, minutes | 3971.0 | 3186.0 |
| duration measured in own candles | 66.18 | 53.1 |
| expectancy per trade (USDT) | -1.9 | -1.05 |
| mean profit p-value | 0.0002499 | 0.0005834 |
| market change % (baseline) | -51.52 | 348.67 |
| strategy total % | -33.63 | -56.9 |
| Sharpe | -1.33 | -0.65 |
| Sortino | -1.6 | -0.47 |
| max drawdown % | 33.63 | 60.5 |
| profit factor | 0.44 | 0.55 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+17.9 pp**, out of sample **-405.6 pp**.

Baseline: buy-and-hold on the same pairs returned **-51.52%**; the strategy returned **-33.63%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-56.9%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 6, выходов 7 из 14 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: move_mean -39.562%, move_mean_x -39.562%, exit_mean -1.425%, exit_mean_x -2.232%, enter_mean 1.536% |
| прогрев объявлен | clean | 400 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
