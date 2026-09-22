# -*- coding: utf-8 -*-
"""calibrate — the static auditor measured against the dynamic one.

WHY THIS EXISTS. LEDGER.csv carries a dynamic lookahead verdict for 284
strategies, produced by running `freqtrade lookahead-analysis`. The static
auditor (`foreign_strategy_audit.py`) reads source instead. This script puts
the two side by side on the same files and prints a confusion matrix — so the
static auditor's worth is a number computed here, not a sentence in STATIC.md.

It also does the thing the dynamic verdict cannot: for every strategy the
dynamic analyser found, it prints the *mechanism* the static one sees, or the
words "mechanism unknown". A verdict without a cause is prose; this turns 40
prose verdicts into N explained and (40 - N) unexplained, and the unexplained
count is a debt with a number.

    python calibrate.py --ledger LEDGER.csv --corpus path/to/repos
    python calibrate.py --selftest

The corpus directory holds one sub-directory per repository, named
`owner_repo` (as `harvest.py` and `reproduce.sh` produce). Strategies whose
repository is not on disk are counted as "not on disk", never as clean.
"""
from __future__ import print_function

import argparse
import csv
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

FOUND, PASSED = u"\u041d\u0410\u0419\u0414\u0415\u041d\u041e", u"\u041f\u0420\u041e\u0428\u041b\u0410"   # НАЙДЕНО / ПРОШЛА


def locate(corpus, repo, relfile):
    """Path on disk for a ledger row: by recorded path first, then by name."""
    d = os.path.join(corpus, repo.replace("/", "_"))
    if not os.path.isdir(d):
        return None
    rest = relfile.split("/", 2)[2] if relfile.count("/") >= 2 else relfile
    p = os.path.join(d, rest)
    if os.path.isfile(p):
        return p
    base = os.path.basename(relfile)
    for dp, dn, fn in os.walk(d):
        dn[:] = [x for x in dn if x != ".git"]
        if base in fn:
            return os.path.join(dp, base)
    return None


def calibrate(rows, corpus, check, framework_of):
    """rows: iterable of dicts with strategy/repo/file/lookahead.

    Returns (matrix, explained, unexplained, false_alarms, missing) where
    matrix is {"tp","fp","fn","tn"} and the lists carry (strategy, repo, evidence).
    """
    m = {"tp": 0, "fp": 0, "fn": 0, "tn": 0}
    explained, unexplained, false_alarms, missing = [], [], [], []
    for r in rows:
        v = r["lookahead"]
        if v not in (FOUND, PASSED):
            continue
        p = locate(corpus, r["repo"], r["file"])
        if p is None:
            missing.append((r["strategy"], r["repo"]))
            continue
        src = io.open(p, encoding="utf-8", errors="replace").read()
        hits = check(src, framework=framework_of(src))
        truth = v == FOUND
        if truth and hits:
            m["tp"] += 1
            explained.append((r["strategy"], r["repo"], "%d: %s" % hits[0]))
        elif truth:
            m["fn"] += 1
            unexplained.append((r["strategy"], r["repo"], "mechanism unknown"))
        elif hits:
            m["fp"] += 1
            false_alarms.append((r["strategy"], r["repo"], "%d: %s" % hits[0]))
        else:
            m["tn"] += 1
    return m, explained, unexplained, false_alarms, missing


def _pct(a, b):
    return "%d/%d = %.0f %%" % (a, b, 100.0 * a / b) if b else "n/a"


def report(m, explained, unexplained, false_alarms, missing):
    n = sum(m.values())
    print("-- STATIC vs DYNAMIC (freqtrade lookahead-analysis)  matched %d" % n)
    print("   not on disk: %d" % len(missing))
    print()
    print("                        dynamic FOUND   dynamic PASSED")
    print("   static FLAGS          %6d (TP)      %6d (FP)" % (m["tp"], m["fp"]))
    print("   static silent         %6d (FN)      %6d (TN)" % (m["fn"], m["tn"]))
    print()
    print("   precision    TP/(TP+FP)  %s" % _pct(m["tp"], m["tp"] + m["fp"]))
    print("   false alarm  FP/(FP+TN)  %s" % _pct(m["fp"], m["fp"] + m["tn"]))
    print("   sensitivity  TP/(TP+FN)  %s" % _pct(m["tp"], m["tp"] + m["fn"]))
    print()
    print("-- DYNAMIC FOUND, MECHANISM EXPLAINED BY STATIC  %d" % len(explained))
    for s, r, e in explained:
        print("   %-32s %-36s %s" % (s[:32], r[:36], e[:60]))
    print()
    print("-- DYNAMIC FOUND, MECHANISM UNKNOWN  %d   <- this number is a debt"
          % len(unexplained))
    for s, r, e in unexplained:
        print("   %-32s %s" % (s[:32], r[:36]))
    print()
    print("-- STATIC FLAGGED, DYNAMIC CLEAN  %d   <- read each; a flag is a "
          "candidate, not a finding" % len(false_alarms))
    for s, r, e in false_alarms:
        print("   %-32s %-36s %s" % (s[:32], r[:36], e[:60]))
    print()
    print("   A zero from the static auditor means none of the forms it knows,")
    print("   not clean. The judge is harness.py, which runs the code.")


