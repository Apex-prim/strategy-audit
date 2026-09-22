# -*- coding: utf-8 -*-
u"""verify_ledger — the published numbers must be reproducible from the
published data, on a machine that has nothing else.

WHAT IT DOES. Reads `LEDGER.csv`, rebuilds the block of counts, and compares it
to the block sitting between the markers in `README.md`. Exit code 1 on any
difference. No candle data, no clones, no freqtrade — only the two files this
repository publishes.

WHY IT EXISTS. On 2026-08-21 the README of this repository said *571 strategies,
55 clean* for about a day after the corpus had grown past 900, and an external
reviewer built a favourable assessment on those figures plus two scripts that
had already been deleted. Nothing was false when written. It simply went stale,
and staleness reads exactly like authority to anyone who was not there.

A rule with no return code does not hold. This is the return code.

    python verify_ledger.py             compare and exit 1 on mismatch
    python verify_ledger.py --selftest  prove the comparison can fail

The self-test is not decoration. A check that has never been shown to reject
anything has not been checked itself — it has only been observed to agree. So
the self-test plants a changed verdict in a copy of the rows and requires the
rebuilt block to differ, then requires an unchanged copy to match.
"""
from __future__ import print_function

import csv
import io
import json
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

from ledger_block import build

BEGIN = u"<!-- LEDGER:BEGIN -->"
END = u"<!-- LEDGER:END -->"

NUM = ("is_trades", "is_exp", "is_p", "is_market", "os_trades", "os_exp",
       "os_p", "os_total", "os_market", "traps_n", "dur_over_candle")


def num(v):
    if v is None or v == "":
        return None
    try:
        return float(v)
    except ValueError:
        return None


def rows_from_csv(path):
    out = []
    with io.open(path, encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            d = dict(r)
            for k in NUM:
                d[k] = num(d.get(k))
            # Python's csv gives strings; "True"/"False"/"" must become a
            # three-valued answer, not a truthy string. "False" is truthy.
            b = (d.get("beats_bh") or "").strip()
            d["beats_bh"] = True if b == "True" else (False if b == "False" else None)
            out.append(d)
    return out


def n_repos(root=None):
    u"""Зовём ту же реализацию, что и ledger.py. Раньше здесь была копия, и
    обе копии ошибались одинаково — поэтому сверка молчала."""
    from ledger_block import n_repos as _n
    return _n(os.path.join(root or _HERE, "corpus_sources.json"))


# ── OUTSIDE THE BLOCK (2026-09-22) ─────────────────────────────────────
# A clean-clone check that day changed the README headline "895" to "896"
# and this script still answered "README numbers reproduce" — exit 0. It
# compared only the block between the markers: 52 of the 241 numbers in the
# README. The repository description ("a CI gate fails if the README
# disagrees") claimed more than the gate did. Now the figures that CAN be
# derived from the published files outside the block are checked too, and
# the coverage is printed instead of implied.
NUM_RX = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)?(?![\w.])")
HEAD_RX = re.compile(r"^#\s+(\d[\d,]*)\s", re.M)


def claims(root):
    path = os.path.join(root, "CLAIMS.csv")
    if not os.path.exists(path):
        return None
    with io.open(path, encoding="utf-8", newline="") as fh:
        return {r["claim"]: r["value"] for r in csv.DictReader(fh)}


def outside_checks(txt, n_rows, repos, cl):
    u"""[(what, ok, detail)] — figures outside the block that the published
    files determine. A missing CLAIMS.csv is a failure, not a pass."""
    out = []
    m = HEAD_RX.search(txt)
    out.append((u"README headline = ledger rows",
                bool(m) and int(m.group(1).replace(",", "")) == n_rows,
                u"headline %s, ledger %d" % (m.group(1) if m else u"—",
                                             n_rows)))
    if cl is None:
        out.append((u"CLAIMS.csv present", False, u"missing"))
        return out
    for key, want in ((u"strategies in corpus", n_rows),
                      (u"repositories swept", repos)):
        got = cl.get(key)
        out.append((u"CLAIMS «%s» = %d" % (key, want),
                    got is not None and got.strip() == str(want),
                    u"CLAIMS says %s" % got))
    return out


