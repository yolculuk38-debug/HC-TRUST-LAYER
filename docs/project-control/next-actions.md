# Next Actions

This file lists safe, advisory next work for HC-TRUST-LAYER. Each item is REPORT ONLY unless the Founder or an authorized reviewer explicitly changes the mode.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Post-runtime stabilization / operating-layer refinement |
| Active focus | Keep navigation aligned with merged vision/roadmap work; review public explorer planning gaps without changing runtime behavior. |
| Next up | Start with public validator / explorer navigation alignment, then run a public explorer planning gap review. |
| Blocked / parked work | Do not modify runtime, code, tests, schemas, validators, workflows, governance rules, records, hashes, QR artifacts, generated artifacts, signing, federation, or policy for this next-actions list. |
| Do-not-repeat references | #628 telemetry contract sufficient; #629 replay / continuity coverage merged; #630 runtime conditionally stabilized; #631 operating layer conditionally sufficient; public validator readiness/spec/implementation planning already exists. Avoid repeating those reviews unless new evidence appears. |
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

## 1. Public validator / explorer navigation alignment

- Priority order: 1
- Mode: DOCUMENTATION ONLY unless explicitly authorized otherwise.
- Risk: Low if limited to onboarding/navigation documents; do not edit protected paths or generated artifacts.
- Safe output: Navigation links that make existing public validator readiness/spec/implementation planning and public verification architecture easy to find from current entry points.
- Why it is next: Navigation refresh work and roadmap/vision linking are now merged; existing public validator planning documents should be discoverable without creating duplicate planning docs.
- Decision language: **PUBLIC VALIDATOR NAVIGATION ALIGNED**.

## 2. Public explorer planning gap review

- Priority order: 2
- Mode: REPORT ONLY.
- Risk: Explorer, API, runtime, validator, schema, federation, signing, workflow, policy, record, hash, QR, generated-artifact, and governance-rule adjacency; keep planning advisory until explicitly authorized.
- Safe output: A concise gap review that identifies which public explorer user paths, evidence boundaries, local-only assumptions, and human-supervised validation points are already documented and which are missing.
- Why it is next: Public validator planning already exists; the remaining adjacent question is whether public explorer planning is equally clear or still fragmented.

## 3. Evidence-triggered runtime follow-up only if needed

- Priority order: 3
- Mode: REPORT ONLY, and only if new repository evidence appears.
- Risk: Runtime and validator adjacency; do not repeat completed telemetry, replay, or runtime stabilization reviews without new evidence.
- Safe output: A narrow evidence report that cites the new trigger and explains whether further review is necessary.
- Why it is parked by default: #628, #629, and #630 already covered the recent telemetry contract, replay / continuity, and runtime stabilization sequence.

## Stale-context guidance

Markdown project-control docs are authoritative for active focus, priority order, protected-path boundaries, and safe handoff state. The `hc_context` directory is advisory and should be used only after reading the markdown control files. When `hc_context`, chat memory, or an external summary appears stale or inconsistent, report the mismatch and cite the repository evidence instead of resolving the conflict automatically.
