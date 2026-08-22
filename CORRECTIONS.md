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

---

## A "trap" that was not one (2026-08-22)

I claimed a tenth trap of my own, not in the community's list: an average trade
shorter than the strategy's own candle. The reasoning was that the engine knows
a candle's high and low but not which came first, so same-candle fills are an
assumption — **"and the assumption is usually the flattering one."**

`stash`, in the freqtrade Discord, replied: *"It's not really a trap."*

He was right, and the code says so. `backtesting.py`, on a trailing stop
triggering inside the entry candle:

```python
# Special case: trailing triggers within same candle as trade opened. Assume most
# pessimistic price movement, which is moving just enough to arm stoploss and
# immediately going down to stop price.
```

and the result is clamped to the candle low so the fill stays realistic —
*"worst realistic case"*, in the source's own words. **freqtrade errs against
the strategy, not for it.** The flattery claim was simply false.

The scale was wrong too. Of 895 strategies, 496 had a measurable duration and
**exactly one** traded below its own candle. Gate `G9_candle` has disqualified
nobody.

**What survives** is weaker and worth keeping: a strategy trading below the
resolution of its own data rests on the engine's model rather than on an
observed price sequence. Since that model is documented and conservative, it is
a reliability caveat, not a flattered number — and the fix is finer data, not an
argument about the model.

The gate stays as a reliability flag, its wording is corrected in
[CHECKLIST.md](CHECKLIST.md) and on every card, and the claim it once carried is
withdrawn. Found by a reader, in public, within hours of publication — which is
the entire reason for publishing.

---

## A trap that was only a trap when tight (2026-08-22)

`traps.py` counted `trailing_stop = True` with no `trailing_stop_positive` as a
trap: freqtrade then trails at the full stoploss distance rather than at a few
percent, which looked like a setting the author did not mean.

`Hippocritical`, in the freqtrade Discord: *"if you have loose trailing you wont
have a trap; if you have things like 0.1% trailing then not."*

He is right, and the distinction is the whole point. A **wide** trailing stop is
executable — it sits far from the spread and fills reliably in live trading. A
**tight** one, at 0.1%, is inside the spread and fills in backtest but not in
reality. Trailing is not the trap; tightness is.

The flag is now recorded as a note rather than a disqualification. Corpus-wide,
strategies carrying at least one trap fall from 393 to 370 (44% to 41%), and
among those clearing every statistical gate from 51 to 50 (71% to 69%).

**The change was checked before it was made.** Of the nine strategies
disqualified at the traps gate, zero were disqualified by that flag alone, and
the ladder after the change is identical: 15 → 6 → 5 → 0. Correcting a rule on
its merits is legitimate exactly when no verdict depends on it — and that is a
measurement, not a reassurance.

**Left open, and asked rather than decided:** `trailing_stop_positive` set while
`trailing_stop` is `False` still counts as a trap, and it is the largest single
category at 177. There the backtest is honest — trailing is off and the engine
runs it off — and it is the *reader* who is misled. Whether that belongs in a
list of backtesting traps is the community's call, not mine, and the question
has been put to them.

---

## Leverage divides the trailing distance, and I had read the line that says so (2026-08-22)

`Hippocritical`, minutes after the previous correction: *"and incorporate
leverage with that check — if you have 1% trailing and do 10x leverage then it
essentially becomes 0.1% trailing."*

Correct, and not a matter of opinion. `backtesting.py`:

```python
stop_rate = row[OPEN_IDX] * (
    1 + side_1 * abs(self.strategy.trailing_stop_positive_offset)
    - side_1 * abs(self.strategy.trailing_stop_positive / leverage)
)
```

The trailing distance is **divided by leverage**, so the figure that must be
compared against the spread is the effective one. A 1% trailing stop at 10×
is a 0.1% price distance — inside the spread, and therefore the very trap the
check exists to find.

**I had read that exact line the same morning**, while checking a different
claim about same-candle fills, and did not connect it to my own tightness
check. Reading a line and seeing what it means for your own code are different
acts.

The check is now leverage-aware. Corpus-wide it moves one strategy — `WTX3`,
1% at 10× = 0.001 effective — from clean to flagged, taking the tight-trailing
count from 37 to 38 and the total from 370 to 371. `WTX3` never produced
numbers, so no verdict moves. Ladder after the change: 15 → 6 → 5 → 0, identical.

**Stated because it weakens the finding:** leverage is detected only from a
literal `return <number>` inside `leverage()`. Leverage set in the config,
computed at runtime, or varying per pair is invisible here. The 36 strategies
found declaring leverage are a floor, not a count — so the true number of
effectively-tight trailing stops in this corpus is **unknown and at least 38**.

---

## Measured, and it did not hold: "most of those are caught by lookahead-analysis"

From the same conversation. Testable directly, so it was tested.

```
strategies carrying at least one trap        371
  lookahead-analysis found bias               11
  lookahead-analysis cleared them             91
  lookahead-analysis could not run           268
```

Among the 102 where the detector actually ran, it flagged 11 — about one in
nine, not most.

**But the honest figure is neither 3% nor 11%.** For 268 of the 371 there is no
lookahead verdict at all, because the analyser could not run on them. Reporting
"only 3% overlap" would be the same overstatement in the opposite direction:
counting an absent verdict as a clean one. The overlap is one in nine where it
is known, and unknown for the other 72%.
