# Next Actions

This file lists safe, advisory next work for HC-TRUST-LAYER. Each item is REPORT ONLY unless the Founder or an authorized reviewer explicitly changes the mode.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Post-runtime stabilization / operating-layer refinement |
| Active focus | Synchronize repository navigation with current state; plan public validator / explorer direction. |
| Next up | Start with docs-only navigation/index refresh, then public validator / explorer planning. |
| Blocked / parked work | Do not modify runtime, code, tests, schemas, validators, workflows, governance rules, records, hashes, QR artifacts, generated artifacts, signing, federation, or policy for this next-actions list. |
| Do-not-repeat references | #628 telemetry contract sufficient; #629 replay / continuity coverage merged; #630 runtime conditionally stabilized; #631 operating layer conditionally sufficient. Avoid repeating those reviews unless new evidence appears. |
| Protected-path reminder | Protected paths still require explicit approval and human-supervised validation before modification. |
| Source-of-truth priority | Markdown project-control docs and repository evidence outrank `hc_context`, chat memory, and advisory summaries. AI output is advisory only; human reviewers retain final authority. |

## Shift-change read order

Before taking the next action, read:

1. `AGENTS.md`
2. `HC_BOOTSTRAP.md`
3. `docs/START_HERE.md`
4. `docs/project-control/project-state.md`
5. `docs/project-control/agent-operating-model.md`
6. `docs/project-control/task-ledger.md`
7. `docs/project-control/next-actions.md`
8. `docs/project-control/active-work-registry.md`
9. `docs/project-control/shift-change-checklist.md`

Use `docs/project-control/active-work-registry.md` only for advisory shift-level coordination; this file remains the priority queue source. If `hc_context` files are useful for orientation, read them after the markdown project-control docs and treat them as advisory only.

## 1. Navigation / index synchronization

- Priority order: 1
- Mode: DOCUMENTATION ONLY unless explicitly authorized otherwise.
- Risk: Low if limited to onboarding/navigation documents; do not edit protected paths or generated artifacts.
- Safe output: Clear entry path linking `README.md`, `docs/START_HERE.md`, `docs/project-control/project-state.md`, and this file.
- Why it is next: #631 identified navigation / current-state synchronization as the primary remaining gap after the operating-layer review.
- Decision language: **NAVIGATION REFRESH COMPLETE**.

## 2. Public validator / explorer planning

- Priority order: 2
- Mode: REPORT ONLY.
- Risk: Runtime, validator, schema, federation, signing, workflow, policy, record, hash, QR, generated-artifact, and governance-rule adjacency; keep planning advisory until explicitly authorized.
- Safe output: A concise plan that identifies user paths, evidence boundaries, local-only processing assumptions where possible, and human-supervised validation points.
- Why it is next: Public validator / explorer planning can improve the repository entry path without changing verification behavior.

## 3. Evidence-triggered runtime follow-up only if needed

- Priority order: 3
- Mode: REPORT ONLY, and only if new repository evidence appears.
- Risk: Runtime and validator adjacency; do not repeat completed telemetry, replay, or runtime stabilization reviews without new evidence.
- Safe output: A narrow evidence report that cites the new trigger and explains whether further review is necessary.
- Why it is parked by default: #628, #629, and #630 already covered the recent telemetry contract, replay / continuity, and runtime stabilization sequence.

## Stale-context guidance

Markdown project-control docs are authoritative for active focus, priority order, protected-path boundaries, and safe handoff state. The `hc_context` directory is advisory and should be used only after reading the markdown control files. When `hc_context`, chat memory, or an external summary appears stale or inconsistent, report the mismatch and cite the repository evidence instead of resolving the conflict automatically.
