# Obelisk_TradePro_Ichi_v2_1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Obelisk_TradePro_Ichi_v2_1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1303 | 5116 |
| average profit per trade % | 0.39 | 0.17 |
| win rate % | 60.8 | 56.2 |
| average trade duration, minutes | 1105.0 | 1186.0 |
| duration measured in own candles | 18.42 | 19.77 |
| expectancy per trade (USDT) | 0.59 | 0.27 |
| mean profit p-value | 0.005324 | 0.1012 |
| market change % (baseline) | -56.47 | 348.67 |
| strategy total % | 77.42 | 140.66 |
| Sharpe | 2.66 | 0.95 |
| Sortino | 4.82 | 1.58 |
| max drawdown % | 21.71 | 35.05 |
| profit factor | 1.19 | 1.05 |

**Retained out of sample: 46%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+133.9 pp**, out of sample **-208.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-56.47%**; the strategy returned **77.42%**.
Out of sample: buy-and-hold **348.67%** vs strategy **140.66%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 180 при потребности 28 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
