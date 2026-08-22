# Auto_EI_t4c0s

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `Auto_EI_t4c0s.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 147 | 241 |
| average profit per trade % | -1.21 | -0.48 |
| win rate % | 87.1 | 93.4 |
| average trade duration, minutes | 1525.0 | 555.0 |
| duration measured in own candles | 305.0 | 111.0 |
| expectancy per trade (USDT) | -1.39 | -0.67 |
| mean profit p-value | 0.004866 | 0.1178 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | -20.41 | -16.21 |
| Sharpe | -0.91 | -0.2 |
| Sortino | -2.29 | -0.17 |
| max drawdown % | 20.9 | 28.15 |
| profit factor | 0.34 | 0.57 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+38.6 pp**, out of sample **-362.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **-20.41%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-16.21%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 10, выходов 13 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: HMA_SQZ -1.232%, EWO -12.317%, EWO_UP -12.317%, EWO_MEAN_UP -87.218%, EWO_UP_FIB -87.218% |
| прогрев объявлен | clean | 200 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
