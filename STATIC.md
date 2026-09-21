# The static auditor, calibrated against the dynamic one

`foreign_strategy_audit.py` reads a strategy's source and answers in a second,
without freqtrade, without data, without a working environment. This page says
exactly how much that answer is worth, because the number was measured — not
assumed — against the only ground truth this repository has: freqtrade's own
`lookahead-analysis`, run on 284 strategies of the ledger.

## Calibration — 2026-09-21

284 strategies in [LEDGER.csv](LEDGER.csv) carry a dynamic lookahead verdict
(40 `НАЙДЕНО` / found, 244 `ПРОШЛА` / passed). 248 of them were on disk when
the static auditor was run over the same files.

```
                          dynamic FOUND     dynamic PASSED
static FLAGS                  13  (TP)            0  (FP)
static is silent              16  (FN)          219  (TN)

precision      TP/(TP+FP)   =  13/13   = 100 %
false alarm    FP/(FP+TN)   =   0/219  =   0.0 %
sensitivity    TP/(TP+FN)   =  13/29   =  45 %
```

Read it plainly: **when the static auditor speaks, it has not been wrong once
on 219 clean strategies. When it is silent, it has missed more than half of
the real cases.** It is a pre-filter that never lies, not a judge. The judge
is `harness.py`, which runs the code.

The same day it stood at 8/29 = 28 %. The step to 45 % came from two needle
families borrowed from a third detector (see *A third detector*, below), each
added with a boundary control and each re-measured here before being kept:
precision did not move.

Two flags counted as hits deserve a footnote. `LorentzianClassification:128`
builds `y_train = shift(-4)` — a training *label*, which may legitimately see
the future; the dynamic analyser flagged the strategy anyway, so the two tools
agree on the verdict while the static one may be pointing at the wrong line.
Two Ichimoku strategies were *initially* counted as hits because the needle
matched `'future_green'` in a plot-config dictionary; the verdict was right and
the evidence was wrong, so the needle was tightened and those two moved to the
misses column. Being right by accident is not being right.

## What it catches — the six forms it knows

| form | what the code looks like | why it is lookahead |
|---|---|---|
| higher timeframe interpolated back down | `df.resample('15min')…; df.resample('5min'); df.interpolate(method='time')` | the 10:05 row is a line drawn between 10:00 and **10:15**; the 10:15 candle has not closed |
| full-sample normalisation | `(x − x.min()) / (x.max() − x.min())`, `MinMaxScaler().fit_transform(x)`, `RobustScaler().fit(df)` | the value at bar *t* depends on extremes that occur after *t* |
| explicit backward shift | `close.shift(-kijun)`, `.shift(-4)` | takes a future row by name |
| centred window | `rolling(n, center=True)` | looks *n/2* bars ahead by definition — unless a matching `.shift()` puts them back, which is checked by reading, not by the needle |
| backward fill | `.bfill()`, `fillna(method='bfill')` | a later value is copied into earlier rows; `ffill()` is the legitimate direction and stays silent. Borrowed from a third detector — see below |
| extrema scan | `argrelextrema(...)`, `find_peaks(...)`, zigzag | an extremum at *t* is only known once price has turned after *t*. This is the path-dependent family that `Renko` also belongs to, named at last. Borrowed likewise |

A fourth category is reported separately and **not** as lookahead:

| category | looks like | why it is separate |
|---|---|---|
| randomness in the signal | `np.random.randint(0, 2, size=len(df))` | not lookahead — non-reproducibility. The dynamic analyser cannot tell a coin toss from a peek: both change the signal when the series is extended. Two of the 40 dynamic "found" are exactly this (`BuyAllSellAllStrategy`, `FrostAuraRandomStrategy`) |

## What it does not catch — the 16 misses, by family

Every one of the 16 was opened and read. They fall into forms the needle set
does not know, and each is named so that a zero from the static auditor on your
own code is read as *"none of the six forms"*, not as *"clean"*.

| family | examples in the ledger | why static is blind |
|---|---|---|
| Ichimoku forward displacement | `Ichi`, `ichiV1`, `Obelisk_TradePro_Ichi_v1_1`, `_v2_1` | the shift is inside `technical.indicators.ichimoku`, not in the strategy text |
| higher-timeframe merge done by hand | `LookaheadStrategy`, `NWEv6`, `BB_RPB_TSL` | `LookaheadStrategy` even uses the correct API (`merge_informative_pair(…, ffill=True)`) and is still flagged dynamically. I do not know why, and this page will not pretend to |
| path-dependent recomputation, hand-written | `Renko` | bricks are rebuilt over the full series each call in a plain loop; the `extrema scan` needle catches the library calls, not the loop |
| last-row reads in callbacks | `UziChan`, `UziChan2` | `dataframe.iloc[-1]` inside `custom_*` callbacks; whether it leaks depends on how the frame was stored, which text alone cannot decide |
| randomness in the signal | `BuyAllSellAllStrategy`, `FrostAuraRandomStrategy` | reported under category 4, deliberately not as lookahead — so they stay in this column on purpose |
| unknown | `ElliotWave`, `grad`, `MSO`, `BBBreakoutStrategy` | not diagnosed. Listed rather than dropped |

Five strategies left this table on the same day when two needle families were
borrowed: four `AlexBattleTankKiller` variants (`.bfill()` after an
interpolation) and `NeuroV1` (`scipy.signal.find_peaks`).

## The auditor's own false positives, and how they were removed

The auditor was first run on 68 files from one community and produced no false
positives. Run on 314 files from eight authors it produced **13 false
accusations out of 26 flags.** Diversity of style, not size, is what exposes a
needle. Each class was fixed once, and each fix is paired in the selftest with
a *boundary control* — a line that must still be caught — because silencing a
check and blinding it look identical on screen.

