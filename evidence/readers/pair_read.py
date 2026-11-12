#!/usr/bin/env python3
"""Paired reading of two arms on the same tasks: duration ratio, resolved among cells known in both, per-task table.
Usage: pair_read.py NEW_OUT NEW_PREFIX OLD_OUT OLD_PREFIX   (e.g. runs/swe_v64_scaled_1111/out_C v64s80 runs/swe_v63_scaled_1111/out_A v63s80)"""
import re, glob, os, sys, statistics as S
def load(d, pre):
    r = {}
    for f in sorted(glob.glob(f'{d}/{pre}-*.out')):
        task = os.path.basename(f)[len(pre) + 1:-4]; o = open(f).read()
        m = re.search(r'resolved=(\w+).*?duration=([\d.]+)s', o)
        if not m: r[task] = (None, None, 'NO RECEIPT'); continue
        herr = re.search(r"harness_error=(?:'|\")([^'\"]{0,60})", o)
        res = m.group(1)
        if herr and 'test_patch' in herr.group(1): res = 'UNKNOWN'
        mc = re.search(r'tool_calls=(\d+)', o)
        r[task] = (res, float(m.group(2)), (herr.group(1)[:40] if herr else '') + (f' calls={mc.group(1)}' if mc else ''))
    return r
N = load(sys.argv[1], sys.argv[2]); O = load(sys.argv[3], sys.argv[4])
tasks = sorted(set(N) & set(O))
print(f"{'task':16} {'new':8} {'old':8} {'new_s':>6} {'old_s':>6}  notes(new | old)")
for t in tasks:
    n, o = N[t], O[t]
    print(f"{t:16} {str(n[0]):8} {str(o[0]):8} {n[1] or float('nan'):6.0f} {o[1] or float('nan'):6.0f}  {n[2]} | {o[2]}")
nd = [N[t][1] for t in tasks]; od = [O[t][1] for t in tasks]
if None in nd or None in od: print('MISSING RECEIPT: no reading'); sys.exit(3)
known = [t for t in tasks if N[t][0] in ('True', 'False') and O[t][0] in ('True', 'False')]
rn = sum(N[t][0] == 'True' for t in known); ro = sum(O[t][0] == 'True' for t in known)
mn, mo = S.mean(nd), S.mean(od)
print(f"n={len(tasks)}  mean new {mn:.0f} s  old {mo:.0f} s  ratio {mn / mo:.3f}  median new {S.median(nd):.0f} old {S.median(od):.0f}")
print(f"resolved among {len(known)} cells known in both: new {rn}  old {ro}  (delta {rn - ro})")
faster = sum(a < b for a, b in zip(nd, od)); print(f"tasks faster in new: {faster} of {len(tasks)}")
for s in (3.6, 4.0, 4.65): print(f"  scenario {s}x: 120 issues {mn * 120 / s / 3600:.1f} h   129 issues {mn * 129 / s / 3600:.1f} h")
