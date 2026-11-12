# Shipped Is Not Used, and the Box Was Ours

*What moved, what did not, and why, for a Gemma-4-31B software agent scored once a day*

## Abstract

We ran more than thirty scored versions of a Gemma-4-31B software agent in the Gemma 4 Developer Agent competition. The regime allows one submission per day; a result returns 13–46 hours later as one public score.

**What did not move the score.** Prompt rules, procedures, multi-role agents, skills, a byte-for-byte copy of the public 0.24 bundle (0.12 for us), and a behaviour-cloning LoRA adapter (0.06). About twenty scored runs sit in a 0.08–0.17 band whose only replicate pair differs by 0.05.

**What we found when we stopped tuning inside our own limits.** Our versions inherited restrictive time, call, turn and reasoning settings. Locally, with the clock scaled to an assumed host speed, our own caps ended most remaining failures, and the prompt falsely told the model that submitting ends the session; sessions looped on submit up to 82 times. Our first hosted unboxed run exceeded the 12-hour wall: by our pre-registered reading, one of our limits had been guarding a real one. Bounded to six minutes, the unboxed agent completed and scored 0.17, tying our best.

**What we found when we stopped measuring inside our own panel.** Every build decision that week was read on the same 24 public tasks, where the bounded agent resolved 19 of 20 known cells, twice. On fresh tasks no decision had touched it resolved 3 of 19 our grader can score, and 4 of 24 on a second fresh panel of gradeable tasks: 0.17, its hosted score. On the first fresh panel the old scored package resolved 2 of 19 scoreable tasks against 3. The gains we had measured were in-sample. In the fresh failures we read, the agent had named the right file and written the wrong fix.

Our working rule, shared with the companion ARC-AGI-3 paper (*Affordance Is All You Need*), became a mantra: **affordance is all we need.** A harness lifts outcomes through what the model can and does use. Telling is not giving, giving is not using, and a limit nobody measured, on the agent or on ourselves, is still a limit.

## 1. Introduction: the regime

- About 120 hidden tasks from private repositories; 129 public tasks. A 12-hour allowance for patch generation, sandbox setup included, validation excluded. Score is the fraction resolved by hidden tests; an unsubmitted working-tree diff is still graded.
- Our experiments use the hosted, quantized Gemma-4-31B; the rules now also allow 12B, E4B and E2B variants. A submission is a prompt, tools, sampling and budget settings, and optional skills and LoRA adapters.
- One submission per day, 13–46 hours from submission to result: about forty scored observations, each a single noisy draw.

## 2. Instruments

**The local mirror.** All 129 public snapshots, the hosts' grader, and the real 31B checkpoint on a Jetson AGX Thor (about 5 completion tokens per second per stream, four streams). Arms are paired per task.

**The clock scale.** Thor is several times slower than the host. One hosted run completed inside the wall although its Thor durations predict 16 hours, which, if tasks run one at a time, implies a host about 3.8 times faster. We use 3.6–4.65 as scenario multipliers, not measurements. Under the 4× scenario, a session cut by a 20-minute clock on Thor has had about five hosted minutes. For six weeks we read such cuts as the agent's failures.

**Pre-registration.** For the comparisons whose gates are stated below, the reading was written before the result.

## 3. The scored record

Public scores, 0–1, on a public split of about 58 tasks.

