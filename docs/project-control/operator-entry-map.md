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

## Assistant Console

The repository-level HC Assistant Console is Issue #763:

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
