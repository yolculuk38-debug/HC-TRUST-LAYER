# Next Actions

This file lists safe, advisory next work for HC-TRUST-LAYER. Each item is REPORT ONLY unless the Founder or an authorized reviewer explicitly changes the mode.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Post-runtime stabilization / operating-layer refinement |
| Active focus | Public explorer planning gap review and maturity checklist are complete; align navigation so the checklist is discoverable without changing runtime behavior. |
| Next up | Public explorer checklist navigation alignment. |
| Blocked / parked work | Do not modify runtime, code, tests, schemas, validators, workflows, governance rules, records, hashes, QR artifacts, generated artifacts, signing, federation, or policy for this next-actions list. |
| Do-not-repeat references | #628 telemetry contract sufficient; #629 replay / continuity coverage merged; #630 runtime conditionally stabilized; #631 operating layer conditionally sufficient; public validator readiness/spec/implementation planning already exists; public validator navigation alignment completed in #682; public explorer navigation map completed in #683; public explorer gap review completed in #685; public explorer maturity checklist completed in #686. Avoid repeating those reviews unless new evidence appears. |
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

## Completed public explorer planning sequence

- Public validator planning navigation was linked in #682.
- Public explorer navigation map was added in #683.
- Public explorer planning gap review was completed in #685.
- Public explorer maturity checklist was added in #686.
- Do not create duplicate public validator or public explorer planning documents unless a new repository-evidence gap appears.

## 1. Public explorer checklist navigation alignment

- Priority order: 1
- Mode: DOCUMENTATION ONLY.
- Risk: Low if limited to navigation references; do not edit runtime, APIs, generated artifacts, protected paths, or implementation behavior.
- Safe output: Make `docs/project-control/public-explorer-planning-gap-review.md` and `docs/project-control/public-explorer-maturity-checklist.md` discoverable from appropriate navigation surfaces such as `docs/project-control/public-explorer-navigation.md`, `docs/START_HERE.md`, or related project-control docs.
- Why it is next: The gap review and maturity checklist now exist, but the navigation map may not yet reference the maturity checklist.
- Decision language: **PUBLIC EXPLORER CHECKLIST NAVIGATION ALIGNED**.

## 2. Evidence-triggered runtime follow-up only if needed

- Priority order: 2
- Mode: REPORT ONLY, and only if new repository evidence appears.
- Risk: Runtime and validator adjacency; do not repeat completed telemetry, replay, runtime stabilization, public validator planning, public explorer gap review, or public explorer maturity checklist work without new evidence.
- Safe output: A narrow evidence report that cites the new trigger and explains whether further review is necessary.
- Why it is parked by default: #628, #629, and #630 already covered the recent telemetry contract, replay / continuity, and runtime stabilization sequence.

## Stale-context guidance

Markdown project-control docs are authoritative for active focus, priority order, protected-path boundaries, and safe handoff state. The `hc_context` directory is advisory and should be used only after reading the markdown control files. When `hc_context`, chat memory, or an external summary appears stale or inconsistent, report the mismatch and cite the repository evidence instead of resolving the conflict automatically.
