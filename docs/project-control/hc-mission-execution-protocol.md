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
7. HC Trust Engineer performs a delayed second inspection before merge-ready status.
8. Feedback or failed checks trigger a scoped fix loop.
9. Merge readiness is reported to the maintainer.
10. Merge occurs only after explicit maintainer command.
11. HC Trust Engineer verifies the merged state and records the result.

## HC Review Wait Gate

This gate is documentation-only operational guidance. It does not create automation, approval authority, merge authority, labels, reviewer requests, closes, or workflow changes.

Rules:

1. When a pull request is opened or updated, record T0 as the latest head SHA observation time.
2. Do not declare merge-ready from the first quick pass.
3. Wait at least 90 seconds before final merge-readiness reporting when Codex review may still arrive.
4. After the wait, perform a second pass over:
   - pull request metadata;
   - head SHA;
   - changed files and diff scope;
   - checks and workflow conclusions;
   - pull request comments;
   - review submissions;
   - review threads and resolved state;
   - Codex comments.
5. If Codex P1/P2 feedback, failed checks, unresolved threads, or scope issues exist, do not merge and do not report merge-ready.
6. If the wait window has passed and the pull request is clean, report merge-ready to the maintainer.
7. Merge still requires explicit maintainer command.
8. After merge, wait about 30 seconds and verify:
   - pull request state is closed;
   - `merged=true`;
   - merge commit SHA is recorded;
   - no unexpected open pull request remains in the same mission scope;
   - relevant actions/checks are not showing a new blocker.

## Boundary

External suggestions are advisory only and do not create task authority.

A coding assistant may implement scoped PR work. It does not decide readiness or replace maintainer judgment.

Trust the record, not the narrative.
