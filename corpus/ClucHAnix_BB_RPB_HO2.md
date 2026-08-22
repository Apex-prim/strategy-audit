# ClucHAnix_BB_RPB_HO2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ClucHAnix_BB_RPB_HO2.py`

## Could not be measured

```
numpy._core._exceptions._ArrayMemoryError: Unable to allocate 337. MiB for an array with shape (48, 920831) and data type float64
```

Declared timeframe: `1m`. This is a named cause, not a verdict on the strategy — see the note on buckets in [../BASELINE.md](../BASELINE.md).

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO 66.246% |
| прогрев объявлен | clean | 200 при потребности 168 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.3207 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