def selftest():
    u"""Diversion: change one verdict and require the block to notice."""
    base = [
        {"code_md5": "aaa", "plan_md5": "bbb", "dropped_at": "",
         "beats_bh": False, "is_trades": 100.0, "is_exp": 1.0, "is_p": 0.001,
         "os_p": 0.001, "os_exp": 1.0},
        {"code_md5": "aaa", "plan_md5": "bbb", "dropped_at": "G7_recursive",
         "beats_bh": True, "is_trades": 100.0, "is_exp": 1.0, "is_p": 0.001,
         "os_p": 0.002, "os_exp": 1.0},
        {"code_md5": "aaa", "plan_md5": "bbb", "dropped_at": "G2_is_pos",
         "beats_bh": None, "is_trades": 100.0, "is_exp": -1.0, "is_p": 0.9,
         "os_p": None, "os_exp": None},
    ]
    ok = []

    a = build(base, 3)
    b = build([dict(r) for r in base], 3)
    ok.append(("identical input gives identical block", a == b))

    # ① a strategy that used to survive now drops at E1 — the epoch table
    #    must change, or the table is not reading dropped_at at all
    hurt = [dict(r) for r in base]
    hurt[0]["dropped_at"] = "G7_recursive"
    ok.append(("a changed verdict changes the block", build(hurt, 3) != a))

    # ② the epoch table must actually separate E0 from E1: row 1 beats the
    #    market and dies at E1, so E0 and E1 cannot report the same count
    e0 = [l for l in a.splitlines() if "up to E0" in l]
    e1 = [l for l in a.splitlines() if "up to E1" in l]
    ok.append(("E0 and E1 are reported separately",
               bool(e0) and bool(e1) and e0[0].split("survivors")[1]
               != e1[0].split("survivors")[1]))

    # ③ the repository count is carried, not invented
    ok.append(("repository count appears", "repositories swept   3" in a))

    # ④ the repo count must be sanity-checked by something other than the
    #    formula that produced it. On 2026-08-22 the README shipped
    #    "repositories swept 3" instead of 53, and this comparison stayed
    #    silent because BOTH sides used the same wrong formula. Agreement is
    #    not correctness.
    many = [dict(base[0]) for _ in range(900)]
    ok.append(("an implausible repo count is flagged",
               "SUSPECT" in build(many, 3)))
    ok.append(("a plausible repo count is not flagged",
               "SUSPECT" not in build(many, 53)))

    # ⑤ mixed provenance must be announced, never averaged away
    mixed = [dict(r) for r in base]
    mixed[0]["code_md5"] = "zzz"
    ok.append(("mixed code versions are announced", "MIXED" in build(mixed, 3)))

    # ⑥ WIRING (2026-09-22): the unit cases above never ran main(). On a
    #    copy of the four real published files, main() itself must pass the
    #    unchanged copy and FAIL each planted lie — including the one lived
    #    that day, the headline changed 895 -> 896 while CI stayed green.
    ok.extend(_wiring())

    bad = [n for n, v in ok if not v]
    for n, v in ok:
        print(u"  %-42s %s" % (n, u"OK" if v else u"FAILED"))
    print(u"self-test: %d/%d" % (len(ok) - len(bad), len(ok)))
    return 1 if bad else 0


