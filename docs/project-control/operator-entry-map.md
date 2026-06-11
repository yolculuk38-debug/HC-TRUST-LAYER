# Operator Entry Map

Status: advisory operating-layer guide.

## Purpose

This document helps human contributors, AI assistants, and agentic tools quickly understand the current operating state of HC-TRUST-LAYER.

## Current Position

- Post-runtime stabilization / operating-layer refinement.
- Navigation synchronization.
- Public validator planning.
- Public explorer planning.
- HC Trust Engineer command-surface planning.
- HC Control Bot advisory comment governance is documented but not enabled.

## Assistant Console

The active repository-level HC Assistant Console is Issue #812:

- https://github.com/yolculuk38-debug/HC-TRUST-LAYER/issues/812

Historical console trail:

- #763 first HC Assistant Console smoke-test trail
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
6. docs/project-control/shift-change-checklist.md
7. docs/project-control/hc-assistant-console-guide.md
8. docs/project-control/hc-trust-engineer-command-interface.md
9. docs/project-control/hc-assistant-console-issue-template.md
10. docs/terminology-audit.md

## HC Control Bot Reference Chain

For HC Control Bot / HC Trust Engineer work, read these documents before proposing new bot behavior:

1. docs/governance/hc-control-bot-authority-policy.md
2. docs/project-control/hc-control-bot-mvp-roadmap.md
3. docs/project-control/hc-control-bot-report-interpretation-guide.md
4. docs/project-control/hc-control-bot-advisory-comment-boundary.md
5. docs/governance/advisory-comment-lifecycle.md
6. docs/project-control/hc-control-bot-advisory-comment-template.md
7. scripts/hc_control_bot.py
8. tests/test_hc_control_bot.py

Current boundary:

```text
comment governance is documented
comment template is documented
comment automation is not enabled by these docs
label application is not enabled by these docs
assignment is not enabled by these docs
LLM review is not enabled by these docs
approve/reject/merge/close remains forbidden
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

- assistant console discoverability
- command-interface implementation planning
- navigation improvements
- onboarding improvements
- public validator planning
- public explorer planning
- vision documentation

## Authority Model

- Repository evidence outranks chat memory.
- AI output is advisory only.
- Human reviewers retain final authority.
