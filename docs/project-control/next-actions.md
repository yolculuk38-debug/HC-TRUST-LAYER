# Next Actions

This file lists safe, advisory next work for HC-TRUST-LAYER. Each item is REPORT ONLY unless the Founder or an authorized reviewer explicitly changes the mode.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Phase 2 — Trust Kernel Enforcement |
| Active focus | Follow the five REPORT ONLY items below in priority order. |
| Next up | Start with PR risk labeler Tier-1 sync review, then safe auto-merge Tier-1 restriction review. |
| Blocked / parked work | Any workflow, runtime, schema, validator, record, policy, federation, signing, trust-kernel index, or governance-enforcement change remains out of scope for this next-actions list. |
| Do-not-repeat references | Cross-check `docs/project-control/project-state.md` and `docs/project-control/task-ledger.md` before proposing work related to #545 through #551. |
| Protected-path reminder | Treat protected paths as read-only in REPORT ONLY mode unless explicit authorization changes the mode. |
| Source-of-truth priority | Markdown project-control docs and repository evidence outrank `hc_context`, chat memory, and advisory summaries. |

## Shift-change read order

Before taking the next action, read:

1. `AGENTS.md`
2. `HC_BOOTSTRAP.md`
3. `docs/project-control/project-state.md`
4. `docs/project-control/agent-operating-model.md`
5. `docs/project-control/task-ledger.md`
6. `docs/project-control/next-actions.md`
7. `docs/project-control/active-work-registry.md`
8. `docs/project-control/shift-change-checklist.md`

Use `docs/project-control/active-work-registry.md` only for advisory shift-level coordination; this file remains the priority queue source. If `hc_context` files are useful for orientation, read them after the markdown project-control docs and treat them as advisory only.

## 1. PR risk labeler Tier-1 sync review

- Priority order: 1
- Mode: REPORT ONLY
- Risk: Governance-enforcement and protected path adjacency; do not modify workflow, policy, script, CODEOWNERS, or trust-kernel index files.
- Allowed inspection scope: Repository documentation, project-control files, existing PR references, current workflow descriptions, risk-labeling documentation, and public repository metadata available to the operator.
- Why it is next: The project-state handoff identifies PR risk labeler Tier-1 review as an active focus, and report-only review can surface gaps without introducing workflow behavior.

## 2. Safe auto-merge Tier-1 restriction review

- Priority order: 2
- Mode: REPORT ONLY
- Risk: Governance-enforcement and merge-control adjacency; do not modify workflows, branch protection, policy, CODEOWNERS, or automation behavior.
- Allowed inspection scope: Repository documentation, project-control files, existing governance notes, safe auto-merge documentation, and current PR or check evidence visible to the operator.
- Why it is next: Tier-1 restriction review supports protected path boundary clarity while preserving advisory-only semantics and avoiding autonomous governance claims.

## 3. HC Guide Bot design review

- Priority order: 3
- Mode: REPORT ONLY
- Risk: Agent operating model and onboarding guidance; avoid uncontrolled architecture expansion or bot capability claims.
- Allowed inspection scope: Repository documentation, project-control files, agent workspace references, HC Control Panel direction, and existing guide or onboarding documents.
- Why it is next: A future HC Guide Bot can improve shift guide and onboarding consistency if its design remains advisory and repository-state based.

## 4. GitHub Project Board and label taxonomy plan

- Priority order: 4
- Mode: REPORT ONLY
- Risk: Governance organization and contributor routing; do not introduce automation, workflow behavior, or policy enforcement.
- Allowed inspection scope: Repository documentation, project-control files, current issue or label references available to the operator, and governance planning documents.
- Why it is next: A label taxonomy and board plan can clarify work order routing, task status, and do-not-repeat rules without changing protected paths.

## 5. `hc_context` machine-readable state proposal

- Priority order: 5
- Mode: REPORT ONLY
- Risk: Machine-readable project memory adjacency; do not create schema, validator, protocol graph, verification map, trust-kernel index, or canonical record changes in this mode.
- Allowed inspection scope: Repository documentation, project-control files, machine-readable index documentation, verification map documentation, protocol graph documentation, and agent context references.
- Why it is next: A future TREX-like `hc_context` JSON proposal can support cross-checking, task barcodes, and shift handoff summaries, but it must remain a proposal until reviewed through human-supervised validation.

## Stale-context guidance

Markdown project-control docs are authoritative for active focus, priority order, protected-path boundaries, and safe handoff state. The `hc_context` directory is advisory and should be used only after reading the markdown control files. When `hc_context`, chat memory, or an external summary appears stale or inconsistent, report the mismatch and cite the repository evidence instead of resolving the conflict automatically.
