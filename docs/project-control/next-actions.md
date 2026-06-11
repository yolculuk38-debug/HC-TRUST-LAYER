# Next Actions

This file lists safe, advisory next work for HC-TRUST-LAYER. Each item is REPORT ONLY unless the Founder or an authorized reviewer explicitly changes the mode.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Post-runtime stabilization / operating-layer refinement |
| Active focus | Public validator and public explorer planning/navigation sequence is complete. HC Control Bot advisory comment governance/navigation and assistant-console rotation state are synchronized. Stay in evidence-triggered report-only mode unless new repository evidence appears. |
| Next up | Docs-only navigation/index synchronization, or evidence-triggered report-only runtime, public validator/public explorer, or bot-governance follow-up only if new repository evidence appears. |
| Blocked / parked work | Do not modify runtime, code, tests, schemas, validators, workflows, governance rules, records, hashes, QR artifacts, generated artifacts, signing, federation, or policy for this next-actions list. |
| Do-not-repeat references | #628 telemetry contract sufficient; #629 replay / continuity coverage merged; #630 runtime conditionally stabilized; #631 operating layer conditionally sufficient; public validator readiness/spec/implementation planning already exists; public validator navigation alignment completed in #682; public explorer navigation map completed in #683; public explorer gap review completed in #685; public explorer maturity checklist completed in #686; public explorer checklist navigation alignment completed in #688; HC Control Bot advisory comment boundary/lifecycle/template/navigation are covered by #701, #794, #795, and #796; assistant-console rotation plan/status/docs/tests/checklist sync is covered by #811, #813, and #814, with #812 active and #763 historical only. Avoid repeating those reviews unless new repository evidence appears. |
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
13. `docs/project-control/operator-entry-map.md`

Use `docs/project-control/active-work-registry.md` only for advisory shift-level coordination; this file remains the priority queue source. If `hc_context` files are useful for orientation, read them after the markdown project-control docs and treat them as advisory only.

## Completed public validator / public explorer planning sequence

- Public validator planning navigation was linked in #682.
- Public explorer navigation map was added in #683.
- Public explorer planning gap review was completed in #685.
- Public explorer maturity checklist was added in #686.
- Public explorer checklist navigation alignment was completed in #688.
- Do not create duplicate public validator or public explorer planning documents unless a new repository-evidence gap appears.

## Completed HC Control Bot advisory comment governance sequence

- Advisory comment boundary was documented in #701.
- Advisory comment lifecycle was documented in #794.
- Advisory comment template was documented in #795.
- Operator Entry Map linked the HC Control Bot reference chain in #796.
- Do not create duplicate bot-comment governance, lifecycle, template, or navigation documents unless new repository evidence appears.
- These documents do not enable comment automation, label application, assignment, LLM review, approval, rejection, merge, or close behavior.

## Completed assistant-console rotation maintenance

- #811 recorded the assistant console rotation plan.
- #812 is the active HC Assistant Console v2 reference.
- #763 is closed and retained only as the historical first smoke-test trail.
- #813 synchronized `/hc status`, command tests, and active-console documentation references.
- #814 synchronized the assistant listener smoke-test checklist.
- Assistant-console rotation should not be repeated unless new repository evidence appears.
- This is operating-layer documentation state only; it does not create implementation work, bot authority, labels, assignments, runtime behavior, workflow behavior, or governance finality.

## 1. Evidence-triggered follow-up only if needed

- Priority order: 1
- Mode: REPORT ONLY, and only if new repository evidence appears.
- Risk: Runtime, validator, API, explorer, generated-artifact, bot-governance, assistant-console, and trust-kernel adjacency; do not repeat completed public validator/public explorer planning, runtime stabilization work, HC Control Bot comment governance work, or assistant-console rotation work without new evidence.
- Safe output: A narrow evidence report that cites the new trigger and explains whether further review, navigation refresh, or implementation planning is necessary.
- Why it is next: The public validator, public explorer, HC Control Bot advisory comment governance/navigation, and assistant-console rotation sequences are complete; future work should be docs-only navigation/index synchronization or triggered by concrete repository evidence, not repeated planning.

## 2. Parked implementation work

- Priority order: 2
- Mode: BLOCKED unless explicitly authorized.
- Risk: Implementation expansion could affect runtime/API behavior, generated artifacts, validation semantics, public UX claims, bot authority boundaries, or trust-kernel-adjacent surfaces.
- Safe output: None by default. Open a separate, explicit implementation proposal only if the Founder or authorized reviewer requests it.
- Why it is parked: Current public explorer, public validator, HC Control Bot comment, and assistant-console rotation work is documentation/planning aligned. Implementation changes require a new scoped task.

## Stale-context guidance

Markdown project-control docs are authoritative for active focus, priority order, protected-path boundaries, and safe handoff state. The `hc_context` directory is advisory and should be used only after reading the markdown control files. When `hc_context`, chat memory, or an external summary appears stale or inconsistent, report the mismatch and cite the repository evidence instead of resolving the conflict automatically.