```
needle caught                        it actually was                       false
`future_`                            `from __future__ import annotations`      6
`MinMaxScaler`                       an import line, not a use                 2
`(x-x.min())/(x.max()-x.min())`      a helper whose only call is commented out 2
`datas[1]`  (backtrader)             the second data feed, not a future bar    1
`center=True`                        compensated by `.shift(2)` — correct code 1
`future_gain = …`                    a training label                          1
`'future_green': {…}`                a plot-config key                         2  (found in calibration)
```

Precision on the same 314 files went from 50 % to 81 % with no true finding
lost; on the 219 dynamically-clean strategies above it is 100 %.

## The corpus behind the static sweep — and why half of it is not there

The static auditor was also run over a **search-defined** corpus: every GitHub
repository returned by nine fixed queries (`freqtrade strategies`,
`backtrader strategies`, `jesse strategy crypto`, …), cloned shallowly, plus
the 53 repositories of this ledger.

```
repositories cloned                          188
repositories with at least one strategy      135
strategy files                              4912
strategy files distinct by content          2173
copies of the same file in other repos      2739   (56 %)
randomness in the signal (category 4)         30
```

**More than half of the public freqtrade strategy corpus is the same
strategies copied between repositories.** Four different accounts publish `NostalgiaForInfinity`
as their own. A survey that counts files counts most strategies twice; this
one deduplicates by content hash and credits each strategy to the first
repository (alphabetically) it appears in — a tie-break, not an attribution.

The 895 strategies of the main ledger were *run*; the 2078 here were *read*.
The two numbers are not the same measurement and this repository does not add
them together.

## Lineage — who copied whom, and what came with it

Because the sweep hashes every strategy by content, it can also say where
each one lives. `foreign_strategy_audit.py --lineage` prints, per distinct
strategy, every repository that carries a byte-identical copy — and whether
any of those copies sits in a folder its owner uses to mark strategies as
broken.

```
distinct strategies                                   2173
present in two or more repositories                    846
lineages where some copy is marked broken by its owner  51
copies of those that carry NO mark                      89
```

**89 copies of strategies that one owner has explicitly labelled as
lookahead-biased sit in other people's repositories with no label at all.**
`NostalgiaForInfinityX`, `NostalgiaForInfinityNextGen`, `Schism2MM`, `Minmax`,
`RaposaDivergenceV1` — each marked in `RoboticAutomations/freqtradestrategies`
under `dirty LA/` (their name for *dirty lookahead*, 137 files, each with the
flagged line in their `docs/LOOKAHEAD.md`) and each present, unmarked, in five
to seven other collections.

Two things this does not say. It does not say who copied from whom: the order
is alphabetical, a tie-break, not an attribution. And it counts byte-identical
copies only; an edited fork — `ntsd`'s `DevilStra2`, 70 changed lines out of
720, a renamed copy of a strategy the freqtrade project itself keeps in
`lookahead_bias/` — is exactly the case this was built for, and exactly the
case a content hash cannot see. That blind spot is named rather than papered
over.

For the strategies above the dynamic ledger has *no* verdict: they fell at
earlier gates (did not load, or made no trades) before `lookahead-analysis`
ran. On them, their owner's static label is the only verdict there is.

## A third detector

`RoboticAutomations/freqtradestrategies` did what this page does, independently:
an `ast`-based static scan, twelve rules, hit counts published, and a stated
refusal to run 1,286 unverified files — the same trade-off, made the same way.
Three detectors now exist for the same question, and they can be measured
against each other.

| | precision | sensitivity | measured on |
|---|---:|---:|---|
| freqtrade `lookahead-analysis` (dynamic) | — | — | the ground truth here; runs the code |
| this static auditor | 13/13 | 13/29 = 45 % | 248 ledger strategies with a dynamic verdict |
| RoboticAutomations `dirty LA` | 7/9 | 7/40 = 18 % | all 284, matched **by file name** |
| this auditor on *their* 125 labelled files | — | 124/125 | agreement, not truth |

Their by-name numbers carry a caveat their own README would insist on: a name
in two repositories is not always the same file, and two of their nine
"false" alarms may be different versions of `NOTankAi_15`.

What each catches that the other does not, read from the rule lists rather
than guessed: they have `backfill`, `extrema_scan`, `negative_diff`,
`reverse_index` and `iloc_last_assign`; this auditor had none of those. It has
time-interpolation of a resampled series (their `interpolate_back` rule looks
for an explicit backward direction and scored zero hits), dead-code exclusion
and import exclusion; they have none of those. Two of their families were
adopted here the same day, each with a boundary control, and re-measured
before being kept: sensitivity 28 % → 45 %, precision unchanged at 100 %.
That is what a third detector is for.

## Run it

```bash
python foreign_strategy_audit.py --selftest              # 48 cases, exit 0
python foreign_strategy_audit.py --root  path/to/repo --lang en
python foreign_strategy_audit.py --corpus path/to/many/ --lang en   # dedups by content
python foreign_strategy_audit.py --lineage path/to/many/           # who copied whom
python calibrate.py --ledger LEDGER.csv --corpus path/to/many/     # the matrix above
```

`calibrate.py` regenerates the confusion matrix on this page from the ledger
and a directory of cloned repositories, and lists every dynamically-found
strategy either with the mechanism the static auditor sees or with the words
*mechanism unknown*. That second count is a debt, and it is printed as one.

Standard library only. The file is byte-identical to its owner in a private
repository and `sync_repo.py` refuses a commit where it is not declared.