# -- selftest: a two-row ledger and a two-file corpus, on disk, so that the
#    path-location logic is exercised and not only the arithmetic.
def _probe():
    import shutil
    import tempfile
    d = tempfile.mkdtemp(prefix="calib_")
    try:
        repo = os.path.join(d, "o_r")
        os.makedirs(repo)
        dirty = ("class S:\n    def populate_entry_trend(self, df, m):\n"
                 "        df['f'] = df['close'].shift(-1)\n        return df\n")
        clean = ("class S:\n    def populate_entry_trend(self, df, m):\n"
                 "        return df\n")
        io.open(os.path.join(repo, "Dirty.py"), "w", encoding="utf-8").write(dirty)
        io.open(os.path.join(repo, "Clean.py"), "w", encoding="utf-8").write(clean)
        io.open(os.path.join(repo, "Missed.py"), "w", encoding="utf-8").write(clean)
        rows = [
            {"strategy": "Dirty", "repo": "o/r", "file": "repos/o_r/Dirty.py",
             "lookahead": FOUND},
            {"strategy": "Clean", "repo": "o/r", "file": "repos/o_r/Clean.py",
             "lookahead": PASSED},
            # dynamic found it, static cannot see it: must land in FN, never TN
            {"strategy": "Missed", "repo": "o/r", "file": "repos/o_r/Missed.py",
             "lookahead": FOUND},
            {"strategy": "Gone", "repo": "o/x", "file": "repos/o_x/Gone.py",
             "lookahead": FOUND},
        ]
        from foreign_strategy_audit import check_lookahead, framework_of
        return calibrate(rows, d, check_lookahead, framework_of)
    finally:
        shutil.rmtree(d, ignore_errors=True)


SELFTEST = [
    ("dirty found by both -> TP",
     lambda: _probe()[0]["tp"] == 1),
    ("clean by both -> TN",
     lambda: _probe()[0]["tn"] == 1),
    ("dynamic found, static blind -> FN, listed as mechanism unknown",
     lambda: _probe()[0]["fn"] == 1 and _probe()[2][0][2] == "mechanism unknown"),
    ("repo not on disk -> missing, never clean",
     lambda: _probe()[4] == [("Gone", "o/x")] and _probe()[0]["tn"] == 1),
    ("no false alarm planted -> FP is exactly zero",
     lambda: _probe()[0]["fp"] == 0),
    # WIRING (2026-09-22): the cases above call calibrate() directly; none
    # proved that main() reads the ledger file, finds the corpus, and prints
    # the matrix. These drive main() itself.
    ("main(): ledger file + corpus -> matrix printed, TP 1, code 0",
     lambda: _main_on_disk() == (0, True)),
    ("main(): no corpus -> refused with code 2, not a matrix of zeros",
     lambda: _main_quiet(["calibrate.py", "--corpus", ""])[0] == 2),
]


def _main_quiet(argv):
    buf, old, olde = io.StringIO(), sys.stdout, sys.stderr
    sys.stdout, sys.stderr = buf, io.StringIO()
    try:
        return main(argv), buf.getvalue()
    finally:
        sys.stdout, sys.stderr = old, olde


def _main_on_disk():
    import shutil
    import tempfile
    d = tempfile.mkdtemp(prefix="calib_main_")
    try:
        repo = os.path.join(d, "o_r")
        os.makedirs(repo)
        io.open(os.path.join(repo, "Dirty.py"), "w", encoding="utf-8").write(
            "class S:\n    def populate_entry_trend(self, df, m):\n"
            "        df['f'] = df['close'].shift(-1)\n        return df\n")
        led = os.path.join(d, "ledger.csv")
        with io.open(led, "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["strategy", "repo", "file", "lookahead"])
            w.writerow(["Dirty", "o/r", "repos/o_r/Dirty.py", FOUND])
        code, out = _main_quiet(["calibrate.py", "--ledger", led,
                                 "--corpus", d])
        return code, "1 (TP)" in out
    finally:
        shutil.rmtree(d, ignore_errors=True)


def selftest():
    ok = fail = 0
    for name, fn in SELFTEST:
        try:
            good = bool(fn())
        except Exception as ex:                          # noqa: BLE001
            good = False
            print("  x %s -- %r" % (name, ex))
        if good:
            ok += 1
        else:
            fail += 1
            print("  x %s" % name)
    print("SELFTEST calibrate: %d passed, %d failed" % (ok, fail))
    return 1 if fail else 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", default=os.path.join(HERE, "LEDGER.csv"))
    ap.add_argument("--corpus", default="")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv[1:])
    if a.selftest:
        return selftest()
    if not a.corpus or not os.path.isdir(a.corpus):
        sys.stderr.write("refused (2): --corpus must be a directory of repositories\n")
        return 2
    if not os.path.isfile(a.ledger):
        sys.stderr.write("refused (2): ledger not found: %s\n" % a.ledger)
        return 2
    from foreign_strategy_audit import check_lookahead, framework_of
    rows = list(csv.DictReader(io.open(a.ledger, encoding="utf-8")))
    report(*calibrate(rows, a.corpus, check_lookahead, framework_of))
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    sys.exit(main(sys.argv))
