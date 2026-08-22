# BinHV27F

Source: [`eovie/freqtrade_strs`](https://github.com/eovie/freqtrade_strs) · file `BinHV27F.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2571 | 8957 |
| average profit per trade % | -0.15 | -0.1 |
| win rate % | 55.8 | 57.1 |
| average trade duration, minutes | 315.0 | 297.0 |
| duration measured in own candles | 63.0 | 59.4 |
| expectancy per trade (USDT) | -0.15 | -0.08 |
| mean profit p-value | 0.0001062 | 0.01234 |
| market change % (baseline) | -59.21 | 346.34 |
| strategy total % | -39.84 | -73.98 |
| Sharpe | -5.15 | -1.92 |
| Sortino | -5.19 | -1.7 |
| max drawdown % | 46.73 | 83.2 |
| profit factor | 0.78 | 0.88 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+19.4 pp**, out of sample **-420.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.21%**; the strategy returned **-39.84%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-73.98%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: trend 134446.967% |
| прогрев объявлен | clean | 240 при потребности 240 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
