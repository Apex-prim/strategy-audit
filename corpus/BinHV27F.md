# BinHV27F

Source: [`eovie/freqtrade_strs`](https://github.com/eovie/freqtrade_strs) · file `BinHV27F.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2571 | 8957 |
| expectancy per trade (USDT) | -0.15 | -0.08 |
| mean profit p-value | 0.0001062 | 0.01234 |
| market change % (baseline) | -59.21 | 346.34 |
| strategy total % | -39.84 | -73.98 |
| Sharpe | -5.15 | -1.92 |
| Sortino | -5.19 | -1.7 |
| max drawdown % | 46.73 | 83.2 |
| profit factor | 0.78 | 0.88 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

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

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
