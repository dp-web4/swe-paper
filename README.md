# When the Harness Holds the Agent Back

*What moved, what did not, and why, for a Gemma-4-31B software agent scored once a day*

Paper-track submission to the Kaggle **Gemma 4 Developer Agent** competition, 2026-11-12. The paper is [`PAPER.md`](PAPER.md) (2,987 words).

It covers more than thirty scored versions of one agent. Most of what we tried did not move the hosted score. The two largest effects were both limits we had set ourselves:
- budgets and a false description of the harness that we had never measured against the host;
- a fixed 24-task development panel. On fresh tasks, gains measured on that panel disappeared.

## What is here

| Path | What it is |
|---|---|
| `PAPER.md` | The submitted text. |
| `evidence/LEDGER.md` | The submission ledger: one row per scored slot, with the artifact's sha256, what it tests, a reading written before the score, and the score. It also covers local builds that were never fired. |
| `evidence/LEDGER_excerpt_1105_1111.md` | The ledger rows for 11-05 to 11-11, excerpted for the paper. |
| `evidence/PRD.md` | The research log, unedited. It records every directive, run and correction in time order (newest first), with run ids such as `000425` and `0004253` that the paper cites. |
| `evidence/panels/` | Task lists for every local panel. `fresh24_seed1111` is the first fresh panel ("panel A"). `panelV1_valid_seed1113` and `panelV2_valid_seed1113` were drawn only from scoreable tasks. |
| `evidence/grader/valid_tasks.json` | The tasks our local grader can score (see below). |
| `evidence/grader/sweep_rescore_REPORT.txt`, `BUDGET_FIT2.txt` | Earlier scored packages replayed on scoreable tasks at a 90-minute local clock. This is the source of the paper's "0.33–0.46 locally". |
| `evidence/SKILL_UPTAKE.md` | Census of how often the agent used skills and graph tools across 2,833 sessions. |
| `evidence/readers/` | Scripts that produced the paper's per-arm numbers: paired reads, locate-vs-repair, rescoring, notes-file uptake, and the graph-tool probe. They use paths from our machines and won't run here as-is. |
| `bundles/v58-…`, `bundles/v68-…` | The two submissions the paper compares directly: v58 (unboxed, 20-minute ceiling, hosted runtime error) and v68 (six-minute ceiling, scored 0.17). |
| `reviews/` | Two pre-submission reviews: cloud-claude's red-team of v4 and Dottie/Nova's review of v4.3. Both sets of corrections are in the paper. |

## Definitions

- **Scoreable task.** A public task counts as scoreable when the reference patch passes our local grader and an empty patch does not pass.
  - 94 of the 129 public tasks meet this rule; they are the ones in `valid_tasks.json`. Every panel count in the paper uses it.
  - 82 meet a stricter version, which also excludes tasks where the empty patch's result was indeterminate rather than a failure.
  - The 12 tasks between the two counts: fastapi_14186, 14262, 14609, 14978, 15030, 15661, 15745, 15785, and rich_3480, 3772, 3930, 4006.
- **Clock scale.** The local model ran on a Jetson AGX Thor, which is several times slower than the competition host. The speed ratios of 3.6 to 4.65 are scenarios, not measurements (paper §2).
- **Seats.** The log and ledger name the agents that did the work, such as thor-claude, kimi-code, thor-codex and cbp-pm (Claude, Kimi and Codex sessions on different machines). "dp" is the human operator.

## What is not here

- **Session traces.** Thousands of sessions; too large to include.
- **Every other submission bundle.** The main competition is still running.
- **The competition's task data.** It is Kaggle's to distribute.

Some links and paths in the log and reviews point to our private working repositories. The files they cite are copied here wherever the paper depends on them.

## Provenance

These files were copied on 2026-11-12 from our private working repositories:
- the paper and ledger from `SWE-SAGE` (main 9193966; ledger and bundles from branch `thor-claude/swe-wip` af79f0f);
- the log, panels, grader data, readers and Dottie's review from `blackbox` (main 3b1b29a).

The only edit was to the paper's evidence appendix and two scoreable-task counts, so that both match this repository.
