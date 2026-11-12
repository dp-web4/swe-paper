"""thor-claude 2026-11-11 rescore_all.py = rescore.py generalised to EVERY fastapi task dir in the run (the original was fixed to 8 ids).
thor-claude 2026-11-08: rescore stored agent patches with a working grader (inline_snapshot stub), CPU only.

The local sandbox lacks inline-snapshot (the scorer image has 0.36.0), so fastapi tasks whose hidden tests import it exit 2
whatever the patch does (FAILURE_CLASSES.md). This replays each stored <arm>-<task>/<task>.agent.patch through repl.py with
--stub and prints the stubbed verdict next to the original one. requests_6629 stays unscorable (gold fails here too).
usage: rescore.py RUN_DIR [RUN_DIR ...]   (dirs holding <arm>-<task>/ subdirs)"""
import json
import os
import re
import subprocess
import sys

SP = '/tmp/claude-2002/-home-dp-ai-workspace/b60b6065-6919-4a44-b5cb-499ad81b4fcd/scratchpad/'
IDS = None  # rescore_all: every task dir whose receipt shows test_exit_code=2 (collection failure) or any fastapi task
rows = []
for d in sys.argv[1:]:
    for sub in sorted(os.listdir(d)):
        m = re.match(r'(.+)-((?:fastapi|requests|rich)_\d+)$', sub)
        if not m or not os.path.isdir(os.path.join(d, sub)) or not m.group(2).startswith('fastapi_'):
            continue
        arm, task = m.groups()
        p = os.path.join(d, sub, task + '.agent.patch')
        orig = ''
        o = os.path.join(d, sub + '.out')
        if os.path.exists(o):
            mm = re.search(r'resolved=(\w+)', open(o, errors='replace').read())
            orig = mm.group(1) if mm else ''
        if not os.path.exists(p) or os.path.getsize(p) == 0:
            rc = 'nopatch'
        else:
            x = subprocess.run(['python3', SP + 'repl.py', task, 'rs_' + arm, p, '--stub'], capture_output=True, text=True,
                               timeout=900)
            mm = re.search(r'pytest rc (-?\d+)', x.stdout)
            rc = mm.group(1) if mm else '?'
        r = dict(run=os.path.basename(os.path.dirname(d.rstrip('/'))) + '/' + os.path.basename(d.rstrip('/')), arm=arm,
                 task=task, orig_resolved=orig, stub_rc=rc, stub_resolved=(rc == '0'))
        rows.append(r)
        print(json.dumps(r), flush=True)
agg = {}
for r in rows:
    k = (r['run'], r['arm'])
    a = agg.setdefault(k, [0, 0, 0])
    a[0] += r['orig_resolved'] == 'True'
    a[1] += r['stub_resolved'] and r['task'] != 'requests_6629'
    a[2] += 1
for (run, arm), (o, s, n) in sorted(agg.items()):
    print(f'SUMMARY {run:45s} {arm:18s} orig {o}/{n}  stubbed(excl requests) {s}/{n}')
