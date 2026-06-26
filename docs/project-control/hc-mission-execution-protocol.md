# HC Mission Execution Protocol

Status: documentation-only project-control protocol.

Issue reference: #1109 HC Mission Control / Active Task Queue.

This document defines how HC-TRUST-LAYER turns a maintainer request into a small, reviewable pull request sequence while keeping final authority with the human maintainer.

## Coordination surfaces

- #1109: Mission Control / Active Task Queue.
- #812: public `/hc` advisory command console.
- #1082: HC Signal Watch console.

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

## Boundary

External suggestions are advisory only and do not create task authority.

A coding assistant may implement scoped PR work. It does not decide readiness or replace maintainer judgment.

Trust the record, not the narrative.
