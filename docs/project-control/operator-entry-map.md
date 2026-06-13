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
- Local verifier example navigation status is recorded by `docs/project-control/local-verifier-example-navigation-status.md`.

## Operating Layer Quick Path

Use this path for a new human, AI assistant, or agent taking over HC:// operating-layer work. This path is advisory only; it preserves `public_safe: true`, `truth_guarantee: false`, and human final authority boundaries.

1. Current project state: [`docs/project-control/project-state.md`](project-state.md)
2. Next safe work: [`docs/project-control/next-actions.md`](next-actions.md)
3. Completed and do-not-repeat work: [`docs/project-control/task-ledger.md`](task-ledger.md)
4. Active shift coordination: [`docs/project-control/active-work-registry.md`](active-work-registry.md)
5. Navigation map and protected areas: [`docs/project-control/operator-entry-map.md`](operator-entry-map.md)
6. Active assistant console: [#812 HC Assistant Console v2](https://github.com/yolculuk38-debug/HC-TRUST-LAYER/issues/812)

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
14. docs/terminology-audit.md

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

- Humanity Chain
- İnsanlık Zinciri
- Insanlik-Zinciri
- GENESIS_BLOCK

Historical provenance records must not be silently rewritten.

## Safe Next Work

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
