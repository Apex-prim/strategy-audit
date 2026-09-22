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

## A file the README links to was never in the repository (2026-08-23)

`CLAIMS.csv` — the table that marks every published figure as descriptive,
pre-registered, repair-adjusted or exploratory — matched `*.csv` in
`.gitignore` and was never committed. The README links to it. The link
returned 404.

`freeze_guard.py` reads that file to compare its own verdict against the
declared claim class. Without it the guard does the correct thing: it refuses
to assert, and exits non-zero. **So CI had been failing on every clean
checkout since the guard began requiring it** — three commits — while the
same commands passed in a working tree where the file happens to exist.

Reproduced before the fix rather than reasoned about: a fresh `git clone` of
this repository fails `freeze_guard.py` with "primary claim not found in
CLAIMS.csv", and the same clone with the file restored exits 0.

**Found by looking at what a reader sees, not at what the local machine
says.** The gates were run locally before the previous push and reported as
passing. They did pass — locally. Nobody looked at the badge.

Two things changed. `CLAIMS.csv` is now committed, excepted from the ignore
rule the way `LEDGER.csv` already was. And `dca.py`, added in the previous
commit, was published without being declared in the pipeline manifest —
`sync_repo.py --orphans` catches exactly that, and it is the CI step after
the one that was failing, so it had never run. It is declared now.

**What it changes in the published numbers:** nothing. It changes whether a
reader can check them, which is the only thing this repository claims to be
for.

## Nine strategies were measured without a mechanism they contain (2026-08-23)

`adjust_trade_position` — the DCA hook — is only called when
`position_adjustment_enable` is set. freqtrade resolves that attribute in one
order and one order only: configuration, then the strategy class, then the
default (`strategy_resolver.py`, `_override_attribute_helper`).

This sweep supplies its own `config.json`. It does not mention the flag, so
for 82 strategies the class attribute wins and their DCA ran. **Nine define
the method and set the flag nowhere in the class** — theirs lives in the
`config.json` shipped alongside, which this sweep replaced. Their DCA did not
run here. `NostalgiaForInfinity772martinsk3` is among them.

Their ledger rows are not wrong. They describe a different thing than their
author built, and until now nothing said so. The column
`suppressed_by_our_config` in [DCA.csv](DCA.csv) marks all nine, and
[DCA.md](DCA.md) explains it.

**Found while answering a question, not by the machinery.** Someone asked in
the Discord for DCA results; checking whether this corpus could answer it at
all meant reading how freqtrade resolves that flag, and the nine fell out of
that reading. Nothing in this repository would have raised them otherwise.

**What it changes in the published numbers:** nothing. None of the nine
survives the ladder under any decision set. The endpoint stands at 0 of 456.
It is published because a count that is right for the wrong reason is still
a thing a reader deserves to know about.

**The general form, for anyone copying a strategy file:** a strategy's
behaviour is not all in the strategy file. Take the `.py` without its config
and you get, silently, a different strategy.

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

## Strategies that never load were counted as strategies (2026-08-24)

**Raised by** froggleston, in the freqtrade Discord: *"it also doesn't list
strategies that simply don't load."*

He is right, and I did not have the number. The funnel showed 399 of 895
strategies falling at the first gate under one label, `G0_measured`, which
says only that a measurable pair of windows never appeared. It does not say
why. A strategy that will not import, one that imports and never trades, and
one that died during the backtest are three different facts, and I collapsed
them into one.

**Why that matters more than a missing column.** Unreported, it makes the
corpus quietly become *code that still runs today*. Strategies depending on a
package that has since vanished drop out silently. That is a survivorship
filter, and it was never declared.

**The reason was not recorded at run time**, so it is reconstructed by
[`loadcheck.py`](loadcheck.py), cheapest route first: if either window
produced a trade count the file demonstrably loaded, which settles those from
the ledger alone; the rest are imported in a subprocess and the exception is
kept. Import takes seconds where a backtest takes minutes.

```
corpus                                        895
never produced a measurable pair of windows   399

  imports fine, reason still downstream       268    29.9% of corpus
  WILL NOT IMPORT                              91    10.2% of corpus
  loaded, one window produced trades            37     4.1% of corpus
  loads but breaks on definition                3     0.3% of corpus
```

Examples of the import failures: `AdaptiveRenkoStrategy` needs `pyrenko`,
`AdvancedRiskFilterStrategy` needs `remora`. Neither is installable from what
the repository ships.

**So the honest number is 94 of 895, about 10.5%, that do not load at
all.** That is froggleston's point, and it now has a figure attached.

**What this correction does not fix.** The 268 that import cleanly still fall
at `G0_measured` for a reason this probe cannot see: no trades in the windows,
a timeout, or a failure during the backtest itself. Import is not execution.
Separating those three requires re-running them with the error captured, which
is the next job, not this one. Saying it is resolved would repeat the mistake
this correction is about.

**Consequence for the reader:** the denominator in every rate quoted from the
funnel included 94 strategies that were never runnable. The published endpoint
— no strategy beats buy-and-hold — sits on later gates and does not move.

---

## Three findings from an outside review, adjudicated by reading the code (2026-09-21)

**Reported by a reader** — an external review of this repository raised three
points about its statistics, with the wording frozen before any answer. Each
was adjudicated by reading the code that produces the number, not the prose
around it. Two stand, one does not, and the impact of each was measured before
being written down.

### 1. The per-strategy p-value assumes independent trades — CONFIRMED, unstated

