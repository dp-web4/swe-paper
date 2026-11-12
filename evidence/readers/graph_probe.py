#!/usr/bin/env python3
"""CPU probe: do the harness's three graph tools work locally now that SWE-SAGE-data/graphs and embeddings hold the competition's
files? Calls the tool functions themselves (swegemma.tools.graph) with a minimal context for one task, the way the harness does, and
prints what a session would see. Usage: graph_probe.py TASK_ID NODE [NODE2 ...]"""
import json, sys, types
D = '/home/dp/ai-workspace/SWE-SAGE-data'
tid = sys.argv[1]; nodes = sys.argv[2:]
task = next(json.loads(l) for l in open(D + '/tasks.jsonl') if json.loads(l)['instance_id'] == tid)
import swegemma.tools.graph as G
import inspect
print('tool functions:', [n for n, f in inspect.getmembers(G, inspect.isfunction) if not n.startswith('_')])
repo = task['repo'].split('/')[-1]
ctx = types.SimpleNamespace(task=task, repo=repo, graph_repo_key=None, graph_dir=D + '/graphs', embeddings_dir=D + '/embeddings',
                            max_stdout_chars=5000, harness=None, tool_calls_used=0, max_tool_calls=200)
def show(label, s):
    s = s if isinstance(s, str) else json.dumps(s)
    print('---', label, len(s), 'chars'); print(s[:1500])
for n in nodes:
    for fn, kw in ((G.get_code_neighbors, dict(node=n)), (G.search_similar_code, dict(query=n, k=5))):
        f = getattr(fn, '__wrapped__', fn)
        try: show(fn.__name__ + ' ' + n, f(ctx, **kw))
        except Exception as e: print('---', fn.__name__, n, 'EXC', type(e).__name__, str(e)[:300])
if hasattr(G, 'get_code_subgraph') and nodes:
    f = getattr(G.get_code_subgraph, '__wrapped__', G.get_code_subgraph)
    try: print(inspect.signature(f)); show('get_code_subgraph', f(ctx, nodes[:2]))
    except Exception as e: print('--- get_code_subgraph EXC', type(e).__name__, str(e)[:300])
