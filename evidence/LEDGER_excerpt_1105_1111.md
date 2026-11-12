# Thor submissions ledger, excerpt 2026-11-05 .. 2026-11-11 (copied 2026-11-11 19:03Z by thor-claude)

Source: SWE-SAGE branch `thor-claude/swe-wip` (worktree branch `thor/g4-submission-v1`), `submissions/LEDGER.md`. `main`'s own
`submissions/LEDGER.md` has diverged (it carries cloud-side sections this branch lacks), so this is a copy of the sections the
paper's v4 draft relies on, not a replacement. Newest first. Each slot has its SHA and a reading written before the score.

## 2026-11-11 15:34Z: v68-empower-uncapped-runfact-think4k-t6 STAGED as the 11-11 card, NOT ARMED, NOT FIRED (thor-claude)
- ZIP `blackbox/runs/swe-v68-empower-uncapped-runfact-think4k-t6-prepared-20261111/submission.zip`, SHA256 4959f5bbe31c554d1d28b46269e3d0ab5a10321ad9a6213d2f4012b5163745bb; tree `submissions/v68-empower-uncapped-runfact-think4k-t6`; builder `blackbox/analysis/claude_swe_earlyfinish_1111/build_v68.py`.
- What it is: v65 (73f0bec9) with `max_time_minutes` 20 → 6 and the prompt's two clock mentions 20 → 6; nothing else. v65 = thought 4,096, max_output 8,192, 200 tool calls, 500 turns, nine flat tools, truthful ending with the literal `SESSION COMPLETE` reply, the run fact (many issues share one 12-hour run).
- Why 6 minutes: v58 (20-minute ceiling) ERRORED with 'exceeded the allowed runtime'. The ceiling is the bound that does not depend on an unverified host clock or on the agent obeying a recommended budget.
- Local evidence (public tasks, one draw each, scaled clock): v68s24 on the frozen 24 = 19 resolved, 1 unresolved, 4 harness UNKNOWN (19 vs v65s80's 20 on the 20 comparable cells; 18 vs v67s32's 14 on 19); mean 1,092 s; 10 sessions reached the clock and 9 of them resolved through the working-tree fallback or an earlier submit. Exact-ZIP smoke receipts present (000419).
- Wall projection, 120 tasks (129 in brackets), from v68s24's durations at a 6-minute ceiling: 9.3 (10.0) / 9.1 (9.8) / 8.4 (9.0) / 7.8 (8.4) h at r = 3.8 / 4.0 / 4.35 / 4.65 with no overhead; +1 h per 30 s of per-task overhead; the one cell over 12 h is 129 tasks at 60 s and r = 3.8 (12.1 h). A scenario under assumed speed and overhead, not a hosted measurement.
- Review: kimi-code AGREE bound to 4959f5bb (15:26Z 11-11, exact-ZIP read: only eval_config.yaml and the two clock mentions differ from v65). kimi is the sole reviewer per dp ('codex is out of usage, proceed with kimi's review'); codex's silence is not agreement. dp's explicit word decides the fire and is NOT yet given.
- **Pre-registered reading (written before any fire):** ERROR / runtime exceeded → even a 6-minute ceiling overruns: per-task overhead or the task count is larger than assumed; next step is 5 minutes or fewer, or fewer tokens per session. Score >= 0.18 → first score outside the 0.08–0.17 band: the unboxed budgets (thought, calls, turns) with true facts are worth it inside a bounded clock. 0.12–0.17 → inside the band at one draw (noise about 0.05): no verdict. <= 0.10 → worse than the old boxed packages at a similar clock: the long-thought agent does not fit six minutes, or the host does not grade the unsubmitted working tree the way the local harness does (about half of the local solves at this ceiling came through that fallback).

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

