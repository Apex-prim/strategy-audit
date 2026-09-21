---
name: Audit a strategy
about: Ask for a strategy to be run through the same pipeline as the 895
title: "Audit: <strategy name>"
labels: audit-request
---

**Link to the strategy file** (a public URL to the `.py`, or a repository):

**Declared timeframe** (from the file, e.g. `5m`):

**Anything the file does not carry** — `minimal_roi`, `max_open_trades`, a
config the author published alongside it. If nothing, say so; the audit will
note the gap rather than guess.

---

What you will get back: both windows, p-value, buy-and-hold baseline, cost
sensitivity, both of freqtrade's own bias detectors, and the static auditor's
reading — as a card in `results/`, with the ledger row behind it.

What you will not get: a verdict on whether the idea is good. Every check here
is about whether the *measurement* can be trusted.

Before opening this, you can run it yourself:

```bash
python foreign_strategy_audit.py --root path/to/strategy --lang en   # seconds, static
python harness.py                                                    # minutes, runs the code
```
