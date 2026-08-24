# -*- coding: utf-8 -*-
"""depth — does buying a deep drawdown work, and can you actually take it?

WHY THIS EXISTS. DCA.md measured what averaging-into-a-position does across
895 public strategies. This asks the question underneath it: after price has
already fallen by u basis points, is the next move better than average?

That question has an answer everyone thinks they know, and the answer changes
sign depending on how deep you cut. Shallow drawdowns are worse than average.
Deep ones are much better. Both are true, and quoting either one alone is how
a real effect turns into a wrong headline.

WHAT IS DELIBERATELY NOT ASSUMED. The obvious objection is that 2020-2026 was
mostly an uptrend, so "buy the dip" wins by construction. That objection is
not argued with — it is measured, year by year, including 2022, when BTC lost
about two thirds of its value.

THE PART THAT MATTERS. An episode mean averages every hour of a crash,
including the hours near the bottom. You do not know where the bottom is
while you are in it. So the episode mean is not a tradeable number. The only
executable entry is the first hour the condition fires, and that is reported
separately. The two numbers disagree by more than an order of magnitude.

    python depth.py --fetch     download and compute, writes depth_run.json
    python depth.py             render depth_run.json into DEPTH.md
"""
from __future__ import print_function

import datetime as dt
import io
import json
import os
import sys
import time

BASE = "https://fapi.binance.com"
HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.join(HERE, "depth_run.json")
DOC = os.path.join(HERE, "DEPTH.md")

LOOKBACK_H = 24        # rolling window the drawdown is measured against
HOLD_H = 24            # how long the forward return is measured over
TAIL_BPS = 500         # frozen before the run; no search over this threshold
GAP_H = 48             # hours of separation that make two episodes distinct
BANDS = [(100, 200), (200, 300), (300, 500), (TAIL_BPS, 10 ** 9)]
SYMBOLS = ["BTCUSDT", "ETHUSDT"]
START = "2020-01-01"


def _klines(symbol, start):
    import urllib.request
    out = []
    t = int(dt.datetime.strptime(start, "%Y-%m-%d")
            .replace(tzinfo=dt.timezone.utc).timestamp() * 1000)
    now = int(time.time() * 1000)
    while t < now:
        url = ("%s/fapi/v1/klines?symbol=%s&interval=1h&startTime=%d&limit=1500"
               % (BASE, symbol, t))
        chunk = json.load(urllib.request.urlopen(url, timeout=45))
        if not chunk:
            break
        out += [(int(x[0]), float(x[4])) for x in chunk]
        t = int(chunk[-1][0]) + 1
        if len(chunk) < 1500:
            break
        time.sleep(0.15)
    return out


def _series(candles):
    """Drawdown from a rolling high, and the forward return, per hour."""
    import numpy as np
    close = np.array([c[1] for c in candles])
    n = len(close)
    dd = np.full(n, np.nan)
    for i in range(LOOKBACK_H, n - HOLD_H):
        high = close[i - LOOKBACK_H:i + 1].max()
        dd[i] = (high - close[i]) / high * 10000
    fwd = np.full(n, np.nan)
    fwd[:n - HOLD_H] = (close[HOLD_H:] / close[:n - HOLD_H] - 1) * 10000
    return dd, fwd, np.array([c[0] for c in candles])


def _episodes(idx):
    """Contiguous runs of qualifying hours, split by a gap of GAP_H."""
    eps, cur = [], [idx[0]]
    for a, b in zip(idx, idx[1:]):
        if b - a <= GAP_H:
            cur.append(b)
        else:
            eps.append(cur)
            cur = [b]
    eps.append(cur)
    return eps


