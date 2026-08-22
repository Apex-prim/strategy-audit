# Errors found in this audit, and what they changed

Every finding below was made *after* something had been published, and every one
of them changed a number or a claim. They are collected here rather than left in
the README because a reader deserves the result first and the process second —
but they are not deleted, because an audit that hides its own corrections is
asking for a trust it has not earned.

Nothing here was reported by a reader unless it says so.

---

## The metric was not scale-free (2026-08-21)

Earlier versions reported freqtrade's `Expectancy` in USDT and called it
configuration-independent, in contrast to `Total profit %`. That was wrong. The
backtests run with `stake_amount: "unlimited"`, under which freqtrade divides
the wallet across open slots and **compounds**: as the balance grows, later
trades use larger stakes, so an expectancy denominated in currency is inflated
by account growth rather than by skill.

The scale-free quantity is average profit per trade in percent.

**What changed.** `RSIDirectionalWithTrendSlow` was published as retaining
**5%** of its edge; measured scale-free it retains **26%** — five times more.
`MACDCrossoverWithTrend` moved from 6% to 12%. The claim *"two retain under
10%"* was an artifact of the metric and is withdrawn.

The cost-sensitivity table moved too: under the old metric
`MACDCrossoverWithTrend` read −0.01 and the claim was "three of five turn
negative". It is two, plus one at zero. **The weaker version is the correct
one.**

*Found because a reader asked what stake the numbers were computed at. It is a
good question to ask of any backtest, including this one.*

---

## A statement about five, made from the one I was looking at (2026-08-21)

An earlier README said *one* of the five strategies was not statistically
significant, citing `MACDCrossoverWithTrend` at p = 0.1283. That was the p-value
of the strategy I happened to be writing about, reported as though it described
the set.

Measuring all five gives **four**.

The error is the same shape as the timeframe defect below: a claim about a
population, made from the single case actually examined.

---

## "Walk-forward" was the wrong word (2026-08-21)

This is an *out-of-sample test*, not a walk-forward analysis. Walk-forward means
rolling or anchored windows with re-fitting at each step; nothing here re-fits.
An earlier version used the wrong term. Corrected rather than quietly edited.

---

## An RSI threshold I assumed instead of read (2026-08-20)

The first run produced 18 trades for `RSIDirectionalWithTrendSlow` against the
author's 108 — an 8× gap that would have made a persuasive *"does not
reproduce"* headline.

It was my bug. I had assumed RSI thresholds of 15/85 by analogy with the
neighbouring strategy; the file uses 25/20. After the fix that strategy
reproduces better than the rest.

**An unexplained anomaly is not a finding — it is a thing to go and check, and
more often than not it is yours.**

---

## The corpus sweep was silently running the wrong timeframe (2026-08-20)

Of the 571 strategies then in the corpus, only **52** declare
`timeframe = '1h'`. The largest group, **351**, declares `5m`. Only 1h data had
been downloaded.

A missing-data run should fail loudly. It did not: the backtest config carried
`"timeframe": "1h"`, and **freqtrade's config overrides the timeframe a strategy
declares for itself**. Every 5-minute strategy was executed on hourly candles and
returned a full, plausible-looking result — 6,014 trades for one of them.
Nothing in the output said anything was wrong.

**Fixed in two parts.** Removing the config key fixes this case. But a fix that
depends on nobody putting the key back is not a fix, so the harness now refuses
any result whose timeframe the engine did not confirm:

```python
used = engine_tf(out)                  # freqtrade's own words, not my assumption
if want_tf and used and used != want_tf:
    return (NA, "wrong subject: strategy declares %s, engine ran %s" % (want_tf, used))
```

The guard is verified by **restoring the defect**: a self-test writes the bad
key back into a copy of the config, runs a 5-minute strategy through it, and
requires the guard to reject the result — then requires the same guard to *pass*
an honest run, because a check that always refuses has not checked anything. 7/7.

Every corpus result computed under the old setting was deleted and recomputed.

**A second silent failure, found while fixing the first.** When candle data for
one pair is missing, freqtrade prints a warning and *continues on the remaining
pairs*. The result looks complete; it is simply computed over fewer instruments.
Every card now records which pairs the engine could not load.

*The number to distrust was never the one that looked wrong. It was the one that
looked fine.*

---

## Published figures went stale while the corpus grew (2026-08-21)

The README carried *"571 strategies, 55 clean"* for about a day after the corpus
had grown past 900. Nothing was false when written. An external reviewer read
the repository and built a favourable assessment on those figures — and on two
scripts, `replicate.py` and `stats.py`, that had already been discarded.

Staleness reads exactly like authority to someone who was not there.

**Fixed with a return code, not a promise.** The counts in the README now sit
between markers and are written by `ledger.py`; `verify_ledger.py` rebuilds them
from the published `LEDGER.csv` and exits non-zero on any difference. It runs in
the pre-commit hook and in CI.

`replicate.py`, `stats.py`, `funnel.py` and `fetch_data.py` were deleted rather
than left lying around: **code that is present is code that is believed,
whatever the prose says about it.** `sync_repo.py` now refuses a tree containing
published code that is not declared part of the pipeline.

---

## A consistency check that could not catch its own error (2026-08-22)

The generated block published **"repositories swept 3"** instead of 53:
`corpus_sources.json` is a dict of three keys, and the list of repositories sits
inside one of them.

`verify_ledger.py` compared the README against a recount and stayed silent —
because **both sides computed it with the same wrong formula.** Agreement
between two figures derived from one source proves agreement, not correctness.

Fixed twice over, deliberately: one implementation instead of two, plus a
plausibility guard that does not depend on the formula at all — 895 strategies
from 3 repositories is 298 per repository, and the block now prints `⚠ SUSPECT`
rather than the number alone.

---

## Ten strategies never reached publication (2026-08-22)

Ten pairs of strategy names differ only by case — `Ichi`/`ichi`, `SAR`/`Sar`,
`SuperTrend`/`Supertrend` and seven more. On a case-insensitive filesystem the
card writer silently overwrote one of each pair, so **ten strategies were
measured and then lost between the result file and the published card.**

The same defect had been found and fixed in `corpus.py` days earlier.
`report.py` was the same class and was missed — the case was fixed, the class
was not. Both are now swept machine-wide; card names carry a hash when they
collide.

---

## A gate that passed what it had never measured (2026-08-22)

The trade-duration gate asked `not card.get("intracandle")`. Cards computed
before that layer existed carry no such field, so the absent value read as
**passed**.

It now fails a strategy whose duration was never measured. Absence of a flag is
not absence of the defect.