`harness.py:190` takes *Mean profit p-value* from freqtrade's own backtest
report: a t-test on per-trade profits. That test treats trades as independent
draws. In a multi-pair backtest they are not — trades overlap in time, share
regimes, and cluster — so the effective sample is smaller than the trade count
and every p-value in the ledger is optimistic. `ci_low()` in `ledger.py` inherits
the same assumption. Nothing in the README said so; the Benjamini–Yekutieli
line addresses dependence *between strategies*, not *within* one.

**Direction of the error:** it favours strategies. Gates G3 and G5 (`p < α`)
pass more than they should; a correct p can only move a strategy *down* the
ladder. The published endpoint — zero survivors beat buy-and-hold — is
therefore not weakened by this finding; it would only get harder to reach.

**What is not yet done:** the fix is a block bootstrap (or an effective-n
correction from the autocorrelation of trade profits) inside the harness, and
a re-run of the corpus. Recorded as debt, not claimed as fixed.

### 2. The FDR family is selected on the sign of the same out-of-sample data — PARTIAL, impact measured

`bh_population()` in `ledger_block.py` admits a strategy to the
Benjamini–Hochberg family only if it has ≥30 trades, positive and significant
expectancy in the author's window, **and positive expectancy out of sample**.
The last condition looks at the very data whose p-values are then corrected.
The in-sample conditions are a legitimate pre-filter (different data); the
out-of-sample one is selection before the test.

Measured on the published ledger, dropping the out-of-sample sign filter:

```
family as published          81 tests   BH threshold 0.03872   72 rejected
family without OOS-sign filter   83 tests   BH threshold 0.03872   73 rejected
excluded by the filter            2   BinHV45HO (p 0.704)
                                      CombinedBinHAndClucHyperV3 (p 0.0038, negative expectancy)
Benjamini–Yekutieli, 83 tests               threshold 0.003761   71 rejected
```

The threshold does not move; the one extra rejection is a strategy that is
significantly *negative* — a two-sided p rejecting in the direction nobody is
claiming. That is the real defect the reviewer's point exposes: the p-values are
two-sided while the claim is one-sided (*positive* edge). The clean form is the
83-strategy family with one-sided p-values, and that is the change to make in
`ledger_block.py` before the next corpus run. **Both survivors keep their status
under either family**, so no published number changes today.

### 3. "threshold" reported as the largest rejected p-value — NOT a defect

`ledger_block.py:306` prints the Benjamini–Hochberg threshold as the largest
p-value rejected by the step-up rule. That is the definition of the BH cutoff:
reject every p ≤ p₍ₖ₎ where k is the largest index with p₍ᵢ₎ ≤ (i/m)·α. Reporting
p₍ₖ₎ is standard and is what the code does. The reviewer's reading — that the
word stands in for a different quantity — was checked against the code and does
not hold. Kept here so that the refutation is as visible as the two findings.

**Consequence for the reader:** no number in the README changes from this
entry. Finding 1 adds a stated assumption and a debt; finding 2 changes how the
family will be defined next run; finding 3 changes nothing. All three were
written down before any of them was fixed.

---

## The README gate checked a quarter of the README (2026-09-22)

The repository description said *"a CI gate fails if the README disagrees"*.
A clean-clone check changed the README headline from **895** to **896** and ran
`verify_ledger.py`: it answered *"README numbers reproduce from LEDGER.csv"*,
exit 0. The gate compared only the block between the `LEDGER` markers —
**52 of the 241 numbers** in the README. The headline, and everything in
prose, was not checked by anything. A change inside the block was caught
(exit 1), so the gate worked; it was the claim about it that was too large.

The same check found two more things of the same kind:

- The self-tests of all three CI gates — `verify_ledger.py`, `freeze_guard.py`,
  `calibrate.py` — exercised only their helper functions. None called
  `main()`, so a green CI proved the arithmetic, not that the gate as run by
  CI could fail.
- The published copy of `foreign_strategy_audit.py` had fallen behind its
  owner: a file that could not be read left the corpus count silently. The
  owner had been fixed the same day; the copy had not.
- `loadscan.py` (a diagnostic, not a source of any published number — the
  "94 of 895 do not load" figure comes from `loadcheck.py`): since commit
  `ade33b2a` (2026-08-22) the directory walk sat one indentation level
  *outside* the loop over repositories, so it scanned only the last one. The
  `# TOTAL:` marker inserted by that commit moved the line. The other ten
  markers of the same commit were checked; none moved code. Its self-test also
  wrote a deliberately broken strategy into `_sabotage/` in the repository
  root and never removed it — one `git add -A` from being published. Both
  fixed. ⚠ The loop fix is verified structurally (the walk is now inside the
  loop, by syntax tree), **not by a run**: the self-test needs freqtrade, and
  the machine that made the fix does not have it.

**What changed.** `verify_ledger.py` now also checks the README headline and
`CLAIMS.csv` (strategies, repositories) against the ledger, fails when
`CLAIMS.csv` is missing, and **prints its coverage** — *53 of 241 numbers
checked; the other 188 are prose and are NOT checked*. Each of the three gates
now has self-test cases that drive `main()` on planted lies; the headline
895 → 896 is one of them. The auditor copy is synced from its owner.

**Consequence for the reader:** no published number changes. What changes is
what the green check means: it covers the ledger block, the headline and
`CLAIMS.csv` — not the prose, which is the reader's to check.

*Found by running the repository's own gates against deliberately altered
copies of its files, not by reading.*
