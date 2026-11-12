#!/usr/bin/env python3
"""Uptake of the /tmp/notes.md affordance (v66). Per session: executed run_command calls that WRITE the notes file (>>, >, tee, cat <<),
calls that READ it afterwards (cat/head/tail/grep/sed -n/less on the file with no write redirect), the first write's exit status, and
whether scratch files were created under /tmp vs in the repo. Usage: notes_uptake.py OUT_DIR [PREFIX]"""
import json, glob, os, re, sys
N = '/tmp/notes.md'
WRITE = re.compile(r'(>>?\s*/tmp/notes\.md|tee\s+(-a\s+)?/tmp/notes\.md)')
READ = re.compile(r'\b(cat|head|tail|grep|less|sed\s+-n|wc)\b[^|;&>]*?/tmp/notes\.md')
d = sys.argv[1]; pre = sys.argv[2] if len(sys.argv) > 2 else ''
rows = []; writers = readers = 0
for p in sorted(glob.glob(f'{d}/{pre}*/traces/*.json')):
    T = json.load(open(p)); name = p.split('/')[-3]
    w = r = 0; first_ok = None; tmp_scratch = repo_scratch = 0; wrote = False; wtool = 0
    for st in T['steps']:
        for tc in st.get('tool_calls') or []:
            a = tc.get('arguments') or {}; fn = tc.get('function_name')
            obs = json.dumps(st.get('observation') or '')
            ok = '"exit_code\\": 0' in obs or 'exit_code": 0' in obs or ('status\\": \\"ok' in obs and fn != 'run_command')
            if fn == 'run_command':
                c = str(a.get('command', ''))
                if N in c:
                    if WRITE.search(c):
                        w += 1; wrote = True
                        if first_ok is None: first_ok = ok
                    elif READ.search(c) and wrote: r += 1
                if re.search(r'(>|tee)\s*/tmp/(?!notes\.md)\S+\.(py|sh|txt)', c) or re.search(r'cat\s*>\s*/tmp/(?!notes)', c): tmp_scratch += 1
            if fn in ('write_file', 'edit_file'):
                fp = str(a.get('filepath') or a.get('file_path') or a.get('path') or '')
                if fp.startswith('/tmp/notes'): wtool += 1; wrote = True; first_ok = ok if first_ok is None else first_ok
                elif fp.startswith('/tmp/'): tmp_scratch += 1
                elif re.search(r'(^|/)(repro|reproduce|test_|scratch|check_|debug)[^/]*\.py$', fp) and 'tests/' not in fp: repo_scratch += 1
            if fn == 'read_file' and str(a.get('filepath', '')).startswith('/tmp/notes') and wrote: r += 1
    writers += (w + wtool) > 0; readers += r > 0
    rows.append((name, w + wtool, r, first_ok, tmp_scratch, repo_scratch))
print(f"{'session':26} {'writes':>6} {'reads':>5} {'first_write_ok':>14} {'tmp_scratch':>11} {'repo_scratch':>12}")
for x in rows: print(f"{x[0]:26} {x[1]:6d} {x[2]:5d} {str(x[3]):>14} {x[4]:11d} {x[5]:12d}")
print(f"sessions {len(rows)}  WRITERS {writers}  READERS-after-write {readers}")
