# ichiV1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `IchisV1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3208 | 10241 |
| expectancy per trade (USDT) | 30.5 | 18260.99 |
| mean profit p-value | 8.266e-89 | 2.562e-152 |
| market change % (baseline) | -58.84 | 346.34 |
| strategy total % | 9785.43 | 18701080.18 |
| Sharpe | 30.57 | 21.89 |
| Sortino | 37.1 | 28.6 |
| max drawdown % | 1.45 | 1.03 |
| profit factor | 5.07 | 5.16 |

**Retained out of sample: 59872%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

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

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
