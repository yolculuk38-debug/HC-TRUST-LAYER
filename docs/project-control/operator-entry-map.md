# Operator Entry Map

Status: advisory operating-layer guide.

## Purpose

This document helps human contributors, AI assistants, and agentic tools quickly understand the current operating state of HC-TRUST-LAYER.

## Current Position

- Post-runtime stabilization / operating-layer refinement.
- Navigation synchronization after #820 official Public Validator MVP Specification.
- Public validator planning is documented; specification work should not be reopened without new repository evidence.
- Public explorer planning is documented.
- HC Trust Engineer command surface is implemented as a narrow deterministic `/hc` command interface and recorded by the #826 status checkpoint.
- Repository assistant baseline status is recorded by #828.
- HC Control Bot advisory observation and reviewer-role suggestion behavior is implemented as advisory-only operating-layer support.
- HC Council local report-only runner, command parser, fixture bridge, and usage guidance are completed through #1203; council output remains advisory and human-reviewed.
- The legacy QR compatibility bridge repair is completed through #1209 and preserves the archived canonical hash without making the bridge canonical evidence.
- Local verifier example navigation status is recorded by `docs/project-control/local-verifier-example-navigation-status.md`.
- Repository cleanup phase 1 mapping is completed and recorded by `docs/project-control/repository-cleanup-phase1-checkpoint-2026-06-16.md`.
- The complete remote branch snapshot is recorded by `docs/project-control/remote-branch-inventory-2026-07-22.md`; destructive deletion remains parked.

## Operating Layer Quick Path

Use this path for a new human, AI assistant, or agent taking over HC:// operating-layer work. This path is advisory only; it preserves `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, and human final authority boundaries. CI/checks are evidence, not trust authority. Generated artifacts are advisory evidence, not canonical records.

## Cleanup Navigation Note

For repository cleanup work, use [`repository-cleanup-audit-2026-06-15.md`](repository-cleanup-audit-2026-06-15.md) as the cleanup source-of-truth, [`repository-structure-triage-2026-06-16.md`](repository-structure-triage-2026-06-16.md) for root/docs/test structure classification, [`repository-index-chain-2026-06-16.md`](repository-index-chain-2026-06-16.md) for the completed purpose-index chain, [`repository-cleanup-phase1-checkpoint-2026-06-16.md`](repository-cleanup-phase1-checkpoint-2026-06-16.md) for phase 1 completion, [`remote-branch-inventory-2026-07-22.md`](remote-branch-inventory-2026-07-22.md) for the complete branch snapshot, [`next-actions.md`](next-actions.md) for active shift work, [`project-state.md`](project-state.md) for current project state, and [`task-ledger.md`](task-ledger.md) for milestone history. Use GitHub PR history for detailed completed PR history.

Cleanup candidates are advisory only. They are not permission to delete files, close issues, delete branches, disable workflows, move files, rename files, archive files, or change repository authority. Issues #812, #1082, and #1109 are intentional operator surfaces and remain active unless explicitly superseded by human review.

Cleanup sequence status:

A. docs navigation cleanup — completed by #994.
B. report-only test duplicate inventory — completed by #995.
C. report-only workflow cleanup recommendation — completed by #996.
D. issue cleanup — classified. #812 is the assistant command console, #1082 is the Signal Watch notification console, and #1109 is Mission Control / Active Task Queue. They are not cleanup candidates.
E. complete branch-list triage — evidence-complete in `remote-branch-inventory-2026-07-22.md`: 76 deletion candidates and 36 hold branches, with no deletion performed. Any destructive batch requires fresh evidence, an exact list, explicit human approval, and post-action audit.


