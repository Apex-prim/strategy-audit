# Out-of-sample audit of a public "strategies that work" repository

An independent replication of the five freqtrade strategies published in
[`paulcpk/freqtrade-strategies-that-work`](https://github.com/paulcpk/freqtrade-strategies-that-work),
tested on 6.5 years of data the original author never saw.

**Headline: all five degrade out of sample, the worst retaining 12% of its
edge and one turning negative — and four of the five were never statistically
significant to begin with.**

Measured with **freqtrade itself**, not a re-implementation, and reported as
**average profit per trade in percent**. Not "Total profit %", which depends on
`max_open_trades`, stake sizing and starting wallet — a configuration the
authors did not publish.

```
                             avg trade %     p     avg trade %     p      survives
                              (in-sample)             (out)
EMAPriceCrossoverWithThreshold   1.39      0.113       0.65      0.161       47%
DoubleEMACrossoverWithTrend      0.38      0.049       0.19      0.290       50%
MACDCrossoverWithTrend           0.42      0.128       0.05      0.883       12%
RSIDirectionalWithTrendSlow      1.03      0.381       0.27      0.924       26%
RSIDirectionalWithTrend          0.34      0.238      -0.07      0.556    negative
```

> **A correction, and a methodological one.** Earlier versions of this table
> reported freqtrade's `Expectancy` in USDT and called it configuration-
> independent, in contrast to `Total profit %`. That was wrong. The backtests
> run with `stake_amount: "unlimited"`, under which freqtrade divides the wallet
> across open slots and **compounds**: as the balance grows, later trades use
> larger stakes, so an expectancy denominated in currency is inflated by
> account growth. The scale-free quantity is average profit per trade in
> percent, which is what the table now shows.
>
> The correction is not cosmetic. `RSIDirectionalWithTrendSlow` was published as
> retaining **5%** of its edge; scale-free it retains **26%** — five times more.
> `MACDCrossoverWithTrend` moves from 6% to 12%. The claim "two retain under 10%"
> was an artifact of the metric and is withdrawn.
>
> Found because a reader asked what stake the numbers were computed at. It is a
> good question to ask of any backtest, including this one.

In-sample window is the authors': 2018-03-01 … 2020-03-01, 1h, 8 USDT pairs.
Out-of-sample: 2020-03-01 … 2026-08-20, same code, same pairs, 0.1% fee per side.

### And two findings that do not need the out-of-sample window at all

**Four of the five are not statistically significant in their own author's
window. None of the five is significant out of sample.**

freqtrade prints `Mean profit p-value` in every backtest; the column is in the
table above. Only `DoubleEMACrossoverWithTrend` clears 0.05 in-sample, and only
just (0.049). The strongest performer of the set —
`EMAPriceCrossoverWithThreshold`, 1.39% per trade — sits at **p = 0.113**: its
average trade is not distinguishable from zero in the window it was developed in.

For most of these strategies the out-of-sample collapse is almost beside the
point. The in-sample result was never established in the first place.

> **A correction.** An earlier version of this README said *one* of them was not
> significant, citing `MACDCrossoverWithTrend` at 0.1283. That was the p-value of
> the strategy I happened to be writing about, reported as though it described
> the set. Measuring all five gives four. The error is mine and it is the same
> shape as the one documented at the bottom of this file: a statement about a
> population, made from the one case actually looked at.

**Two of five turn negative in-sample once execution is priced honestly, and a
third lands on zero.**
freqtrade fills at the candle open with no spread and no slippage. On XLM, DASH
and ADA in 2018–2020, hourly spreads of 0.3–0.5% were routine. Raising the cost
assumption to 0.3% per side — fee plus spread plus slippage:

```
avg trade %                     0.1%     0.2%     0.3%  per side
EMAPriceCrossoverWithThreshold  1.39     1.19     0.99
RSIDirectionalWithTrendSlow     1.03     0.82     0.62
MACDCrossoverWithTrend          0.42     0.21     0.01   <- indistinguishable from zero
DoubleEMACrossoverWithTrend     0.38     0.18    -0.02   <- negative
RSIDirectionalWithTrend         0.34     0.14    -0.06   <- negative
```

So the claim here is not "these strategies fail out of sample". It is narrower
and harder to argue with: **under honest execution assumptions, three of the five
have nothing left in the window their own author chose** — two negative, one at
+0.01% per trade, which is zero wearing a plus sign.

*This table was also recomputed scale-free. Under the old currency-denominated
metric `MACDCrossoverWithTrend` read −0.01 and the claim was "three of five turn
negative". It is two, plus one at zero. The weaker version is the correct one.*

**[BASELINE.md](BASELINE.md) — fifty-five corpus strategies pass every
statistical test in this repository, and none of them beats buy-and-hold.**
Full sweep, 571 strategies. By the statistics most people use, 17% survive; by
one free column they skip, 0% do.

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
| Statistical significance | `Mean profit p-value` per strategy — **4 of 5 fail in-sample, 5 of 5 fail out** |
| Baseline | `Market change` — buy-and-hold on the same pairs, reported alongside |
| Reproducibility of the headline figure | **fails** — no config is published |
| Metric is scale-free | corrected here: currency expectancy compounds under `stake_amount: unlimited` |
| Filter interaction | one of two exits is unreachable by construction |
| Cost sensitivity | fee 0.0 / 0.1 / 0.2% per side |
| Out-of-sample test | 6.5 years the authors never saw |
| Data coverage per pair | measured, not assumed — **3 of 8 pairs span the author's window** |

> **Terminology, stated precisely:** this is an *out-of-sample test*, not a
> walk-forward analysis. Walk-forward means rolling or anchored windows with
> re-fitting at each step. An earlier version of this README used the wrong
> word; it is corrected here rather than quietly edited away.

**Auditing your own strategy?** → **[CHECKLIST.md](CHECKLIST.md)** — ten
mechanical questions, each tied to a defect actually found here — nine in the
audited strategies, one in this pipeline.

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

**The original `.py` files are run by freqtrade 2026.7 itself** — same engine,
same execution semantics, zero interpretation on my part. Fee 0.1% per side,
eight USDT pairs, 1h.

This replaced an earlier pandas re-implementation, and the difference matters:
the hand-written version produced 334 trades for `MACDCrossoverWithTrend` where
freqtrade produces 303 against the author's claimed 300. A re-implementation
invites the perfectly fair reply *"you rewrote my logic wrong"*. The engine
does not.

Two of freqtrade's own analysers run on every strategy — `lookahead-analysis`
and `recursive-analysis` — and both are reported whatever they say, including
when they clear the strategy.

Remaining caveats, stated rather than omitted:

- `minimal_roi` is not applied, because it is commented out in the published
  files. If the authors' config carried one, the numbers move.
- Fee is a proxy for total round-trip cost. freqtrade fills at the candle open
  with no spread and no slippage, so **every figure here is optimistic**, which
  is why the cost sensitivity table exists.
- Trade counts still differ from the authors' because `max_open_trades` is not
  published; that is a property of the repository, not of the measurement.
- **"Eight pairs" is the request list, not what traded throughout.** Measured
  with `coverage.py`:

```
pair        first        last         author's window   out-of-sample
BTC_USDT    2018-03-01   2026-08-20        100.0%           100.0%
ETH_USDT    2018-03-01   2026-08-20        100.0%           100.0%
LTC_USDT    2018-03-01   2026-08-20        100.0%           100.0%
ADA_USDT    2018-04-17   2026-08-20         93.5%           100.0%
XRP_USDT    2018-05-04   2026-08-20         91.2%           100.0%
XLM_USDT    2018-05-31   2026-08-20         87.5%           100.0%
XMR_USDT    2019-03-15   2024-02-20         48.1%            61.4%   <- delisted
DASH_USDT   2019-03-28   2026-08-20         46.4%           100.0%   <- listed late
```

  Three of the eight span the author's window. DASH did not exist on Binance
  until it was more than half over, and **XMR was delisted on 2024-02-20**, so
  the basket's composition changes partway through both windows. This does not
  corrupt the results — you cannot trade a pair that is not listed, and the
  engine correctly does not — but a reader who sees "8 pairs" will assume eight
  throughout, and that assumption is wrong.

  Note also what this check does *not* see: it measures the first and last
  candle inside each window, not gaps in the middle. A ragged series with intact
  edges would report 100%.

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

**📧 faxesuxan24@gmail.com** — for a private audit of a strategy you would
rather not post publicly. That is most of them, and it is a reasonable thing to
want.

Or, in the open:

- **Want your strategy audited the same way?** Open an issue with a link to the
  code — or run `harness.py` yourself. It is the exact pipeline used here, not a
  demonstration of one.
- **Found an error in this audit?** Open an issue. Errors found in this
  repository get published *in* it rather than quietly patched — two already
  are: a wrong RSI threshold in [ANALYSIS.md](ANALYSIS.md), and a p-value parser
  that returned 5.896 for a probability, caught before publication because a
  value outside [0,1] means a broken instrument, not a surprising result.

**What you get:** the ten checks in [CHECKLIST.md](CHECKLIST.md) run against
your code — in-sample and out-of-sample expectancy, p-value, buy-and-hold
baseline, cost sensitivity, and freqtrade's own bias detectors — plus a written
finding for anything that does not hold.

**What you will not get:** a verdict on whether your idea is good. Every check
here is about whether your *measurement* can be trusted. A well-measured
strategy with no edge is still a strategy with no edge; you will simply learn it
sooner and cheaper.

## Status

This is a growing corpus, not a one-off post. The same procedure is being run
across every public freqtrade strategy that can be found and loaded.

```
repositories cloned          10
strategy classes found     1055
unique after dedup          571   (484 are copies — Schism alone appears in 16 repos)
swept                       571   complete
produced numbers            344   the other 227 are categorised by cause
passed every stat test       57   of which 2 have look-ahead bias
beat buy-and-hold             0   of 55 clean — see BASELINE.md
```

### A methodological defect found in this project, before publication

The corpus sweep was producing numbers that were **silently wrong**, and the
mechanism is worth writing down because it is the exact failure this repository
exists to catch.

Only **52 of the 571 strategies declare `timeframe = '1h'`**. The largest group —
**351** — declares `5m`. Only 1h data had been downloaded.

A missing-data run should fail loudly. It did not, because the backtest config
carried `"timeframe": "1h"`, and **freqtrade's config overrides the timeframe a
strategy declares for itself**. Every 5-minute strategy was therefore executed on
hourly candles and returned a full, plausible-looking result — 6,014 trades for
one of them. Nothing in the output said anything was wrong.

Removing `timeframe` from the config makes the engine say *"Strategy using
timeframe: 5m"* and then refuse: *"No history for BTC/USDT, spot, 5m found."*
Loud failure, which is what should have happened all along.

**What was done, in two parts.** Removing the config key fixes *this* case:
the engine now says *"Strategy using timeframe: 5m"* and refuses with *"No
history found"*. But a fix that depends on nobody putting the key back is not a
fix. So the harness now refuses any backtest result whose timeframe the engine
did not confirm:

```python
used = engine_tf(out)                      # freqtrade's own words, not my assumption
if want_tf and used and used != want_tf:
    return (NA, "wrong subject: strategy declares %s, engine ran %s" % (want_tf, used))
```

That guard is verified by **restoring the defect**: a self-test writes the bad
`timeframe` key back into a copy of the config, runs a 5-minute strategy through
it, and requires the guard to reject the result — then requires the same guard to
*pass* an honest run, because a check that always refuses has not checked
anything. 7/7.

Every corpus result computed under the old setting was deleted, and per-timeframe
data is being re-downloaded from Binance's monthly archives. **The five published
audits are unaffected** — those strategies declare `1h` themselves, and re-running
them without the override reproduces 303 trades and 0.53 expectancy exactly as
published.

**A second silent failure, found while fixing the first.** When candle data for
one pair is missing, freqtrade prints a warning and *continues on the remaining
pairs*. The result looks complete; it is simply computed over fewer instruments,
and comparing it to a full-coverage result is invalid. Every card now records
which pairs the engine could not load, so coverage is a field rather than an
assumption.

The number to distrust was never the one that looked wrong. It was the one that
looked fine.

Nearly half of the public strategy ecosystem is copies of a few originals,
propagated without anyone re-testing them. That is a finding in itself.

### The corpus is biased, and that is the point

Who publishes a strategy on GitHub? Someone whose in-sample curve looked good.
Nobody uploads the version that lost money in backtest. **This corpus is
selected by its own authors for best in-sample result** — the survivorship
filter runs before we ever see the file.

That is not a weakness in the sample; it is what makes the number meaningful.
The question this corpus answers is not "how do random strategies perform" but:

> Of the strategies people were confident enough to publish, how many hold up
> when someone re-runs them on data the author never saw?

A low survival rate in a sample pre-filtered for good results is a much stronger
statement than the same rate in a random sample would be.