| Version | Score | The arm |
|---|---|---|
| v2, v3, v4, v6 | 0.10 each | 120-s command timeout; thought off/on; procedure variants |
| v7, v8 | 0.10, 0.10 | two multi-role agents |
| v9 → v11 | 0.13 → 0.15 | command timeout 120 → 300 → 600 s |
| **v12** / v12r | **0.17** / 0.12 | premature-closure prompt fix; byte-identical resubmit |
| v14, v15, v16 | 0.13, 0.13, 0.12 | locate-code skill; turns 40 → 80; understand-before-edit step |
| v18, v22, v23b, v24 | 0.15, 0.08, 0.15, 0.10 | lessons header; related-files skill read / acted on; three procedure asks |
| v25, v27, v28 | 0.15, 0.15, 0.12 | timeout 1,800 s; thought budget 4,096; exact status call |
| v26 | 0.12 | the public LB-0.24 bundle, byte-for-byte |
| v32c | 0.12 | stop sequence removed |
| v33 | 0.06 | v32c + behaviour-cloning LoRA adapter |
| v37 | 0.15 | **no skills at all**, six minutes |
| v41 | 0.13 | flat tool calls, 28-call cap |
| v58 | **error** | first unboxed run: thought 4,096, 20-minute ceiling; exceeded the 12-hour wall |
| **v68** | **0.17** | unboxed budgets and true facts, six-minute ceiling |

v12 and its byte-identical resubmit differ by 0.05, about three tasks: no single slot is a verdict.

## 4. What did not work

**D1: Telling.** Prompt rules, procedure steps, role splits and an exact status-check call did not leave the band. On 11-12, two rewrites aimed at ordering and scope ("commit an edit early", "make the minimal change") and their baseline each resolved 4 of the same 24 fresh tasks.

**D2: Giving without uptake.**
- A related-files skill, aimed at a measured gap (a missed reference file was one import hop away in 44 of 51 runs), climbed one rung per version: called then dismissed (15 of 20 runs; a listed file edited in 0); read, every verdict "no change"; cited but not acted on.
- Three code-graph tools were called 0 times in 96 sessions. Availability was also broken locally: in the wider record 20 sessions attempted them and every call failed, because the graph files the competition ships had never been copied to our mirror (§8). Rarely attempted, never functional locally.

**D3: Cloning behaviour into weights.** A rank-8 LoRA adapter on the query projections of all 60 layers, trained to reproduce the next call in public agent trajectories: telling the model how to think, in weights. Trained on the source agent's short pre-call prose, the adapter cut reasoning before a file read from 87–191 tokens to 1, while all 15 tool names still matched the base model. v33, the incumbent plus the adapter, scored 0.06 against 0.12: inside its pre-registered "the adapter hurts" band, one draw. It tests cloning other agents' calls, not post-training in general.

**D4: A rule against a fault that is not behavioural.** Skill-using versions resent identical malformed tool calls, one up to 66 times. "Never send the identical call again" did not stop it: a backtick inside a code argument closes the string early, and the harness rejects the call before the tool-call cap counts it, though each still spends a turn. Flat tools avoided the vulnerable argument class.

## 5. The box was ours

On 11-10 we asked why the scored versions ran at six minutes. The answer was a 12-hour wall we had read about and never measured against the host's speed. The same was true of the other budgets.

**B1: The clock.** A measurement copy of the unboxed package, its per-task clock scaled ×4 to give a Thor session roughly a hosted 20-minute token budget, ran once on 24 public tasks:

| | Count |
|---|---|
| Resolved | 17 |
| Unresolved | 3 |
| Unknown (local harness could not apply the test patch) | 4 |
| Sessions at the per-task clock | 0 |

**B2: The tool-call cap.** Two of the three unresolved sessions were ended by the 60-call cap we had kept.

**B3: A fact stated falsely.** The prompt said `submit_patch` "ends agent work" and should be the "final tool action". A session ends when the model replies with no tool call. With an added sentence urging early submission, three of five submitting sessions on eight tasks then called `submit_patch` 28, 64 and 82 times until the clock, each turn saying "I'll stop." Replacing the two false sentences with the true mechanism, urging sentence kept, left far fewer loops in later runs; one remained.

**B4: What binds instead.** 98% of session time is generation: about 44 model steps and 7,900 completion tokens per session. Projected to 120 tasks, the 1,565-second mean session is 14.5, 13.0 or 11.2 hours at host speed ratios of 3.6, 4.0 and 4.65. On this projection the run's average binds, not the per-task ceiling; v58's error is consistent with that, not proof of it.

