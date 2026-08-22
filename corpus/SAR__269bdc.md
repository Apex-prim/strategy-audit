# SAR

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `SAR (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 16632 | 14248 |
| average profit per trade % | -0.16 | -0.19 |
| win rate % | 30.0 | 27.8 |
| average trade duration, minutes | 57.0 | 58.0 |
| duration measured in own candles | 11.4 | 11.6 |
| expectancy per trade (USDT) | -0.06 | -0.07 |
| mean profit p-value | 5.212e-55 | 2.82e-45 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -96.57 | -96.58 |
| Sharpe | -52.92 | -13.68 |
| Sortino | -75.87 | -18.52 |
| max drawdown % | 96.57 | 96.58 |
| profit factor | 0.66 | 0.63 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.2 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: adx -27.315%, rsi 0.935% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
