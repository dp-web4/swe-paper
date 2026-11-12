# D2 component: skill / offered-affordance uptake (thor-claude, 2026-11-12 04:3xZ, research loop, CPU only)

dp 11-12 03:2xZ: "that might be another curiosity lora item - skills use?". The PRD row named the gauge: did the
session consult an offered affordance at the decision where it applies, before its first repeat or its first
scratch reproduction? `skill_uptake.py` builds that gauge over every stored trace (tracelib.discover, 2,997 sessions
with an offered or used affordance; 57 have an unknown offer because the tree is not found, so they read `?`).
Output: `skill_uptake_stdout.txt`; per-session rows in `runs/curiosity_e1_1111/cpu/skill_uptake.jsonl` (not in git).

## Validation (criteria written into the file header before it scored anything)

| case | criterion | result |
|---|---|---|
| K1 v70 out_L (000424), run-clock "your first action" | accepted in 3 of 8 | **3 of 8, lands** (2 of them as the first call; one more after a rejected attempt; offer `?` for the ZIP arm, so read from the calls) |
| K2 runcmd3 cand_t6 (000367), repair-context "Your FIRST call, always" | first call 0 of 8 | **0 of 8, lands** (accepted at some point 6 of 8; attempted at k=0 0 of 8) |
| K3 code-graph tools, v41/v45/v49/v50 t20 | offered in >= 96, called in 0 | **offered 96, called 0, lands** |
| S1 a name never offered | 0 accepted everywhere | 0 |
| S2 decision point forced to call 0 | before_D 0 | 0 of 11,954; a construction lock, not a firing gauge |
| S3 decision point forced past the last call | before_D == ever_accepted in every cell, with positives | 15,650 of 15,650, 1,946 positive (the comparison fires both ways) |

## Corpus readout (offer known; local Thor dryruns; hosted `?`)

| name | offered | attempted | accepted | first call | accepted before D | never reach D |
|---|---|---|---|---|---|---|
| locate-code | 1985 | 572 | 570 | 37 | 213/1852 | 133 |
| related-files | 1443 | 928 | 923 | 0 | 25/1340 | 103 |
| repair-context | 488 | 214 | 209 | 49 | 99/475 | 13 |
| repo-paging | 344 | 229 | 227 | 7 | 105/333 | 11 |
| navkit | 52 | 15 | 15 | 0 | 6/49 | 3 |
| run-clock | 6 | 2 | 2 | 2 | 2/6 | 0 |
| get_code_neighbors | 2833 | 16 | 0 | 0 | 0/2633 | 200 |
| search_similar_code | 2833 | 4 | 0 | 0 | 0/2633 | 200 |
| get_code_subgraph | 2833 | 0 | 0 | 0 | 0/2633 | 200 |

Pooled, any offered name accepted before D: 395 of 2,633 sessions. D comes from a scratch reproduction first in 1,896
and from an exact repeat first in 737.

**Construct caveat (stated in the file before scoring).** repo-paging, locate-code and repair-context are working
routes: calling them is ordinary work, not affordance seeking. The pooled 395 is not a curiosity reading. The clean
cases are the ones offered as advice and not needed for the work: run-clock and the code-graph tools.

## A finding the gauge surfaced: locally, the code-graph tools have never worked

All 20 sessions that attempted a code-graph tool (22 counting two with an unknown offer; every first attempt
listed) got a tool error: `GraphLookupError` / `SimilaritySearchError` "Repository <owner/repo> not found in local
files at /home/dp/ai-workspace/...". Accepted: 0 of 2,833 offered sessions. So the "0 of 96" zero-uptake record
(PRD 11-10) and the v51 subtraction were measured where the affordance could not work: the model did reach for it, in
about 1 session in 140, and was refused by a missing index each time. Whether the graph exists on the hosted grader
is `?`. Not claimed: that the model would use a working tool, or that v51's null would change. The record should read
"offered, rarely attempted, never functional locally", not "never reached for".

## What this means for the adapter track

The curiosity behaviour dp named is measurable at session level from traces: uptake of an advisory affordance before
the first grind point. It has two validated base rates on file (run-clock 3 of 8, repair-context first-call 0 of 8),
both small n. The working-route skills are the wrong place to train it. A training pair for this item needs an offer
the work does not require, and the gauge reads it only where the offer is known and the tool works.

Next: add `skill_uptake` to the D2 bundle as a validated component; ask the SWE lane whether hosted repos carry the
code graph (if not, the three tool schemas ride every turn for nothing); name two NEW advisory-affordance known cases
before any adapter result is read on this gauge.
