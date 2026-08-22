# MacheteV8bRallimod

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `MacheteV8bRallimod.py`

## Could not be measured

```
TypeError: IStrategy.min_roi_reached_entry() missing 2 required positional arguments: 'trade_dur' and 'current_time'
```

Declared timeframe: `15m`. This is a named cause, not a verdict on the strategy — see the note on buckets in [../BASELINE.md](../BASELINE.md).

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: macd 0.458%, plus_di 0.021%, minus_di -0.015%, EWO -46.056%, ema100 0.019% |
| прогрев объявлен | clean | 500 при потребности 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
