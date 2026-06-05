# Project State

This file is the repository-native shift handoff summary for HC-TRUST-LAYER. Every agent must read this file before proposing work.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Post-runtime stabilization / operating-layer refinement |
| Active focus | Navigation / current-state synchronization; public validator / explorer planning. |
| Next up | Prefer docs-only navigation/index refresh or public validator / explorer planning. Avoid repeating telemetry, replay, or runtime review unless new evidence appears. |
| Blocked / parked work | Workflow, runtime, schema, validator, record, policy, federation, signing, trust-kernel index, and governance-enforcement changes are parked unless explicitly authorized and validated. |
| Do-not-repeat references | Treat #628, #629, #630, and #631 as recent completed review references for the current stabilization sequence. |
| Protected-path reminder | Do not modify `schema/**`, `validators/**`, `federation/**`, `signatures/**`, `canonical/**`, `policy/**`, `.github/workflows/**`, `records/**`, or trust-kernel indexes unless explicitly requested and approved. |
| Source-of-truth priority | Repository markdown docs, merged files, checks, PR evidence, and human review decisions outrank chat memory and advisory machine-readable context. |

## Current phase

Post-runtime stabilization / operating-layer refinement.

## Repository status

HC-TRUST-LAYER is advisory-only, early-stage trust infrastructure. Repository evidence, merged files, checks, and human review decisions are the source of truth for current state. AI agents and automation are advisory only; human reviewers retain final authority, especially for trust-kernel-adjacent or protected-path work.

## Last known completed stabilization sequence

- #628 telemetry contract review: TELEMETRY CONTRACT SUFFICIENT
- #629 replay / continuity edge-case coverage: merged
- #630 runtime stabilization review: RUNTIME CONDITIONALLY STABILIZED
- #631 HC Operating Layer review: OPERATING LAYER CONDITIONALLY SUFFICIENT

## Current focus

- Keep onboarding and navigation documents synchronized with the current project state.
- Plan public validator / explorer work without making runtime, validator, schema, federation, signing, policy, workflow, record, hash, QR, generated artifact, or governance-rule changes.
- Avoid repeating telemetry contract, replay / continuity, or runtime stabilization review unless new repository evidence appears.

## Next safe task

The next safe task is a small documentation-only navigation/index synchronization or a report-only public validator / explorer planning pass. Protected paths still require explicit approval and human-supervised validation before modification.

Recommended decision language after the navigation refresh is complete: **NAVIGATION REFRESH COMPLETE**.

## Shift-change checklist

Use `docs/project-control/shift-change-checklist.md` for the full operator handoff checklist. Minimum handoff steps are:

1. Read the project-control files in the documented order before proposing work.
2. Reconcile current state against repository evidence, changed files, recent commits or PRs, checks, and task-ledger notes.
3. Check in with role, scope, intended files, protected-path assessment, expected checks, and any evidence gaps.
4. Use `docs/project-control/active-work-registry.md` only as an advisory shift-level coordination snapshot when active, blocked, parked, or checkout status needs to be recorded.
5. Check out with changed files, commit or PR references when available, checks run, unresolved gaps, and next safe action.
6. Attach an evidence bundle that includes task reference, changed files, checks, review notes when available, and stale-context observations.

## Stale-context guidance

Markdown project-control docs are authoritative for shift handoff, current focus, safe next work, and do-not-repeat boundaries. The `hc_context` directory is advisory agent context and may lag behind markdown docs, merged files, checks, PR records, protected indexes, or human review decisions. If `hc_context` or chat memory conflicts with markdown project-control docs or other repository evidence, report the mismatch in the handoff notes instead of resolving or rewriting state automatically.

## Operating rule

Every agent must read this file before proposing work. Do not rely on chat memory alone, and do not repeat merged, superseded, abandoned, or closed work.
