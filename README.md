# Out-of-sample audit of a public "strategies that work" repository

An independent replication of the five freqtrade strategies published in
[`paulcpk/freqtrade-strategies-that-work`](https://github.com/paulcpk/freqtrade-strategies-that-work),
tested on 6.5 years of data the original author never saw.

**Headline: all five degrade out of sample. On average about 15% of the reported
per-trade edge survives. Two of the five go to zero or below.**

```
                                in-sample     out-of-sample   trades    survives
DoubleEMACrossoverWithTrend       +0.38%         +0.11%        4043        29%
MACDCrossoverWithTrend            +0.36%         +0.01%        1436         3%
RSIDirectionalWithTrend           +0.35%         -0.08%         757      negative
RSIDirectionalWithTrendSlow       +1.01%         +0.19%         545        19%
EMAPriceCrossoverWithThreshold    +1.17%         +0.51%        1812        44%
```

In-sample window is the author's: 2018-03-01 … 2020-03-01, 1h, 8 USDT pairs.
Out-of-sample: 2020-03-01 … 2026-08-20, same code, same pairs, 0.1% fee per side.

Full write-up: **[ANALYSIS.md](ANALYSIS.md)** · [на русском](ANALYSIS.ru.md)

---

## This is not a takedown

The author labels the repository experimental and educational, publishes the
code in full, and hides nothing. Nothing here suggests bad faith. The point is
what a reader takes from a results table — not what the author did.

## What the audit checked

| Check | Result |
|---|---|
| Replication of the published numbers | all five within an order of magnitude |
| Look-ahead bias | **none found** — looked for it specifically |
| Reproducibility of the headline figure | **fails** — no config is published |
| Indicator warm-up declaration | `startup_candle_count` absent in 5/5 files |
| Filter interaction | one of two exits is unreachable by construction |
| Fee sensitivity | 0.1% per side = 0.20 pp of average trade |
| Walk-forward | not performed by the author; performed here |

## Reproduce it yourself

```bash
pip install -r requirements.txt
python fetch_data.py      # ~74k hourly candles per pair from Binance public data
python replicate.py       # in-sample, out-of-sample, fee sensitivity
```

No API key required — the data comes from Binance's public data mirror.
Nothing here talks to an exchange account.

Expect roughly 15 minutes for the download and 2 minutes for the run.

## What is deliberately *not* in this repository

- **The price data.** 48 MB that anyone can re-download. Publishing the fetch
  script instead is both lighter and better science: you get the data yourself
  rather than trusting mine.
- **Any configuration, key, or host.** The audit touches no account and no
  server. `tools/secret_gate.py` is a pre-commit gate that refuses a commit
  containing a private key, token, or credentials — with a self-test and a
  deliberate-sabotage check that plants three real-shaped secrets and requires
  the gate to catch all three.

## Method, briefly

Strategies were re-implemented in pandas under freqtrade's execution model — a
signal on candle `i` fills at the **open of candle `i+1`** — with TA-Lib-faithful
indicators (SMA-seeded EMA, Wilder's RSI). Stops and trailing stops are checked
intra-candle against the low. One open position per pair.

The replication is not freqtrade itself, so trade counts differ from the
author's by +3% to +47%; the most likely cause is `max_open_trades`, which is
not published. Every caveat is listed in the analysis rather than omitted.

## An error I made, and kept

The first run produced 18 trades for `RSIDirectionalWithTrendSlow` against the
author's 108 — an 8× gap that would have made a persuasive "does not reproduce"
headline. It was my bug: I had assumed RSI thresholds of 15/85 by analogy with
the neighbouring strategy, where the file actually uses 25/20. After the fix
that strategy reproduces better than the rest.

It stays in the write-up on purpose. An unexplained anomaly is not a finding —
it is a thing to go and check, and more often than not it is yours.

## Licence

MIT for the code. The analysis text may be quoted freely with attribution.
