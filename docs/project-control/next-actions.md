# Next Actions

This file lists safe, advisory next work for HC-TRUST-LAYER. Each item is REPORT ONLY unless the Founder or an authorized reviewer explicitly changes the mode.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Post-runtime stabilization / operating-layer refinement |
| Active focus | Public validator and public explorer navigation alignment are complete; run a public explorer planning gap review without changing runtime behavior. |
| Next up | Public explorer planning gap review. |
| Blocked / parked work | Do not modify runtime, code, tests, schemas, validators, workflows, governance rules, records, hashes, QR artifacts, generated artifacts, signing, federation, or policy for this next-actions list. |
| Do-not-repeat references | #628 telemetry contract sufficient; #629 replay / continuity coverage merged; #630 runtime conditionally stabilized; #631 operating layer conditionally sufficient; public validator readiness/spec/implementation planning already exists; public validator navigation alignment completed in #682; public explorer navigation map completed in #683. Avoid repeating those reviews unless new evidence appears. |
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
10. `docs/project-control/public-explorer-navigation.md`

Use `docs/project-control/active-work-registry.md` only for advisory shift-level coordination; this file remains the priority queue source. If `hc_context` files are useful for orientation, read them after the markdown project-control docs and treat them as advisory only.

## Completed navigation alignment

- Public validator planning navigation was linked in #682.
- Public explorer navigation map was added in #683.
- Do not create duplicate public validator or public explorer planning documents unless a new repository-evidence gap appears.

## 1. Public explorer planning gap review

- Priority order: 1
- Mode: REPORT ONLY.
- Risk: Explorer, API, runtime, validator, schema, federation, signing, workflow, policy, record, hash, QR, generated-artifact, and governance-rule adjacency; keep planning advisory until explicitly authorized.
- Safe output: A concise gap review that identifies which public explorer user paths, evidence boundaries, generated-index assumptions, local/static-only assumptions, public-safe output language, and human-supervised validation points are already documented and which are missing.
- Starting evidence: `docs/project-control/public-explorer-navigation.md`, `docs/public-explorer-mvp.md`, `docs/verification-explorer-architecture.md`, `docs/explorer/README.md`, `docs/api/explorer-api-v1.md`, `docs/public-verification-routing.md`, and `docs/public-verification-boundaries.md`.
- Why it is next: Public validator and public explorer navigation alignment are now complete; the remaining adjacent question is whether the existing public explorer planning surface has clear gaps.

## 2. Evidence-triggered runtime follow-up only if needed

- Priority order: 2
- Mode: REPORT ONLY, and only if new repository evidence appears.
- Risk: Runtime and validator adjacency; do not repeat completed telemetry, replay, or runtime stabilization reviews without new evidence.
- Safe output: A narrow evidence report that cites the new trigger and explains whether further review is necessary.
- Why it is parked by default: #628, #629, and #630 already covered the recent telemetry contract, replay / continuity, and runtime stabilization sequence.

## Stale-context guidance

Markdown project-control docs are authoritative for active focus, priority order, protected-path boundaries, and safe handoff state. The `hc_context` directory is advisory and should be used only after reading the markdown control files. When `hc_context`, chat memory, or an external summary appears stale or inconsistent, report the mismatch and cite the repository evidence instead of resolving the conflict automatically.
