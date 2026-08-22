# NWEv6

Source: [`anakein/beastbotXB`](https://github.com/anakein/beastbotXB) · file `NWEv6.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2032 | 6347 |
| average profit per trade % | -0.37 | -0.35 |
| win rate % | 65.1 | 65.1 |
| average trade duration, minutes | 436.0 | 470.0 |
| duration measured in own candles | 87.2 | 94.0 |
| expectancy per trade (USDT) | -0.31 | -0.15 |
| mean profit p-value | 2.002e-10 | 8.065e-17 |
| market change % (baseline) | -59.35 | 346.34 |
| strategy total % | -61.98 | -94.16 |
| Sharpe | -7.56 | -5.38 |
| Sortino | -8.93 | -4.85 |
| max drawdown % | 62.57 | 94.3 |
| profit factor | 0.68 | 0.71 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-2.6 pp**, out of sample **-440.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.35%**; the strategy returned **-61.98%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-94.16%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 9, выходов 7 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: btctrend -200.000% |
| прогрев не объявлен | **found** | самый длинный индикатор 500 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
