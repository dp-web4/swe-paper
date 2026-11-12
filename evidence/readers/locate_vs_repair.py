#!/usr/bin/env python3
"""Where do failed sessions fail: finding the place, or fixing it? For each session in OUT_DIR compare the files of the agent's final
patch (non-test source files) with the files of the gold patch (non-test), and report:
  NOPATCH   no source change at all
  MISS      changed source, but none of the gold files
  PARTIAL   touched some gold files, not all
  LOCATED   touched every gold file (the fix itself was wrong or unfinished, if unresolved)
Also: when the first edit to a gold file happened (session seconds), from the trace.
usage: locate_vs_repair.py OUT_DIR [RESCORED_JSONL]   (rescored: lines with task/stub_resolved from rescore_all.py, optional)"""
import collections, glob, json, os, re, sys
out = sys.argv[1]
TEST = re.compile(r'(^|/)(tests?|testing)/|(^|/)test_[^/]*\.py$|_test\.py$|(^|/)conftest\.py$')
def files(diff):
    return ({m.group(1) for m in re.finditer(r'^diff --git a/(\S+) b/', diff or '', re.M)}
            | {m.group(1) for m in re.finditer(r'^\+\+\+ b/(\S+)', diff or '', re.M)})
def src(fs):
    return {f for f in fs if not TEST.search(f)}
gold = {}
for l in open('/home/dp/ai-workspace/SWE-SAGE-data/comp/tasks.jsonl'):
    d = json.loads(l)
    gold[d['repo'].split('/')[1] + '_' + re.search(r'(\d+)$', d['instance_id']).group(1)] = src(files(d['patch']))
resc = {}
if len(sys.argv) > 2:
    for l in open(sys.argv[2]):
        try:
            d = json.loads(l); resc[d['task']] = d.get('stub_resolved')
        except Exception: pass
cnt = collections.Counter(); rows = []
for d in sorted(glob.glob(out + '/*/')):
    name = os.path.basename(d.rstrip('/')); task = re.search(r'([a-z]+_\d+)$', name).group(1)
    o = open(d.rstrip('/') + '.out', errors='replace').read() if os.path.exists(d.rstrip('/') + '.out') else ''
    m = re.search(r'resolved=(\w+)', o); res = (m.group(1) == 'True') if m else None
    if resc.get(task): res = True
    pf = glob.glob(d + '*.agent.patch'); patch = open(pf[0], errors='replace').read() if pf else ''
    mine = src(files(patch)); g = gold.get(task, set())
    cls = 'NOPATCH' if not mine else 'MISS' if not (mine & g) else 'LOCATED' if g <= mine else 'PARTIAL'
    first = None
    for tr in glob.glob(d + 'traces/*.json'):
        for st in json.load(open(tr)).get('steps', []):
            for tc in st.get('tool_calls') or []:
                a = json.dumps(tc.get('arguments') or {})
                if tc.get('function_name') in ('edit_file', 'write_file') and any(gf in a for gf in g):
                    el = (tc.get('extra') or {}).get('elapsed_s')
                    if el is not None and first is None: first = el
    seen = None; nsteps = 0; first_src = None
    for tr in glob.glob(d + 'traces/*.json'):
        for st in json.load(open(tr)).get('steps', []):
            for tc in st.get('tool_calls') or []:
                nsteps += 1
                a = json.dumps(tc.get('arguments') or {}); el = (tc.get('extra') or {}).get('elapsed_s')
                if seen is None and el is not None and any(gf in a for gf in g): seen = el  # first call that names a gold file (read, grep, edit)
                if first_src is None and el is not None and tc.get('function_name') in ('edit_file', 'write_file'):
                    fp = (tc.get('arguments') or {}).get('filepath') or (tc.get('arguments') or {}).get('file_path') or ''
                    if fp.endswith('.py') and not TEST.search(fp) and not re.search(r'(^|/)(repro|reproduc|check_|test)', fp): first_src = el
    cut = 'session timeout' in o
    rows.append((name, res, cls, len(g), len(mine & g), sorted(mine - g)[:3], first, cut, seen, first_src))
    cnt[(bool(res), cls)] += 1
print(f"{'session':26} {'res':5} {'class':8} gold hit  gold-named  1st-src-edit  1st-gold-edit  cut  other files changed")
for name, res, cls, ng, hit, other, first, cut, seen, first_src in rows:
    f = lambda x: ('%6.0f' % x) if x is not None else '     -'
    print(f"{name:26} {str(res):5} {cls:8} {ng:3d} {hit:3d}  {f(seen)}      {f(first_src)}        {f(first)}       {'cut' if cut else '   '}  {other}")
print()
un = [r for r in rows if not r[1]]
print(f"unresolved {len(un)}: gold file named in some call {sum(r[8] is not None for r in un)}; any source edit {sum(r[9] is not None for r in un)}; gold file edited {sum(r[6] is not None for r in un)}")
for res in (True, False):
    print('resolved' if res else 'UNRESOLVED', {c: cnt[(res, c)] for c in ('NOPATCH', 'MISS', 'PARTIAL', 'LOCATED')})