1. Current project state: [`docs/project-control/project-state.md`](project-state.md)
2. Next safe work: [`docs/project-control/next-actions.md`](next-actions.md)
3. Completed and do-not-repeat work: [`docs/project-control/task-ledger.md`](task-ledger.md)
4. Active shift coordination: [`docs/project-control/active-work-registry.md`](active-work-registry.md)
5. Navigation map and protected areas: [`docs/project-control/operator-entry-map.md`](operator-entry-map.md)
6. Repository structure triage: [`docs/project-control/repository-structure-triage-2026-06-16.md`](repository-structure-triage-2026-06-16.md)
7. Repository index chain: [`docs/project-control/repository-index-chain-2026-06-16.md`](repository-index-chain-2026-06-16.md)
8. Cleanup phase 1 checkpoint: [`docs/project-control/repository-cleanup-phase1-checkpoint-2026-06-16.md`](repository-cleanup-phase1-checkpoint-2026-06-16.md)
9. HC Trust Engineer operating loop: [`docs/project-control/hc-trust-engineer-operating-loop.md`](hc-trust-engineer-operating-loop.md)
10. HC Trust Engineer operating loop output contract: [`docs/project-control/hc-trust-engineer-operating-loop-output-contract.md`](hc-trust-engineer-operating-loop-output-contract.md)
11. HC Trust Engineer local emitter implementation plan: [`docs/project-control/hc-trust-engineer-local-emitter-plan.md`](hc-trust-engineer-local-emitter-plan.md)
12. HC Trust Engineer local emitter quickstart: [`docs/project-control/hc-trust-engineer-local-emitter-quickstart.md`](hc-trust-engineer-local-emitter-quickstart.md)
13. Governance evidence review checklist: [`docs/project-control/governance-evidence-review-checklist.md`](governance-evidence-review-checklist.md)
14. Governance evidence review handoff: [`docs/project-control/governance-evidence-review-handoff.md`](governance-evidence-review-handoff.md)
15. Evidence artifact inspection guide: [`docs/project-control/evidence-artifact-inspection-guide.md`](evidence-artifact-inspection-guide.md)
16. Active assistant console: [#812 HC Assistant Console v2](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/issues/812)
17. Signal Watch notification console: [#1082 HC Signal Watch Console](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/issues/1082)
18. Mission coordination queue: [#1109 HC Mission Control / Active Task Queue](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/issues/1109)
19. Complete remote branch snapshot: [`docs/project-control/remote-branch-inventory-2026-07-22.md`](remote-branch-inventory-2026-07-22.md)

Do not repeat #811, #813, #814, #826, #828, or assistant-console / command-surface / repository-assistant-baseline synchronization work unless new repository evidence appears. Treat #763 as closed historical evidence only.

## Assistant Console

The active repository-level HC Assistant Console is Issue #812:

- https://github.com/yolculuk38-debug/HC-TRUST-LAYER/issues/812

Historical console trail:

- #763 first HC Assistant Console smoke-test trail; closed and historical only, not active, not to be reopened for this rotation.
- https://github.com/yolculuk38-debug/HC-TRUST-LAYER/issues/763

Use it for project-level `/hc` commands such as:

```text
/hc help
/hc status
/hc next
```

For task coordination, use the claim and queue extension in [`docs/project-control/hc-task-handoff-queue.md`](hc-task-handoff-queue.md) as an advisory-only reference before opening duplicate work.

Use pull request comments for PR-specific commands such as:

```text
/hc review
/hc risks
/hc evidence
```

Boundary: advisory only. Human maintainers retain final authority.

## Read Order

1. AGENTS.md
2. HC_BOOTSTRAP.md
3. docs/START_HERE.md
4. docs/project-control/project-state.md
5. docs/project-control/next-actions.md
6. docs/project-control/public-validator-mvp-specification.md
7. docs/project-control/shift-change-checklist.md
8. docs/project-control/hc-assistant-console-guide.md
9. docs/project-control/hc-trust-engineer-command-interface.md
10. docs/project-control/hc-engineer-command-surface-status.md
11. docs/project-control/repository-assistant-baseline-status.md
12. docs/project-control/local-verifier-example-navigation-status.md
13. docs/project-control/hc-assistant-console-issue-template.md
14. docs/project-control/governance-evidence-review-checklist.md
15. docs/project-control/governance-evidence-review-handoff.md
16. docs/project-control/evidence-artifact-inspection-guide.md
17. docs/project-control/repository-structure-triage-2026-06-16.md
18. docs/project-control/repository-index-chain-2026-06-16.md
19. docs/project-control/repository-cleanup-phase1-checkpoint-2026-06-16.md
20. docs/terminology-audit.md

## Public Validator Planning Reference

The official documentation-only Public Validator MVP Specification is [`docs/project-control/public-validator-mvp-specification.md`](public-validator-mvp-specification.md), added by #820. Treat older readiness review, MVP contract, and implementation planning documents as supporting references; do not reopen duplicate Public Validator MVP specification work unless new repository evidence appears.

Boundary: advisory only, `public_safe: true`, `truth_guarantee: false`, local-only first where possible, and human reviewers retain final authority. This planning reference does not enable production hosting, backend readiness, legal/security certification, forensic certainty, truth verification, runtime behavior, validator changes, workflow changes, or autonomous governance authority.

## HC Control Bot Reference Chain

For HC Control Bot / HC Trust Engineer work, read these documents before proposing new bot behavior:

1. docs/governance/hc-control-bot-authority-policy.md
2. docs/project-control/hc-control-bot-mvp-roadmap.md
3. docs/project-control/hc-control-bot-report-interpretation-guide.md
4. docs/project-control/hc-control-bot-advisory-comment-boundary.md
5. docs/governance/advisory-comment-lifecycle.md
6. docs/project-control/hc-control-bot-advisory-comment-template.md
7. docs/project-control/hc-trust-engineer-command-interface.md
8. docs/project-control/hc-engineer-command-surface-status.md
9. docs/project-control/repository-assistant-baseline-status.md
10. scripts/hc_control_bot.py
11. tests/test_hc_control_bot.py

Current boundary:

```text
advisory observation is enabled
reviewer-role suggestions are advisory only
command surface is deterministic and narrow
repository assistant baseline is documentation-only
label application is not enabled by these docs
assignment is not enabled by these docs
LLM review is not enabled by these docs
human maintainers retain final authority
```

## Protected Areas

Do not modify without explicit approval:

- schema/**
- validators/**
- records/**
- signatures/**
- federation/**
- policy/**
- canonical/**
- .github/workflows/**

## Terminology Boundary

Active:

- HC://
- HC-TRUST-LAYER
- HC Trust Layer

Historical:

- legacy source project
- legacy source repository
- legacy-archive-repo
- Project Origin Record

Historical provenance records must not be silently rewritten.

## Safe Next Work

- phase 2 cleanup work only if small, reversible, and evidence-backed
- assistant console discoverability only if new evidence appears
- command-surface follow-up only if new evidence appears
- repository assistant baseline follow-up only if new evidence appears
- local verifier example navigation only when repository evidence changes
- navigation improvements
- onboarding improvements
- public validator navigation refreshes only when repository evidence changes
- public explorer planning
- vision documentation

## Authority Model

- Repository evidence outranks chat memory.
- AI output is advisory only.
- Human reviewers retain final authority.
