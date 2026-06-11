# Project State

This file is the repository-native shift handoff summary for HC-TRUST-LAYER. Every agent must read this file before proposing work.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Post-runtime stabilization / operating-layer refinement |
| Active focus | Public validator / explorer planning and navigation are synchronized through #821; HC Control Bot advisory comment governance/navigation and assistant-console rotation state are synchronized. Stay in evidence-triggered REPORT ONLY mode unless new repository evidence appears. |
| Next up | Prefer docs-only navigation/index synchronization, or evidence-triggered report-only runtime, public validator/public explorer, or bot-governance follow-up only if new repository evidence appears. Do not reopen Public Validator MVP specification work after #820/#821 without new repository evidence. |
| Blocked / parked work | Workflow, runtime, schema, validator, record, policy, federation, signing, trust-kernel index, generated artifact, QR/hash, and governance-enforcement changes are parked unless explicitly authorized and validated. |
| Do-not-repeat references | Treat #628, #629, #630, #631, #682, #683, #685, #686, #688, #701, #794, #795, #796, #811, #813, #814, #820, and #821 as completed review/navigation references. #812 remains the active HC Assistant Console v2 reference; #763 remains historical only. |
| Protected-path reminder | Do not modify `schema/**`, `validators/**`, `federation/**`, `signatures/**`, `canonical/**`, `policy/**`, `.github/workflows/**`, `records/**`, generated artifacts, QR/hash evidence, or trust-kernel indexes unless explicitly requested and approved. |
| Source-of-truth priority | Repository markdown docs, merged files, checks, PR evidence, and human review decisions outrank chat memory and advisory machine-readable context. |

## Current phase

Post-runtime stabilization / operating-layer refinement.

## Repository status

HC-TRUST-LAYER is advisory-only, early-stage trust infrastructure. Repository evidence, merged files, checks, and human review decisions are the source of truth for current state. AI agents and automation are advisory only; human reviewers retain final authority, especially for trust-kernel-adjacent or protected-path work.

The `v0.1.0` tag remains the initial protected protocol infrastructure and release-candidate documentation baseline. `main` has continued beyond that tag and is the active development line.

## Last known completed stabilization sequence

- #628 telemetry contract review: TELEMETRY CONTRACT SUFFICIENT
- #629 replay / continuity edge-case coverage: merged
- #630 runtime stabilization review: RUNTIME CONDITIONALLY STABILIZED
- #631 HC Operating Layer review: OPERATING LAYER CONDITIONALLY SUFFICIENT

## Completed public validator / public explorer planning sequence

- #682 linked public validator planning navigation.
- #820 added the official documentation-only Public Validator MVP Specification.
- #821 synchronized navigation and project-control references so the #820 specification is the primary planner entry and duplicate Public Validator MVP specification work is avoided.
- #683 added the public explorer navigation map.
- #685 completed the public explorer planning gap review.
- #686 added the public explorer maturity checklist.
- #688 completed public explorer checklist navigation alignment.
- Public validator and public explorer planning should not be repeated unless new repository evidence appears.

## Completed HC Control Bot advisory comment governance sequence

- #701 documented the HC Control Bot advisory comment boundary.
- #794 documented the advisory comment lifecycle.
- #795 documented the advisory comment template.
- #796 linked the HC Control Bot reference chain in the Operator Entry Map.
- HC Control Bot scanner, advisory comment, and `/hc` command surfaces remain advisory-only and do not create approval, rejection, merge, close, label, assignment, LLM review, production-readiness, certification, or truth-finality authority.

## Recent completed assistant-console maintenance

- #811 recorded the assistant console rotation plan as completed operating-layer planning evidence.
- #812 is the active HC Assistant Console v2 reference for current assistant-console work.
- #763 is closed and retained only as the historical first smoke-test trail; do not treat it as the active console or reopen it for rotation work.
- #813 synchronized `/hc status`, command tests, and active-console documentation references with #812 as active.
- #814 synchronized the assistant listener smoke-test checklist with the current rotation state.
- #811, #813, and #814 are do-not-repeat references for assistant-console rotation synchronization unless new repository evidence appears.

## Current focus

- Keep onboarding, navigation, and project-control documents synchronized with current repository state.
- Use evidence-triggered report-only follow-up for runtime, public validator, public explorer, bot-governance, assistant-console, generated-artifact, QR/hash, or trust-kernel-adjacent questions.
- Avoid repeating public validator/public explorer planning, HC Control Bot comment governance, assistant-console rotation, telemetry contract, replay / continuity, or runtime stabilization review unless new repository evidence appears.

## Next safe task

The next safe task is a small documentation-only navigation/index synchronization or a narrow evidence-triggered REPORT ONLY review. Protected paths still require explicit approval and human-supervised validation before modification.

Recommended decision language after a navigation refresh is complete: **NAVIGATION REFRESH COMPLETE**.

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
