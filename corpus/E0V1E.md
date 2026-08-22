# E0V1E

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `E0V1E.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 39 | 290 |
| average profit per trade % | 2.34 | 3.21 |
| win rate % | 82.1 | 84.1 |
| average trade duration, minutes | 207.0 | 41.0 |
| duration measured in own candles | 41.4 | 8.2 |
| expectancy per trade (USDT) | 3.04 | 7.34 |
| mean profit p-value | 0.0001465 | 5.176e-31 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | 11.87 | 212.84 |
| Sharpe | 0.7 | 1.8 |
| Sortino | 0.81 | 1.38 |
| max drawdown % | 1.89 | 3.32 |
| profit factor | 5.21 | 8.03 |

**Retained out of sample: 241%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+70.3 pp**, out of sample **-133.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **11.87%**.
Out of sample: buy-and-hold **346.34%** vs strategy **212.84%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 12.447%, rsi_fast 0.045%, rsi_slow 12.811% |
| прогрев объявлен | clean | 20 при потребности 20 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