def compute():
    import numpy as np
    out = {"params": {"lookback_h": LOOKBACK_H, "hold_h": HOLD_H,
                      "tail_bps": TAIL_BPS, "gap_h": GAP_H, "start": START},
           "symbols": {}}
    for sym in SYMBOLS:
        candles = _klines(sym, START)
        dd, fwd, ts = _series(candles)
        ok = ~np.isnan(dd) & ~np.isnan(fwd)
        base = float(fwd[ok].mean())
        rec = {"hours": int(len(candles)), "baseline_bps": base, "bands": [],
               "episodes": {}, "by_year": []}
        for lo, hi in BANDS:
            m = ok & (dd >= lo) & (dd < hi)
            v = fwd[m]
            rec["bands"].append({"lo": lo, "hi": None if hi > 10 ** 8 else hi,
                                 "n": int(m.sum()),
                                 "mean_bps": float(v.mean()) if m.sum() else None,
                                 "excess_bps": float(v.mean() - base) if m.sum() else None})
        idx = np.where(ok & (dd >= TAIL_BPS))[0]
        eps = _episodes(idx)
        ep_mean = np.array([fwd[e].mean() for e in eps])
        first = np.array([fwd[e[0]] for e in eps])
        rec["episodes"] = {
            "count": int(len(eps)),
            "median_len_h": float(np.median([len(e) for e in eps])),
            "episode_mean_bps": float(ep_mean.mean()),
            "episode_excess_bps": float(ep_mean.mean() - base),
            "share_up": float((ep_mean > 0).mean()),
            "first_hour_excess_bps": float((first - base).mean()),
            "first_hour_share_up": float((first > 0).mean()),
            "first_hour_ci": [
                float((first - base).mean()
                      - 1.96 * (first - base).std(ddof=1) / np.sqrt(len(first))),
                float((first - base).mean()
                      + 1.96 * (first - base).std(ddof=1) / np.sqrt(len(first)))],
        }
        years = np.array([dt.datetime.fromtimestamp(t / 1000, dt.timezone.utc).year
                          for t in ts])
        for y in sorted(set(years.tolist())):
            m = ok & (years == y)
            if m.sum() < 500:
                continue
            ey = [e for e in eps if years[e[0]] == y]
            if len(ey) < 5:
                continue
            b = float(fwd[m].mean())
            em = np.array([fwd[e].mean() for e in ey])
            fh = np.array([fwd[e[0]] for e in ey])
            cl = np.array([c[1] for c in candles])[m]
            rec["by_year"].append({
                "year": int(y), "episodes": int(len(ey)),
                "year_return_pct": float((cl[-1] / cl[0] - 1) * 100),
                "episode_excess_bps": float(em.mean() - b),
                "first_hour_excess_bps": float(fh.mean() - b)})
        out["symbols"][sym] = rec
    return out


def render(d):
    L = []
    L.append("generated by depth.py — do not edit by hand")
    L.append("hourly candles from %s, drawdown measured against a %dh rolling high,"
             % (d["params"]["start"], d["params"]["lookback_h"]))
    L.append("forward return over the next %dh, tail threshold %d bps (frozen)"
             % (d["params"]["hold_h"], d["params"]["tail_bps"]))
    for sym, r in d["symbols"].items():
        L.append("")
        L.append("%s   %d hourly candles   unconditional %dh move %+.1f bps"
                 % (sym, r["hours"], d["params"]["hold_h"], r["baseline_bps"]))
        L.append("  drawdown band          n        mean      excess")
        for b in r["bands"]:
            name = ("%d-%d" % (b["lo"], b["hi"])) if b["hi"] else (">=%d  TAIL" % b["lo"])
            L.append("  %-18s %7d  %+10.2f  %+10.2f"
                     % (name, b["n"], b["mean_bps"], b["excess_bps"]))
        e = r["episodes"]
        L.append("  tail as episodes      %7d  median length %.0f h  share up %.1f%%"
                 % (e["count"], e["median_len_h"], 100 * e["share_up"]))
        L.append("    mean over episode     %+.1f bps excess" % e["episode_excess_bps"])
        L.append("    FIRST HOUR ONLY       %+.1f bps excess   95%% CI [%+.1f, %+.1f]   share up %.1f%%"
                 % (e["first_hour_excess_bps"], e["first_hour_ci"][0],
                    e["first_hour_ci"][1], 100 * e["first_hour_share_up"]))
        L.append("  year   episodes   year return   episode excess   first hour")
        for y in r["by_year"]:
            L.append("  %-6d %8d      %+8.0f%%       %+10.1f     %+10.1f"
                     % (y["year"], y["episodes"], y["year_return_pct"],
                        y["episode_excess_bps"], y["first_hour_excess_bps"]))
    return "\n".join(L)


def main():
    if "--fetch" in sys.argv:
        d = compute()
        io.open(RUN, "w", encoding="utf-8").write(json.dumps(d, indent=1))
        print("wrote %s" % RUN)
    d = json.load(io.open(RUN, encoding="utf-8"))
    block = render(d)
    if os.path.exists(DOC):
        src = io.open(DOC, encoding="utf-8").read()
        a, b = "<!-- DEPTH:BEGIN -->", "<!-- DEPTH:END -->"
        if a in src and b in src:
            src = src[:src.index(a) + len(a)] + "\n```\n" + block + "\n```\n" + src[src.index(b):]
            io.open(DOC, "w", encoding="utf-8").write(src)
            print("updated %s" % DOC)
            return 0
    print(block)
    return 0


if __name__ == "__main__":
    sys.exit(main())
