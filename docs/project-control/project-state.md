# Project State

This file is the repository-native shift handoff summary for HC-TRUST-LAYER. Every agent must read this file before proposing work.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Phase 2 — Trust Kernel Enforcement |
| Active focus | PR risk labeler Tier-1 review; safe auto-merge Tier-1 review; HC Guide Bot design; GitHub Project Board and label taxonomy; `hc_context` machine-readable state proposal |
| Next up | Follow `docs/project-control/next-actions.md` in priority order and keep listed items REPORT ONLY unless authorized otherwise. |
| Blocked / parked work | Workflow, runtime, schema, validator, record, policy, federation, signing, trust-kernel index, and governance-enforcement changes are parked unless explicitly authorized and validated. |
| Do-not-repeat references | Treat #545, #546, #547, #548, #550, and #551 as completed references; do not reuse #549 because it is closed and conflicted. |
| Protected-path reminder | Do not modify `schema/**`, `validators/**`, `federation/**`, `signatures/**`, `canonical/**`, `policy/**`, `.github/workflows/**`, `records/**`, or trust-kernel indexes unless explicitly requested. |
| Source-of-truth priority | Repository markdown docs, merged files, checks, PR evidence, and human review decisions outrank chat memory and advisory machine-readable context. |

## Current phase

Phase 2 — Trust Kernel Enforcement

## Repository status

HC-TRUST-LAYER is advisory-only, early-stage trust infrastructure. Repository evidence, merged files, checks, and human review decisions are the source of truth for current state.

## Last known completed governance sequence

- #545 verification package alignment
- #546 runtime public response contract
- #547 expanded trust-kernel protected paths
- #548 CODEOWNERS Tier-1 alignment
- #550 rate-limit advisory docs fix
- #551 governance preflight Tier-1 sync

## Closed / do not reuse

- #549 conflicted governance preflight PR

## Current focus

- PR risk labeler Tier-1 review
- safe auto-merge Tier-1 review
- HC Guide Bot design
- GitHub Project Board and label taxonomy
- `hc_context` machine-readable state proposal

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
