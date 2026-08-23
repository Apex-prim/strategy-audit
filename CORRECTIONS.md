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

## Two detectors compared as rivals, when they have different subjects (2026-08-22)

An earlier version of this file carried the section below under the heading
*"Measured, and it did not hold"*, treating the overlap between `traps.py` and
`lookahead-analysis` as a test of the latter.

`Hippocritical`: *"careful — traps and lookahead-analysis check on different
things, you mix them together."* He then said what his tool does:

> *"It does a full backtest and then n cut-off backtests with the same start but
> cut off where the trade would buy. If the trade buys at a different time, then
> something fucked with the backtest dataframe and looked into the future. It
> doesn't look into the strategy at all, it just checks its behaviour."*

A black-box behavioural probe and a white-box reading of declared constants do
not have the same subject. **Low overlap between them is what should be
expected, and it is evidence about neither.** The numbers below are unchanged
and still worth recording; what is withdrawn is the framing that made them a
verdict on a detector.

The mistake is worth naming precisely, because it is not the same as the others
in this file: nothing was miscomputed. The arithmetic was right and the question
was wrong.

---

## The measurement itself, kept without the framing

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

---

## The trap list was not using the community's definition of a trap (2026-08-22)

`Hippocritical`, asked directly whether `trailing_stop_positive` set while
`trailing_stop` is `False` — 177 of 895 — belongs in a list of backtesting traps:

> *"A backtesting trap is where you have a different result from backtest to dry
> run. Backtesting works on candles, where dry / live runs work on ticker data
> (which is not available, only max resolution of 1 minute via
> timeframe-detail)."*

Under that definition two of the four checks do not qualify. An inert trailing
setting runs with trailing off in backtest *and* live; a −0.99 stoploss behaves
identically in both. Neither produces divergence. They are a reader-misleading
declaration and a risk decision respectively — real defects, wrong list.

**What changed.** Both became notes. Strategies carrying at least one
disqualifying trap fall from **371 to 42** (41% → 5%), and the number of
strategies this layer removes from the ladder falls from **9 to 1** — `SMAIP3v2`,
trailing tighter than the spread.

The published endpoint is unchanged: **0 of 456 eligible strategies** clear every
gate. Checked before the change, not after: the eight strategies held only by
those two flags were carried through the remaining gates on their own recorded
numbers, and all eight fail G12.

**Said plainly, because it is the least flattering way to put it:** a layer
introduced as flagging 41% of the corpus disqualifies one strategy in 895. The
earlier figure was mostly counting things that are not backtesting traps.

*My first version of the pre-check said the endpoint moved from 0 to 8. It was
wrong: it counted "never evaluated at this gate" as "passed" — the identical
defect this audit had already fixed once, in `G9_candle`, and written up above.
It was caught by a plausibility guard that refused a ladder whose first rung was
zero out of 895. Third occurrence of that class in one day, and the first one an
automatic guard caught rather than a reader.*

---

## The ceiling on this instrument, stated by the people who build the engine

`froggleston`: *"any callback can add a backtesting trap — it can be very
subtle."*

`Hippocritical`: *"you'll quickly run into limitations with your script. Without
you understanding what it's actually looking for, your result is impossible to
verify — and to sanity check. Imagine why freqtrade didn't bother to implement
such a thing. It's simply impossible to catch all that — since the facts there
in traps, for example, are floating."*

Both are correct and neither is answerable with a better regex. A trap built
inside `custom_exit`, `confirm_trade_entry` or a custom stoploss is invisible to
something that reads declared constants, and the thresholds are practitioner
judgement rather than physics.

**[TRAPS.md](TRAPS.md) now states the scope as a necessary condition on declared
configuration, not a detector**, and the headline count went with it. The part of
the criticism that is not accepted is left explicit rather than quietly dropped:
the checks are individually verifiable — each is a named constant, a documented
threshold from the community's own article, and a number regenerated from
`LEDGER.csv` by `verify_ledger.py`. Verifiability of *what it does* is not the
same claim as completeness of *what exists*, and only the second is refused here.

---

## The freeze guard watched the names of the gates, not their meaning (2026-08-22)

`freeze_guard.py` exists to answer one question against its own author: was the
rule fixed before the data were seen, or adjusted after? It derives the answer
from `git log`.

It was reading the history of **one** file — `ledger_block.py`, where the ladder's
*names* are declared. But what a gate *means* lives in the code that decides who
passes it: `traps.py` for G8, `ledger.py` for G11 and G12. On the day
`traps.py` was rewritten three times, the meaning of G8 moved with it and the
guard kept reporting the day before yesterday.

Found by the guard itself: it printed a timestamp hours older than the commit it
was gating.

**Fixed** by taking the latest change across every file that defines a gate — a
rule is no older than its freshest part. The reported gap widens from 15.7 h to
20.5 h; the verdict class does not change (`repair-adjusted` either way), so
nothing published moves. Two self-test cases now pin it: that the semantic files
are in the watch list, and that the reported time equals the maximum over them.

This is the same class as three other entries here — **a check that asked about
the word rather than the subject.** It is on record because a machine built to
catch that class had it, in the part of itself that judges its author.

---

## A gate that passed what it had never measured — again, in the gate that matters most (2026-08-22, evening)

Above, under *"A gate that passed what it had never measured"*, this file
records fixing `G9_candle`: a card with no duration field read as **passed**.
Earlier the same day `G8_traps` was fixed for the identical reason — a strategy
whose source could not be found scored as having no traps.

The case was fixed twice. **The class was never swept.** `ledger.py` read:

```python
g["G6_lookahead"] = r["runs"]["lookahead"]["level"] != FOUND
g["G7_recursive"] = r["runs"]["recursive"]["level"] != FOUND
```

`НЕ ПРИМЕНИМА` — *the check could not be run* — is not `FOUND`, so it passed.

**The scale.** Look-ahead analysis returns no verdict for **611 of 895**
strategies. Of the 72 reaching `G6`: **49 unmeasured, 17 clean, 6 flagged** —
and all 49 passed. Of the fourteen strategies this repository published as
survivors, **twelve had never been successfully look-ahead-tested.** Two had.

Root cause in `harness.py`: freqtrade emits a three-cell row for
`"too few trades caught (N/M). Test failed."` and for `"error while checking"`;
the parser expects a four-column Yes/No row, fails, and returns NA. A strategy
freqtrade explicitly marked **Test failed** was scored clean — contradicting
`harness.py`'s own docstring, which says in as many words that "could not
check" must never print as "clean".

**What changed.** Both gates now require a positive verdict, exactly as `G8`
and `G9` already did:

```
                          before        after
G6_lookahead          72 ->  66      72 ->  17
G7_recursive          66 ->  15      17 ->   2
survivors published          14             2
clear the effect-size gate   10             1
PRIMARY ENDPOINT        0 of 456       0 of 456
```

**The headline shrinks sevenfold and the conclusion does not move.** That is
the whole argument for making the change.

**Stated because it is the least flattering part:** this was found by an
independent audit, not by the machinery built to catch it, and it is the sixth
occurrence in one day of a single class — a check that asks about the word
rather than the subject. This repository's own sealed rule says *fix the class,
not the case*; that rule was cited here hours before this gate was found still
broken. A rule invoked and not executed is not a rule.

**Consequence for the reader:** every earlier statement about "six survivors"
or "fourteen survivors" described populations containing strategies never
tested for look-ahead bias. The published endpoint — no strategy beats
buy-and-hold — is unchanged under all three versions.
