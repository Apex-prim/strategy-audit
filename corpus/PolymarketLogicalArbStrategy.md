# PolymarketLogicalArbStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `PolymarketLogicalArbStrategy.py`

## Could not be measured

```
FileNotFoundError: Could not find pair source at './strategy/PolymarketLogicalArb/freqtrade_pair_mapping.csv'. Update PAIR_SOURCE_PATH in the strategy.
```

Declared timeframe: `4h`. This is a named cause, not a verdict on the strategy — see the note on buckets in [../BASELINE.md](../BASELINE.md).

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | could not run | Fatal exception! |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
