# Submission ledger: Gemma 4 Developer Agent (prediction track)

One scored submission per day (`max_daily_submissions = 1`). Same philosophy as the ARC scored runs (dp,
2026-09-30): **local runs learn; a scored run is a gauge.** It is time- and resource-limited, gives no telemetry
beyond the score, and so must spend its budget for the best overall score. Every row records the exact artifact
(committed next to this file), its sha256, what it tests, and the score once it arrives.

## 2026-11-12 21:26Z: v77-graphtools-described-think4k-t6 BUILT, IN TEST, NOT FIRED (awaiting the local read and dp's word) (thor-claude)

- **Bytes:** `blackbox/runs/swe-v77-graphtools-described-think4k-t6-prepared-20261112/submission.zip`, SHA `d3bc852bf7192fe774d56170492a593e3c12423ee254ba561534981bab9dc409` (builder `blackbox/analysis/claude_swe_earlyfinish_1111/build_v77.py`). v68 with ONE change in `prompts/system.md`: the half-sentence "code-neighbor, similarity and subgraph tools can reveal relationships" is replaced by an accurate description of the three code-graph tools (nodes are full dotted paths; a bare name returns an empty result; what each tool returns). No procedure is mandated. Thinking 4096, 6-minute ceiling, no call cap, 31B.
- **Why:** the competition data ships a call graph and an embedding file per repository commit (`graphs/` 127, `embeddings/` 127). On Thor both directories were empty until 11-12 20:5xZ, so every local graph-tool call failed for six weeks (20 attempts in 2,833 offered sessions, 0 accepted) and the tools were read as unused. Found from Dottie/Nova's paper review. dp: "another case of footgun - not using valuable available affordances".
- **Hypothesis (written before any fire):** on the host the graph data is mounted and the tools work; the agent does not reach them because nothing tells it the node naming, and a bare name returns an empty `ok`. Told accurately, it will call them and find sibling/caller sites faster. Host facts a fire reveals: whether the hosted graph tools are functional for our agent, and whether reaching them moves the score.
- **Pre-registered reading of a hosted score:** >= 0.22 = joins the leaders' pack; the graph route is real and is developed next (panels with working graphs). 0.14-0.21 = same class as v68 (0.17): no verdict on the tools from one draw. <= 0.12 = the description costs on the host (or the hosted tools fail and waste calls): v68 stays the base and the graph route is tested locally before any further fire. ERROR = cause unknown without evidence.
- **Local test in progress** (gpuq 000427f, pool 4, 24-minute clock, eight V2 tasks; comparator the base's pool-4 record, 4 of 8): uptake >= 5 of 8 sessions with a non-empty graph result = reachable; outcome >= 6 of 8 with <= 1 base-only loss = evidence, 3-5 tie, <= 2 costs. Results are appended here when read.
- **Caveat:** the host's graph mount is assumed from the dataset listing, not verified.
- **Status:** NOT FIRED. Fires only on dp's explicit word, once, with `--day 2026-11-12 --stop-file runs/STOP_swe_1112`.

## 2026-11-12 20:33Z: v75-12b-empower-uncapped-runfact-think4k-t6 BUILT, SMOKED, TESTED (partial), NOT A CANDIDATE (thor-claude)

- **Bytes:** `blackbox/runs/swe-v75-12b-empower-uncapped-runfact-think4k-t6-prepared-20261112/submission.zip`, SHA `fd3bb9011b448901773125e65be79ccca37adbf5d8b254d22a363583409b19bb` (builder `blackbox/analysis/claude_swe_earlyfinish_1111/build_v75.py`): v68 with only the model line changed to `gemma-4-12b-it-qat-w4a16-ct`.
- **Why built:** dp 11-12 19:3xZ asked for a breakthrough candidate today; a faster allowed model is the only in-bundle route to more steps inside the 6-minute ceiling.
- **Result:** 12B READ, PARTIAL (gpuq 000427a, 20:01-20:32Z, stopped by me after the four base-solved tasks; `runs/swe_v75_12b_1112/out_S`; `rescore_all.py` + `arm_read.py`): v75s24 (v68 on gemma-4-12b-it-qat-w4a16-ct) resolved 0 of the 4 tasks the 31B base resolved on panel V1 (rich_4075, rich_3006, rich_3480, fastapi_14349; base 4 of 4 by construction of the order). 12B does produce more: median 45 steps against the base's 28 and 15,238 completion tokens against 6,264 (2.4x), tool calls 79 / 44 / 46 / 32. It does not convert them: all four sessions were cut at the 24-minute clock, a source file was edited in 1 of 4, a gold file was touched in 0 of 4 (base on V1: 9 of 24 sessions touch a gold file), the first named file came at a median 186 s against 95 s, and rich_3480 ended with an empty patch. Exact-ZIP smoke at the shipped 6 minutes (ZIP fd3bb901…19bb, verified): fastapi_14301 resolved in 30 calls; rich_3894 cut after 6 calls, unresolved (the 31B's v73 smoke resolved both). Served model checked by the job before any session (`/v1/models` names gemma-4-12b-it-qat-w4a16-ct rooted at the 12B checkpoint dir; weights sha256 60b6e398…bfa3 = the hub's). Reading, with kimi's boundary kept: the pre-registered thresholds belong to a completed 24-task panel, and this is 4 cells, so it is PARTIAL, not the gate's verdict. What it does show: on the four tasks where the base's solves are, 12B lost all four at equal wall time, and to reach the converting threshold (>= 7 of 24) it would have needed 7 of the 20 tasks the base did not solve. I stopped it early by the rule I stated to kimi at 20:15Z (decisive after the 31B-solved tasks) to give v76 the GPU 50 minutes sooner. Caveat that stays open: the host's 12B speed relative to its 31B is unknown; if the host's ratio were far above Thor's 2.4x in tokens, the picture could differ, but the failure here is weaker steps (not locating, not editing source), not too few steps. v75 is NOT a candidate for tonight; it stays an unfired, smoked package. GPU handed to kimi's v76 smoke + panel at 20:32:48Z.
- **Status:** NOT FIRED and not proposed. kimi-code AGREED the pre-registration (19:58Z, 20:24Z) with the boundary that a stopped read is partial.

## 2026-11-12 19:00Z: v73-commit-early-minimal-think4k-t6 STAGED AND SMOKED, NOT FIRED (awaiting dp's word for the 11-12 slot) (thor-claude)

- **Bytes:** `blackbox/runs/swe-v73-commit-early-minimal-think4k-t6-prepared-20261112/submission.zip`, SHA `961fc12aa1e3be841a6a5f38f411bd3bddba21ab068540455a2d71db0a4e973c` (builder `blackbox/analysis/claude_swe_earlyfinish_1111/build_v72b_v73.py`). v68 with two prompt additions (commit an edit early; make the minimal change); thinking 4096; 6-minute ceiling; no call cap.
- **Local evidence:** 4 of 24 on valid panel V1 at the scaled clock, equal to the base v68s24 (4 of 24); net 0. Exact-ZIP smoke (gpuq 000426zz, 11-12 18:21-18:27Z): both receipts, dryrun_rc=0, fastapi_14301 and rich_3894 resolved, no agent or harness error.
- **Hypothesis (written before any fire):** v73 is a v68-class package with different bytes, so its hosted score is one more draw from the same distribution (v68 0.17; v12 0.17 and 0.12; v18/v23b/v25/v27/v37 0.15). Host fact it reveals: the spread of distinct v68-class bytes on the public ~58.
- **Pre-registered reading:** 0.12-0.19 = same class, no information beyond the draw; >= 0.22 = joins the leaders' pack, and the wording is replicated locally before any claim; <= 0.10 = the wording costs on the host and v68 stays the base; ERROR = cause unknown without evidence (v68 at the same 6-minute ceiling completed).
- **Prediction (thor-claude):** 0.15.
- **Known cost:** not a breakthrough candidate; no local effect over the base. dp counts a known-incremental slot as a cost; the alternative tonight is an unused slot. kimi's bound view requested 11-12 18:29Z (default: hold).
- **kimi-code's bound view (11-12 19:24Z, mail `2026-11-12-1924-kimi-code-to-thor-claude-v73-hold.md`): HOLD.** No local lift over v68; two resolved in-sample smoke tasks do not estimate hosted performance; keep the slot unused rather than spend it on another v68-class draw. If dp explicitly chooses v73 despite the hold, the pre-registered reading and prediction stand. So the two seats disagree: thor-claude PREFERS firing v73 as a draw, kimi-code HOLDS; codex is out of usage. dp's word decides.
- **Status:** NOT FIRED. Fires only on dp's explicit word, once, with `--day 2026-11-12 --stop-file runs/STOP_swe_1112`.

## 2026-11-11 20:40Z: v70-runclock-adaptive-think4k-t20 BUILT AND TESTED, NOT FIRED (the agent mostly did not read the clock and did not obey it; dp chose v68) (thor-claude)
- ZIP `blackbox/runs/swe-v70-runclock-adaptive-think4k-t20-prepared-20261111/submission.zip`, SHA256 b58c8e95981763c32455af2087b835915d8559d71b19b46dfd8b4d4bc4d199cd (rebuilt 20:41Z; the first build 78e56c91 keyed an issue by the script's working directory, which is a fresh temp folder on every skill call, so each call would have counted as a new issue; found in the first minute of the smoke, never fired); tree `submissions/v70-runclock-adaptive-think4k-t20`; builder `blackbox/analysis/claude_swe_earlyfinish_1111/build_v70.py`.
- dp 11-11 20:3xZ: "we need adaptive effort per task, so build it. i'd rather ship built-not-tested adaptive than tested fixed." This supersedes v68 (fixed 6) and v69 (fixed 5, rejected by dp) for tonight.
- What it is: v65 (73f0bec9; 20-minute hard ceiling, thought 4,096, 200 calls, 500 turns) + skill `run-clock` (`scripts/clock.py`) + a rewritten first resources bullet. The clock keeps a ledger of issue starts outside the per-task folder and prints an allowance for each issue (1 to 20 minutes; 6 when no earlier issue is on record), from the run time left, the issues left (130 assumed, 11.5 h usable) and a slack measured from the ledger.
- What enforces it: nothing but the agent. The harness cuts a session only at 20 minutes. If sessions ignore the allowance, the run overruns as v58 did.
- Untested on the host by construction: whether the host runs the subprocess sandbox, whether the ledger persists, whether tasks run in sequence. Without persistence it degrades to "6 minutes advised, 20 enforced".
- **Pre-registered reading (written before any fire):** an explicit runtime-exceeded receipt → the advisory clock did not bound the run (non-compliance, or no persistence plus non-compliance); adaptive effort then needs something that ends sessions, not advice. Score >= 0.18 → first score above the band; consistent with longer allowances on some issues paying, at one draw. 0.12-0.17 → inside the band: the run completed with a 20-minute ceiling, which itself shows the clock (or early endings) bounded it; no verdict on adaptive effort. <= 0.11 → below the band, mechanism unresolved (short late allowances, skill overhead, or the unsubmitted tree not being graded). A score cannot show whether the ledger persisted; only the completion can hint at it.

## 2026-11-11 20:16Z: v69-empower-uncapped-runfact-think4k-t5 REJECTED by dp ("shorting ourselves 2 hours of runtime - NO"), NOT FIRED (thor-claude)
- ZIP `blackbox/runs/swe-v69-empower-uncapped-runfact-think4k-t5-prepared-20261111/submission.zip`, SHA256 3f9d187af6769843e08f257eca18f6dc819e889a62f5b6bf87d1e11df28d40a1; tree `submissions/v69-empower-uncapped-runfact-think4k-t5`; builder `blackbox/analysis/claude_swe_earlyfinish_1111/build_v69.py`.
- What it is: v65 (73f0bec9) with `max_time_minutes` 20 → 5 and the prompt's two clock mentions 20 → 5; nothing else. Identical to v68 except the number 6 → 5.
- Why 5 and not 6: the fresh 24-task sample (000421, out of sample, v68s24) had 19 of 24 sessions run to the clock, mean 92% of the ceiling. If hosted sessions use the clock the same way, run time is about N x ceiling: 120 x 6 min x 0.92 = 11.1 h before any overhead (129: 11.9 h); at 5 minutes 9.2 h (129: 9.9 h), which leaves 77 s (120) or 58 s (129) of per-task overhead before 12 h. Hosted execution time itself is unknown: elapsed includes queue (dp), the API has no run-time field, and the page's download returns our own bundle.
- Local evidence: exact-ZIP smoke receipts present (000422: rich_3894 resolved, 306.9 s; fastapi_14301 cut at Thor's 5 minutes, as expected at Thor speed). The frozen-24 run at the matching 20-minute Thor clock was still running when this was written. **The frozen 24 are in-sample and are not a forecast:** on the fresh sample v68 resolved 3 of 24 (1 as recorded, 2 more after the inline-snapshot rescoring) against 19 of 20 on the frozen 24. No scored baseline has been run on the fresh tasks.
- Review: requested from kimi-code at 19:34Z and 20:08Z, bound to 3f9d187a; NOT yet answered when this was written. kimi is the sole reviewer per dp; codex's silence is not agreement. dp's explicit word decides the fire and is NOT yet given.
- **Pre-registered reading (written before any fire):** ERROR / runtime exceeded → even a 5-minute ceiling with 200 calls overruns: sessions must be ended by something other than the clock, or per-task overhead is above about a minute. Score >= 0.18 → first score outside the 0.08–0.17 band. 0.12–0.17 → inside the band at one draw (noise about 0.05): no verdict on the unboxed budgets; it does show the package completes inside the wall. <= 0.10 → the long-thought agent does not fit five minutes, or the host does not grade the unsubmitted working tree the way the local harness does. The fresh-sample rate (3 of 24) predicts the inside-the-band outcome.

## 2026-11-11 21:22:19Z: v68-empower-uncapped-runfact-think4k-t6 SUBMITTED, ref 58250837, SCORED 0.17 (thor-claude, on dp's word; staged 15:34Z)
- ZIP `blackbox/runs/swe-v68-empower-uncapped-runfact-think4k-t6-prepared-20261111/submission.zip`, SHA256 4959f5bbe31c554d1d28b46269e3d0ab5a10321ad9a6213d2f4012b5163745bb; tree `submissions/v68-empower-uncapped-runfact-think4k-t6`; builder `blackbox/analysis/claude_swe_earlyfinish_1111/build_v68.py`.
- What it is: v65 (73f0bec9) with `max_time_minutes` 20 → 6 and the prompt's two clock mentions 20 → 6; nothing else. v65 = thought 4,096, max_output 8,192, 200 tool calls, 500 turns, nine flat tools, truthful ending with the literal `SESSION COMPLETE` reply, the run fact (many issues share one 12-hour run).
- Why 6 minutes: v58 (20-minute ceiling) ERRORED with 'exceeded the allowed runtime'. The ceiling is the bound that does not depend on an unverified host clock or on the agent obeying a recommended budget.
- Local evidence (public tasks, one draw each, scaled clock): v68s24 on the frozen 24 = 19 resolved, 1 unresolved, 4 harness UNKNOWN (19 vs v65s80's 20 on the 20 comparable cells; 18 vs v67s32's 14 on 19); mean 1,092 s; 10 sessions reached the clock and 9 of them resolved through the working-tree fallback or an earlier submit. Exact-ZIP smoke receipts present (000419).
- Wall projection, 120 tasks (129 in brackets), from v68s24's durations at a 6-minute ceiling: 9.3 (10.0) / 9.1 (9.8) / 8.4 (9.0) / 7.8 (8.4) h at r = 3.8 / 4.0 / 4.35 / 4.65 with no overhead; +1 h per 30 s of per-task overhead; the one cell over 12 h is 129 tasks at 60 s and r = 3.8 (12.1 h). A scenario under assumed speed and overhead, not a hosted measurement.
- Review: kimi-code AGREE bound to 4959f5bb (15:26Z 11-11, exact-ZIP read: only eval_config.yaml and the two clock mentions differ from v65). kimi is the sole reviewer per dp ('codex is out of usage, proceed with kimi's review'); codex's silence is not agreement. dp's explicit word decides the fire and is NOT yet given.
- **Pre-registered reading (written before any fire):** ERROR / runtime exceeded → even a 6-minute ceiling overruns: per-task overhead or the task count is larger than assumed; next step is 5 minutes or fewer, or fewer tokens per session. Score >= 0.18 → first score outside the 0.08–0.17 band: the unboxed budgets (thought, calls, turns) with true facts are worth it inside a bounded clock. 0.12–0.17 → inside the band at one draw (noise about 0.05): no verdict. <= 0.10 → worse than the old boxed packages at a similar clock: the long-thought agent does not fit six minutes, or the host does not grade the unsubmitted working tree the way the local harness does (about half of the local solves at this ceiling came through that fallback).
- **Update 20:27Z 11-11 (before any fire):** dp rejected the 5-minute v69 ("shorting ourselves 2 hours of runtime - NO ... none of our other 6-minute runs errored out, so at least do that"); v68 is dp's card. kimi-code (sole reviewer) at 20:24Z WITHDREW its AGREE on 4959f5bb in favour of v69 (reason: at the fresh sample's 92% clock occupancy, 120 x 6 min is ~11.0 h and 129 is ~11.9 h before overhead; inadequate headroom if that transfers); its mail crossed dp's decision. So a v68 fire goes on dp's word WITHOUT a standing peer AGREE, and that is recorded here. Reading tightened per kimi: only an explicit runtime-exceeded receipt supports a timeout reading (a bare ERROR does not); bands contiguous at two decimals: >= 0.18 above, 0.12-0.17 inside, <= 0.11 below; a below-band score leaves the mechanism unresolved. The frozen 24 are an in-sample regression panel, not a forecast: on a fresh 24-task sample v68s24 resolved 3 of 24.
- **21:22Z 11-11, dp's word and predictions, written BEFORE the fire:** dp: "ok, fire v68. i predict .15 - make your prediction :)". thor-claude predicts **0.13** if it completes (the fresh 24-task sample resolved 3 of 24 = 0.125; nothing measured out of sample says the unboxed budgets beat the old packages), and puts about one chance in three on a runtime-exceeded error (19 of 24 fresh sessions used the whole clock; 120 x 6 min is 12.0 h before overhead; the earlier 6-minute packages had call/turn caps this one lacks). v70 (run clock) was built and tested tonight and NOT fired: sessions mostly did not read the clock and did not obey it. Fired without a standing peer AGREE (kimi withdrew at 20:24Z).
- **SCORED 0.17** (first read without PENDING 2026-11-12 10:21Z; still PENDING at 09:50Z, so COMPLETE 12.5-13.0 h after submit). Against the pre-registered reading: no runtime error, so **the unboxed budgets (thought 4,096, 200 calls, 500 turns) at a 6-minute ceiling fit the 12-hour wall**; 0.17 is inside the 0.12-0.17 band at one draw (noise about 0.05): no verdict on whether unboxing helps. It ties our best hosted score (v12, 0.17, whose replicate scored 0.12). Predictions made before the fire: dp 0.15, thor-claude 0.13 with one chance in three of a runtime error: both low, dp closer, my error risk did not materialise. Local reads beside it: 3 of 24 on fresh panel A (3 of 19 valid), 4 of 24 on valid panel V1 (0.17). On about 58 public tasks 0.17 is 10 solved. Host fact also bought: most local sessions at this ceiling were cut with nothing submitted, and the score is in the band, which is consistent with the host grading the unsubmitted working tree (not proven: the score could come from the submitted sessions alone).

## 2026-11-10 22:53:47Z: v58-empower-final-think4k-t20 SUBMITTED, ref 58216375 (thor-claude)
- ZIP `blackbox/runs/swe-v58-empower-final-think4k-t20-prepared-20261110/submission.zip`, SHA256 befccab4e0f1588f1e196b038bb640a0a7b58dc81500346b0742157c50c72d0a; tree `submissions/v58-empower-final-think4k-t20`; builder `blackbox/analysis/claude_swe_next_1109/build_v58.py`.
- What it is: codex's final flat package (4206897f: 31B, thinking 4,096, max_output 16,384, 60 calls, 100 turns, nine flat tools, discretionary procedure, submit-last, full-file write wording) with exactly two edits: max_time_minutes 8 → 20 and the prompt's stated clock. First fire of an unboxed thinking agent.
- Selection: dp's non-negotiables (thinking on, 20-minute ceiling: the cap is a ceiling for hard tasks, the wall is managed through the average); codex AGREE bound to card 4 (22:37Z), claude AGREE, dp "fire v58" (22:5xZ); kimi's vote had not arrived (kimi's own v56 = this prompt at 6 min read rc=3 on Thor). The day's earlier card (v45, thought off) was voided at 20:02Z when codex withdrew on dp's directive.
- Evidence: exact-ZIP smokes on Thor — 4206897f at 8 min resolved both tasks (326 s, 487 s); v58 at 20 min: rich_3894 resolved at 447 s with a 587-char patch (fastapi_14301 still running at fire). Hosted scale ~3.6–4.65× Thor (codex; v26 8-min thinking-4,096 completed hosted).
- Risk accepted by dp: exceeding the 12 h sequential wall errors the whole submission (secondary sources). Codex scenarios for 120 tasks: 11.2 h at 4.65×, 12.8 h at 4×, 14.2 h at 3.6×.
- Pre-registered reading: ERROR/timeout → the wall binds at this average; next build needs the run-level soft timer and early termination before a long ceiling. Score ≥0.18 → outside the 0.12–0.17 band for the first time: the box was the variable. 0.12–0.17 → inside the band; the unboxed agent neither helped nor hurt at one draw (noise ±0.05). ≤0.10 → harmful as built (deliberation without early finish).
- **ref 58216375: ERRORED, no score (public field empty; read 11-11 11:1xZ, thor-claude).** Kaggle list: status COMPLETE, public score empty, total_bytes 0; API `error_description`: "Your submission notebook exceeded the allowed runtime. Review the competition's Code Requirements page for the time limits. Note that the hidden dataset can be larger/smaller/different than the public dataset." PENDING at the 10:50Z check, COMPLETE at 11:09Z: 11.9–12.3 h after the 22:53:47Z submit. It is not a 0.00; the run did not finish. **By the reading registered above: the wall binds at this average.** First-party confirmation that exceeding the limit errors the whole submission (until now secondary sources only). Calibration: v26 (8-minute clock) completed and v58 (20-minute clock, thought 4,096, 60 calls) did not, so for these bytes hosted mean session + overhead exceeded 12 h / N. Local scaled-clock mean for the same family (v63s80, 24 public tasks) was 1,565 s on Thor. Next: no fire of a 20-minute-ceiling package without a mechanism that bounds the run (`blackbox/analysis/claude_swe_earlyfinish_1111/capped_mean.py` gives the ceiling x speed x overhead table).

## 2026-11-09 21:28:31Z: v41-flatcall28-t6 (kimi-code's candidate) SUBMITTED, ref 58175687 (thor-claude)
- Selection: no 11-09 candidate met its own pre-registered PRIMARY (v41 early-edit 14/24 vs 18; v42 t20 15 < 16; v45 t20 14 < 16; v43-on B 11; v43-off; v47; v48 HARM; v49 B 10). Under the fallback (non-HARM, smoke-passed, kimi's t20-first ordering with a paired draw when views disagree): paired 000385 v45 13/21 vs v42 7/21; paired 000387 v41 10/15 vs v45 5/15 → v41 by thor-claude's pre-registered reading.
- Devil's-advocate caveat on record (PRD 18:3xZ): 5 of v41's 10 panel wins were harvested at the 20-min wall (854–1207 s Thor); all 5 v45 wins ≤ 632 s; 5 vs 5 without them; v41 leads only if hosted ≥ ~3.2× Thor (unmeasured). Every tighter view (T360 11 vs 2, B=3.5k 14 vs 13) favours v45. The fire therefore measures 'thought channel on + 28-call cap + early-edit plan at hosted speed' against v37's 0.15.
- Agreement: kimi-code is the candidate owner (PREREGISTER.md 0c9430c0); asked 16:14Z/18:12Z/18:16Z/21:06Z, no mail since 23:08Z 11-08 → 'asked, no objection'. Codex unavailable (dp 11-08). dp veto file runs/STOP_swe_1109 absent at fire time.
- Pre-fire checks: no veto file; ZIP sha256 1ddc3bc44f589b3888a9de7203aebec976adb52973cd6e9ef0083377c2d25b16 re-verified; dry-run passed 18:09Z and at fire time; v37 (scored) not refired.
- Fired with `blackbox/runs/swe_submit_once.py --zip /home/dp/ai-workspace/SWE-SAGE-wt-kimi-next-1109/submissions/v41-flatcall28-t6_submission.zip --sha 1ddc3bc44f589b3888a9de7203aebec976adb52973cd6e9ef0083377c2d25b16 --day 2026-11-09` (one attempt). Kaggle ref 58175687.
- **Pre-registered reading** (written before the score; noise ≈ ±0.05 on one draw): **≥ 0.17** the thought channel and the call-cap plan survive the hosted clock → 11-10 line v49 (channel + v45 paragraph). **0.13–0.16** no evidence either way → 11-10 picks by the paired 6-minute view (v45 line). **≤ 0.12** the tight views were right; the channel costs the hosted clock → 11-10 thought-off from v45.
- **SCORED 0.13 public (58175687; field `publicScore`, scale 0-1 = fraction of tasks resolved, about 8 of ~58).** COMPLETE between 09:37Z (last PENDING read by the supervisor) and 10:37Z 11-10, about 13-14 h after the fire. Row written by the Thor supervisor at the 10:37Z wake.
  - Under the pre-registered reading (0.13-0.16): inside the band, no evidence either way; per the prereg the 11-10 pick goes by the paired 6-minute view (v45 line). Against v37's 0.15 it is 0.02 lower (about 1 task), inside the ~±0.05 noise.
  - Devil's-advocate caveat: 0.13 is the lowest score in the band; one task fewer (<= 0.12) would have switched the 11-10 pick to thought-off. The ±0.05 noise rests on the single v12 pair (0.17/0.12), the ~58 denominator is inferred from the score lattice, and the three stacked levers (thought channel, 28-call cap, early-edit plan) cannot be separated by this score. What would settle it: a paired local v41 vs v37 at T360 counting discordant tasks, or a scored replicate.
- **SCORED 2026-11-10 10:39Z: 0.13** (public). Below v37's 0.15 (no skills, thought on, 6 min); the scored ladder is v28 0.12 → v41 0.13 → v23b/v18/v37 0.15 → v12 0.17. Pre-registered reading (PROPOSAL_1110 tree, written before the score): 0.13–0.16 → **fire v45 (58bcb756, thought off)** today, v51 excluded (HARM/NULL 000392); backstop v49. What the score says (corrected 10:4xZ on codex's exact-ZIP comparison): v41 = v49 minus the tool-argument-format paragraph, so it differs from v45 in BOTH the thought channel and that paragraph and isolates neither; one unpaired submission against v37's 0.15 does not measure the hosted clock ratio. It removes nothing from the six-minute local reads and gives no sign that the hosted clock is long enough for the thought channel to pay; the pre-score band rule applies. Every six-minute view (000391 12 vs 7, 000393 qualified 2 vs 0 with one v45 UNKNOWN (raw 1 vs 0), T360 11 vs 2) favours v45. Recorded by thor-claude; card to codex + kimi follows.

## 2026-11-08 19:29:59Z: v37-noskills-t6 SUBMITTED, ref 58139177 (scored 0.15, row below) (thor-claude)
- dp 19:2xZ: "kimi agreed on v37, fire when ready". Codex unavailable (dp); its standing criteria were applied.
- Pre-fire checks: no veto file; ZIP sha256 ae66025ad47b6d4b88f2bca4cc31debeefc65ed1cad66a313194c64e908388c6 re-verified; no earlier attempt marker for 11-08.
- Fired with `blackbox/runs/swe-v37-noskills-t6-prepared-20261108/fire.sh` (swe_submit_once.py, one attempt). Kaggle: "Successfully submitted", ref 58139177.
- **Pre-registered reading** (written before the score; noise is about +/-0.05 on one draw):
  - **>= 0.17:** removing the broken skill affordance helps under the hosted clock, the t20 view wins, and the budget model's ordering is wrong for v37.
  - **0.10-0.16:** inside the band; no evidence either way.
  - **<= 0.09:** consistent with the budget model (v37 trails v32c at ~3.5k tokens); test the model directly next.
- **SCORED 0.15 public (58139177; field `publicScore`, scale 0-1 = fraction of tasks resolved, about 9 of ~58).** COMPLETE between 08:37Z (last PENDING check by the supervisor wrapper) and 09:04Z 11-09 (the interactive seat's read), about 13.6 h after the fire. Row written by the Thor supervisor at the 09:37Z wake; check_subs.py had reported "0 changed", see the supervisor log.
  - Under the pre-registered reading (0.10-0.16): inside the band, no evidence either way. One draw. Noise about +/-0.05, and that figure is one replicate pair (v12 0.17 / 0.12), not a confidence interval.
  - Devil's-advocate caveats: direction against v32c (0.15 vs 0.12, about 9 vs 7 tasks) is uninformative, so the budget model is untested, not "0 for 1"; only >= 0.17 would have counted against it. Best on Kaggle's list remains v12 0.17 (57104463), whose replicate scored 0.12 (57124955); 0.15 now appears on 6 refs. "~58" is inferred from the score lattice (all 25 numeric scores fit truncated k/58), not read from the host, and k/120 cannot be excluded.

## 2026-11-08 18:58Z: SELECTED for the 11-08 slot by the posted rule: v37-noskills-t6 (fire ~21:30Z unless kimi HOLDs by 20:30Z) (thor-claude)
- **Candidates tested** (frozen 24-task panel at t20, fail-closed stubbed rescore, valid 19-21):
  - v37 t20 16/19, budget B=3.5k 9/21.
  - v38c 15/19, 8/19 (misses its bar).
  - v39 16/19, 6/19 (gate not met).
  - codex flat3 15/18, 10/18 (navkit 6/24).
  - kimi matrix 15/21, 10/20 (HARM by kimi's own rule).
  - hybrid 14/21, 7/21.
  - v32c reference 15/19, 12/19.
- All seven exact ZIPs passed the 6-min Thor GPU smoke (000372 and 000373z).
- **v37** = scored v32c minus skills, flat tools. ZIP ae66025ad47b6d4b88f2bca4cc31debeefc65ed1cad66a313194c64e908388c6. 000371 PROMOTE over v36c (16 vs 15; malformed 0 vs 71).
- **Stated risk:** the budget view (working model of the hosted clock) puts v37 below v32c (9 vs 12).
- **Agreement:** codex is unavailable (dp), and its standing criteria were applied. kimi was asked (10881, 10883, 10884). Fire script `blackbox/runs/swe-v37-noskills-t6-prepared-20261108/fire.sh`; dry run passed 15:39Z; veto `blackbox/runs/STOP_swe_1108`.

## 2026-11-08 02:58Z: v37-noskills-t6 STAGED as the 11-08 PRIMARY candidate, NOT ARMED (thor-claude)
- **v37:** the scored v32c bytes with the four skills removed (agent.yaml `skills:` block and `skills/` dir) and prompt steps 2, 3 and 6 routed to `run_command` grep, `read_file` line ranges and `get_code_neighbors`. Clock 6, budgets unchanged. `blackbox/runs/swe-v37-noskills-t6-prepared-20261108/submission.zip`, sha ae66025ad47b6d4b88f2bca4cc31debeefc65ed1cad66a313194c64e908388c6 (7,657 bytes). Builder `blackbox/analysis/claude_swe_primary_1108/build_v37.py`. compile_check COMPILES.
- **Why:** 17% of calls in failing base_t90 runs were `run_skill_script` calls mangled into INVALID_ARGUMENTS on the nested `args` object. v12 (0.17, best scored) had no skills.
- **Gate:** gpuq 000370 (two draws at t90), read on the inline_snapshot-stubbed rescore. PROMOTE over the v36c backstop if >= 6/14 resolved (requests excluded), rich_2725 >= 1/2, 0 malformed; HARM if <= 3/14 or rich_2725 0/2. Plus codex AGREE.
- **Local grader gap (blackbox PRD 11-08 02:58Z):** the local sandbox lacks inline-snapshot (the scorer image has 0.36.0), so 28 fastapi tasks could never resolve locally. Rescored with a stub, base_t90 is 3/2/3 of 7 and no stored variant beats it.

## 2026-11-08 02:39Z: v36c-v32c-issuefact-t6 STAGED as the 11-08 BACKSTOP, NOT ARMED (thor-claude)
- dp 11-08: "queue it tonight on the backstop, but keep working on a better one".
- **v36c:** the scored v32c bytes + one Facts bullet (issue numbers are not in the code), clock 6, budgets unchanged. `blackbox/runs/swe-v36c-v32c-issuefact-t6-prepared-20261108/submission.zip`, sha fc5659334bfb5707c9bc2c6b4d710eaa75970970a3650c8d70f4caf14b68b04a (42,088 bytes). Tree `submissions/v36c-v32c-issuefact-t6/`; builder `blackbox/analysis/claude_swe_runcmd_1106/build_v36c.py`. `diff -r` vs the scored ZIP's contents: the one bullet only. compile_check COMPILES.
- **Gate:** gpuq 000369 (two draws at t90, 16 sessions). Pre-registered harm (any blocks): rich_2725 unresolved in both draws; nonempty <= 8/16; source-file patches <= 8/16; a task with > 10 grep exit-1 results. Plus codex AGREE.
- **Fire:** `fire.sh` staged; submitter dry run passed 02:39Z, nothing sent. Veto `blackbox/runs/STOP_swe_1108`. A better primary candidate may replace it.

## 2026-11-07 18:02Z: v36 HELD (codex), v36b NOT FIRED (000368 tripped its harm gate); 11-07 SLOT MISSED (thor-claude)
- **v36** held by codex: its scratch-in-/tmp bullet steered `write_file` to /tmp/repro.py in 000367, which the tool rejects (workspace-only paths). Dropped.
- **v36b** = scored v32c bytes + exit-code and issue-number bullets. `blackbox/runs/swe-v36b-v32c-exitfacts-t6-prepared-20261107/submission.zip`, sha 697a4d55e64fc63ec2963c887c77ea6c5dd6423ed6eae65116d26b8074f4406c (42,251 bytes); tree `submissions/v36b-v32c-exitfacts-t6/`. Never armed (no fire.sh).
- **000368** (v36b local twin at t90, 8 tasks): 0/8. rich_2725 unresolved (80-turn cap) vs base_t90 resolved 3/3 on file. Pre-registered harm clause tripped, so no fire. Nonempty 7/8, source-file patches 5/8 (base 6/8), scratch in patch 4/8 (base 1/8), grep exit-1 max 5.
- **No SWE submission on 2026-11-07.** No unscored fallback survived its checks.

## 2026-11-07 16:02Z: v35 NOT FIRED (000367 tripped its gate); v36-v32c-facts-t6 STAGED, NOT ARMED, on codex AGREE (thor-claude)
- **000367** (runs/swe_runcmd3_1107/pair_out, 15:34-15:59Z; v35 bytes vs the scored v32c bytes, both at 6 min on Thor, paired per wave): every task in both arms hit the 6-min clock after 3-11 calls (Thor ~40-60 s/call); nonempty patches cand 1/8, v32c 2/8; 0 crashes in either arm. v32c scored 0.12 hosted with these bytes, so the host is much faster than Thor and absolute numbers here do not predict a score.
- **v35's gate tripped** (pre-registered: no new failure class vs v32c): runcmd3's "first call, always" install step was obeyed **0/8** (every task's first call was run_command), and 2/8 tasks hit "No such file" for /tmp/skills, which v32c cannot hit (direct run_skill_script). v35 does not fire. runcmd v1 has the same class (6/8) plus the echo loop, so it is out too.
- **v36:** the scored v32c bytes + three Facts bullets (exit codes; issue numbers are not in the code; scratch files go in /tmp), clock 6, budgets unchanged. `blackbox/runs/swe-v36-v32c-facts-t6-prepared-20261107/submission.zip`, sha 6d4c0594dc82317ede92338927389eb61cf480aecb1f85d501be675daff76ae4 (42,298 bytes). Tree `submissions/v36-v32c-facts-t6/`; builder `blackbox/analysis/claude_swe_runcmd_1106/build_v36.py`. `diff -r` vs the scored ZIP's contents: the three bullets only.
- **Validation:** compile_check COMPILES (6 min, 90 calls, 80 turns). The e2e sandbox test is runcmd-specific (install dir, cap note) and fails identically on the scored v32c bytes, so it does not apply here. The v32c bytes ran cleanly in 000367. Submitter dry run passed 16:01Z, nothing sent.
- **Reading (codex wording):** bundle-level only. A one-draw delta against v32c's 0.12 sits inside about ±0.05 noise and attributes nothing to the facts.

## 2026-11-07 15:08Z: v35-runcmd3-t6 STAGED, NOT ARMED (thor-claude): 11-07 slot candidate, gated on the 000367 smoke and codex AGREE
- **Bytes:** `blackbox/runs/swe-v35-runcmd3-t6-prepared-20261107/submission.zip`, sha 026b6503da9a63ec2034b73aee31f13d98196b5c495bb53c6dcc61a425bb55e3 (116,470 bytes). Tree `submissions/v35-runcmd3-t6/`, identical to `blackbox/runs/swe_runcmd3_1107/cand_t6` (built by `analysis/claude_swe_runcmd_1106/build_runcmd3.py`, packaged by `package_v35.py`).
- **What it is:** the scored v32c prompt lineage (single agent) + skill scripts via run_command (runcmd: malformed skill calls 66 resends -> 0) + runcmd2 (echo loop 59 -> 0, output-cap note) + three facts that bound today: install first (runcmd "No such file" 6/8 tasks; staged2 0/8 with it), exit codes (grep exit-1 max 64 -> 9), scratch in /tmp. Clock 6 min (v32c's scored clock), 80 turns / 90 calls, timeout 600.
- **Local evidence so far:** runcmd v1 0/8 (000360), runcmd2 0/4 (000361; it ran without the CLI hints that are now in the tree). No local run of these bytes yet: **000367** (queued after 000366, ~21:00-21:30Z) runs them against the scored v32c bytes at 6 min, paired per wave.
- **Fire gate:** 000367 shows no new failure class against v32c (install errors, crashes, empty-patch rate clearly worse), and codex AGREE; fire ~22:00Z, before the submitter's 23:30Z cutoff. If 000367 shows a defect: no fire of v35, and the decision goes to codex (v32c + exit fact, or runcmd v1).
- **Reading (codex wording):** a score is a bundle-level observation; >= 0.18 encouraging, <= 0.11 a disappointing draw; neither attributes cause without hosted task-level timing.
- **Validation:** compile_check COMPILES (time 6, calls 90, turns 80); e2e `--cap` FAILS none; submitter dry run 15:08Z: every gate passes, nothing sent.

## 2026-11-07 15:05Z: v34-loop2b-t8 WITHDRAWN on codex HOLD (thor-claude)
- Codex HOLD (bound to 10475; `blackbox/analysis/codex_heartbeat_v34_review_1500_1107/`): the bytes match the tree, but the pick is unsupported. Thor's first fixer call came after 480 s in all 8 000365 tasks, so the locator alone exceeded the 8-min clock locally; the review loop never cycled (0 CHANGE); the one resolve was an unreviewed timeout capture. Accepted. My "~25 s/call" host figure was illustrative, not evidence.
- Amended readings (codex), kept for any future fire of this shape: >= 0.18 is an encouraging bundle-level observation, <= 0.11 a disappointing draw; neither attributes cause without hosted task-level timing.
- Scratch in the local 000365 patches: 2/8, not 1/8 (requests_6629 test_simplejson.py).

## 2026-11-07 14:59Z: v34-loop2b-t8 STAGED, NOT ARMED (thor-claude): candidate for the 11-07 slot (~21:30Z), on codex AGREE
- **Bytes:** `blackbox/runs/swe-v34-loop2b-t8-prepared-20261107/submission.zip`, sha c0c5bac76f042f68ca439097a867b879656d41665cf22fc38d79551e7a35751b (120,757 bytes, 32 files). Tree `submissions/v34-loop2b-t8/`, built by `blackbox/analysis/claude_swe_loop_1107/package_v34.py`.
- **What it is:** the 000365 loop2b tree with ONLY the clock changed, 90 -> 8 min (the longest clock that completed scored, v26). staged2 locator -> LoopAgent(3)[fix, fresh-context reviewer that diffs as submit_patch does and approves by submitting] -> fallback submit. max_turns/calls 160, timeout 600.
- **Local evidence (Thor, 90-min clock, 8 predeclared tasks):** 1/8 resolved (rich_2725), tying base and staged; the reviewer approved 3/3 reached tasks with 0 CHANGE (a rubber stamp); the fixer is unbounded (4/8 timeouts). The working parts are facts: install first, exit codes, scratch in /tmp (graded scratch 1/8 vs 4/8).
- **Why it over v32c + exit-code fact:** the unknown-shot rule (dp 11-01/11-07). The v32c family is a known 0.12-0.17 band; loop2b is a new shape, never scored.
- **Known risk, stated before the result:** at 8 min the locator (local median 13.5 calls, max 60) may consume most of the clock. A truncated fixer still yields its dirty tree (the harness captures it), but a locator that runs out the clock yields an empty patch.
- **Pre-registered reading:** >= 0.18 = the staged shape transfers under the scored clock (beats every score on file); 0.12-0.17 = inside the band, no evidence either way; <= 0.11 = the locator eats the clock (check for empty patches if Kaggle exposes any detail; it usually does not).
- **Validation:** scorer compile_check COMPILES (time_minutes=8, turns 160, calls 160); e2e sandbox (`--cap`) FAILS none; swe_submit_once.py --dry-run 14:59Z: every gate passes, nothing sent. Fire script `fire.sh` (veto `blackbox/runs/STOP_swe_1107`). Fallback: runcmd v1 (never scored).

## 2026-11-05 21:02Z: v33 EXPLORATORY LoRA SUBMITTED, ref 58035448 (score pending)
- **Bytes:** `v33_lora_r2_step400_list_submission.zip`, sha 65a9371f5fb1cbc06354173e269b9eaddef7adb61187e5c62551dc05ea2f2412.
  It is the scored 8101 v32c baseline unchanged, plus `adapter: swe_lora_1105` in agent.yaml and `adapters/swe_lora_1105/`.
  The adapter is a q_proj-only rank-8 LoRA over 60 layers: run 2 of codex train.py, step 400 (weights 7e2f…95c6). Its config is the list form, `target_modules ["q_proj"]` (config 5c04…b0c).
  Codex checked the package byte by byte against 8101: integrity PASS (heartbeat 10107).
- **Fire:** dp ruled "go ahead and fire it. the learning will be valuable" at about 21:00Z. Fired 21:02:30Z via swe_submit_once.py. The marker is `blackbox/runs/SWE_ATTEMPT_2026-11-05.json`.
- **EXPLORATORY, not a quality candidate.** Codex selection was HOLD (10109/10110): it wanted a paired base-vs-step-400 multi-step check and a panel run of the zeroed copy, and neither ran before the slot. This is the first hosted score of ANY adapter.
- **Pre-registered readings** (written before the score):
  - **0.00 or an error:** the hosted harness did not load the adapter, or it broke the agent. Read the error before blaming the weights.
  - **≈0.12:** no detectable effect within noise of ±0.05, n=1.
  - **≥0.17:** the first evidence that the adapter helps.
  - **≤0.07:** the adapter hurts. Prime suspect: reasoning collapse.
- **Known unknowns:**
  - On the local panel the adapter cut reasoning tokens hard: read_file 87–191 → 1, run_command 252–522 → 45–57.
  - The cause is that the training targets carry OpenHands' short pre-call prose as reasoning.
  - Decode measured 0.614× base on synthetic prompts. That doesn't establish full-task time.
  - 15/15 matching tool names does not make the decisions equivalent.
- **Local evidence:** `blackbox/analysis/claude_swe_lora_eval_1105/RESULT_1105.md`, from gpuq 000355.
- **SCORED 0.06 public (58035448; field `publicScore`, scale 0-1 = fraction of tasks resolved, about 3-4 of ~58).** COMPLETE between 11-06 02:38Z and 03:37Z (supervisor check_subs). Thor supervisor, 11-06 03:4xZ.
  - Lowest COMPLETE SWE score on file. Previous low v22 0.08 (adapter-free); range so far 0.08-0.17 counting v22 (the "Band so far" line in the v32c row omits v22 and the 0.10s). 0.06 below v32c (same bytes without the adapter), 0.02 below v22.
  - Pre-registered band: "<= 0.07: the adapter hurts". Recorded as CONCERNING, n=1, not established (codex 10165 caveat: the ±0.05 figure is one replicate pair, v12 0.17/0.12, not a confidence interval; ~3 tasks of ~58 cannot be separated by one draw).
  - "Reasoning collapse" is untested: it comes from a 15-decision single-step panel. Adapter load on the hosted runtime is `?` (no receipt). Hosted run finished in ~6.5 h vs 13-46 h for recent runs: unexplained, worth reading (it would fit shorter reasoning OR an early-stop path).
  - Local paired base-vs-lora t90 (gpuq 000356/000357, `blackbox/runs/swe_lora_pair_1105/out/`) speaks to neither side yet: 0 resolved in either arm over 14 finished receipts, so 0 discordant pairs; base hit the 80-turn budget more often than lora. Codex HOLD 10172 on aggregating it stands.
  - What would settle it: more paired tasks with discordant counts; a local multi-step test of the zeroed adapter (does the adapter path alone, 0.614x decode, cost tasks?). Reviewed by thor-devils-advocate before writing.

## 2026-11-05 13:3xZ: v32c nostopseq-t6 (57999357) scored 0.12 public: ADDS ONE POINT TO THE BAND
- COMPLETE, `publicScore` 0.12 (scale 0-1, the fraction of public tasks resolved; the ~7 of ~58 conversion is copied
  from the v28 row, not checked). check_subs.py found it between 11-05 12:37:55Z and 13:37:55Z, about 16 h after the
  21:30Z fire. Run-to-run noise is about +/-0.05; n=1.
- **Reading:** none on the levers. v32c had no pre-registered score reading. The v32 "<= 0.12: no gain" bar below
  belonged to the autostop-t8 bytes (stop sequence, 8 min) and does not transfer. context2 has no scored run of its
  own, so none of the three stacked changes (context2, repo-paging default, SESSION COMPLETE step text; no stop
  sequence, 6 min) can be credited or blamed. (Caveat from thor-devils-advocate, accepted.)
- **Band so far:** v12 0.17 (its replicate 0.12), v18 0.15, v23b 0.15, v27 0.15, v25 0.15, v28 0.12, v32c 0.12,
  v26 0.12, v24 0.10.
- **What would settle it:** a paired local t90 sweep of v32c vs v28 on the same tasks (count discordant), or a scored
  run of context2 alone. Thor supervisor (thor-claude).

## 2026-11-04 21:30Z: v32c nostopseq-t6 SUBMITTED, ref 57999357 (score pending)
- One attempt. The marker `blackbox/runs/SWE_ATTEMPT_2026-11-04.json` records submitted_ref 57999357 at 21:30:06Z.
- A fresh list read shows that row at the top. The timer is disabled. Receipt mailed to codex as 9899.

## 2026-11-04 18:03Z: v32c nostopseq-t6 (ZIP 8101f855) ARMED for 21:30Z, on codex AGREE 9876
- **FIRED 21:30:06Z: Kaggle ref 57999357.** Sources: the local fire log and attempt marker (heartbeat 900564 mail); the supervisor's check_subs.py remote listing at 21:37:55Z shows 57999357 PENDING, public score not yet posted. When it posts, put the score here (public field; run-to-run noise about ±0.05). (thor-claude supervisor)
- **Picked under the frozen rule:** blackbox `analysis/claude_swe_malformed_1104/RULE_1104.md` (9576f6e3, frozen before results). Verdict: `VERDICT_1104.md`.
- **Rule 1 failed on branch 4.** argfix-t6's malformed fraction was .231 vs nostop's .200; resolved 4/8 vs 4/8; no successful submit 4 vs 3.
  - The backtick shape persists in argfix (99/125), so the inline-code priming route is refuted on this sample.
- **Stop sequence excluded:** autostop resolved 1/5 vs 2/5.
- **Branch 4 chose nostopseq-t6 over pagerdefault.**
  - Resolved is tied: 2/5 vs 2/5 and 5/9 vs 5/9.
  - Pager is better on no-submit and on malformed. Nostop cleans up its repro files, then stops within 6-14 calls; pager makes 41-63 more (codex 9873).
  - Close call (codex). One t90 draw; no t6 or private lift claimed.
- **Accepted for this slot:** the shared pager dot-dir completeness risk (codex 9767/9866, disposition 9875). Fix and test it before the next promotion.
- **Bytes:**
  - fire dir `blackbox/runs/swe-nostopseq-t6-8101-prepared-20261104/`, fire.sh 6d215694…e4a8.
  - submitter rev 3 7b5a6cf0…d2a (one attempt, fail-closed).
  - timer `swe-fire-1104.timer`, veto `blackbox/runs/STOP_swe_1104`.
  - live dry run 15:33Z passed.

## 2026-11-04 09:2xZ UPDATE: v32 DISARMED pending review and ablation
- codex 9805 held the fire on two counts.
  - **The fire gate:** `swe_submit_when_clear.sh` retried after refused or ambiguous outcomes, and its inner wait
    skipped the veto/day/cutoff recheck. It is replaced by the one-attempt, fail-closed `blackbox/runs/swe_submit_once.py`
    (364555e9; 15 fake-API tests, 8/8 mutants killed, live dry run).
  - **The evidence:** 000348's autostop_t90 made 178/518 malformed tool calls, vs pagerdefault 43/659 and dirthink 22/519.
- The timer `thor-swe-fire-1104b` is stopped.
- gpuq 000349 ablates the stop sequence: no-stop vs autostop seed 2 vs pagerdefault seed 2, on 5 tasks.
- The fallback is nostop-t8 (a8b2d8f1). Nothing fires before codex reviews the exact bytes.

## 2026-11-04 08:4xZ: v32 autostop-t8 ARMED for the 11-04 slot (21:30Z), replacing dirthink (superseded above)
- dp 11-04: "swing bold. conservative just assures defeat". The timer `thor-swe-fire-1104` (dirthink e5e83c78, codex
  9620's pick) is stopped; `thor-swe-fire-1104b` fires `blackbox/runs/swe-autostop-t8-99aa-prepared-20261104/fire.sh`.
  Veto: `blackbox/runs/STOP_swe_1104`. The dirthink dir is kept as the fallback.
- Artifact: `submissions/v32-autostop-t8_submission.zip`, sha256 99aa4d13…d1e2 (source
  SWE-SAGE-wt-bold-1103 `submissions/claude-context2-autostop-t8`, commit 6982dcb). VALID, compile_check COMPILES.
- Three levers on codex's context2:
  1. **repo-paging as the default read path.** 000347, t90: paging was used in 6/8 runs (v2r3's optional skill: 0/2).
     Resolved 4/8 vs dirthink 3/8; one discordant task, so this is not evidence of a gain.
  2. **An end-of-session stop.** `stop_sequences: ["SESSION COMPLETE"]` plus prompt step 7 asking for that reply.
     The harness passes no callback registry, so this goes through the generation config. 000348, t90: calls after the
     first submit were 0, 0 and 1 on the tasks where pagerdefault made 62, 65 and 20; none of those three runs was
     nudged.
  3. **`max_time_minutes` 6 -> 8,** with the prompt's session facts matched. 000348 exact bytes: rich_3043 resolved in
     487 s; every 6-minute version timed out on it on Thor. fastapi_11194 timed out with a patch.
- **Pre-registered reading (noise about +/-0.05):**
  - **>= 0.20:** the levers together help; the wall did not bind at 8 minutes.
  - **0.13-0.19:** inside the band; no reading on the levers.
  - **<= 0.12:** no gain.
  - **ERROR / wall overrun:** the 12-h wall binds between 6 and 8 minutes at 90 calls (v26 ran 8 minutes with a 28-call
    cap). The next clock bet then needs a call cap or a shorter clock.
- Thor interactive (thor-claude).

## 2026-11-02 06:4xZ: v28 (57851870) scored 0.12 public: INCONCLUSIVE
- COMPLETE, `publicScore` 0.12 (scale 0-1, the fraction of public tasks resolved, about 7 of ~58). check_subs.py
  found it between 11-02 05:37Z and 06:37Z, about 32 h after the 10-31 22:15Z fire. Run-to-run noise is about +/-0.05.
- **Reading:** 0.03 below v23b's 0.15 (v28 = v23b + one prompt change, an exact fenced get_status() call at step 5).
  That is inside the noise, n=1, so it neither shows the change helps nor that it hurts.
- **Caveat (thor-devils-advocate, accepted):** the planned paired local v28 vs v23b reading was never written here.
  Recomputed 11-02 with blackbox/analysis/claude_swe_verify_census_1027/paired_read.py on the Thor t90 sweep (public
  repos, a proxy): resolved 35/128 vs 31/128, discordant 7 v28-only / 3 v23b-only (10 < 20, sign p about 0.34).
  get_status was called on 44/124 tasks vs 26/124, so the call landed, with no shown effect on score. The local
  proxy (+4) and the scored run (-0.03) point in opposite directions and both are noise. The v29/v30 pairings quoted in
  the row below were an earlier ledger state; today v29 vs v28 is 3/6 and v30 vs v28 is 5/5. Cheapest settler: rerun
  the 10 discordant tasks, both arms, 3 seeds each (after the SWE pause ends).
- **Band so far:** v12 0.17 (its replicate 0.12), v18 0.15, v23b 0.15, v27 0.15, v25 0.15, v28 0.12, v26 0.12, v24 0.10.
  SWE stays paused until after the ARC final (dp 10-31). Thor supervisor (thor-claude).

## 2026-10-31 22:15:31Z: v28 submitted (57851870), score pending
- Fired by the dp-directed waiter `blackbox/runs/swe_v28_after_sweep_1031.sh` (interactive thor-claude lane, dp 10-31:
  v28 is the last SWE submit, then SWE pauses until the ARC final) when sweep 900446 ended (22:14:27Z, rc=0).
  Waiter log: `blackbox/runs/swe_v28_after_sweep_1031.log` ("pending submissions: 0", then ref 57851870).
- Artifact: `submissions/v28_submission.zip`, sha256 d14b383c…3469b (staged 10-27, section below).
- Local proxy before the fire (Thor sweep, public repos, t90): v28 125 graded / 35 resolved; paired vs v29 5/3 and vs
  v30 5/4 discordant, below 20, so no local winner. Public noise about +/-0.05 on a 0-1 scale.
- Row written by the Thor supervisor (22:4xZ wake); the waiter did not write one.

## 2026-10-28 00:4xZ: v25 (57676927) scored 0.15 public: INCONCLUSIVE by its pre-registered reading
- COMPLETE, `publicScore` 0.15 (scale 0-1, the fraction of public tasks resolved, about 9 of ~58). check_subs.py found it
  between 10-27 23:37Z and 10-28 00:37Z, about 28-29 h after the 19:44Z fire. Run-to-run noise is about +/-0.05.
- **Reading (registered 10-26):** 0.10-0.19 is the noise band, so the result is inconclusive.
- **Caveat (thor-devils-advocate, accepted):** agent commands are clamped to the time left in the 6-min task
  (v25/eval_config.yaml:6-12). Above 360 s, this value changes only the timeout of the grading pytest. Its effect on
  public tasks is at most about 1 task (3/129 local hangs), well inside the noise. This score cannot test the
  private-suite bet, and grading time is outside the wall, so it says nothing about wall charging either way.
  (The clamp is read from the bundle note; swegemma execution.py has not been re-read.)
- **Band so far:** v12 0.17 (its replicate 0.12), v18 0.15, v23b 0.15, v27 0.15, v25 0.15, v24 0.10, v26 0.12.
  Thor supervisor (thor-claude).

## 2026-10-27 16:36Z: v30 RE-STAGED, NOT ARMED (thor-claude): v23b + step 8 ONLY, the final-message contract (codex 2217/2219)
- 16:22Z first staging (d1914ce) bundled three components (pre-submit cleanup with an explicit delete, suppressed
  files_changed investigation, text-only final + never resubmit). Codex's review: the delete wording could remove a
  needed new source module (HOLD); submit_patch SNAPSHOTS the diff and later edits do not update it (CPU control), so
  "never resubmit" has a correctness cost after an early submit; 5/26 long tails do recover to text-only; the ledger's
  stop column has 53 explicit turns-budget stops (64 was a >=80-step proxy). All accepted.
- v30 now: step 7 = v23b verbatim; new step 8: once submit_patch returned status ok and nothing was edited since, the
  next message is the LAST, 2-4 plain sentences naming files/functions, NO function call of any kind (get_status and
  submit_patch named), the mechanism stated; an edit after a submit -> submit once more (it replaces the recorded
  patch), then the final message. `diff v23b v30` = one added line (42a43). One component.
- Census (blackbox analysis/claude_swe_verify_census_1027/): of 119 v23b@t90 traces, 24 submitted and then ran to the
  cap; the first post-submit turn separates 50/50 clean text-only vs 26/26 loopers calling (13 get_status, 13
  run_command after a files_changed surprise). The harness's voluntary completion path after submit is a text-only
  turn (agent_runner.py 569-581); other exits are the cap, timeout and the post-run patch_submitted exit.
- compile_check (scorer's compiler): COMPILES. validate (wheelhouse venv, ADK schema + both skills): VALID.
- First local rows (18:17Z, 4 paired tasks): 4/4 text-only endings, 0 submit tails, 0 cap stops (v23b 1); fastapi_15589
  resolved (v23b capped unresolved). Direction as claimed; 4 pairs are not a reading.
- Gauge on the paired local sweep: first-post-submit-turn text-only rate and tail submit_patch runs (26/76 -> near 0 is
  the claim); resolution is NOT the claim (loopers resolved 7/26 vs 23/77). Kaggle eval budget is 6 min/task, so the
  scored value is wall-clock unless the 40 never-submit cap stops share the "how do I end" confusion (open).

## 2026-10-27 05:50Z: v29 STAGED, NOT ARMED (thor-claude): v23b + ONE prompt change, numeric loop breakers (5b')
- The other half of the census (see v28): loopers page a 4,000-line file 150 lines at a time ("I'll keep reading." x10)
  or retry a failing edit verbatim ("I am sorry. I will try again." x10). v29 adds two Rules with numbers: at most 3
  `read_file` calls per file, then `grep -n` and a line-ranged read; a failed `edit_file` is retried once after reading
  the exact lines, then re-anchored, never a third identical attempt. Step 5 and everything else = v23b
  (`diff -rq v23b v29` = system.md only; two added bullets).
- compile_check (scorer's compiler): COMPILES. validate (wheelhouse venv, ADK schema + both skills): VALID.
- Measure on the paired local sweep vs v23b with v28 (one variable each); if both lift, v30 = v23b + both.

## 2026-10-27 05:45Z: v28 STAGED, NOT ARMED (thor-claude): v23b + ONE prompt change, the clock made an exact required call
- Census (blackbox/analysis/claude_swe_verify_census_1027/FINDING.md): 42/119 local v23b tasks never submit, 36 of them on
  the 80-turn cap, looping (paging a 4,000-line file 150 lines at a time; a failing edit retried verbatim; grep-hunting).
  The free `get_status` clock is named twice in v23b's prompt and read by 1/42 loopers (26/77 submitters).
- v28 = v23b with step 5 requiring an EXACT fenced `get_status()` call after every repro rerun and a numeric rule
  (tool_calls_remaining < 15 or time_seconds_remaining < 90 -> keep the best edit, go to submit); the end rule made
  numeric. The locator precedent (0/4 calls as prose -> 105/119 as an exact call) is the reason to expect obedience.
  Skills, tools, budgets unchanged (`diff -rq v23b v28` = system.md only).
- compile_check (scorer's compiler): COMPILES. validate (wheelhouse venv, ADK schema + both skills): VALID.
- Measure FIRST on Thor's paired local sweep vs v23b (n=119) when the ARC jobs release the GPU (~10:00Z): gauges =
  get_status calls by loopers, non-submitters, turns at submit, paired resolved. No slot for v28 before that reading.

## 2026-10-26 19:44:34Z: v25 FIRED (57676927) for the 10-26 slot, on dp's call ("we don't skip free runs but let's see if we can fire a swing")
- **Bundle:** v25 = v23b + command timeout 600 -> 1800 (one variable), sha e66d4bf3...a2b, staged and validated 10-23.
  It is the only staged non-rerun.
- **Codex's 10-23 withhold** (`runs/STOP_swe_v25`, kept as evidence) asked for a v23b replicate first; that ran 10-24.
  Today codex was asked (mesh 1837); dp's call came first. Fired with a fresh veto path, `STOP_swe_v25_1026`.
- **Registered reading (before any result):**
  - at or above 0.20: the timeout lever is still live; next is the wall accounting on the Thor sweep;
  - 0.10-0.19: inconclusive (noise band);
  - 0.09 or below, or a slow ERROR (wall overrun): 1800 s costs more wall than it buys. Return to 600, and the timeout
    arm moves to the local sweep only.
- Why this swing: timeout is the only knob that ever moved our score (120 -> 300 -> 600 s: 0.10 -> 0.13 -> 0.15/0.17).
  (thor-claude)
- **Interpretation narrowed (codex 1857, 10-26 ~19:48Z, accepted):**
  - The cutoffs are ACTION rules, not findings. >= 0.20 is encouraging screening evidence, not proof that the timeout
    lever is live.
  - A low score or a slow ERROR does not establish wall charging without its terminal error or timing evidence.
  - The grading-only mechanism and the unobserved private-suite tail remain hypotheses whatever one stochastic score
    does.
  - Recorded with dp's choice: dp's operator call superseded codex's experiment-selection veto for this run only.

## 2026-10-26 19:37Z: v27 (57638871) scored 0.15 public: INCONCLUSIVE by its pre-registered reading
- COMPLETE, `publicScore` 0.15 (about 9 of ~58 public tasks), after about 25.7 h PENDING.
- **Reading (registered 10-25 17:42Z):** 0.10-0.19 is inside the +/-0.05 noise around v23b's 0.15, so inconclusive.
  Four times the thinking budget under the same 6-min clock neither helped nor hurt measurably.
- **Band so far:** v12 0.17 (its replicate 0.12), v18 0.15, v23b 0.15, v27 0.15, v24 0.10, v26 0.12.
- **Next:** see the NEXT_ARMS_1026.md menu. The command timeout remains the only lever that ever moved the score
  (120 -> 300 -> 600 s: 0.10 -> 0.13 -> 0.15/0.17). (thor-claude)

## 2026-10-25 17:57:43Z: v27 FIRED (57638871) on codex AGREE 17:57:36Z (mesh 1624). One scored submission, no fallback or ERROR resubmit.

## 2026-10-25 17:42Z: v27 STAGED: v23b + thinking_budget 1024 -> 4096 (one variable). Fires only on codex AGREE.
- **Artifact:** `submissions/v27/` (copy of v23b). Only `configs/sampling.yaml` differs: a 3-line header plus `thinking_budget: 4096`.
  Zip sha `13e5cd1b88b398965a2b9bab8cd95308db7abda79aeb5dce1295ed005efe6c89`. Zip members = v23b's 8; only sampling.yaml differs.
- **Checks:** validate VALID; compile_check COMPILES (scorer's compiler: gen config thinking_budget 4096,
  max_output_tokens 8192; budget 6 min / 90 calls / 80 turns; command timeout 600, all unchanged from v23b).
- **Why:**
  - The thinking budget is the one v26 knob never tested on our base. v26 (0.12) bundled it with 28 calls and a 240 s timeout.
  - The target is WRONG FIX in a gold file (73% of failed patches): more reasoning per call.
  - dp 10-25: "build, we don't want to skip free runs".
- **Risk:** 4x thinking per call under the same 6-min clock can cost calls and turns per task. v26 had 8 min.
- **Reading:**
  - At or above 0.20: encouragement.
  - 0.10 to 0.19: inside the ±0.05 noise around v23b's 0.15, so inconclusive.
  - 0.09 or below: thinking under a 6-min clock likely hurts.
  - A fast ERROR's cause is unknown.
- **Waiter:** `blackbox/runs/swe_v27_on_codex_agree.sh` (AGREE_swe_v27_codex, veto STOP_swe_v27, until 22:30Z). (thor-claude)

## Ring facts (competition pages, fetched 2026-09-30 via `competition_list_pages`)
- About **120 hidden test tasks** from **private repositories**, split evenly between public and private
  leaderboards. The 129 training tasks (fastapi / rich / requests / httpx) are NOT the test repos.
- **12 h wall for all tasks, including sandbox setup** (excluding patch validation). Per-task budgets are
  ours to set in `eval_config.yaml`. The `inference.py` default (60 min / 100 tool calls) needs about 120 h.
- Score = resolution rate: `pytest` exit 0 and every FAIL_TO_PASS / PASS_TO_PASS node passed. Patches are
  extracted even when the budget ends the session (HARNESS_README §8.1). Edits to tests and test config are
  reset before grading (§8.2).
- The compiler (`adk-submission`) and harness (`swegemma`) are NOT public (absent from PyPI and from the
  data files). Local validation is `submissions/validate.py`: every documented rule plus the public
  google-adk `LlmAgentConfig` schema. It FIRES on 5 seeded defects (wrong model, unknown tool, include
  outside root, bad extension, misspelled field). The organisers' sample passes except its un-downloaded
  weights; that control corrected the validator's `..` rule.

## How to submit (measured 2026-09-30)
- The uploaded file must be NAMED `submission.zip`. `kaggle competitions submit -f submissions/v1_submission.zip`
  uploaded fine, then `CreateSubmission` returned a bare **400** and used no slot (numToday stayed 0). The same
  bytes under the name `submission.zip` were accepted at once. So copy the versioned artifact to a file called
  `submission.zip` and submit that.
- Check the slot first: `competition_get_submission_limits` → `numAllowedNow`.

## Rows

| ver | date (UTC) | artifact sha256 | what it tests | per-task budget | score |
|---|---|---|---|---|---|
| v1 | 2026-09-30 22:31 (ref 56720270) | `e466c5ea…dd790` | Baseline and **completion first**: one LlmAgent, the 9 harness tools, a numbered procedure that tells the model its real budget, that an unfinished edit is still graded, and that test edits are discarded. No adapters (the sample's are untrained placeholders). thinking 2048 / output 8192. | 4 min, 30 calls, 40 turns, 120 s per command → 120 × (4 + setup) ≈ 10-11 h | **ERROR** at 22:41 (<10 min): *"Your notebook hit an unhandled error while rerunning your code."* No score. |

| v1b | 2026-10-01 00:33 (ref 56739502) | `e466c5ea…dd790` (byte-identical) | **Control:** platform or package? The local harness dry run passes end to end, and the organisers' own sample has failed with the same generic message. | same | **ERROR again**, 00:48, same message. So it's NOT a one-off platform failure. |
| v2 | armed for 2026-10-02 00:0x | `d23d00e5…af6dd` | v1 with **thinking OFF** (`include_thoughts: false`, `thinking_budget: 0`). The dry run shows the request carries `enable_thinking: false` and NO `thinking_token_budget`. | same | *pending* |

**What v1's score can tell us:** first, that the package compiles and the run completes inside the wall
(an ERROR is the answer to that too); second, the floor for a budget-disciplined single agent. With no
telemetry, the next lever is chosen on the training tasks locally, never on the score alone.

— thor-claude

## v1 ERROR: what is known (2026-09-30 22:45 UTC)
- It failed inside 10 minutes, so this is NOT the 12 h wall; it is startup or the first task.
- **Every check the harness ships passes on v1.** The hosts publish the harness as the dataset
  `metric/gemma-4-developer-agent-wheelhouse` (swegemma 0.2.7, adk-submission 0.2.12, google-adk **1.36.1**;
  my first validator used 2.10.0, the wrong ADK). `compile_check.py` runs the scorer's own
  `validate_single_declared_model` + `compile_submission` (all 9 tools resolved, generation config accepted,
  budget parsed), and `adk_submission.validate_directory` is also OK. The prompt holds no `{...}`, which ADK
  would read as a state variable.
- A missing `adapters/` is handled (`discover_adapters` returns empty; vLLM starts without `--enable-lora`).
- **Next instrument:** `dryrun/`, the harness's own `Evaluator` (a mirror of the host notebook's section 5,
  the closest published copy of `inference.py`) on one training task against a stub model
  (`stub_model.py`: get_status → submit_patch → text). It reproduces any crash that does not depend on
  the model's skill. Blocked on a gate grant for the wheelhouse venv interpreter (asked of dp).
- Rule for v2: do not spend a slot until the dry run completes a task end to end.

## Dry run on the real harness (2026-10-01 00:20 UTC): v1 PASSES end to end
`dryrun/dryrun.py`, the hosts' `Evaluator` in subprocess mode (a mirror of the Getting Started notebook,
section 5), on `rich_3061` against `stub_model.py`:
- the system and task prompts reached the model;
- `get_status` and `submit_patch` dispatched and returned;
- the patch was extracted and the agent finished cleanly (7.4 s, 0 counted tool calls, because both
  tools are free).
- Requests carried `max_completion_tokens` 8192, `chat_template_kwargs.enable_thinking`,
  `thinking_token_budget` 2048 and 9 tools.

So v1's error does NOT reproduce in the harness. Forum evidence that it is platform-side:
- **743213:** the organisers' `sample_submission`, byte-for-byte, failed with the same "unhandled error".
- **Several plain-YAML bundles** failed on a platform resource error in the same week; the host fixed
  it and has re-run affected submissions (743683).
- **743063, host:** "Currently, hitting the 12-hour limit will error", which confirms the per-task budget.

v1b resubmits the identical bytes to separate platform from package with one variable (time). If it
fails the same way, the cause is in the scorer's wrapper, the one layer we cannot run locally.

## Why v2 turns thinking off (2026-10-01 01:00 UTC): a CANDIDATE cause, not a found one
- **vLLM 0.19.1** `v1/engine/input_processor.py` raises `ValueError("thinking_token_budget is set but
  reasoning_config is …")` when a request carries `thinking_token_budget` and the server has no
  `reasoning_config`.
- **The 09-30 wheelhouse** (adk-submission 0.2.12, published 20:33 UTC) began sending
  `thinking_token_budget` whenever thinking is on and the budget is > 0. Before the host's patch,
  forum 744566 measured that 0.2.11 sent no budget. Our dry run captured `thinking_token_budget: 2048`.
  Both v1 failures came after that publish.
- **Bundles that score have thinking off:** the 0.10 notebook uses `include_thoughts: false`. The
  organisers' sample (thinking on, budget 4096) failed with our exact message (743213).
- **Against the hypothesis:** 0.2.12's own `VllmServer` passes `--reasoning-config` (Gemma 4 channel
  tokens) whenever the parser is `gemma4`, which satisfies vLLM's check. If the scorer launches through
  that code, this cannot be the cause. We cannot see the scorer's `inference.py`.
- **So v2 removes the dependence** instead of betting on the cause: with thinking off, the bridge pops
  the field. If v2 scores, thinking-on is implicated (cause narrowed, not proven). If v2 also errors,
  thinking is cleared and the next suspect is the eval_config budget values. Cost: no thinking, which
  public notebooks also report as much faster per turn.

## v2 SCORED 0.10 (2026-10-02 06:16 UTC): thinking-on is implicated; the next lever is turning it back on safely
- **Ref 56761070** (submitted 00:01:14 UTC 10-02, COMPLETE at ~06:16, about 6 h): **public 0.10**, error ''.
  Our first completed SWE submission; v1 and v1b errored. Same score as the public thinking-off notebook.
- **What it narrows:** v2 differs from v1 only in thinking OFF (no `thinking_token_budget` in requests). Per the
  pre-registration above: v2 scores, so **thinking-on is implicated (narrowed, not proven)**. Consistent with
  vLLM 0.19.1 rejecting a budget without `reasoning_config` in the scorer's server.
- **What it does not say:** whether our package adds anything over the plain baseline. 0.10 equals the public
  thinking-off notebook, so this is the floor, not our method.
- **Next (ring discipline, one variable per slot):**
  - v3 = the same package with thinking ON but NO budget field (thinking via the chat template, the budget
    unset). If it scores, the budget field was the trigger, and thinking is back.
  - Separately, the agent-side work (the ARC philosophy: priors, situational awareness, cheap hypothesis
    tests) goes in a variant only once the floor is reproducible.
- Wall time ~6 h of the 12, so roughly half the budget is free for more turns per task.

## v3 (armed for the 2026-10-03 slot): v2 + a 6-minute budget, ONE variable
- **Why not thinking-on-without-a-budget:** it can't be expressed. `adk_submission/limits.py` (step 6) fills
  `thinking_budget = limits.thinking_budget.max` (4096) whenever thinking is on and no budget is given. The dry run
  confirms it: `include_thoughts: true` with no budget sends `thinking_token_budget: 4096`, and `thinking_budget: 0`
  forces thinking off. So every thinking-on config carries the field that, by the evidence (v1 ×2, the organisers'
  sample), errors in the scorer. **Thinking stays OFF until the host changes the server.**
- **The lever that's left:** v2 used ~6 h of the 12 for ~120 tasks, about 3 min per task including setup, so the
  4-min cap was binding. v3: `max_time_minutes` 4 → 6, `max_tool_calls` 30 → 45, and the prompt's session facts
  updated to match ("about 6 minutes", "12-18 tool calls"). Estimated wall ~9 h, under the 12 h that errors.
- validate VALID, compile_check COMPILES, dry run on rich_3061 sends `enable_thinking: false` and no budget field.
- zip sha256 `13b258fb1b24e9b1c33a6071ceead9f39ecc3fc3760e05972a51108db702dcb2`.
- **Pre-registered reading:** >0.10 means the budget was binding and more time pays; 0.10 means the floor is not
  time-limited, so the next lever is the agent's method; an ERROR means a 6-min budget overran the wall, so
  return to 4 and use the time differently.

## v4 (2026-10-04 slot): v3 + ONE variable, the PROCEDURE (reproduce first, fix against the reproduction)
- **Why:** v3's pre-registered reading triggered. 6 min scored the same 0.10 as 4 min, so time is not the lever; the
  agent's method is.
- **The change:**
  1. Write `/tmp/repro.py` asserting the issue's EXPECTED behaviour and run it; it should fail.
  2. Locate the code, then edit it.
  3. Rerun the repro until it passes, then run one related test file.
- **Basis:** the duck (a model writing and running its own probes), and the leaderboard study (only verified plans
  are committed).
- **Unchanged:** budgets (6 min, 45 calls, 40 turns), thinking OFF (the budget field still errors in the scorer),
  temperature 0.2.
- **Checks:** validate VALID; compile_check COMPILES (the scorer's own adk-submission 0.2.12 / google-adk 1.36.1);
  the prompt contains no `{...}`.
- zip sha256 `584cfdddb49b7d1e3edf4cbc0679cc7c16f2ba95cc1599e8e5ec4d9a53beab36`.
- **dp, 10-04:** "doesn't have to be fully tested, the run is a test in itself". Untested on tasks; that is the
  point of the slot.
- **Pre-registered reading:**
  - **above 0.10:** reproduce-first helps. Keep it, and next try a larger tool-call budget for the repro loop.
  - **0.10:** the repro costs calls without changing outcomes. Next lever: temperature or a two-pass edit.
  - **below 0.10:** the repro eats the budget before any edit lands. Next: repro only after a first edit.
  - **ERROR:** a run-level failure, not a method reading. Diff against v3.

## v4 SCORED 0.10 (2026-10-04 08:57 UTC, ref 56810803)
- Per its pre-registered reading: the reproduction costs calls without changing outcomes.
- Three very different variants (thinking off; 6 min; reproduce-first) all score exactly 0.10, and 271 teams on the
  board sit at exactly 0.10. Something structural caps this band. Neither the procedure nor the budget is the lever.

## v5 (2026-10-05 slot): v4 + ONE variable, temperature 0.2 -> 0.7
- **Why:** v4's reading names temperature as the next lever. Open coding agents run at 0.6–0.7, and 0.2 may lock
  the agent into its first, wrong, idea.
- **Not tried:** thinking ON with an explicit budget would repeat a KNOWN fail (v1 at 2048, and the organisers'
  sample at 4096, both errored).
- **Checks:** validate VALID; compile_check COMPILES.
- zip sha256 `39a4a68e0d60980338f77bc8412029abb1fd25c840e51d40fbd69aef490b2e9c`.
- **Pre-registered reading:**
  - **above 0.10:** sampling diversity matters; next try 1.0, or best-of-N edits within the budget.
  - **0.10:** neither procedure, budget nor sampling moves this band. The cap is the model or the scorer's setup;
    next, investigate what the 0.12–0.24 entries do differently (public notebooks and discussion).
  - **below 0.10:** randomness hurts small edits; go back to 0.2.

## 2026-10-04 19:10 UTC: CORRECTION, and v6 replaces v5 for the 10-05 slot
- **The SWE study** (research/swe_study_1004) found two things:
  - **v1/v1b's errors are confounded:** both ran during a host-confirmed GPU outage (forum 744807), when
    thinking-off and byte-identical bundles errored too. Thinking-on is UNTESTED, not a known fail. v2's
    "thinking implicated" reading above is withdrawn.
  - **The public split is 58 tasks;** one submission's SD is about 2.3 tasks. The same top public bundle scored
    0.08–0.15. Our 0.10 ×3 are correlated runs at temperature 0.2.
- **v5 (temperature 0.7) is withdrawn before firing:** the forum measured temperature 0.7 worsening loops
  (5/10 tasks). Not fired; v5 files kept.
- **v6 = v4 + thinking ON** (`include_thoughts: true`, `thinking_budget: 1024`), with the dead
  `search_similar_code("<keyword>")` step removed (it matches only full dotted names; 140/142 calls returned
  nothing).
  - **Checks:** validate VALID; compile_check COMPILES (gen config carries `include_thoughts: True,
    thinking_budget: 1024`).
  - zip sha256 `868a0d8f7e3dd5b3c2a35ad82aac746567047edad3bda88d13d6675f6506d309`.
  - **Pre-registered reading:**
    - **ERROR:** after the outage fix, thinking IS implicated. Return to thinking OFF.
    - **above 0.10:** thinking helps; tune the budget next.
    - **0.10 or below:** within noise. Next, the analyzer structure (the study's #1).

## v9 (thor-claude, 2026-10-05): v6 + timeout_seconds 120 -> 300, ONE variable; fires 10-06
- Source-checked in the public wheel: `config.py:179-188` copies `timeout_seconds` into `harness.command_timeout_seconds`, which
  `verification.py:502` uses as the timeout of the hidden GRADING pytest. At 120 s a correct patch whose tests run
  longer is graded unresolved. The default is 300 (`budget.py:29`). Unverified: whether the scorer honours our eval_config.
- Why now: v2/v3/v4/v6 each solved exactly 6/58. Identical counts across four variants point to a systemic cap, not the
  agent. Public 0.12-0.15 bundles shipped no eval_config (300 s). Study: research/swe_study_1004/DELTA_017_vs_010.md.
- Risk: the 12 h wall (setup + 6 min/task); 300 s only costs time on tasks whose tests are slow.
- zip sha256 5427f12319aa7d3a52998e070ce58677b0b41897933cdd1e1b316303b1b20b3b; compile_check: COMPILES, command_timeout_seconds=300.
- Slots re-planned: 10-06 v9, 10-07 v7 (codex), 10-08 v8 (codex).

## v7t300 / v8t300 (thor-claude, 2026-10-05): codex v7 / v8 + timeout_seconds 300 only; conditional
- Built and compiled (command_timeout_seconds=300). Each differs from codex's original by 3 lines.
  - v7t300 sha256 b30da2e9b396942f9800f31d7c87a74f14d49752eba98807d63f74975a9910b9
  - v8t300 sha256 447c0dd5139b44c0cf4932af3b7007e5051d3c52c672d4642294782ccdd15c3f
- `blackbox/runs/swe_timeout_swap_1006.sh`: if v9's FINAL beats 0.10, replace the v7 (10-07) and v8 (10-08) waiters
  with these twins; otherwise leave them. A 120-s structural arm after a timeout win would waste its slot.

## v9 RESULT (2026-10-06 13:15 UTC): public 0.13 (sub 56864122)
First score off 0.10 after four 120-s variants (v2/v3/v4/v6) each solved exactly 6/58. v9 changed only
timeout_seconds 120 -> 300, which in the public wheel also bounds the grading pytest. It's one run (~±2.3 tasks), but
the mechanism and the direction agree. v7t300 (10-07) and v8t300 (10-08) are now armed in place of the 120-s v7/v8.

## v10 (thor-claude, 2026-10-06): v9 + max_output_tokens 8192 -> 4096, ONE variable; fires 10-09
A context overflow discards the patch (agent_runner.py:799 generic except skips the git-diff fallback at :741-776);
forum 744692 measured 12-33% of sessions overflowing. Compiles. zip sha256
cb1c87391b116dce23bc371a06153360f3d215220c8b794aaaffbb3ea212dcf9. Slots: 10-07 v7t300, 10-08 v8t300, 10-09 v10.

## v11 (thor-claude, 2026-10-09): v9 + timeout_seconds 300 -> 600, ONE variable; fires 10-10
- **Why:** the 10-10 slot opened when the v8t300 "retry" proved to be a resubmit (Kaggle re-ran the errored 56924966 to COMPLETE 0.10). The only lever that ever moved SWE off 0.10 is the grading timeout (v9 120 -> 300 gave 0.13). This takes the same direction one step further.
- **Basis:** v9, the best known, not v10 (pending).
- **Risk, accepted as a long shot:** the value also bounds the agent's own shell commands, and slow grading costs wall time against the 12-h wall shared by ~120 tasks. An overrun would ERROR, which is informative.
- **Checks:** compile_check COMPILES with command_timeout_seconds=600; the other three files are byte-identical to v9.
- **zip sha256:** 51d3fc625c231ef1458480d983edc8b075cd8acce2a69617713debe21b921366

## v11 / v11b (2026-10-10): bare 400s at CreateSubmission
- **v11 (600 s):** refused at 00:00Z and ~00:55Z.
- **v11b (450 s, sha a75e4417…):** refused at ~01:00Z.
- No slot used (numToday 0, numAllowedNow 1).
- **Hypothesis:** v10 still PENDING (~25 h) blocks new submissions.
- **Retry:** `blackbox/runs/swe_v11_retry_after_v10.sh` (detached) retries after v10 completes. If v11 is refused again with v10 complete, the 400 is about timeout > 300.
- **Note:** `adk_submission/limits.py:184` allows 3 GiB "including adapters", so the SWE track supports adapters.

## The real cause of the 400s, and v12 (2026-10-10)
- **The server's body behind the bare 400:** "Submission not allowed: Your team already has 1 pending submissions; please wait for one to finish scoring." SWE allows ONE pending submission per team.
- **v10 (56979096)** has been PENDING ~29 h against a 12-h runtime, so it's stuck. dp to cancel it in the web UI.
- **v11 (600 s):** never actually evaluated by the server; whether timeout > 300 is accepted is still unknown.
- **v12 = v9 + ONE variable, the prompt** (codex's REA read: premature closure):
  - step 1: a passing reproduction re-opens assumptions instead of being forced to fail;
  - step 6: "a correct fix changes source" stated as a reason, not a rule.
  - COMPILES; zip sha256 b63c3ea6…
- **Runners:** `blackbox/runs/swe_submit_when_clear.sh` (DETACHED) — v11 for the 10-10 UTC slot, v12 for 10-11, each when 0 pending.

## 2026-10-10 22:22Z: v10 scored 0.12; v11 submitted (ref 57053652)
- **v10 (56979096):** COMPLETE with publicScore **0.12**, against v9's 0.13. Lowering max_output_tokens to 4096 did not help; it lands within a point of v9. It ran ~46 h; the "stuck" state was a very slow scoring, not a dead job. The one-pending-per-team rule blocked v11 the whole time.
- **v11:** v9 + timeout 600, submitted 22:22Z 10-10 for the 10-10 slot by `swe_submit_when_clear.sh`.
- **v12** (prompt fix) waits for the 10-11 slot, and for v11 to stop pending. If v11 also takes ~46 h, the 10-11 slot is lost to the same rule.

## Grading durations (thor-claude, 2026-10-11 18:00Z; from `kaggle competitions submissions` + the v11 waiter's poll log)
- **v9 (300 s): ~13 h.** Submitted 10-06 00:00Z; scored 0.13 by ~13:15Z.
- **v10 (300 s, out 4096): ~46 h.** Submitted 10-09 00:00:53Z; COMPLETE between 10-10 22:12Z and 22:22Z; scored 0.12.
- **v11 (600 s):** submitted 10-10 22:22Z; still PENDING at 19 h.

**Not stuck: grading runs past 12 h, and the same timeout can take 13 h or 46 h.** (The 10-10 "stuck, dp to cancel" line above was wrong.)

**The cost is the one-pending rule:** every grading day beyond 24 h is a lost daily slot. Weigh any timeout increase against the slots it consumes; v11 is the measurement.

**v12:** waits on v11. `blackbox/runs/swe_v12_rearm_1012.sh` takes over for 10-12, but only if the 10-11 waiter ends "slot missed".

## Where grading time goes (thor-claude, 2026-10-11; research/gradetime_1011)
- **Method:** the wheelhouse's own `verify_task` was run on all 129 public snapshots on thor, with the gold patch and with no patch.
- **Non-agent time per task: ~5 s setup plus ~1–40 s of pytest.** requests is the slowest at ~33–41 s.
- **Hangs:** 3/129 no-patch runs (rich_3480, rich_3772, rich_4006: infinite loop or recursion bugs) hang to the cap, because of `-o timeout=0`.
- **Implied full run:** ~12.5–13.5 h at 300 s or 600 s, which matches v9's ~13 h. The ceiling is ~23 h at 300 s and ~33 h at 600 s, and only if every task hangs.
- **Conclusion:** v10's 46 h is not our config. The excess (≥ ~22 h) is outside the agent and grading steps: queue, model load, or retries. That fits the slowdown starting 10-09 with no relevant change on our side (v7t300 and v8t300 at 300 s each finished in under 24 h).
- **Timeout:** 600 vs 300 costs at most ~15 min per run at the public hang rate; its main cost is the slot rule, not runtime.
- The forum question to the host is drafted in `research/forum_drafts/` for dp to post.
- **dp, 10-12:** the SWE forum confirms other teams also see multi-day grading. It's competition-wide, not our config. The draft question can still ask about queue time and cancellation.

## 2026-10-13 00:50Z: v11 0.15, v12 0.17 (new best); v12 RESUBMITTED by mistake (57124955)
- **v11** (timeout 600): COMPLETE **0.15**, vs v9's 0.13 at 300 s.
- **v12** (prompt fix, 300 s): submitted 10-12 10:35Z (57104463), COMPLETE **0.17**. Best so far.
- **Defect:** `fire_when_slot_opens.py` keeps watching for the final score after submitting. The waiter wraps it in `timeout 900`, so every SUCCESSFUL submit exited non-zero. The waiter logged "fire failed", then "slot missed".
- **My error:** my multi-day re-arm (`swe_v12_rearm_multi.sh`) trusted that log line, not Kaggle's submission list, and resubmitted v12 at 10-13 00:46Z (57124955). That's against the no-resubmit rule. I killed the chain and its hung fire process minutes later, before any third submit.
- **Use of it:** 57124955 is an unplanned REPLICATE of v12. Its score bounds per-submission noise on SWE.
- **Fixes:**
  - `fire_when_slot_opens.py --no-watch` returns 0 after a successful submit.
  - `swe_submit_when_clear.sh` counts a `submitted:` line as success.
  - The waiter now REFUSES if Kaggle already holds a submission with the same message. Checked on the known case: the v12 message matches 2.
- **Nothing SWE is armed now.** v13 (locator) waits on codex's peer review.

## 2026-10-13 19:15Z: v13 superseded by v14 (stacked); the v12 resubmit was a violation
- **dp:** "we already have the 'make each swing count' rule. seems you re-ran a swe submit? that would be a violation. especially since a single swe run can cost us several days presently. make every swing for the bleachers the best we know how."
- **57124955 is a violation, not a "replicate":** the 00:50Z line above calling it "use of it" was wrong framing. It costs SWE grading days with no new idea, and Kaggle has no cancel.
- **v14 = v13 (codex-reviewed v12 + locate-code skill) + timeout_seconds 300 -> 600.** v11's 600 s scored 0.15 vs v9's 0.13 at 300 s (within noise; direction and mechanism agree; ≤ ~15 min/run grading cost per gradetime_1011). One config line differs from v13; the other 5 files are byte-identical.
  - validate VALID (skill loads); compile_check COMPILES with command_timeout_seconds=600.
  - zip sha256 `ad06bc968dfcf51f63e5348aba1a577ffe97a16cf688b173a44a01ded128d13a`; the unzip equals `submissions/v14/`.
- **Runner:** the v13 waiter was stopped before it fired. `blackbox/runs/swe_v14_when_clear_multi.sh` fires v14 on the first day nothing is pending, with the server-side duplicate guard. Peer veto `blackbox/runs/STOP_swe_v14` is checked at arming and before every submit attempt.

## 2026-10-14 06:10Z: v12 replicate scored 0.12; v14 submitted (ref 57169486)
- **57124955 (v12 resubmitted by mistake) = 0.12.** The identical config scored 0.17 on 10-12. That pair is our only
  noise measurement: about ±0.05 per run (≈6 of ~120 tasks). v10/v11/v12 (0.12/0.15/0.17) are therefore not
  separable, and the +0.02 credited to v12's prompt change was within noise. The resubmit remains a violation; this
  row records what it happened to measure.
- **v14 (v12 + locate-code skill + timeout 600)** fired at 06:05Z from `swe_v14_when_clear_multi.sh` once nothing was
  pending. Confirmed in Kaggle's own list as 57169486. Read its score against ±0.05.
- **Arm verdicts move off the scored board.** Real Gemma-4-31B QAT now serves on Thor (:8011). `blackbox/runs/gpuq`
  runs a paired v12/v14 sweep through the real swegemma grader on all 129 local snapshots (fetched 10-14). Local
  mode raises only `max_time_minutes` 6 → 40, because Thor decodes ~10 tok/s/stream and the 6-min cap ended a real
  smoke after 16 tool calls. Every row carries the mode (`v12@t40`). These are public training repos, so a delta is a
  proxy; paired and n=129, though, it can resolve what one ±0.05 scored run can't.

## 2026-10-15 04:41Z: v14 scored 0.13; the SWE slot is open
- **57169486 (v14 = v12 + locate-code skill + timeout 600) = 0.13.** Inside the ±0.05 band of v12's 0.17/0.12 pair, so
  no lift and no loss is shown. The local paired sweep reads the same way (04:45Z: 67 paired tasks, 1 v12-only,
  1 v14-only, 19 both, 46 neither). The locate skill's offline hit@1/5/10 (41/71/85 of 122) did not become solves:
  the binding limit is downstream of finding the code (the edit, or the run that checks it).
- Scored SWE so far: 0.10 floor; 0.13 / 0.15 / 0.17 / 0.12 / 0.13 since the timeout moved. Nothing is separable from
  noise in single runs; only the paired local sweep can now give arm verdicts.
- Submit-to-score latency this time: 06:05Z → ~04:40Z, about 22.5 h.

## 2026-10-15 08:01Z: v15 submitted (57222184), score pending
- **v15 = v14 + turn budget doubled** (max_turns 40 -> 80, max_tool_calls 45 -> 90; zip sha256 c34fd4ab...; commit
  0e6e39e). Why: 108 of 174 graded local real-Gemma runs ended on the 40-turn cap (41 of them with no edit).
- Fired by the transient timer thor-swe-v15 (fire-when-clear waiter, peer OK codex 0719, veto STOP_swe_v15 absent):
  `submitted ... ref 57222184` at 08:01:06Z (runs/swe_v15_when_clear_multi.log). Kaggle's list shows 57222184 PENDING.
- Read its public score against the ±0.05 run-to-run band (v14 0.13, v12 0.17/0.12). Local proxy so far: v15@t90 0 of
  9 graded resolved, but only 1 task is paired with v14@t90, so that says nothing yet. (thor-claude supervisor 08:43Z)

## 2026-10-16 04:38Z: v15 scored 0.13 (public)
- **57222184 (v15 = v14 + turn budget doubled, 40 -> 80 turns, 45 -> 90 tool calls) = 0.13**, field publicScore,
  scale 0-1 (fraction resolved), privateScore empty (state/subs_gemma-4-developer-agent.json, check_subs 04:38Z).
  Same as v14's 0.13; v12 0.17/0.12. Run-to-run noise is about ±0.05, so one run cannot tell v15 from v14.
- Local proxy (public repos, real Gemma, gpuq sweep/ledger.tsv): v15@t90 11 of 52 resolved. Paired with v14@t90 on 20
  tasks: 2 v14-only, 0 v15-only; with v14@t40 on 34 tasks: 2 / 0. Far below 20 discordant pairs; no verdict.
- Advocate caveat (thor-devils-advocate): locally v15 still ends on the 80-turn cap in 27 of 52 runs and rescued 0
  tasks; the cap still binds, and this test lacks the power to show a lift. Some capped v15 runs used only 26-48 tool
  calls, so turns are being spent without tool calls; a bigger budget will not reach those. Next sharper question:
  sort v15's capped runs into tool-call turns vs talk-only turns (if talk, the lever is the reply format).
- Submit-to-score latency: 08:01Z -> ~04:38Z, about 20.5 h. (thor-claude supervisor 04:38Z)

## 2026-10-18 12:01Z: v16 submitted (57353245), scored 0.12 public (read 10-19 07:03Z)
- **Result: 0.12**, inside the ±0.05 band of v15 0.13 / v14 0.13: no measurable lift from the completeness step.
- **v16 = v15 + an "understand before you edit" step** (read the whole function, one grep for sibling code paths,
  edit every site). The timer entry submitted `submissions/v16_submission.zip` at 12:01:05Z, ref 57353245
  (blackbox/runs/swe_v16_when_clear_multi.log). Kaggle's list shows 57353245 PENDING, public=- (check_subs 12:38Z).
  v17 (v16 + repro covers every listed site) is staged, not armed: +40% tool calls.
- Read its public score (0-1, fraction resolved) against the ±0.05 run-to-run band (v15 0.13, v14 0.13, v12 0.17/0.12).
  Expected about 08:00-09:00Z on 10-19 (v15 took ~20.5 h). Local proxy (public repos, real Gemma): v16@t90 10/33
  resolved; paired with v15@t90 on 33 tasks 0 v15-only / 2 v16-only, far below 20 discordant pairs, no verdict.
  (thor-claude supervisor 12:38Z)
- Supervisor caveat 10-19 07:45Z (thor-devils-advocate, holds-with-caveats): the ±0.05 "band" is a single replicate
  difference (v12 0.17 vs its resubmit 0.12), not an estimated CI. So 0.12 shows no demonstrated improvement, not
  equivalence (codex 0730 says the same). The local paired proxy leans the other way: v15/v16@t90 on 49 tasks,
  0 v15-only / 3 v16-only (one-sided sign p about 0.125). Scored and local readings disagree in direction; settling
  it needs v16 paired on all ~110 tasks v15 already has (local GPU only). (thor-claude supervisor 07:45Z)

## 2026-10-23 23:40Z: v25 WITHHELD (codex peer veto); the 10-24 slot fires a byte-identical v23b replicate
- v25 was armed 22:16Z. codex wrote STOP_swe_v25 at 22:18Z (mailbox 2220, 2230): the timeout change has no demonstrated benefit
  and no primary wall-accounting evidence, and it confounds a clean replicate. The waiter honored it at 22:19:30Z.
- Fallback, at codex's request: v23b_submission.zip, sha 23d7f4da...822131 (= 57523743), message "swe-sage v23b replicate:
  byte-identical to 57523743 (noise pair)", waiter blackbox/runs/swe_v23brep_when_clear_multi.sh, 10-24 12:00Z, veto STOP_swe_v23brep.
  It is the second same-config pair for the noise band (v12 0.17 / v12r 0.12 is the only one). (thor-claude)

## 2026-10-23 ~22:10Z: v25 STAGED (not armed): v23b + timeout_seconds 600 -> 1800. Reviews: artifact clean; claim UNPROVEN
- **Artifact** (b993030): `submissions/v25/`, zip sha `e66d4bf35262d277961ee2782c34f0cf7942b4dbebb6b0037854402e47a7fa2b`.
  Base v23b (0.15), not v24 (0.10). Only `eval_config.yaml` differs from v23b, in the dir and in the zip.
  - **Validation:** validate VALID; compile_check COMPILES (`HarnessLimits command_timeout_seconds=1800`); zip == dir.
  - **Stub dry run** (rich_3061): no agent error and no harness error. The task prompt reads "Single command timeout: 1800 seconds".
- **Why the agent clock was not the lever:**
  - v3 raised 4 -> 6 min and gave no lift (above).
  - Tasks run SEQUENTIALLY, and a run past 12 h ERRORS (host, forum 743063, 2026-09-24). The host reads only the four budget fields.
  - Local enumeration (sweep ledger, every graded row, at a 90-min local budget):
    - v23b: 23 resolved; 71 wrong (40 hit the 80-turn cap, 30 submitted, 1 clock); 5 empty (all at the turn cap).
    - v24: 22 resolved; 67 wrong (28 turn cap, 36 submitted, 3 clock); 9 empty (8 turn cap, 1 clock); 2 TOOLPARSE.
    - Every local resolve took > 360 s on Thor, so the local sweep cannot see what the hosted 6-min clock cuts.
- **What 1800 changes (swegemma 0.2.7):**
  - **Agent phase: nothing.** Agent commands and skill scripts are clamped to `min(timeout, time left)`: `tools/execution.py:32-42`, `adk_eval_core/sandbox/base.py:187-196`.
  - **Grading:** it raises the hidden grading pytest timeout (`harness/verification.py:502`, `-o timeout=0`).
  - **Setup:** it is the setup-command default (`evaluate.py:62-77`), which matters only on a hang.
- **thor-devils-advocate: UNPROVEN.**
  - Pooled by timeout, 300 s n=5 averages 0.128 and 600 s n=8 averages 0.126. The best score, 0.17, ran at 300. So "timeout moved the score" was two pairs picked out of the set; only the 120 -> 300 step has a sign. Values re-checked from each eval_config.yaml.
  - Gold tests never ran past 41 s on public tasks (gradetime_1011). The upside rests on a guess that private-repo suites are slow, with no data behind it.
  - The wall: `evaluate.py:353-377` runs grading INLINE per task. "Excluding patch validation" is only the rules text. gradetime_1011's own model puts 600-s runs at 12.6-13.5 h, and they did not error, so either that model or the wall reading is off.
  - Read v25 as a near-replicate of v23b that carries a small hang-cost risk: each hang costs up to 30 min instead of 10 if grading counts against the wall.
- **thor-reviewer: no defect in v25.** Zip members, order and modes match v23b; the YAML parses; nothing in adk_submission or EvalConfig caps the value.
  - **Hazard (CONFIRMED): the fire waiter.** `swe_v24_when_clear_multi.sh:25` gates on `v24@t90` rows. A partial copy would gate on v24's rows while shipping v25.
  - Every name has to change: ZIP, SHA, MSG, log, STOP_swe_v24 (lines 21/32/34), DAY (line 31).
  - The honest gate is v23b's rows, labelled as v23b's, since v25's agent phase is identical.
- **Status: NOT armed.** Arm it only as a labelled near-replicate of v23b, or not at all. What would settle the wall question: a host answer on whether inline grading counts against the 12 h. A stronger candidate needs a local change the enumeration supports. The turn cap ends most wrong and every empty local run, but v15's 40 -> 80 gave no hosted lift. (thor-claude)

## 2026-10-23 ~21:40Z: v24 (57549462) scored 0.10 public
- Kaggle's list (`kaggle competitions submissions -c gemma-4-developer-agent`, read ~21:40Z, reported done by dp): COMPLETE,
  publicScore 0.10 (fraction resolved, 0-1 scale; public split ~58 tasks, so about 6 tasks vs v23b's about 9).
- Read: 0.05 below v23b 0.15 and v18 0.15, at the edge of the ±0.05 spread (one replicate difference, v12 0.17 vs 0.12,
  not a CI). A likely regression, not a demonstrated one. Best stays v12 0.17; v23b is the base to build on.
- What could carry a real drop: of v24's three prompt changes only repro-via-run_command was live locally (loop remedy
  and early first edit were not taken up), and empty patches rose 7/66 vs 5/67, the same signal that came with v22's
  0.08 (9/71). Local resolves were flat (17/66 vs 18/67). Next test before stacking more prompt text: the empty-patch
  runs of v24 vs v23b read one by one (enumerate, not sample) for whether run_command repro ate the clock.
  (thor-claude)

## 2026-10-23 04:45Z: v24 SUBMITTED (57549462)
- **v24 = v23b + prompt only** (e73b184, staged 10-21, armed 10-23 03:45Z after dp asked why the 10-23 slot was unused).
  zip sha e7345173...075dc, VALID, zip == dir. Fired by blackbox/runs/swe_v24_when_clear_multi.sh at 04:45:36Z after a
  kimi veto window (kimi 04:31Z: PASS, every claim re-derived, no veto). Kaggle's list shows it PENDING.
- Local gauge (blackbox/analysis/claude_swe_v24_1023/gauge_v24.py, tool calls counted): repro via run_command LIVE
  (write_file->/tmp 0 vs v23b 102); loop remedy NOT (5x identical-call loops in 24 runs vs 25); first edit by call 30
  NOT (median call 20 vs 17). Resolved 17/66 vs 18/67 vs v18 20/77 (noise). Empty patches 7/66 vs 5/67 vs 3/77 (watch:
  v22's 0.08 came with 9/71). Gate (>= 3 empty of the first 16 = refuse): 0.
- Fixed before the fire: swe_submit_when_clear.sh's pending and duplicate checks read the CLI's new "outdated version"
  Warning line as the CSV header, so both always said 0. Fire-tested (test_submit_parsers.py: new 6/6, old fails both).
- Read against v23b 0.15 / v18 0.15 / best 0.17, +-0.05. (thor-claude)

## 2026-10-23 01:38Z: v23b (57523743) scored 0.15 public
- Kaggle's list (check_subs 01:38Z): COMPLETE, publicScore 0.15 (fraction resolved, 0-1 scale; public split ~58 tasks,
  so about 9 tasks). It ran to completion, so v23b did not repeat v23's fast rerun error. It ties v18 (0.15), is above
  v22 (0.08), and best is 0.17. Run-to-run noise about ±0.05, and that is one replicate difference, not a CI.
- Local proxy (public repos, real Gemma, first grade): v23b@t90 16/65 resolved; paired with v18 on 65 tasks 2 v18-only /
  3 v23b-only; with v22 1/1. Far below 20 discordant pairs, no verdict. v23b is not shown to improve over v18.
- Caveat (thor-devils-advocate, supervisor 01:38Z): the cause of v23's rerun error is still unknown. The related.py bug
  was already judged unable to fail the run (10-21 13:25Z code read), and one v23b completion cannot tell the bug from
  a one-off platform failure. The v22 0.08 is consistent with noise (5 vs 9 of 58, p about 0.25; local v18/v22 paired
  2/3 of 71); v23b's 0.15 adds nothing to that, because v23b changes more than v22. What would settle the error cause:
  the v22 byte-identical control in a later slot. (thor-claude supervisor)

## 2026-10-22 12:01Z: v23b SUBMITTED (57523743)
- `blackbox/runs/swe_v23b_when_clear_multi.log`: submitted 12:01:05Z, 0 pending before. Fire-time gate on local v23b
  traces: 47 traces, 30 called related-files, 0 crashed, 14 cited verdicts, 2 empty patches of the first 16 graded.
- Read at about 12:40Z: an error before then repeats v23's fast failure, which points to the platform; the next move
  is the v22 byte-identical control. Otherwise read the score against v18 0.15 within the ±0.05 noise. (thor-claude)

## 2026-10-21 13:25Z: v23b STAGED and armed for 10-22 12:00Z; the related.py bug cannot be v23's rerun error
- **v23b = v23 + one line** (`names_from` returns `out, alias` on a parse failure). `diff -r v23 v23b` is that line only.
  VALID, COMPILES, the zip equals the tree byte for byte, sha `23d7f4da...2131`.
- Bug reproduced (`blackbox/analysis/claude_swe_v23_1021/test_unparsable.sh`). It fires only when an EDITED file imports
  a module that ast cannot parse: v23 exits 1 with `ValueError: not enough values to unpack`, v23b lists it. A file
  that ast cannot parse has no parsed imports, so it never becomes a neighbour the other way round. 0 of 48 local v23
  runs hit it.
- **The bug cannot have errored the run (code read, 10-21).** Skill scripts run inside the task's sandbox:
  `AdkSandboxCodeExecutor.execute_code` (adk_eval_core/sandbox/base.py:176) writes the wrapper to the sandbox, runs
  `python3` there and returns a non-zero exit as stderr. Nothing is raised host-side, and skill_toolset.py:553 catches
  any exception that is. The rest of v23 matches v22 host-side: only `prompts/system.md` and `related.py` differ in
  the zip (`zip_compare.py`), and the prompt's `{...}` spans are identical, so ADK's instruction templating has
  nothing new to fail on. v22 completed (0.08).
- The cause is therefore unknown and probably outside the bundle. ARC's IDJ2 also failed twice in ~33 min on the scored
  rerun (10-20, 10-21) while every part replays cleanly on Kaggle hardware. Two competitions now show fast rerun
  failures that our own runs do not reproduce. That is a pattern, not a proof.
- **10-22 12:00Z fire** (`blackbox/runs/swe_v23b_when_clear_multi.sh`, timer thor-swe-v23b): v23's pre-registered gate
  is read on local v23b traces (the sweep filler now runs v23b). A score answers v23's question. A second fast error
  points to the platform, and the next move is a v22 byte-identical control, not more bundle changes. (thor-claude)

## 2026-10-21 12:38Z: v23 (57480646) ERRORED on rerun, no score (public field empty)
- Kaggle's list (12:38Z) shows status COMPLETE, publicScore empty, total_bytes 0. The API field error_description
  (KaggleApi.competition_submissions, read 12:4xZ) says: "Your notebook hit an unhandled error while rerunning your
  code. Note that the hidden dataset can be larger/smaller/different than the public dataset". Submitted 12:00:05Z
  (blackbox/runs/swe_v23_when_clear_multi.log); it ended before the 12:38Z check, under 38 min (v22 took ~19 h to score).
  It is not a 0.00; the run did not finish. The CSV check printed "COMPLETE public=-"; check_subs.py now prints the error.
- The bundle differs from v22 (0.08) only in prompts/system.md (the cited CHANGE/NO CHANGE step) and
  skills/related-files/scripts/related.py. agent.yaml, eval_config.yaml, configs and locate-code are byte-identical.
  The local gate saw 0 crashed and 3 of 15 cited verdicts; that crash count has never fired on a known crash.
- **v23 related.py has a latent bug.** names_from() returns ONE set on a parse failure (line 93, `return out`), but
  the caller unpacks two (line 306, `nm, al = ...`). Fired 12:5xZ: unparsable source -> ValueError "not enough
  values to unpack". The toolset should catch a script exception per call
  (wheelhouse google/adk/tools/skill_toolset.py ~537-560), so this is not shown to be the cause. The script runs
  in-process with no timeout and chdirs, so a whole-run failure is not ruled out. Cause unknown: this bug, or the
  platform (the same generic message as v1/v1b, which a host GPU outage confounded).
- What would settle it: fix line 93 to `return out, alias`, rerun the 15-task local gate plus one repo with an
  unparsable neighbour, and fire the fixed bundle in a later slot. If a second ~38-min error comes back, that points
  to the platform. (thor-claude supervisor; thor-devils-advocate: holds with caveats, wording above is its version)

## 2026-10-21 07:35Z: v22 (57436765) scored 0.08 public
- The lowest since v12: v18 0.15, v16 0.12, best 0.17; same-code spread ~0.05 (v12 0.17 vs 0.12). n=1, likely regression.
- The local sweep (v22 vs v18 paired over 70 tasks: 3 vs 2) ran at a 90-min budget; the hosted session is ~6 min. v22's
  extra step (3 excerpts + 3 per-file verdicts) costs time only the hosted run feels. Next: a local sweep at 6 min, v18 vs
  v22 vs v23, before v23's 12:00Z fire. (thor-claude)
- Caveat (supervisor 07:45Z, thor-devils-advocate: holds with caveats). The public split is 58 tasks (line ~171), so
  0.08 vs 0.15 is about 5 vs 9 tasks, z~1.1, p~0.25. That is NOT a demonstrated regression. The 6 min is our own
  `max_time_minutes: 6` (v22/eval_config.yaml:63, v18 too), not a hosted limit. Locally v22 adds only ~1.2 min and
  1.5 calls (36.0 vs 34.8 min, n=72/77), so the time-cost cause is untested. Lead: v22 has 9 no-patch endings vs
  v18's 3, 8 of them at the 80-turn cap. A clock scaled to hosted speed is what would settle it.

## 2026-10-20 12:01Z: v22 submitted (57436765), score pending
- **v22 = v18 + related-files skill made to be read** (91949b2; zip sha 5c48a4f4...71f0c): 1-hop import neighbours of
  the edited files, a sibling-gap flag, code excerpts of the first three, a per-file verdict before submit. Timer entry
  submitted at 12:01:05Z after 0 pending (blackbox/runs/swe_v22_when_clear_multi.log).
- Pre-registered gate passed (recomputed 12:02Z: 16 local v22 traces, 12 called related-files, 0 crashed). The gate's own
  print was erased from the fire log: `tee /dev/stderr` reopened the appended log with O_TRUNC (also in v13-v18 logs);
  the fire script now uses `tee -a`.
- Local before the fire (first 8 runs): v22 0/8, v18 0/8 on the same tasks; verdicts written in 2/4 listed runs, all
  "no change" (15030 skipped its #3, the missed gold file). Read against v18 0.15 / v16 0.12 / best 0.17, ±0.05.
  Expected ~07:00Z 10-21. (thor-claude)

## 2026-10-20 06:51Z: v18 (57395456) scored 0.15 public
- COMPLETE, read by the waiter at 06:51Z (submitted 10-19 12:01Z). Previous: v16 0.12, v15 0.13, v14 0.13; best 0.17
  (v12, 10-12; its byte-identical rerun gave 0.12).
- +3 tasks over v16, inside noise (±0.05 between replicates; binomial SE ~0.03 at ~120 tasks). Locally v18 did not beat
  v16 (5 v16-only / 1 v18-only of 58 paired), so the rise is not attributable to the identity/lessons header.
- Local follow-up: v19-v21's related-files skill was called (v21: 15/20) but its list was dismissed (a listed file
  touched 2/15, edited 0/15; v18 vs v21 paired 0/0 of 19). v22 (91949b2) prints code excerpts and sibling gaps and asks a
  per-file verdict; the sweep runs v18 vs v22. (thor-claude 10-20)

## 2026-10-19 12:01Z: v18 submitted (57395456), score pending
- **v18 = v16 + a run-identity header** (SAGE, a scored competition run over ~120 different repos, one overall score)
  **+ a practice-memory header** (dp 10-18; staged in d7f46d0). The timer entry submitted
  `submissions/v18_submission.zip` at 12:01:06Z, ref 57395456, after it saw 0 pending submissions
  (blackbox/runs/swe_v18_when_clear_multi.log). Kaggle's list shows 57395456 PENDING, public=- (check_subs 12:38Z).
- Read its public score (0-1, fraction resolved) against v16 0.12 / v15 0.13 / v14 0.13; run-to-run noise about
  ±0.05 (one replicate pair, not a CI). Expected about 07:00-09:00Z on 10-20 (v16 took about 19 h).
  Local proxy (public repos, real Gemma, first grade per task): v18@t90 14/59 resolved; paired with v16@t90 on
  58 tasks, 5 v16-only / 1 v18-only. Far below 20 discordant pairs, so no verdict. (thor-claude supervisor 12:45Z)

## v26 STAGED, NOT ARMED (2026-10-24 ~07:10Z, thor-claude): the public SuperAgent-lineage bundle, byte-for-byte
- **Why:** dp 10-24 ruled out reruns and in-noise variants: every slot is an aggressive swing. The public board's top
  (0.24; we hold 0.15) is one config lineage, matterhorn3838 "SuperAgent" → flexonafft budget-aware v2 (reported 0.18,
  then 0.22) → honghanhhh "Baseline | LB 0.24" (prompt-only edits on the 0.22 config).
- **v26 = honghanhhh/gemma-4-baseline-lb-0-24, extracted byte-for-byte** (`submissions/extract_public_bundle.py`).
  It differs from v23b on exactly the levers this ledger called closed or minor:
  - thinking_budget 4096 (ours 1024). v3's "4096 errors" reading was outage-confounded, and this lineage scores at 4096.
  - 8-min clock (ours 6) with 28 tool calls (ours 90). F6's "raising the clock is not open" is contradicted by
    public bundles that score at 8 min; the 28-call cap keeps the 12-h wall.
  - timeout 240 s.
  - NO skills (ours: locate-code, related-files); graph tools banned in the prompt.
  - A call plan that forces an edit by call 12, and "an unedited tree scores zero".
- **Checks:** validate VALID; compile_check COMPILES (gen config sends thinking_budget 4096; EvaluationBudget 8 min /
  28 calls / 80 turns; command_timeout 240). zip sha256 `7a9be57eb4cf6709a4e286e4939bcbbccdbfbca6e71a6fc28445b78d8401939c`.
- **Pre-registered reading:** public SD ≈ 0.04.
  - **≥ 0.20:** the lineage reproduces in our hands. Our v9-v24 agent work sits below a lean public config, and the next
    swings stack OUR measured levers (F3 import neighbours) on v26, not on v23b.
  - **0.15-0.19:** inside noise of both; the 0.24 was partly a lucky draw. Next: v23b + thinking 4096 alone.
  - **≤ 0.14:** the public score doesn't transfer; read the gap as variance, not config.
  - **ERROR:** a fast error points at thinking 4096 on the host; a slow one at the wall.
- **Credit:** matterhorn3838, flexonafft, honghanhhh (public notebooks; Kaggle's public-sharing rules). The paper
  says so.
- **Not armed:** dp decides whether it fires (DECISIONS 10-24 06:53Z: fly manual).
- **ARMED 10-24 07:14Z, on dp's go conditional on codex** ("yes, go v26 if codex agrees").
  - Codex AGREE at 07:16:54Z (`blackbox/runs/AGREE_swe_v26_codex`, mail 0716), for this exact sha and 10-24 only, with no fallback and no ERROR retry.
  - Codex checked a fresh Kaggle download: all 4 files match the staged tree and the zip exactly. validate VALID; the installed scorer COMPILES. Review: `blackbox/analysis/codex_swe_v26_review_1024`.
  - Waiter: `blackbox/runs/swe_v26_on_codex_agree.sh`.
- **The pre-registered reading, AMENDED by codex before the result** (it supersedes the four bullets above; the originals stay for provenance):
  - **≥ 0.20:** encouragement at the bundle level, NOT attribution to a single knob such as thinking 4096 or the call plan.
  - **0.15-0.19:** inconclusive. It does NOT show the author's 0.24 was luck.
  - **≤ 0.14:** this draw failed to reproduce. It does NOT show variance, or that config is irrelevant.
  - **A fast ERROR:** cause unknown without evidence. It is not a thinking-4096 diagnosis; v23 errored at 1024.
  - **The source's 0.24** is its reported performance (the notebook title), not a score receipt for these exact bytes. The leaderboard shows four teams at 0.24, but not which bytes they ran.
  - **F3 (import neighbours) is NOT yet a measured solve lever:** the latest 117-pair v23b/v24 sweep is 5 vs 5 discordant (codex 0704). Stack a lever only after it shows utility.
- **SCORED 0.12 public (57586384; field `publicScore`, scale 0-1 = fraction of tasks resolved, about 7 of ~58).** COMPLETE between 10-25 04:38Z and 05:37Z (supervisor check_subs). Thor supervisor, 10-25 05:4xZ.
  - Under the codex-amended reading (<= 0.14): this draw failed to reproduce the source's reported 0.24. It does not show variance, or that config is irrelevant.
  - Against ours: v18 0.15, v23b 0.15, v16 0.12, v24 0.10 (57549462), v22 0.08, best 0.17. Noise about ±0.05, n=1: 0.12 sits inside our own 0.08-0.15 range. One draw, not a ranking.
  - Devil's-advocate caveat: the 0.24 source may be the best of several draws (four teams at 0.24, bytes unknown), so one draw cannot rank the lineages either way. v26 has no skills, 28 calls and an 8-min clock and lands where our skill-heavy v22-v24 land: weak evidence that our skill stack adds nothing measurable over a lean config. Weak, not none.
  - What settles it costs no slot: the local paired sweep. As of 10-25 04:38Z, v23b vs v26@t120 on 99 shared tasks is 3 v23b-only / 3 v26-only discordant (a proxy on public repos; far below 20 pairs).
