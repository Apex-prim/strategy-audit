# ichiV1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `IchisV1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3208 | 10241 |
| average profit per trade % | 1.16 | 1.18 |
| win rate % | 74.5 | 72.3 |
| average trade duration, minutes | 60.0 | 56.0 |
| duration measured in own candles | 12.0 | 11.2 |
| expectancy per trade (USDT) | 30.5 | 18260.99 |
| mean profit p-value | 8.266e-89 | 2.562e-152 |
| market change % (baseline) | -58.84 | 346.34 |
| strategy total % | 9785.43 | 18701080.18 |
| Sharpe | 30.57 | 21.89 |
| Sortino | 37.1 | 28.6 |
| max drawdown % | 1.45 | 1.03 |
| profit factor | 5.07 | 5.16 |

**Retained out of sample: 59872%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+9844.3 pp**, out of sample **+18700733.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.84%**; the strategy returned **9785.43%**.
Out of sample: buy-and-hold **346.34%** vs strategy **18701080.18%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 7, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: trend_open_6h -0.013%, trend_open_8h -0.013% |
| прогрев объявлен | clean | 96 при потребности 96 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
