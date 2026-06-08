# Next Actions

This file lists safe, advisory next work for HC-TRUST-LAYER. Each item is REPORT ONLY unless the Founder or an authorized reviewer explicitly changes the mode.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Post-runtime stabilization / operating-layer refinement |
| Active focus | Public validator and public explorer planning/navigation sequence is complete. Stay in evidence-triggered report-only mode unless new repository evidence appears. |
| Next up | Evidence-triggered runtime or planning follow-up only if new evidence appears. |
| Blocked / parked work | Do not modify runtime, code, tests, schemas, validators, workflows, governance rules, records, hashes, QR artifacts, generated artifacts, signing, federation, or policy for this next-actions list. |
| Do-not-repeat references | #628 telemetry contract sufficient; #629 replay / continuity coverage merged; #630 runtime conditionally stabilized; #631 operating layer conditionally sufficient; public validator readiness/spec/implementation planning already exists; public validator navigation alignment completed in #682; public explorer navigation map completed in #683; public explorer gap review completed in #685; public explorer maturity checklist completed in #686; public explorer checklist navigation alignment completed in #688. Avoid repeating those reviews unless new evidence appears. |
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
11. `docs/project-control/public-explorer-planning-gap-review.md`
12. `docs/project-control/public-explorer-maturity-checklist.md`

Use `docs/project-control/active-work-registry.md` only for advisory shift-level coordination; this file remains the priority queue source. If `hc_context` files are useful for orientation, read them after the markdown project-control docs and treat them as advisory only.

## Completed public validator / public explorer planning sequence

- Public validator planning navigation was linked in #682.
- Public explorer navigation map was added in #683.
- Public explorer planning gap review was completed in #685.
- Public explorer maturity checklist was added in #686.
- Public explorer checklist navigation alignment was completed in #688.
- Do not create duplicate public validator or public explorer planning documents unless a new repository-evidence gap appears.

## 1. Evidence-triggered follow-up only if needed

- Priority order: 1
- Mode: REPORT ONLY, and only if new repository evidence appears.
- Risk: Runtime, validator, API, explorer, generated-artifact, and trust-kernel adjacency; do not repeat completed public validator/public explorer planning or runtime stabilization work without new evidence.
- Safe output: A narrow evidence report that cites the new trigger and explains whether further review, navigation refresh, or implementation planning is necessary.
- Why it is next: The public validator and public explorer planning/navigation sequence is complete; future work should be triggered by concrete repository evidence, not repeated planning.

## 2. Parked implementation work

- Priority order: 2
- Mode: BLOCKED unless explicitly authorized.
- Risk: Implementation expansion could affect runtime/API behavior, generated artifacts, validation semantics, public UX claims, or trust-kernel-adjacent surfaces.
- Safe output: None by default. Open a separate, explicit implementation proposal only if the Founder or authorized reviewer requests it.
- Why it is parked: Current public explorer and public validator work is documentation/planning aligned. Implementation changes require a new scoped task.

## Stale-context guidance

Markdown project-control docs are authoritative for active focus, priority order, protected-path boundaries, and safe handoff state. The `hc_context` directory is advisory and should be used only after reading the markdown control files. When `hc_context`, chat memory, or an external summary appears stale or inconsistent, report the mismatch and cite the repository evidence instead of resolving the conflict automatically.