**The scored test.** v58 ran this configuration hosted (thought 4,096, 20-minute ceiling, 60 calls), with its reading registered before submission: an error means the wall binds at this average. Result: **error**, "exceeded the allowed runtime", about twelve hours after submission. No score.

**Bounding the run.** After the hosted error, v68 added a six-minute ceiling and the run's arithmetic to the later local configuration (200 calls, 500 turns, 8,192 output tokens, true termination text). At the matching local clock, two draws each resolved 19 of the 20 comparable cells. Hosted, it completed 12.5–13 hours after submission, like the old six-minute packages, and scored **0.17**: our best, tied, inside one draw's noise. The registered reading for that band is no verdict on unboxing.

**The panel was ours too.** Most numbers above come from the same 24 public tasks, on which every decision of the week was read. Before firing v68 we ran it on 24 fresh public tasks, with a rule set in advance: more than 15 points below the frozen figure means the week's local numbers overstate the package. It resolved **3 of 24**, and nineteen sessions ran to the clock. Then two more facts arrived.
- **Our grader could not score every task.** Only 94 of the 129 public tasks pass the check that the reference patch resolves and an empty patch does not (82 if an indeterminate empty-patch result also fails); the frozen panel held 19 such tasks, the fresh panel 19. Two baseline patches identical to the reference fix were graded unresolved. On scoreable tasks the fresh figure is 3 of 19.
- **A second fresh panel of 24 scoreable tasks** gave v68 **4 of 24 (0.17)**, the same as its hosted score.

The old scored package (v37 bytes, hosted 0.15) resolved 2 of the first fresh panel's 19 scoreable tasks, both among v68's 3: no demonstrated out-of-sample gain from the unboxing under the pre-stated rule.

## 6. Where the agent loses

- **In the cases we read, the wrong fix in the right place.** Naming a file in a tool call is a proxy, not proof it was read or understood, and six cases are not a rate. The old package named a reference-patch file in 21 of 24 fresh sessions and edited one in 15, and resolved 2. It edits sooner and more often than v68 and converts no better. Of six located-but-unresolved v68 cases read beside the reference fix, five are wrong in substance (two wrong ideas, three wrong exact behaviours) and one misses a sibling change. Arms mostly fail the same tasks: two rewrites and their baseline resolved 4 each and 6 in union on one panel, and on another v68 solved the old package's two plus one.

## 7. Why: given, used, and unmeasured

This is interpretation.

- **Telling is not giving.** Rules, procedures and role splits are decisions imposed on the model. None moved the band; the one cloned into weights lowered it. A run clock offered as advice was mostly not read, and a call cap with the harness's own warning resolved 2 of 24 against 3.
- **Giving is not using.** A shipped tool becomes an affordance only if the model reaches for it; each rung (shipped, called, read, acted on) needs its own gauge.
- **Taking one away did not help.** With the thought channel off, the same package resolved 2 of 24 fresh scoreable tasks against 4 with it on: inside the pre-registered inconclusive band, with fewer source edits and more malformed calls. Trading capability for speed did no better: the allowed 12B model produced 2.4 times the tokens in the same wall time and resolved none of four tasks chosen because the 31B had solved them (a stopped, partial read).
- **An affordance left unused is a footgun too.** The competition ships the files the graph tools need. We never gave the agent a working copy to learn on, and read the silence as its lack of interest.
- **Withholding is the common failure, and it is quiet.** Most budgets in §5 were leftovers, not decisions, and each cut looked, in the traces, like the agent failing. The prompt did not say how a session ends or the run's arithmetic, and one thing it said was false.
- **A statement of fact is cheaper than a rule and did more.** The one prompt change in this record with a clear local effect corrects a false sentence (B3).
- **The same holds for the measurer.** A fixed panel, and a grader nobody checked per task, are limits on what the builder can see. Ours turned the week's improvements into facts about 24 tasks.

The sequence that mattered was: stop telling, measure what the agent actually runs into, remove what is ours to remove, tell it the truth about the rest, and check every gain on tasks no decision has touched. That is what we mean by *affordance is all we need*: resources and true facts the agent can act on, rather than rules about how to act.

