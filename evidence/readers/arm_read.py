#!/usr/bin/env python3
"""Readout for a multi-arm panel (sessions named <arm>-<task> in one OUT_DIR). Per arm: resolved (as recorded, or True when a
rescore line says stub_resolved), mechanism columns, and paired flips between arms by task.
Mechanism per session: first call naming a gold file, first read_file of a gold file, first source edit (non-test, non-scratch .py),
first submit, cut at the clock, steps, completion tokens, changed source lines, source files touched outside the gold files
(over-reach, counted on sessions that touched a gold file), scratch files left in the final patch, longest run of submits.
usage: arm_read.py OUT_DIR [RESCORE_JSONL] [BASE_ARM]"""
import collections, glob, json, os, re, statistics, sys
out = sys.argv[1]; base = sys.argv[3] if len(sys.argv) > 3 else None
TEST = re.compile(r'(^|/)(tests?|testing)/|(^|/)test_[^/]*\.py$|_test\.py$|(^|/)conftest\.py$')
SCRATCH = re.compile(r'(^|/)(repro|reproduc|check_|debug|scratch|tmp_|demo)[^/]*$')
def files(diff):
    return ({m.group(1) for m in re.finditer(r'^diff --git a/(\S+) b/', diff or '', re.M)} | {m.group(1) for m in re.finditer(r'^\+\+\+ b/(\S+)', diff or '', re.M)})
gold = {}
for l in open('/home/dp/ai-workspace/SWE-SAGE-data/comp/tasks.jsonl'):
    d = json.loads(l)
    gold[d['repo'].split('/')[1] + '_' + re.search(r'(\d+)$', d['instance_id']).group(1)] = {f for f in files(d['patch']) if not TEST.search(f)}
resc = {}
if len(sys.argv) > 2 and os.path.exists(sys.argv[2]):
    for l in open(sys.argv[2]):
        try:
            d = json.loads(l); resc[(d.get('arm'), d['task'])] = d.get('stub_resolved')
        except Exception: pass
S = collections.defaultdict(dict)
for d in sorted(glob.glob(out + '/*/')):
    name = os.path.basename(d.rstrip('/')); m = re.match(r'(.+)-([a-z]+_\d+)$', name)
    if not m: continue
    arm, task = m.groups()
    op = d.rstrip('/') + '.out'; o = open(op, errors='replace').read() if os.path.exists(op) else ''
    mm = re.search(r'resolved=(\w+)', o)
    if not mm: continue
    res = mm.group(1) == 'True' or bool(resc.get((arm, task)))
    pf = glob.glob(d + '*.agent.patch'); patch = open(pf[0], errors='replace').read() if pf else ''
    allf = files(patch); srcf = {f for f in allf if not TEST.search(f) and not SCRATCH.search(f)}
    g = gold.get(task, set())
    lines = 0; cur = None
    for ln in patch.split('\n'):
        mh = re.match(r'^\+\+\+ b/(\S+)', ln)
        if mh: cur = mh.group(1); continue
        if cur in srcf and (ln.startswith('+') or ln.startswith('-')) and not ln.startswith(('+++', '---')): lines += 1
    r = dict(res=res, cut='session timeout' in o, named=None, read=None, edit=None, submit=None, steps=0, ctok=None, lines=lines,
             malf=0, malf28=0, gold_hit=bool(srcf & g), over=len(srcf - g) if (srcf & g) else None, scratch=len({f for f in allf if SCRATCH.search(f)}), sub_run=0, any_src=bool(srcf))
    run = 0
    for tr in glob.glob(d + 'traces/*.json'):
        t = json.load(open(tr)); r['ctok'] = (t.get('final_metrics') or {}).get('total_completion_tokens')
        for st in t.get('steps', []):
            for tc in st.get('tool_calls') or []:
                r['steps'] += 1
                ob = json.dumps(st.get('observation') or {})
                if 'mandatory input parameters' in ob or 'Tool not found' in ob or 'not found in' in ob[:200]:
                    r['malf'] += 1; r['malf28'] += r['steps'] > 28
                fn = tc.get('function_name'); a = tc.get('arguments') or {}; aj = json.dumps(a); el = (tc.get('extra') or {}).get('elapsed_s')
                if el is None: continue
                if r['named'] is None and any(gf in aj for gf in g): r['named'] = el
                if r['read'] is None and fn == 'read_file' and any(gf in aj for gf in g): r['read'] = el
                if r['edit'] is None and fn in ('edit_file', 'write_file'):
                    fp = a.get('filepath') or a.get('file_path') or ''
                    if fp.endswith('.py') and not TEST.search(fp) and not SCRATCH.search(fp): r['edit'] = el
                if fn == 'submit_patch':
                    if r['submit'] is None: r['submit'] = el
                    run += 1; r['sub_run'] = max(r['sub_run'], run)
                else: run = 0
    S[arm][task] = r
med = lambda xs: (round(statistics.median(xs)) if xs else None)
arms = sorted(S)
print(f"{'arm':10} {'n':>3} {'res':>4} {'srcedit':>7} {'goldhit':>7} {'cut':>4} {'nosub&cut':>9} {'t_named':>7} {'t_read':>6} {'t_edit':>6} {'t_submit':>8} {'steps':>5} {'ctok':>6} {'lines':>5} {'overreach':>9} {'scratch':>7} {'subloop>3':>9} {'malformed(sessions; calls; after step 28)':>40}")
for a in arms:
    R = list(S[a].values())
    ov = [r['over'] for r in R if r['over'] is not None]
    print(f"{a:10} {len(R):3d} {sum(r['res'] for r in R):4d} {sum(r['edit'] is not None for r in R):7d} {sum(r['gold_hit'] for r in R):7d} {sum(r['cut'] for r in R):4d} "
          f"{sum(r['cut'] and r['submit'] is None for r in R):9d} {str(med([r['named'] for r in R if r['named'] is not None])):>7} {str(med([r['read'] for r in R if r['read'] is not None])):>6} "
          f"{str(med([r['edit'] for r in R if r['edit'] is not None])):>6} {str(med([r['submit'] for r in R if r['submit'] is not None])):>8} {str(med([r['steps'] for r in R])):>5} "
          f"{str(med([r['ctok'] for r in R if r['ctok']])):>6} {str(med([r['lines'] for r in R if r['any_src']])):>5} {sum(1 for x in ov if x > 0):>4}/{len(ov):<4} {sum(r['scratch'] > 0 for r in R):7d} {sum(r['sub_run'] > 3 for r in R):9d} "
          f"{sum(r['malf'] > 0 for r in R):>14}; {sum(r['malf'] for r in R)}; {sum(r['malf28'] for r in R)}")
print('\npaired flips (row arm resolves, column arm does not), on tasks present in both:')
for a in arms:
    print(f"  {a:10}", {b: sum(1 for t in S[a] if t in S[b] and S[a][t]['res'] and not S[b][t]['res']) for b in arms if b != a})
if base in S:
    for a in arms:
        if a == base: continue
        won = sorted(t for t in S[a] if t in S[base] and S[a][t]['res'] and not S[base][t]['res']); lost = sorted(t for t in S[a] if t in S[base] and S[base][t]['res'] and not S[a][t]['res'])
        print(f"  {a} vs {base}: +{len(won)} {won}  -{len(lost)} {lost}  net {len(won) - len(lost):+d}")
print('resolved by any arm:', len({t for a in arms for t in S[a] if S[a][t]['res']}), 'of', len({t for a in arms for t in S[a]}))
