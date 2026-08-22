# TrendRiderStrategy

Source: [`freqtrade/freqtrade-strategies`](https://github.com/freqtrade/freqtrade-strategies) · file `TrendRiderStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2008 | 7937 |
| average profit per trade % | -0.29 | -0.34 |
| win rate % | 23.8 | 23.1 |
| average trade duration, minutes | 312.0 | 308.0 |
| duration measured in own candles | 5.2 | 5.13 |
| expectancy per trade (USDT) | -0.26 | -0.12 |
| mean profit p-value | 5.209e-14 | 1.481e-28 |
| market change % (baseline) | -55.02 | 348.67 |
| strategy total % | -52.06 | -96.59 |
| Sharpe | -8.99 | -8.02 |
| Sortino | -14.78 | -11.73 |
| max drawdown % | 53.4 | 96.59 |
| profit factor | 0.6 | 0.62 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+3.0 pp**, out of sample **-445.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.02%**; the strategy returned **-52.06%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-96.59%** — loses to it.

⚠ **Incomplete coverage:** the engine found no history for BTC/USDT:USDT and computed on the rest. Not comparable to a full-coverage result.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_200 -0.448%, obv -49.801%, obv_ema -55.038% |
| прогрев объявлен | clean | 210 при потребности 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
