# E0V1E_DCA3

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `E0V1E_DCA3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 338 | 1814 |
| average profit per trade % | 1.13 | 1.36 |
| win rate % | 87.9 | 87.3 |
| average trade duration, minutes | 52.0 | 38.0 |
| duration measured in own candles | 10.4 | 7.6 |
| expectancy per trade (USDT) | 0.96 | 2.92 |
| mean profit p-value | 1.401e-12 | 6.037e-30 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | 32.5 | 529.1 |
| Sharpe | 3.55 | 3.99 |
| Sortino | 2.23 | 2.19 |
| max drawdown % | 3.25 | 6.8 |
| profit factor | 3.48 | 2.78 |

**Retained out of sample: 304%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+90.9 pp**, out of sample **+182.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **32.5%**.
Out of sample: buy-and-hold **346.34%** vs strategy **529.1%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 12.447%, rsi_fast 0.045%, rsi_slow 12.811% |
| прогрев объявлен | clean | 20 при потребности 20 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
