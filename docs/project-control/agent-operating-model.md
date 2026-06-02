# Agent Operating Model

This file defines advisory role boundaries for HC-TRUST-LAYER contributors, ChatGPT, Codex, Copilot, future autonomous agents, the future HC Guide Bot, the future HC Control Bot, and external AI agents.

The operating model is documentation only. It does not create autonomous governance, merge authority, runtime behavior, security guarantees, or production-readiness claims.

## Agent check-in

Before work begins, an operator must declare:

- Role, such as Founder, ChatGPT, Codex, Copilot, future HC Guide Bot, future HC Control Bot, external contributor, or external AI agent.
- Requested scope and allowed files.
- Authority level.
- Protected path boundaries that must not be changed.
- Expected evidence bundle.
- Whether human-supervised validation is required before merge or further action.

If the operator cannot inspect the necessary repository evidence, the operator must stop and report the gap.

## Agent checkout

Before handoff, an operator must report:

- Work performed.
- Files changed or inspected.
- PR, issue, or commit task barcode when available.
- Checks run and results.
- Evidence bundle status.
- Risks, uncertainties, and reviewer decisions needed.
- Do-not-repeat rules discovered during the task.

## Roles

### Founder

The Founder acts as the primary human supervisor and direction setter for project priorities, protected boundary decisions, and human-supervised validation. Founder decisions should be recorded through repository evidence whenever possible.

### ChatGPT

ChatGPT may assist with planning, review, documentation drafting, cross-checking, and advisory analysis. ChatGPT must not claim repository state it cannot inspect and must preserve advisory-only semantics.

### Codex

Codex may inspect repository files, prepare bounded patches, run checks, produce commits, and prepare PR descriptions within assigned scope. Codex must not work outside allowed files and must not autonomously merge trust-critical changes.

### Copilot

Copilot may assist with in-editor suggestions, drafting, and implementation support under human supervision. Copilot output requires review against repository evidence and protected path boundaries.

### Future HC Guide Bot

The future HC Guide Bot is a shift guide and onboarding assistant. Its expected role is to help operators find project state, task history, next actions, terminology, and evidence requirements. It must remain advisory unless explicitly changed by validated repository governance.

### Future HC Control Bot

The future HC Control Bot is a risk and control officer. Its expected role is to flag protected path boundaries, missing evidence, do-not-repeat conflicts, and human-supervised validation requirements. It must not autonomously approve or merge trust-critical changes.

### External contributors / external AI agents

External contributors and external AI agents must follow repository instructions, declare scope, preserve terminology, respect protected path boundaries, and provide evidence for claims. They must not assume authority from chat context or external memory.

## Authority levels

| Level | Name | Meaning |
| --- | --- | --- |
| Level 0 | Report only | Inspect and report findings. No file changes. |
| Level 1 | Docs only | Modify documentation within explicitly allowed scope. No code, workflow, schema, record, validator, policy, signing, federation, or trust-kernel index changes. |
| Level 2 | Tests only | Modify or add tests within explicitly allowed scope. No runtime behavior changes. |
| Level 3 | Low-risk implementation | Make bounded implementation changes outside protected path boundaries, with relevant tests and review. |
| Level 4 | Protected path PR allowed, merge blocked | Prepare a PR touching protected path boundaries only when explicitly authorized. Merge remains blocked pending human-supervised validation. |
| Level 5 | Human approval required | Work cannot proceed, or cannot merge, without explicit human approval and repository-recorded validation. |

## Capability rules

- Agents must declare their role and scope before work.
- Agents must not claim capability for areas they cannot inspect or safely modify.
- Agents must stop and report if repository evidence is incomplete.
- Agents must not work outside allowed files.
- Agents must not autonomously merge trust-critical changes.
- Agents must cross-check task history before repeating prior work.
- Agents must preserve advisory-only semantics unless repository evidence explicitly says otherwise.

## Protected and trust-critical boundaries

Trust-kernel, schema, workflow, records, signing, federation, policy, runtime-sensitive, and governance-enforcement changes require human-supervised validation.

No agent may autonomously merge trust-critical changes.
