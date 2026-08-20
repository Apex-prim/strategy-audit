# Out-of-sample audit of a public "strategies that work" repository

An independent replication of the five freqtrade strategies published in
[`paulcpk/freqtrade-strategies-that-work`](https://github.com/paulcpk/freqtrade-strategies-that-work),
tested on 6.5 years of data the original author never saw.

**Headline: all five degrade out of sample. Two retain under 10% of their
edge, one turns negative.**

Measured with **freqtrade itself** — not a re-implementation — and reported as
**expectancy per trade**, because "Total profit %" depends on `max_open_trades`
and stake sizing, i.e. on a configuration the authors did not publish.

```
                                in-sample   out-of-sample   survives
EMAPriceCrossoverWithThreshold     1.63          0.90          55%
DoubleEMACrossoverWithTrend        0.49          0.22          45%
MACDCrossoverWithTrend             0.53          0.03           6%
RSIDirectionalWithTrendSlow        1.13          0.06           5%
RSIDirectionalWithTrend            0.42         -0.09       negative
```

In-sample window is the authors': 2018-03-01 … 2020-03-01, 1h, 8 USDT pairs.
Out-of-sample: 2020-03-01 … 2026-08-20, same code, same pairs, 0.1% fee per side.

Per-strategy cards: **[results/INDEX.md](results/INDEX.md)**
Full write-up: **[ANALYSIS.md](ANALYSIS.md)** · [на русском](ANALYSIS.ru.md)

---

## This is not a takedown

The author labels the repository experimental and educational, publishes the
code in full, and hides nothing. Nothing here suggests bad faith. The point is
what a reader takes from a results table — not what the author did.

## What the audit checked

| Check | Result |
|---|---|
| Replication with freqtrade itself | trade counts land near the authors' (303 vs 300) |
| Look-ahead bias (`lookahead-analysis`) | **none found** — the engine's own detector agrees |
| Indicator warm-up (`recursive-analysis`) | engine **refuses to run**: `startup_candle_count` is 0 in 5/5 |
| Statistical significance | `Mean profit p-value` reported per strategy; one is 0.13 in-sample |
| Baseline | `Market change` — buy-and-hold on the same pairs, reported alongside |
| Reproducibility of the headline figure | **fails** — no config is published |
| Filter interaction | one of two exits is unreachable by construction |
| Cost sensitivity | fee 0.0 / 0.1 / 0.2% per side |
| Out-of-sample test | 6.5 years the authors never saw |

> **Terminology, stated precisely:** this is an *out-of-sample test*, not a
> walk-forward analysis. Walk-forward means rolling or anchored windows with
> re-fitting at each step. An earlier version of this README used the wrong
> word; it is corrected here rather than quietly edited away.

**Auditing your own strategy?** → **[CHECKLIST.md](CHECKLIST.md)** — nine
mechanical questions, each tied to a defect actually found here.

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

---

## Get in touch

- **Want your strategy audited the same way?** Open an issue in this repository
  with a link to the code, or run `harness.py` yourself — it is the exact
  pipeline used here, not a demo of one.
- **Found an error in this audit?** Open an issue. Errors found in this
  repository get published in it, not quietly patched — one is already in
  [ANALYSIS.md](ANALYSIS.md).

## Status

This is a growing corpus, not a one-off post. The same procedure is being run
across every public freqtrade strategy that can be found and loaded.

```
repositories cloned          10
strategy classes found     1055
unique after dedup          571   (484 are copies — Schism alone appears in 16 repos)
audited so far              see results/INDEX.md
```

Nearly half of the public strategy ecosystem is copies of a few originals,
propagated without anyone re-testing them. That is a finding in itself.
