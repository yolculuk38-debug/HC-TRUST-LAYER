# PR Review Timing Audit — 2026-07-25

Status: report-only project-control evidence.

## Purpose

This audit compares the review and merge timelines of pull requests
[#1222](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/pull/1222)
and
[#1223](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/pull/1223).
It records why Automation Gate success and an elapsed 90-second review window
did not prove that Codex had reviewed the current head before merge.

The audit proposes a deterministic current-head review-evidence contract for
human operators. It does not implement or change a workflow, required check,
permission, review request, comment writer, label, assignment, approval,
rejection, close, merge, or auto-merge behavior.

Boundary flags:

- `advisory_only=true`
- `report_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- `human_review_required=true`
- `approval_authority=false`
- `merge_authority=false`

## Evidence basis

Evidence was collected from the live GitHub pull request timeline, Actions run,
review, comment, thread, and merge records on 2026-07-28 UTC. Repository files
were checked at `main` commit
[`ac07d76a0cdba3e635d7621adc2309ab3b8f915b`](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/commit/ac07d76a0cdba3e635d7621adc2309ab3b8f915b).

The audit uses these source records:

- #1222 head: `45ebfb7b5045d4077274d02ab46ccb1878bfe8ad`
- [#1222 Automation Gate run 1238](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/actions/runs/30172665369)
- [#1222 Codex review](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/pull/1222#pullrequestreview-4780075076)
- [#1222 actionable P1 thread](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/pull/1222#discussion_r3650925452)
- [#1222 merge commit](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/commit/451405d48739a10555982ead6a223723d418591d)
- #1223 head: `9e98b927b51a5c2da8e2699aa7fe1cdf502c7d8d`
- [#1223 Automation Gate run 1239](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/actions/runs/30173017794)
- [#1223 explicit Codex request](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/pull/1223#issuecomment-5080401965)
- [#1223 Codex result](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/pull/1223#issuecomment-5080408589)
- [#1223 merge commit](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/commit/1e2a4e1051c95b69fde37a2906032d2021e65710)
- `.github/workflows/automation-gate.yml`
- `docs/project-control/hc-trust-engineer-command-interface.md`
- `docs/project-control/hc-mission-execution-protocol.md`
- `docs/project-control/human-final-reviewer-pr-checklist-boundary-review.md`
- `docs/project-control/ai-assisted-contribution-and-bot-comment-handling-review.md`

## Observed timeline

All timestamps are UTC.

| Evidence | #1222 | #1223 |
| --- | --- | --- |
| Ready for review | 2026-07-25 19:59:28 | 2026-07-25 20:09:56 |
| Automation Gate | `success`; completed 19:58:58 on the current head | `success`; completed 20:09:35 on the current head |
| Gate relation to ready state | Completed 30 seconds before ready | Completed 21 seconds before ready |
| Explicit `@codex review` request | None recorded | 20:13:48 |
| Codex review/result | 20:02:22; actionable P1 | 20:15:51; no major issue reported |
| Reviewed head evidence | `45ebfb7b50`, matching the 40-character #1222 head | `9e98b927b5`, matching the 40-character #1223 head |
| Merge time | 20:02:07 | 20:17:24 |
| Review relation to merge | Review arrived 15 seconds after merge | Review arrived 93 seconds before merge |
| Ready-to-review duration | 174 seconds | 355 seconds |
| Ready-to-merge duration | 159 seconds | 448 seconds |
| Explicit human exception | None recorded before merge | None recorded or required for missing-review handling |

For #1223, the explicit request-to-result interval was 123 seconds. This is an
observed interval, not a Codex service guarantee or a causal claim.

## Findings

### 1. Automation Gate success is not Codex review evidence

The Automation Gate workflow checks PR title/body presence, blocked binary file
extensions, and Python syntax. Its `pull_request` trigger list does not include
`ready_for_review`. In both audited PRs, the successful Gate run completed while
the PR was still a draft.

The Gate correctly provided its defined check evidence. It did not assert that
Codex had started or completed a review, and its success must not be interpreted
as that assertion.

### 2. Ninety seconds is a minimum observation window, not completion proof

#1222 remained ready for 159 seconds before merge, but its Codex review arrived
at 174 seconds and contained an actionable P1. Therefore, an elapsed 90-second
window plus a clean comment/thread snapshot can still precede a current-head
review result.

The 90-second marker remains useful as a minimum anti-rush observation signal.
It is not sufficient evidence for `codex_review_completed=true`.

### 3. Review evidence can be bound to the current head

Both Codex results declared a reviewed commit prefix that matched the PR head.
#1223 preserved that same head through merge. #1222 also received a review for
the correct head, but only after merge.

A review result is current-head evidence only when its declared commit SHA or
unambiguous SHA prefix matches the current PR head at the decision time.

### 4. No exception should be inferred from silence or elapsed time

No explicit GitHub-recorded missing-review exception was found before #1222
merged. The audit therefore classifies the merge-time state as
`merged_without_current_head_review_evidence`, not as an authorized exception.

Chat context, a previously broad instruction, a successful check, a quiet
comment list, or an elapsed timer must not be converted into an exception
record.

### 5. Post-merge audit reduced impact but did not repair the timing gap

The #1222 post-merge audit detected the late P1, #1223 reproduced the wheel
failure, fixed it, added regression coverage, received a current-head Codex
result before merge, and resolved the #1222 thread.

This recovery preserved auditability. It does not make merge-before-review the
preferred path.

## Proposed current-head review-evidence contract

The contract is a manual/reporting contract in this slice. It does not grant
automation or merge authority.

### Required evidence fields

Before merge-readiness guidance, record:

- `pr_number`
- `current_head_sha`
- `ready_at`
- `review_requested_at`
- `minimum_review_window_seconds`
- `minimum_review_window_elapsed`
- `codex_review_status`
- `codex_review_completed_at`
- `codex_reviewed_head_ref`
- `codex_review_head_match`
- `codex_review_outcome`
- `blocking_findings_open`
- `unresolved_threads_open`
- `current_head_checks_status`
- `review_timeout_seconds`
- `review_timeout_at`
- `human_exception_recorded`
- `human_exception_actor`
- `human_exception_at`
- `human_exception_head_sha`
- `human_exception_reason`
- `human_exception_accepted_risk`
- `merge_guidance`

### Deterministic evaluation

1. A new head SHA invalidates prior timing, check, and review evidence. Restart
   the evaluation for the new head.
2. Keep 90 seconds as the minimum review window. Its completion changes only
   `minimum_review_window_elapsed`; it must not set Codex review status.
3. Request Codex review for the current head when the PR becomes ready or when
   the head changes.
4. A Codex result satisfies the presence requirement only when:
   - the source is the configured Codex review identity;
   - the result has a completion timestamp;
   - its reviewed SHA is the full current head or a hexadecimal prefix of at
     least 10 characters that matches the current head;
   - the PR head has not changed after the review evidence was produced.
5. An actionable P1 or P2, an unresolved applicable thread, a failed or missing
   required check, or a head mismatch produces `hold_for_review`.
6. A clean current-head Codex result may produce
   `eligible_for_human_decision` only after the minimum window, current-head
   checks, diff/scope review, and thread review are also complete.
7. No report state approves or merges a PR. Human final authority remains
   required.

### Provisional bounded timeout

Use 300 seconds from `review_requested_at` as a provisional operator timeout for
the current head. The two audited response intervals—174 seconds from ready for
#1222 and 123 seconds from explicit request for #1223—fit inside that bound, but
two observations are not enough to establish a service-level objective.

At timeout:

- set `codex_review_status=timeout`;
- set `merge_guidance=hold_for_human_decision`;
- do not infer a clean review;
- continue waiting, or use an explicit human exception for the exact current
  head.

The timeout is a bounded decision point for the operator. It is not a passing
check, reviewer substitute, approval, or automatic merge signal.

### Explicit human exception

A missing-review exception is valid audit evidence only when a human maintainer
records it on GitHub before merge and includes:

- the exact current head SHA;
- the maintainer identity;
- the UTC timestamp;
- why the Codex result is unavailable or not being awaited;
- the specific risk being accepted;
- confirmation that diff, scope, checks, comments, and threads were reviewed.

The exception does not claim that Codex reviewed the PR. It records a human
decision to proceed without that evidence. A head change invalidates the
exception.

Suggested manual record:

```text
HC-REVIEW-EXCEPTION
Head SHA: <40-character current head SHA>
Recorded at: <UTC timestamp>
Reason: <why current-head Codex evidence is unavailable>
Accepted risk: <specific risk accepted by the maintainer>
Other evidence reviewed: diff, scope, checks, comments, and threads
Decision: human maintainer will make the final merge decision
```

## Result classification

| PR | Audit classification | Reason |
| --- | --- | --- |
| #1222 | `merged_without_current_head_review_evidence` | Same-head Codex P1 arrived 15 seconds after merge; no explicit pre-merge exception was recorded. |
| #1223 | `current_head_review_evidence_present_before_merge` | Same-head Codex result was recorded 93 seconds before merge and no review thread remained open. |

These classifications describe review evidence timing only. They do not certify
the code, establish truth, or replace human judgment.

## Recommended follow-up

After human acceptance of this report, use a separate documentation-only PR to
align the existing review-window, mission-execution, lifecycle, final-reviewer,
and PR-template wording with this contract. Any workflow, permission, required
check, comment automation, reviewer request, or merge behavior change requires a
separate governance review and explicit authorization.