def _wiring():
    import shutil
    import tempfile
    need = ("LEDGER.csv", "README.md", "CLAIMS.csv", "corpus_sources.json")
    if not all(os.path.exists(os.path.join(_HERE, f)) for f in need):
        return [(u"main() wiring: published files present", False)]

    def run(mutate):
        d = tempfile.mkdtemp(prefix="vledger_")
        try:
            for f in need:
                shutil.copy(os.path.join(_HERE, f), d)
            if mutate:
                mutate(d)
            buf, old = io.StringIO(), sys.stdout
            sys.stdout = buf
            try:
                return main([], root=d)
            finally:
                sys.stdout = old
        finally:
            shutil.rmtree(d, ignore_errors=True)

    def edit(name, fn):
        def m(d):
            p = os.path.join(d, name)
            t = io.open(p, encoding="utf-8", newline="").read()
            io.open(p, "w", encoding="utf-8", newline="").write(fn(t))
        return m

    def bump_headline(t):
        m = HEAD_RX.search(t)
        return t[:m.start(1)] + str(int(m.group(1).replace(",", "")) + 1) + \
            t[m.end(1):]

    def bump_block(t):
        a = t.index(BEGIN)
        m = NUM_RX.search(t, t.index("\n", t.index("\n", a) + 1))
        return t[:m.start()] + "9" + t[m.start():]

    def bump_claims(t):
        return t.replace(u"strategies in corpus,", u"strategies in corpus,1", 1)

    return [
        (u"main(): unchanged published copy passes", run(None) == 0),
        (u"main(): headline +1 fails (lived 2026-09-22)",
         run(edit("README.md", bump_headline)) == 1),
        (u"main(): a number inside the block fails",
         run(edit("README.md", bump_block)) == 1),
        (u"main(): CLAIMS strategies wrong fails",
         run(edit("CLAIMS.csv", bump_claims)) == 1),
        (u"main(): CLAIMS.csv missing fails",
         run(lambda d: os.remove(os.path.join(d, "CLAIMS.csv"))) == 1),
    ]


def main(argv=None, root=None):
    argv = sys.argv[1:] if argv is None else argv
    if "--selftest" in argv:
        return selftest()
    root = root or _HERE
    csv_path = os.path.join(root, "LEDGER.csv")
    md_path = os.path.join(root, "README.md")
    if not os.path.exists(csv_path):
        print(u"REFUSED: LEDGER.csv is missing — the published numbers cannot")
        print(u"be checked against anything. That is a failure, not a pass.")
        return 1

    rows = rows_from_csv(csv_path)
    repos = n_repos(root)
    want = build(rows, repos).strip()

    txt = io.open(md_path, encoding="utf-8").read()
    if BEGIN not in txt or END not in txt:
        print(u"REFUSED: README.md carries no ledger markers")
        return 1
    have = txt.split(BEGIN, 1)[1].split(END, 1)[0].strip()
    extra = outside_checks(txt, len(rows), repos, claims(root))

    n_all = len(NUM_RX.findall(txt))
    n_block = len(NUM_RX.findall(have))
    cover = (u"coverage: %d of %d numbers in README.md are checked (the "
             u"block, the headline, and CLAIMS.csv against the ledger); the "
             u"other %d are prose and are NOT checked by this script"
             % (n_block + 1, n_all, n_all - n_block - 1))

    bad_extra = [e for e in extra if not e[1]]
    if have == want and not bad_extra:
        print(u"README numbers reproduce from LEDGER.csv (%d rows)" % len(rows))
        print(u"  " + cover)
        return 0

    if have != want:
        print(u"MISMATCH: the README block does not reproduce from LEDGER.csv")
        hl, wl = have.splitlines(), want.splitlines()
        for i in range(max(len(hl), len(wl))):
            a = hl[i] if i < len(hl) else u"(no line)"
            b = wl[i] if i < len(wl) else u"(no line)"
            if a != b:
                print(u"  README: %s" % a)
                print(u"  ledger: %s" % b)
    for what, _, detail in bad_extra:
        print(u"MISMATCH outside the block: %s — %s" % (what, detail))
    return 1


if __name__ == "__main__":
    sys.exit(main())
