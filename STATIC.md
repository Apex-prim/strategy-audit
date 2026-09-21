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
static FLAGS                   8  (TP)            0  (FP)
static is silent              21  (FN)          219  (TN)

precision      TP/(TP+FP)   =   8/8    = 100 %
false alarm    FP/(FP+TN)   =   0/219  =   0.0 %
sensitivity    TP/(TP+FN)   =   8/29   =  28 %
```

Read it plainly: **when the static auditor speaks, it has not been wrong once
on 219 clean strategies. When it is silent, it has missed almost three in four
of the real cases.** It is a pre-filter that never lies, not a judge. The judge
is `harness.py`, which runs the code.

Two flags counted as hits deserve a footnote. `LorentzianClassification:128`
builds `y_train = shift(-4)` — a training *label*, which may legitimately see
the future; the dynamic analyser flagged the strategy anyway, so the two tools
agree on the verdict while the static one may be pointing at the wrong line.
Two Ichimoku strategies were *initially* counted as hits because the needle
matched `'future_green'` in a plot-config dictionary; the verdict was right and
the evidence was wrong, so the needle was tightened and those two moved to the
misses column. Being right by accident is not being right.

## What it catches — the four forms it knows

| form | what the code looks like | why it is lookahead |
|---|---|---|
| higher timeframe interpolated back down | `df.resample('15min')…; df.resample('5min'); df.interpolate(method='time')` | the 10:05 row is a line drawn between 10:00 and **10:15**; the 10:15 candle has not closed |
| full-sample normalisation | `(x − x.min()) / (x.max() − x.min())`, `MinMaxScaler().fit_transform(x)`, `RobustScaler().fit(df)` | the value at bar *t* depends on extremes that occur after *t* |
| explicit backward shift | `close.shift(-kijun)`, `.shift(-4)` | takes a future row by name |
| centred window | `rolling(n, center=True)` | looks *n/2* bars ahead by definition — unless a matching `.shift()` puts them back, which is checked by reading, not by the needle |

A fourth category is reported separately and **not** as lookahead:

| category | looks like | why it is separate |
|---|---|---|
| randomness in the signal | `np.random.randint(0, 2, size=len(df))` | not lookahead — non-reproducibility. The dynamic analyser cannot tell a coin toss from a peek: both change the signal when the series is extended. Two of the 40 dynamic "found" are exactly this (`BuyAllSellAllStrategy`, `FrostAuraRandomStrategy`) |

## What it does not catch — the 21 misses, by family

Every one of the 21 was opened and read. They fall into forms the needle set
does not know, and each is named so that a zero from the static auditor on your
own code is read as *"none of the four forms"*, not as *"clean"*.

| family | examples in the ledger | why static is blind |
|---|---|---|
| Ichimoku forward displacement | `Ichi`, `ichiV1`, `Obelisk_TradePro_Ichi_v1_1`, `_v2_1` | the shift is inside `technical.indicators.ichimoku`, not in the strategy text |
| higher-timeframe merge done by hand | `LookaheadStrategy`, `NWEv6`, `BB_RPB_TSL` | `LookaheadStrategy` even uses the correct API (`merge_informative_pair(…, ffill=True)`) and is still flagged dynamically. I do not know why, and this page will not pretend to |
| path-dependent recomputation | `Renko` | bricks are rebuilt over the full series each call; where a brick boundary falls depends on later prices |
| last-row reads in callbacks | `UziChan`, `UziChan2` | `dataframe.iloc[-1]` inside `custom_*` callbacks; whether it leaks depends on how the frame was stored, which text alone cannot decide |
| unknown | 7 strategies from `jaredrsommer/freqtradestrategies`, `BBBreakoutStrategy` | not diagnosed. Listed rather than dropped |

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
repositories with at least one strategy      130+
strategy files                              4306
strategy files distinct by content          2078
copies of the same file in other repos      2153   (51 %)
```

**Half of the public freqtrade strategy corpus is the same strategies copied
between repositories.** Four different accounts publish `NostalgiaForInfinity`
as their own. A survey that counts files counts most strategies twice; this
one deduplicates by content hash and credits each strategy to the first
repository (alphabetically) it appears in — a tie-break, not an attribution.

The 895 strategies of the main ledger were *run*; the 2078 here were *read*.
The two numbers are not the same measurement and this repository does not add
them together.

## Run it

```bash
python foreign_strategy_audit.py --selftest              # 38 cases, exit 0
python foreign_strategy_audit.py --root  path/to/repo --lang en
python foreign_strategy_audit.py --corpus path/to/many/ --lang en   # dedups by content
```

Standard library only. The file is byte-identical to its owner in a private
repository and `sync_repo.py` refuses a commit where it is not declared.
