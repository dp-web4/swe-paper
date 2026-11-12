# SWE paper v4.3: evidence and submission review

Reviewer: Dottie. Date: 2026-11-12 UTC.
Requested by Dennis: full review from the connected session, then permission to post these notes to git.

## Scope and verdict

Reviewed [PAPER_DRAFT_v4.3.md](https://github.com/dp-web4/SWE-SAGE/blob/2c886aa6389551e0665373c44d38125c17e9c1df/paper/swe-paper-track-2026/PAPER_DRAFT_v4.3.md), pinned to SWE-SAGE commit `2c886aa6389551e0665373c44d38125c17e9c1df`, against the current blackbox PRD, graph-uptake audit, SWE competition documentation and official Kaggle indexed guidance.

**The central finding is worthwhile: misleading harness descriptions, inherited limits and an overused development panel can masquerade as model failures. The draft needs factual and interpretive corrections before submission.** These notes do not edit the paper, authorize a scored submission, or claim that any Kaggle Writeup has been submitted.

This is a document/source audit, not an independent rerun of raw Thor traces. Primary receipts remain stronger than the living PRD where they differ. The main numerical results below were checked against that PRD, not regenerated from all raw artifacts.

## 1. Required factual corrections

Line references below refer to the pinned draft, not future versions.

### 1.1 Model restriction changed (line 38)

“Every team uses the same hosted, quantized Gemma-4-31B” is no longer correct.

Kaggle staff's [new-model announcement](https://www.kaggle.com/competitions/gemma-4-developer-agent/discussion/748287) and [updated official guidance](https://www.kaggle.com/competitions/gemma-4-developer-agent/overview/prizes) permit these exact variants:

- `gemma-4-31b-it-qat-w4a16-ct`
- `gemma-4-12b-it-qat-w4a16-ct`
- `gemma-4-e4b-it-qat-w4a16-ct`
- `gemma-4-e2b-it-qat-w4a16-ct`

Every agent/subagent in one submission must use the same variant. Different LoRA adapters are allowed. This does not permit arbitrary checkpoints or quantizations.

Dennis's recollection of the 31B-only rule is correct historically: old official overview text still appears in the search index, and the repository's `submissions/validate.py` still hardcodes 31B. [COMPETITION.md](https://github.com/dp-web4/SWE-SAGE/blob/main/docs/COMPETITION.md), updated November 2, explicitly supersedes the September 26 31B-only statement. The staff announcement is stronger evidence of the current allowance than an old local validator. I have not independently inspected the currently deployed private scorer.

Suggested replacement: **“Our experiments use the hosted, quantized Gemma-4-31B.”**

The E2B/E4B bonus prize is additional to general leaderboard eligibility; it is not the sole permission for smaller models. 12B is allowed but not eligible for that small-model bonus. The paper track also accepts related unpublished research without requiring participation in the benchmark.

### 1.2 Baseline panel mixed up in abstract (line 31)

“The old scored package resolved 2 of the same fresh 24” follows V1's 4/24, but v37 was tested on the first fresh panel A, not V1.

Replace with: **“On the first fresh panel, the old package resolved 2/19 scoreable tasks versus 3/19 for v68.”**

PRD 000425 and November 12 00:2x grading correction identify the five invalid panel-A tasks. Do not turn the two gold-identical patches in invalid cells into verified solves.

### 1.3 Coverage census is stale (line 121)

“Only 57 of the 129 public tasks had ever been run locally” conflicts with the later panels. Frozen 24, fresh A 24, V1 24 and V2 24 are described as disjoint; that already implies at least 96 unique tasks. Delete the 57 claim unless replaced by a freshly checked unique-task inventory. Do not substitute 96 as an exact all-history census.

### 1.4 Two rewrites, not three (line 74)

Panel 0004253 ran v68s24 baseline, v72bs24 and v73s24. These are **two rewrites and their baseline**, not three rewrites. All resolved 4/24; union 6/24.

### 1.5 Abstract's universal budget history is false (line 29)

“For six weeks every version” at six minutes, 80–100 turns and thought off/capped at 1,024 contradicts the paper's own record: v27's 4,096 setting, other task ceilings and the earlier 40-turn setting.

Suggested replacement: **“Our versions inherited restrictive time, call, turn and reasoning settings.”** If exact historical ranges are retained, audit each configuration and distinguish a configured thought budget from evidence that the runtime honored it.

### 1.6 Timeout/no-return claim contradicts v24

The paragraph after the score table says that after raising command timeout no run returned to 6/58. The same table lists later v24 at 0.10. Delete that universal no-return statement. If distinguishing an exact count from a displayed rounded/truncated score, provide the underlying receipt rather than treating displayed 0.10 as proof of a different count.

### 1.7 Submit-loop denominator needs reconciliation (line 103)

“1 of 18 sessions: the same eight ... and twelve others” mixes denominators: those cohorts total 20 sessions. The PRD November 11 03:1x correction says **1 of 18 submitters**, not all sessions; the row-level descriptions should be reconciled with the raw census before retaining this exact rate.

Safe replacement: **“Subsequent runs showed far fewer loops, but one remained.”**

“Urging sentence kept” is supported by PRD 000409b: v62 is v59 plus truthful termination semantics. The later literal terminal utterance is another change; do not attribute the whole progression to one sentence.

### 1.8 Universal preregistration is too strong (line 47)

“Every scored slot and local run” is not supported as written. PRD 000376 explicitly records missing preregistration received for v41 at that point, while the initial scaled-clock row says “No gate.” Later gates and decisions exist, but a universal claim requires their timestamps.

Suggested wording: **“We recorded prospective decision rules for the comparisons where gates are stated below.”**

### 1.9 Define the 12-hour budget accurately (line 37)

Official guidance says the allowance covers patch generation **including sandbox setup, excluding patch validation**, not literally the whole submission-to-result interval. Use that definition. Completion latency also includes queueing and other stages.

## 2. Required interpretive corrections

### 2.1 Thinking-off result is inconclusive by its own gate (line 134)

0004254 gives thought off 2/24 versus on 4/24, paired +1/-3. The preregistered band -3 through +3 is inconclusive on improvement; the result does not meet the <= -4 “thought does work” threshold.

Suggested replacement:

> Thinking off resolved 2/24 versus 4/24 with thinking on, within the pre-registered inconclusive band. It also produced fewer source-edit sessions and more malformed calls. This does not establish the size or reliability of a reasoning benefit.

The mechanistic observations are useful; “taking one away costs” and “footgun” should not be presented as an established outcome effect from this one draw.

### 2.2 Graph nonuse was measured with broken local tools (line 78)

0 calls in the particular 96-session sample is verified. But the [wider uptake audit](../claude_curiosity_lora_1110/e1/SKILL_UPTAKE.md) found 20 sessions attempted graph tools among 2,833 known-offer sessions, and every attempt failed with a missing repository/index error. Two additional attempted sessions had unknown offer status.

Append near the 0/96 claim:

> In the wider corpus, 20 sessions attempted graph tools; every attempt failed because the local index was missing.

The evidence supports “rarely attempted, never functional locally,” not “working tools were ignored.” Hosted graph availability remains unknown.

### 2.3 Speed ratios are scenarios, not measurements (line 45)

3.6–4.65 are scenario multipliers. Do not leave “implies at least 3.8 times faster” as an unconditional empirical bound without the supporting assumptions and derivation. A 20-minute Thor session corresponds to five hosted minutes **under the 4x scenario**, not by direct measurement. Scaled local trees also changed the stated prompt budget, so the comparison is not hardware scaling alone.

v58's actual runtime error is relevant; it does not identify every runtime component. v68's completed 0.17 is relevant; it does not prove that a six-minute cap will always fit. Six minutes times 120 tasks already consumes twelve hours before setup overhead.

### 2.4 Scope the “wrong fix in the right place” claim

Gold-file naming in serialized tool arguments is a proxy, not necessarily a successful read or understanding. The six manually read v68 failures are selected cases, not a population-rate estimate. Keep the concrete five wrong-in-substance / one missing-sibling observations, but soften “usually” in the abstract and distinguish naming, opening, editing and passing.

Earlier invalid grader cells cannot establish bad fixes. The two gold-identical cases are a warning about the evaluator, not automatically verified solves; extra differences from a gold patch are not automatically wrong either.

### 2.5 Agreement at 0.17 is consistency, not calibration proof

Fresh local 4/24 and hosted 0.17 are consistent at this precision. Their numerical equality does not validate the speed model, establish distribution equivalence, or prove selection bias is the only source of the frozen/hosted gap.

Likewise, “no out-of-sample gain” should read **“no demonstrated out-of-sample gain under the preregistered rule,”** not proof of zero effect.

### 2.6 Avoid universal conclusions from null uptake

0/12 notes-file use supports an unused offer in this test, not the claim that prose cannot provide an affordance or that external memory cannot help. “An offer in prose is still not an affordance” is rhetorically stronger than the experiment.

The ending “not more instructions” also exceeds the scope: the record itself contains useful corrections to instructions describing actual harness behavior.

## 3. Findings that should be preserved

The following agree with the PRD record inspected:

- v68 hosted result: 0.17, no error, tying best, not proof that unboxing improved the hosted score.
- v58: runtime error, no score; fired configuration retained 60 calls, not the later 200-call setting.
- Frozen v68 draws: both 19/20 among jointly known cells, with different losses.
- Fresh A: v68 3/19 scoreable versus v37 2/19.
- V1: v68/v72b/v73 each 4/24, union 6/24, no arm passes its improvement gate.
- Thought-off: 2/24 versus on 4/24, inside its inconclusive band.
- B2's **two cap-bound failures is supported** by the later November 11 04:27Z correction. Do not replace it with the earlier single-failure reading.
- The local termination description was false and later runs retained a residual loop. This is a strong concrete example of the central thesis.
- Multiple changes were bundled when raising caps; the paper correctly avoids individual attribution there.

## 4. Paper-track completion requirements and editorial priorities

[Official paper-track guidance](https://www.kaggle.com/competitions/gemma-4-developer-agent-paper) was retrieved through its official-domain search index; dynamic direct retrieval did not produce readable page lines.

- Deadline: **2026-11-12 23:59 UTC = 15:59 PST.**
- Maximum: **3,000 words**.
- Required content includes title/subtitle, abstract, introduction, methods/experiments, **related works and citations**.
- Saving a Writeup is not submitting it. The final **Submit** action must happen before the deadline; drafts are not considered.
- Code/notebook/project assets are optional. Public assets must be accessible. Attaching private Kaggle resources can cause them to become public after the deadline; avoid accidental disclosure.
- No submission receipt was verified in this review.

The draft's evidence appendix is not a substitute for related work. Add a short, properly sourced comparison with relevant software-agent/benchmark and agent-interface literature; verify bibliographic details rather than inventing them. Explain the contribution as empirical diagnosis of harness/evaluation failures, not the unproven universal sufficiency of affordances.

The existing “regime” section can serve the introduction if made explicit. Replace private-only paths with a reviewer-usable evidence plan where possible; do not publish raw traces or private material without authorization.

Word count of the pinned draft: **2,944** with HTML comments stripped and whitespace tokens counted, using the README's stated method. That leaves about 56 words, not enough for a useful related-work section without cuts. Trim repeated slogans, chronology and overstrong claims before cutting necessary caveats.

## 5. Suggested integration order

1. Correct model eligibility, panel identity, stale coverage, rewrite count and universal budget/preregistration claims.
2. Fix the timeout/no-return statement and submit-loop denominator.
3. Qualify thinking-off, graph availability, speed scenarios and selected-case interpretation.
4. Add related work and citations; count the final submitted text again.
5. Recheck the final draft against the pinned receipts and verify an actual Kaggle submission receipt separately.

This review does not require new GPU experiments. It asks for accurate reporting of the evidence already obtained.

## Sources and provenance

- [Pinned paper v4.3 commit](https://github.com/dp-web4/SWE-SAGE/commit/2c886aa6389551e0665373c44d38125c17e9c1df).
- [Running SWE PRD](../claude_swe_affordance_prd/PRD.md): rows 000409/000409b, 000412/000414, 000414b, 000419/000420, 000425/0004253/0004254; corrections November 11 03:1x and 04:3x; November 12 00:2x and 00:3x.
- [Skill/graph uptake audit](../claude_curiosity_lora_1110/e1/SKILL_UPTAKE.md).
- [SWE competition context](https://github.com/dp-web4/SWE-SAGE/blob/main/docs/COMPETITION.md).
- [Official model-expansion announcement](https://www.kaggle.com/competitions/gemma-4-developer-agent/discussion/748287).
- [Official model/budget/prize guidance](https://www.kaggle.com/competitions/gemma-4-developer-agent/overview/prizes).
- [Official paper-track requirements](https://www.kaggle.com/competitions/gemma-4-developer-agent-paper).

Publication scope: new review file only. No source code, existing paper draft, shared coordination record, GPU job, scored bundle, or Kaggle submission changed.
