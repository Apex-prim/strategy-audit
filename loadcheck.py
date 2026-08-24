# -*- coding: utf-8 -*-
"""loadcheck — why did 399 strategies never get measured?

WHERE THIS CAME FROM. froggleston, in the freqtrade Discord: "it also doesn't
list strategies that simply don't load." He is right, and I did not have the
number. The funnel showed 399 strategies falling at the first gate with one
label on them, G0_measured, which says only that both halves failed to
produce a result. It does not say why.

A strategy that will not import, one that imports and never trades, and one
that timed out are three different facts. Collapsing them is a survivorship
filter that was never declared: the corpus quietly became "code that still
runs", and nobody was told.

HOW THE REASON IS RECOVERED. It was not recorded at run time, so it is
reconstructed two ways, cheapest first:

  1. From the ledger. If either window produced a trade count, the file
     loaded. That settles those without running anything.
  2. For the rest, the module is imported in a subprocess with a timeout and
     the exception is kept. Import is seconds; a backtest is minutes.

    python loadcheck.py --run     classify, writes loadcheck_run.json
    python loadcheck.py           render loadcheck_run.json into CORRECTIONS.md
"""
from __future__ import print_function

import csv
import io
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(HERE)
RUN = os.path.join(HERE, "loadcheck_run.json")
LEDGER = os.path.join(HERE, "LEDGER.csv")
TIMEOUT_S = 60
WORKERS = 6

PROBE = r"""
import sys, importlib.util, warnings
warnings.filterwarnings("ignore")
path = sys.argv[1]
try:
    spec = importlib.util.spec_from_file_location("probe_mod", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
except SyntaxError as e:
    print("SYNTAX|%s" % (str(e).split("(")[0].strip()[:80],)); raise SystemExit(0)
except ImportError as e:
    print("IMPORT|%s" % (str(e)[:80],)); raise SystemExit(0)
except BaseException as e:
    print("OTHER|%s: %s" % (type(e).__name__, str(e)[:70])); raise SystemExit(0)
try:
    from freqtrade.strategy import IStrategy
except Exception:
    print("NOFREQTRADE|"); raise SystemExit(0)
found = [n for n in dir(mod)
         if isinstance(getattr(mod, n), type)
         and issubclass(getattr(mod, n), IStrategy)
         and getattr(mod, n) is not IStrategy]
print("OK|%d" % len(found))
"""


def rows():
    with io.open(LEDGER, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def probe(path):
    p = os.path.join(HERE, "_probe.py")
    try:
        out = subprocess.run([sys.executable, p, path], capture_output=True,
                             timeout=TIMEOUT_S)
        text = (out.stdout or b"").decode("utf-8", "replace").strip().split("\n")[-1]
        if "|" not in text:
            return "SILENT", (out.stderr or b"").decode("utf-8", "replace")[-80:]
        kind, detail = text.split("|", 1)
        return kind, detail
    except subprocess.TimeoutExpired:
        return "TIMEOUT", "%ds" % TIMEOUT_S
    except Exception as e:
        return "PROBE_FAILED", repr(e)[:60]


def classify():
    io.open(os.path.join(HERE, "_probe.py"), "w", encoding="utf-8").write(PROBE)
    g0 = [r for r in rows() if r.get("dropped_at") == "G0_measured"]
    # (1) the ledger already settles the ones that produced a count anywhere
    loaded_by_ledger, unknown = [], []
    for r in g0:
        if (r.get("is_trades") or "").strip() or (r.get("os_trades") or "").strip():
            loaded_by_ledger.append(r)
        else:
            unknown.append(r)
    print("G0 total %d | settled by ledger (a window produced trades) %d | to probe %d"
          % (len(g0), len(loaded_by_ledger), len(unknown)))

    res = {"total_corpus": len(rows()), "g0": len(g0),
           "loaded_by_ledger": len(loaded_by_ledger), "probed": len(unknown),
           "buckets": {}, "examples": {}}

    def work(r):
        path = os.path.join(ROOT, r["file"].replace("/", os.sep))
        if not os.path.exists(path):
            return r["strategy"], "MISSING_FILE", path[-60:]
        k, d = probe(path)
        return r["strategy"], k, d

    done = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        for name, kind, detail in ex.map(work, unknown):
            key = kind if kind != "OK" else ("OK_NO_CLASS" if detail == "0" else "OK_LOADS")
            res["buckets"][key] = res["buckets"].get(key, 0) + 1
            res["examples"].setdefault(key, [])
            if len(res["examples"][key]) < 3:
                res["examples"][key].append({"strategy": name, "detail": detail})
            done += 1
            if done % 40 == 0:
                print("  %d/%d" % (done, len(unknown)))
    res["buckets"]["LOADS_BUT_NO_RESULT_BOTH_WINDOWS"] = len(loaded_by_ledger)
    try:
        os.remove(os.path.join(HERE, "_probe.py"))
    except OSError:
        pass
    return res


def render(d):
    L = ["generated by loadcheck.py — do not edit by hand", ""]
    L.append("corpus %d strategies, %d never produced a measurable pair of windows"
             % (d["total_corpus"], d["g0"]))
    L.append("that bucket, split by reason:")
    order = sorted(d["buckets"].items(), key=lambda kv: -kv[1])
    for k, v in order:
        L.append("   %-38s %4d   %4.1f%% of corpus"
                 % (k, v, 100.0 * v / d["total_corpus"]))
    L.append("")
    for k, ex in d["examples"].items():
        if k in ("OK_LOADS",):
            continue
        for e in ex[:2]:
            L.append("   %-30s %s: %s" % (e["strategy"][:30], k, e["detail"][:60]))
    return "\n".join(L)


def main():
    if "--run" in sys.argv:
        d = classify()
        io.open(RUN, "w", encoding="utf-8").write(json.dumps(d, indent=1))
        print("wrote %s" % RUN)
    d = json.load(io.open(RUN, encoding="utf-8"))
    print(render(d))
    return 0


if __name__ == "__main__":
    sys.exit(main())