## 8. Instrument failures

- **The local graph tools ran against empty directories** for six weeks: the competition data ships a graph and an embedding file per repository commit, and we had not copied them. A reviewer's question found it on the last day; whether the tools work once the files are in place is untested.
- **The local grader could not score 35 public tasks**; we drew panels without checking.
- **Thor's clock was read as the host's** (§2).
- **The regression panel became the benchmark** (§5).

Every gauge must fire on a known case before it is read, and every panel must be checked against tasks it has not seen.

## 9. Limits

- **One draw per cell.** Local panels are small (4–24 tasks) and draws few. The hidden set differs from the public tasks.
- **Local and hosted.** The frozen panel (85–95%) and hosted scores (0.08–0.17) disagreed fivefold; on fresh scoreable tasks they are consistent (0.17 and 0.17) at this precision. That is consistency at one draw each, not calibration of the gauge or of the clock model.
- **The scaled clock is a model** (§2).
- **Post-training is one failed recipe** (D3): imitation of other agents' calls. Nothing here speaks to other objectives.

## 10. Conclusion

The scored channel, one noisy draw a day, can confirm a large change but cannot find one. The largest things we found were not in the agent. The first was the set of limits we had placed around it without measuring them. Most were ours to remove; one, the short clock, was guarding the host's wall. The second was the limit we had placed around ourselves: a fixed panel on which every decision was read. On tasks it had never seen, the improved agent resolved what the scored versions score on the host. The lesson is to measure every limit, including the measurer's, not to remove them all.

What is left is not more rules. On scoreable public tasks, with about four times our per-task time, the old packages resolved 0.33–0.46 locally while scoring 0.08–0.15 hosted. Inside a fixed wall, the open problem is solving more per hosted minute: a better first fix, and affordances the agent can actually reach, starting with the ones already shipped.

**Practical rules for agent builders:**
- list every budget in the package and find out which one a session actually hits first;
- convert local clocks to the host's speed, and budget the run's average, not only the per-task ceiling;
- check every sentence in the prompt that describes the harness against the harness;
- gauge every tool from shipped to called to read to acted on, and check that it works where you measure;
- check that your grader can score each task, rotate fresh tasks into every panel, and read no gain until it holds on them;
- calibrate noise with deliberate same-bytes replicates, and register every reading before the score arrives.

## Related work

SWE-bench [1] set the task form this competition uses: real repository issues, resolved when hidden tests pass. SWE-agent [2] showed that the agent-computer interface shapes results; we measure the step after design, whether a shipped tool is called, read and acted on. Agentless [3] separates localization from repair; our fresh failures sit in the second step. Audits of SWE-bench and other agentic benchmarks found weak tests and invalid tasks that misstate scores [4, 5]; our grader check (§5) is that audit, done late. Reading every decision on one panel is the adaptive-overfitting problem the reusable holdout addresses [6].

[1] Jimenez et al., SWE-bench, ICLR 2024. [2] Yang et al., SWE-agent, NeurIPS 2024. [3] Xia et al., Agentless, arXiv:2407.01489. [4] Aleithan et al., SWE-Bench+, arXiv:2410.06992. [5] Zhu et al., Establishing Best Practices for Building Rigorous Agentic Benchmarks, arXiv:2507.02825. [6] Dwork et al., The reusable holdout, Science 349, 2015.

## Evidence appendix

Public at github.com/dp-web4/swe-paper:
- `evidence/LEDGER.md`: one SHA and a pre-registered reading per scored slot; `bundles/`: v58 and v68.
- `evidence/PRD.md`: the research log, every directive and run, including 000419–000426, 0004253–0004254 and the grader-validity correction.
- `evidence/panels/`, `evidence/grader/valid_tasks.json`, `evidence/readers/`: panel lists, scoreable tasks, readers.
- `reviews/`: cloud-claude's red-team of v4 and Dottie/Nova's review, whose corrections are folded in. Other reads (thor-codex, kimi-code) are in the log.
