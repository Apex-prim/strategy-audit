# -*- coding: utf-8 -*-
u"""DCA in the corpus: detection, group comparison, and a paired A/B.

    python dca.py            print the block
    python dca.py --publish  rewrite DCA.csv and the machine block in DCA.md

WHY THIS FILE EXISTS. Someone in the freqtrade Discord asked whether anyone
would share results from a DCA (dollar-cost-averaging) strategy. The corpus
already contains the answer: 895 community strategies, some of which enable
`position_adjustment_enable` and implement `adjust_trade_position`. That is
DCA as running code, not as an opinion.

DETECTION IS STRUCTURAL, NOT LEXICAL. Grepping for the word would count a
comment, a docstring and commented-out code as the real thing. Worse, a
per-file count silently merges two DIFFERENT classes in one file (flag on one,
method on the other). So: parse the AST, find the ClassDef whose name matches
the strategy, walk base classes defined in the same file, and require all
three of flag / method / a method that returns a value.

THE MEASUREMENT THAT MATTERS IS THE DENOMINATOR. A ladder strategy RESERVES
capital: its `custom_stake_amount` divides the first entry by the ladder
multiplier when the flag is on. So "DCA on" and "DCA off" are different
POSITION SIZES, not just different mechanisms, and comparing wallet-percentage
totals compares exposure. Both denominators are published here, side by side,
because they point in opposite directions and only one of them is a fair
comparison.

Sources this file reads (none of them are typed by hand):
  LEDGER.csv          the published per-strategy record
  <root>/repos/...    the strategy sources (fetch with corpus.py)
  <root>/results/...  the per-strategy result cards
  dca_ab_2024.json    raw paired A/B output, one entry per strategy
"""
from __future__ import print_function

import ast
import csv
import io
import json
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(HERE)
LEDGER = os.path.join(HERE, "LEDGER.csv")
AB = os.path.join(HERE, "dca_ab_2024.json")
BEGIN = u"<!-- DCA:BEGIN -->"
END = u"<!-- DCA:END -->"


# ─────────────────────────────────────────────── detection
def class_facts(cls):
    flag = None
    meth = ret = False
    for st in cls.body:
        if isinstance(st, (ast.Assign, ast.AnnAssign)):
            tgts = st.targets if isinstance(st, ast.Assign) else [st.target]
            for t in tgts:
                if isinstance(t, ast.Name) and t.id == "position_adjustment_enable":
                    v = st.value
                    flag = False if (isinstance(v, ast.Constant)
                                     and v.value is False) else True
        if isinstance(st, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                and st.name == "adjust_trade_position":
            meth = True
            for sub in ast.walk(st):
                if isinstance(sub, ast.Return) and sub.value is not None:
                    if not (isinstance(sub.value, ast.Constant)
                            and sub.value.value is None):
                        ret = True
    return flag, meth, ret


def resolve(path, name):
    try:
        tree = ast.parse(io.open(path, encoding="utf-8", errors="replace").read())
    except Exception:
        return None
    classes = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)}
    if name not in classes:
        if len(classes) != 1:
            return None
        name = list(classes)[0]
    flag = None
    meth = ret = False
    seen, stack = set(), [name]
    while stack:
        cn = stack.pop(0)
        if cn in seen or cn not in classes:
            continue
        seen.add(cn)
        f, m, r = class_facts(classes[cn])
        if flag is None and f is not None:
            flag = f
        meth, ret = meth or m, ret or r
        for b in classes[cn].bases:
            if isinstance(b, ast.Name):
                stack.append(b.id)
            elif isinstance(b, ast.Attribute):
                stack.append(b.attr)
    return bool(flag), meth, ret


def detect():
    rows = list(csv.DictReader(io.open(LEDGER, encoding="utf-8")))
    out = []
    for r in rows:
        c = resolve(os.path.join(ROOT, r["file"].replace("/", os.sep)),
                    r["strategy"])
        flag, meth, ret = c if c else (False, False, False)
        out.append(dict(strategy=r["strategy"], repo=r["repo"], file=r["file"],
                        dropped_at=r["dropped_at"], beats_bh=r["beats_bh"],
                        flag=int(bool(flag)), method=int(bool(meth)),
                        returns_value=int(bool(ret)),
                        dca_active=int(bool(flag and meth and ret)),
                        # method present, flag absent: the author keeps the flag
                        # in their own config.json, which this sweep replaced
                        # with its own. Their DCA did not run here.
                        suppressed_by_our_config=int(bool(meth and not flag))))
    return out


