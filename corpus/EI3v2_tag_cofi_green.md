# EI3v2_tag_cofi_green

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `EI3v2_tag_cofi_green.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 738 | 2628 |
| expectancy per trade (USDT) | 0.39 | 3.16 |
| mean profit p-value | 0.05133 | 1.57e-17 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 29.01 | 831.52 |
| Sharpe | 1.39 | 3.56 |
| Sortino | 0.93 | 1.32 |
| max drawdown % | 13.0 | 18.71 |
| profit factor | 1.29 | 2.07 |

**Retained out of sample: 810%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.05133 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **29.01%**.
Out of sample: buy-and-hold **346.34%** vs strategy **831.52%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 400 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
