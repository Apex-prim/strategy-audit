# FAdxSmaStrategy

Source: [`freqtrade/freqtrade-strategies`](https://github.com/freqtrade/freqtrade-strategies) · file `FAdxSmaStrategy.py`

## Could not be measured

```
ImportError: Short strategies cannot run in spot markets. Please make sure that this is the correct strategy and that your trading mode configuration is correct
```

Declared timeframe: `1h`. This is a named cause, not a verdict on the strategy — see the note on buckets in [../BASELINE.md](../BASELINE.md).

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | could not run | Fatal exception! |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `2da4e157b88f` · strategy list `dac6309df791d209`*
