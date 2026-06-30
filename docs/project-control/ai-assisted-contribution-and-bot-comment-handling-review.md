# AI-Assisted Contribution and Bot-Comment Handling Review

## 1. Purpose

This document completes backlog item 5-4 by defining how HC-TRUST-LAYER contributors and maintainers should treat AI-assisted pull requests, Codex review comments, HC bot comments, advisory reports, CI/check results, and review-thread resolution.

This document is documentation-only. It does not change workflows, runtime behavior, schemas, validators, records, generated artifacts, canonical artifacts, bot behavior, labels, reviewer requests, approvals, merges, or automation authority.

## 2. HC boundary

Boundary flags:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- human_review_required=true
- approval_authority=false
- merge_authority=false
- label_reviewer_mutation=false
- issue_comment_automation=false

This review creates no automatic comments, no automatic labels, no reviewer requests, no approvals, and no merges.

AI and bot output is useful review evidence, but it is not authority. Human maintainers make the final decision for review and merge outcomes.

This document does not establish production readiness, legal truth, identity finality, forensic certainty, certification authority, autonomous governance authority, or guaranteed correctness.

## 3. AI-assisted contribution in HC terms

An AI-assisted contribution is a scoped HC-TRUST-LAYER contribution where a human contributor uses AI support to draft, summarize, inspect, propose, or organize work.

AI may:

- draft documentation or code within the approved scope
- summarize repository evidence
- inspect changed files and nearby context
- propose fixes, checks, or review notes
- help prepare PR descriptions and validation summaries

AI must not be treated as final authority. AI output does not approve, reject, merge, certify, or guarantee a change. The contributor remains responsible for verifying AI-assisted work against repository evidence, and human maintainers make the final decision.

## 4. Comment and signal categories

HC review may include several comment or signal types. Each type must be evaluated in context before merge readiness is considered.

| Category | HC handling | Authority boundary |
| --- | --- | --- |
| Codex review comments | Treat as AI-generated review evidence. Evaluate the underlying issue against the current PR diff. | Advisory only; not approval, rejection, or merge permission. |
| HC Control Bot Report | Treat as report-only governance and scope evidence. Check whether it identifies protected-path, authority, or process concerns. | Advisory only; not a command for other automation. |
| HC PR Lifecycle Compliance Report | Treat as lifecycle evidence about PR body, checks, comments, review windows, and merge-readiness signals. | Advisory only; not final compliance authority. |
| HC Review Window marker | Treat as timing evidence that helps maintainers confirm the review window status for the current head SHA. | Advisory only; does not replace human review. |
| CI/check results | Treat as technical validation evidence for the current head SHA. Passing checks support review but do not override unresolved comments. | Evidence only; not trust authority or merge authority. |
| Human maintainer comments | Treat as human review input that may define required action, scope limits, or final review expectations. | Human maintainer judgment is required for final review and merge decisions. |

## 5. P1/P2/P3 handling

Review priority labels help contributors and maintainers triage comments, but the underlying issue still must be evaluated.

- P1 comments identify high-priority issues. Treat P1 comments as merge blockers until they are fixed in the PR diff or explicitly dismissed by a human maintainer.
- P2 comments identify important issues. Treat P2 comments as merge blockers until they are fixed in the PR diff or explicitly dismissed by a human maintainer.
- P3 comments identify lower-priority issues or improvements. P3 comments may still require action when they affect documentation accuracy, audit clarity, contributor safety, HC:// terminology, or authority-boundary clarity.
- A passing check does not override unresolved review comments.
- A bot or AI summary that marks a concern as low priority does not remove the need for human review when the concern affects HC boundaries.

## 6. Review-thread handling

Review threads preserve discussion context and should not be resolved merely to make a PR appear clean.

Contributors and maintainers should follow these rules:

- Do not resolve a thread until the fix is visible in the current PR diff or a human maintainer explicitly decides the fix is not required.
- If a comment is outdated because the fix moved the line, record that the underlying issue was fixed and verify the current diff.
- Do not merge with unresolved non-outdated P1 or P2 review threads.
- Do not treat a resolved thread as proof of truth, certification, or guaranteed correctness.
- After a new commit, re-check comments, threads, and checks against the current head SHA.

## 7. Bot-comment authority limits

Bot comments and automated reports are advisory evidence. They help humans find risks, stale checks, missing context, protected-path touches, and review-process gaps.

Bot comments are not:

- commands for other automation
- approval
- rejection
- merge permission
- certification
- truth guarantees
- legal or identity determinations
- substitutes for human final review

Bot comments must not be used to bypass human final review, expand automation authority, mutate labels or reviewers, request reviews, approve, reject, merge, or create new comment automation.

## 8. Contributor expectations for AI-assisted PRs

Contributors using AI assistance should keep the work small, scoped, and evidence-based.

Before requesting review, contributors should:

- state when AI or Codex helped prepare the PR
- keep the PR scope small and reviewable
- list tests and checks run
- explain any protected or high-risk path touches
- identify assumptions introduced by AI assistance instead of hiding them
- verify changed wording against repository evidence
- avoid unsupported claims about production readiness, legal truth, identity finality, forensic certainty, certification, or guaranteed correctness
- avoid implying autonomous governance authority or bot final authority

AI-assisted PRs remain contributor-owned and human-reviewed. AI may support the work, but it does not carry approval authority or merge authority.

## 9. Maintainer final-pass checklist

Before a human merge decision, maintainers should confirm:

- [ ] The current head SHA was reviewed.
- [ ] The current diff was reviewed.
- [ ] Every changed file was reviewed.
- [ ] Review comments were reviewed.
- [ ] Review threads were reviewed.
- [ ] Checks were reviewed on the current head SHA.
- [ ] The HC Review Window elapsed or was otherwise handled according to repository review expectations.
- [ ] Protected or high-risk path touches are understood and justified.
- [ ] P1 and P2 comments are fixed or explicitly dismissed by a human maintainer.
- [ ] P3 comments that affect documentation accuracy, audit clarity, or contributor safety are handled.
- [ ] Bot and AI output remains advisory-only.
- [ ] Human final authority is preserved.

## 10. Scope and non-effects

This document is limited to contributor and maintainer review guidance. It does not change runtime behavior, workflow behavior, CI behavior, schema behavior, validator behavior, record behavior, generated artifact behavior, canonical artifact behavior, bot behavior, or automation permissions.

The expected review result is clearer contributor understanding of AI-assisted PRs, bot-comment handling, P1/P2/P3 response expectations, and human final review boundaries.