# ─────────────────────────────────────────────── helpers with no dependencies
def median(v):
    v = sorted(v)
    n = len(v)
    if n == 0:
        return float("nan")
    return v[n // 2] if n % 2 else 0.5 * (v[n // 2 - 1] + v[n // 2])


def comb(n, k):
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r


def sign_test(pos, n):
    u"""Exact two-sided binomial test at p=0.5. No dependency, no excuse."""
    lo = min(pos, n - pos)
    tail = sum(comb(n, k) for k in range(lo + 1))
    return min(1.0, 2.0 * tail / float(2 ** n))


def card(name):
    p = os.path.join(ROOT, "results", name + ".json")
    if not os.path.exists(p):
        return None
    try:
        return json.load(io.open(p, encoding="utf-8"))
    except Exception:
        return None


def num(v):
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return f


# ─────────────────────────────────────────────── the block
def block(rows):
    L = []
    a = L.append
    a(u"generated by dca.py — do not edit by hand")
    n = len(rows)
    act = [r for r in rows if r["dca_active"]]
    a(u"strategies in ledger          %4d" % n)
    a(u"  position_adjustment_enable  %4d" % sum(r["flag"] for r in rows))
    a(u"  adjust_trade_position       %4d" % sum(r["method"] for r in rows))
    a(u"  DCA actually active         %4d   (%.1f%% of the corpus)"
      % (len(act), 100.0 * len(act) / n))
    a(u"  flag set, no method         %4d   (the flag does nothing)"
      % sum(1 for r in rows if r["flag"] and not r["method"]))
    a(u"  method, flag not in class   %4d   (freqtrade never calls it here)"
      % sum(r["suppressed_by_our_config"] for r in rows))
    a(u"")

    # ── group comparison, out of sample
    led = {r["strategy"]: r for r in csv.DictReader(io.open(LEDGER, encoding="utf-8"))}
    def stats(sub, key, from_card=None):
        v = []
        for r in sub:
            if from_card:
                c = card(r["strategy"])
                if not c:
                    continue
                s = (c.get("runs", {}).get("out_sample", {}) or {}).get("summary") or {}
                x = num(s.get(from_card))
            else:
                x = num(led[r["strategy"]].get(key))
            if x is not None:
                v.append(x)
        return v
    D = act
    N = [r for r in rows if not r["dca_active"]]
    a(u"out of sample, medians                     DCA      non-DCA")
    for lab, key, ck in ((u"win rate, %", None, "win_pct"),
                         (u"profit factor", None, "profit_factor"),
                         (u"expectancy per trade", "os_exp", None),
                         (u"trades", "os_trades", None)):
        d, nn = stats(D, key, ck), stats(N, key, ck)
        if len(d) >= 5 and len(nn) >= 5:
            a(u"  %-38s %8.2f %12.2f" % (lab, median(d), median(nn)))
    # average loss / average win, from win rate and profit factor
    def ratio(sub):
        out = []
        for r in sub:
            c = card(r["strategy"])
            if not c:
                continue
            s = (c.get("runs", {}).get("out_sample", {}) or {}).get("summary") or {}
            w, pf = num(s.get("win_pct")), num(s.get("profit_factor"))
            if w and pf and 0 < w < 100 and pf > 0:
                out.append((w / (100.0 - w)) / pf)
        return out
    rd, rn = ratio(D), ratio(N)
    if rd and rn:
        a(u"  %-38s %8.2f %12.2f" % (u"average loss / average win", median(rd), median(rn)))
    a(u"  %-38s %8d %12d"
      % (u"cleared the whole ladder", sum(1 for r in D if not r["dropped_at"]),
         sum(1 for r in N if not r["dropped_at"])))
    a(u"")

    # ── paired A/B
    if os.path.exists(AB):
        ab = json.load(io.open(AB, encoding="utf-8"))
        pairs, fired = 0, []
        for k, v in ab.items():
            on, off = v.get("on") or {}, v.get("off") or {}
            if "error" in on or "error" in off or not on or not off:
                continue
            pairs += 1
            if (on["entries"] > on["trades"]) or (on["exits"] > on["trades"]):
                fired.append((k, on, off))
        a(u"paired A/B — the same code with the mechanism on and off, 2024")
        a(u"  pairs that ran              %4d" % pairs)
        a(u"  mechanism actually fired    %4d   (the rest carry no information)"
          % len(fired))
        wallet = [on["total_pct"] - off["total_pct"] for _, on, off in fired]
        cap = [on["total_abs"] / on["peak_sum"] * 1e4
               - off["total_abs"] / off["peak_sum"] * 1e4
               for _, on, off in fired if on["peak_sum"] and off["peak_sum"]]
        pw = sum(1 for x in wallet if x > 0)
        pc = sum(1 for x in cap if x > 0)
        a(u"")
        a(u"  denominator                       median diff   better in   sign test")
        a(u"  total, %% of wallet              %+10.2f pp   %2d of %2d   %9.4f"
          % (median(wallet), pw, len(wallet), sign_test(pw, len(wallet))))
        a(u"  return per unit of capital      %+10.1f bps   %2d of %2d   %9.4f"
          % (median(cap), pc, len(cap), sign_test(pc, len(cap))))
        a(u"")
        a(u"  The same pairs, the same year. One denominator says the mechanism")
        a(u"  helps, the other says it costs. A ladder strategy reserves capital,")
        a(u"  so with the flag on it enters SMALLER: the first row compares")
        a(u"  exposure, the second compares the mechanism.")
    return u"\n".join(L)


def main():
    rows = detect()
    blk = block(rows)
    if "--publish" not in sys.argv:
        print(blk)
        return 0
    with io.open(os.path.join(HERE, "DCA.csv"), "w", encoding="utf-8",
                 newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            w.writerow(r)
    p = os.path.join(HERE, "DCA.md")
    text = io.open(p, encoding="utf-8").read() if os.path.exists(p) else u""
    if BEGIN in text and END in text:
        head = text[:text.index(BEGIN)]
        tail = text[text.index(END) + len(END):]
        text = head + BEGIN + u"\n```\n" + blk + u"\n```\n" + END + tail
        io.open(p, "w", encoding="utf-8").write(text)
        print(u"DCA.csv and the block in DCA.md rewritten")
    else:
        print(u"DCA.md has no machine block markers — nothing rewritten")
    return 0


if __name__ == "__main__":
    sys.exit(main())
