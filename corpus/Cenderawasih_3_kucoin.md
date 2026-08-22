# Cenderawasih_3_kucoin

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `Cenderawasih_3_kucoin.py`

## Could not be measured

```
Impossible to load Strategy 'Cenderawasih_3_kucoin'. This class does not exist or contains Python code errors.
```

Declared timeframe: `5m`. This is a named cause, not a verdict on the strategy — see the note on buckets in [../BASELINE.md](../BASELINE.md).

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Impossible to load Strategy 'Cenderawasih_3_kucoin'. This class does not exist or contains Python code errors. |
| indicator recursion (freqtrade's own `recursive-analysis`) | could not run | Impossible to load Strategy 'Cenderawasih_3_kucoin'. This class does not exist or contains Python code errors. |
| прогрев объявлен | clean | 200 при потребности 72 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
