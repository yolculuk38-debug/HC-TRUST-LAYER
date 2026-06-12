# Next Actions

This file lists safe, advisory next work for HC-TRUST-LAYER. Each item is REPORT ONLY unless the Founder or an authorized reviewer explicitly changes the mode.

## Operator Status Card

| Field | Status |
| --- | --- |
| Current phase | Working verification core / post-runtime stabilization |
| Active focus | Public validator and public explorer planning/navigation sequence is complete, including #820 official Public Validator MVP Specification. HC Control Bot advisory comment governance/navigation, advisory reviewer-role suggestions, roadmap synchronization, assistant-console rotation state, HC Engineer command-surface status, repository assistant baseline status, and operator-entry-map navigation are synchronized through #831. Validator pipeline nested response contract coverage is locked by #834. Verification package hash core was added in #838 and hardened in #839. |
| Next up | Docs-only synchronization after #838/#839, then a separate scoped working-core PR if authorized. The most practical next core step is a local CLI / documented entry point for `verify_verification_package`; signature/witness/QR/C2PA/OpenTimestamps layers remain later steps. |
| Blocked / parked work | Do not modify schemas, validators, workflows, governance rules, records, hashes, QR artifacts, generated artifacts, signing, federation, or policy for this next-actions list. |
| Do-not-repeat references | #628 telemetry contract sufficient; #629 replay / continuity coverage merged; #630 runtime conditionally stabilized; #631 operating layer conditionally sufficient; #820/#821/#822 completed public validator project-control state; #823/#824 completed HC Control Bot reviewer-role and roadmap state; #826 completed HC Engineer command-surface status checkpoint; #828 completed repository assistant baseline status; #831 completed operator-entry-map synchronization; #834 completed validator pipeline nested response contract test hardening; #838 completed verification package hash-core baseline; #839 completed package hash-core hardening; #812 remains active console and #763 remains historical only. |
| Review / merge rule | Before merge: verify changed files, checks, Codex/review comments, and risk scope. If comments exist, fix first. Do not merge without explicit human merge approval. |
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
14. `docs/project-control/hc-engineer-command-surface-status.md`
15. `docs/project-control/repository-assistant-baseline-status.md`

Use `docs/project-control/active-work-registry.md` only for advisory shift-level coordination; this file remains the priority queue source. If `hc_context` files are useful for orientation, read them after the markdown docs and treat them as advisory only.

## Completed public validator / public explorer planning sequence

- Public validator planning navigation was linked in #682.
- #820 added the official Public Validator MVP Specification.
- #821 synchronized navigation and project-control references so the #820 specification is the primary planner entry.
- #822 synchronized project-state and task-ledger references after #820/#821 public validator navigation.
- Public explorer navigation map was added in #683.
- Public explorer planning gap review was completed in #685.
- Public explorer maturity checklist was added in #686.
- Public explorer checklist navigation alignment was completed in #688.
- Do not create duplicate public validator or public explorer planning documents, including duplicate Public Validator MVP specification work, unless a new repository-evidence gap appears.

## Completed HC Control Bot advisory comment governance sequence

- Advisory comment boundary was documented in #701.
- Advisory comment lifecycle was documented in #794.
- Advisory comment template was documented in #795.
- Operator Entry Map linked the HC Control Bot reference chain in #796 and was refreshed after #826/#828 in #831.
- Advisory human reviewer-role suggestions were added in #823 while preserving advisory-only boundaries.
- The HC Control Bot MVP roadmap was synchronized after #823 in #824.
- Do not create duplicate bot-comment governance, lifecycle, template, navigation, reviewer-role, roadmap synchronization, or operator-entry-map bot-line synchronization documents unless new repository evidence appears.
- These documents and features do not enable independent decision authority, production readiness, certification, or truth-finality.

## Completed assistant-console and command-surface maintenance

- #811 recorded the assistant console rotation plan.
- #812 is the active HC Assistant Console v2 reference.
- #763 is closed and retained only as the historical first smoke-test trail.
- #813 synchronized `/hc status`, command tests, and active-console documentation references.
- #814 synchronized the assistant listener smoke-test checklist.
- #826 recorded the HC Engineer / HC Assistant command-surface status checkpoint.
- #828 recorded the repository assistant baseline status.
- #831 synchronized the Operator Entry Map after #826/#828 so command-surface and repository-assistant baseline references are current.
- Assistant-console rotation, command-surface status checkpointing, repository assistant baseline work, and operator-entry-map synchronization should not be repeated unless new repository evidence appears.
- This is operating-layer documentation state only; it does not create implementation work, bot authority, runtime behavior, workflow behavior, or governance finality.

## Completed validator pipeline test hardening

- #834 locked nested `ValidatorPipeline` response contract coverage for `canonical_bridge`, `schema_result`, `hash_result`, `trust_assignment`, and `escalation`.
- #834 was test-only and changed `tests/test_hc_runtime_pipeline.py`; it did not change runtime implementation, workflows, schemas, validators, records, QR/hash evidence, signing, federation, policy, generated artifacts, or trust-kernel indexes.
- Do not repeat validator pipeline nested response contract test work unless new repository evidence appears.

## Completed verification package hash core

- #838 added a local verification package hash core.
- #839 hardened that core after automated review by handling malformed manifest files without raising and enforcing resolved package-path containment before hashing.
- This core verifies local package integrity only: manifest presence, listed file existence, SHA-256 digest matches, missing evidence, conflicting evidence, advisory-only output, public-safe output, and `truth_guarantee=false`.
- It does not verify signatures, witnesses, QR authenticity, legal truth, C2PA claims, OpenTimestamps attestations, federation state, or production readiness.
- Do not repeat #838/#839 unless new repository evidence appears.

## 1. Docs-only synchronization after #838/#839

- Priority order: 1
- Mode: DOCS ONLY.
- Risk: Low, if limited to project-control documentation.
- Safe output: Project-control docs reflect #838/#839 and do-not-repeat boundaries.
- Why it is next: Project-control must match merged code/test state before the next working-core implementation slice.

## 2. Candidate next working-core PR

- Priority order: 2
- Mode: IMPLEMENTATION ONLY AFTER explicit authorization and a new scoped PR.
- Candidate: add a local CLI / documented entry point around `verify_verification_package`.
- Risk: Runtime/API/public UX claims if over-scoped; keep local-only and advisory-only.
- Safe output: a small command or documented invocation that returns the existing verifier response without changing schema, validators, records, workflow, signing, federation, policy, generated artifacts, or trust-kernel indexes.
- Why it is next: The package hash core exists; a local operator entry point makes it practically usable before signature/witness/QR/C2PA/OpenTimestamps layers.

## 3. Parked larger implementation work

- Priority order: 3
- Mode: BLOCKED unless explicitly authorized.
- Risk: Implementation expansion could affect runtime/API behavior, generated artifacts, validation semantics, public UX claims, bot boundaries, reviewer routing behavior, command-surface behavior, repository assistant behavior, or trust-kernel-adjacent surfaces.
- Parked examples: signature verification, witness authority, QR canonical-domain binding, C2PA ingestion, OpenTimestamps verification, federation, dispute/governance implementation, production-readiness claims.
- Safe output: None by default. Open a separate, explicit implementation proposal only if the Founder or authorized reviewer requests it.

## Stale-context guidance

Markdown project-control docs are authoritative for active focus, priority order, protected-path boundaries, and safe handoff state. The `hc_context` directory is advisory and should be used only after reading the markdown project-control docs. When `hc_context`, chat memory, or an external summary appears stale or inconsistent, report the mismatch and cite the repository evidence instead of resolving the conflict automatically.
