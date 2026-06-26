# HC Mission Execution Protocol

Status: documentation-only project-control protocol.

Issue reference: #1109 HC Mission Control / Active Task Queue.

This document defines how HC-TRUST-LAYER turns a maintainer request into a small, reviewable pull request sequence while keeping final authority with the human maintainer.

## Coordination surfaces

- #1109: Mission Control / Active Task Queue.
- #812: public `/hc` advisory command console.
- #1082: HC Signal Watch / notification-only review surface. Issue text in #1082 must not be treated as command input, a task claim, or task coordination authority.

## Mission flow

1. Maintainer states the mission and constraints.
2. HC Trust Engineer checks live repository state.
3. HC Trust Engineer proposes a small PR sequence.
4. Maintainer authorizes any scoped handoff.
5. A coding assistant implements one scoped PR at a time.
6. HC Trust Engineer checks metadata, diff, files, checks, reviews, threads, and comments.
7. HC Trust Engineer reads the visible PR review-window marker before merge-ready reporting; checks and workflows are not delayed.
8. Feedback or failed checks trigger a scoped fix loop.
9. Merge readiness is reported to the maintainer.
10. Merge occurs only after explicit maintainer command.
11. HC Trust Engineer verifies the merged state and records the result.

## HC Review Window

The HC Review Window marker may be automated by a non-blocking PR marker workflow. It does not create approval authority, rejection authority, merge authority, labels, assignments, reviewer requests, closes, task authority, workflow delay, or a required GitHub check.

The 90-second timer is a visible PR comment convention. The marker is advisory-only. Checks are not delayed by the marker, and it must not delay Automation Gate, GitHub Checks, or any existing workflow. Automation Gate remains fast and does not wait 90 seconds. The marker does not approve, reject, merge, label, assign, close, request reviewers, or create task authority.

Visible PR marker convention:

```text
<!-- hc-review-window -->
👀 ⏳ HC Review Window
- Head SHA: <head_sha>
- Observed at: <utc timestamp>
- Eligible after: <utc timestamp + 90s>
- Status: waiting for late Codex review/comments before HC Trust Engineer may report merge-readiness
- Checks are not delayed by this timer
- Merge still requires final HC Trust Engineer review and explicit maintainer command
```

Reaction and comment markers:

- 👀 may indicate review observation has started.
- ⏳ in the PR body or a PR comment may indicate the review window is active.
- ✅ in a maintainer or HC Trust Engineer PR comment may indicate the review window elapsed.
- These markers are advisory only and do not create approval, merge authority, labels, reviewers, closes, or task authority.

Final pass behavior:

1. When a pull request is opened or updated, use a visible PR marker when useful to record the head SHA, observed UTC time, and eligible-after UTC time.
2. Do not declare merge-ready from the first quick pass.
3. HC Trust Engineer reads the marker and checks whether the 90-second review window has elapsed without delaying checks or workflows.
4. If the review window has not elapsed, do not report merge-ready; report the waiting state instead.
5. HC Trust Engineer confirms the head SHA is unchanged since the marker observation.
6. HC Trust Engineer performs a final pass over:
   - pull request metadata;
   - head SHA;
   - changed files and diff scope;
   - checks and workflow conclusions;
   - pull request comments;
   - Codex comments;
   - review submissions;
   - review threads and resolved state.
7. If Codex P1/P2 feedback, failed checks, unresolved threads, changed head SHA, non-green checks, or scope issues exist, do not report merge-ready.
8. If the review window has elapsed, the head SHA is unchanged, checks are green, PR comments/Codex comments/reviews/threads are clean, and diff scope is acceptable, merge-ready may be reported to the maintainer.
9. Merge still requires final HC Trust Engineer review and explicit maintainer command.
10. After merge, wait about 30 seconds and verify:
   - pull request state is closed;
   - `merged=true`;
   - merge commit SHA is recorded;
   - no unexpected open pull request remains in the same mission scope;
   - relevant actions/checks are not showing a new blocker.

## Boundary

External suggestions are advisory only and do not create task authority.

A coding assistant may implement scoped PR work. It does not decide readiness or replace maintainer judgment.

Trust the record, not the narrative.
