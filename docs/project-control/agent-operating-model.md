# Agent Operating Model

This file defines advisory role boundaries for humans, ChatGPT, Codex, Copilot, future HC Guide Bot, future HC Control Bot, and external contributors or external AI agents working in HC-TRUST-LAYER.

## Roles

### Founder

- Provides project direction, priority calls, and supervisor decisions.
- Approves or rejects trust-kernel-sensitive changes through human-supervised validation.
- Resolves ambiguity when repository evidence and proposed work are incomplete.

### ChatGPT

- Provides planning, design review, documentation drafting, and advisory analysis.
- Should cite repository evidence when making project-state claims.
- Must not claim authority to inspect or modify files outside the active repository context.

### Codex

- Performs repository-local inspection, documentation edits, scoped implementation when authorized, checks, commits, and PR preparation.
- Must declare scope, avoid protected paths unless explicitly authorized, and preserve repository guardrails.
- Must stop and report when requested work exceeds allowed scope or repository evidence is incomplete.

### Copilot

- Assists with local authoring and code or documentation suggestions inside the contributor's environment.
- Suggestions remain advisory until reviewed, tested, and committed by an authorized operator.
- Must not be treated as a source of truth over repository evidence.

### Future HC Guide Bot

- Acts as a shift guide and onboarding assistant.
- May summarize project state, suggest next safe work, and route operators to relevant files.
- Must preserve advisory-only semantics and avoid autonomous governance claims.

### Future HC Control Bot

- Acts as a risk/control officer.
- May flag protected path boundaries, missing evidence bundles, stale task barcodes, and review requirements.
- Must not autonomously approve or merge trust-critical changes.

### External contributors / external AI agents

- Must follow `AGENTS.md`, this operating model, protected path boundaries, and repository checks.
- Must declare role, scope, and intended file changes before work.
- Must treat repository state as authoritative and report uncertainty instead of inferring unsupported guarantees.

## Authority levels

| Level | Name | Allowed activity |
| --- | --- | --- |
| Level 0 | Report only | Inspect and report findings; no file changes. |
| Level 1 | Docs only | Create or edit documentation within allowed scope. |
| Level 2 | Tests only | Create or edit tests within allowed scope; no runtime behavior changes. |
| Level 3 | Low-risk implementation | Make low-risk implementation changes outside protected paths when explicitly authorized. |
| Level 4 | Protected path PR allowed, merge blocked | Prepare protected path changes only when explicitly authorized; merge remains blocked pending human-supervised validation. |
| Level 5 | Human approval required | Human supervisor decision required before proceeding or merging. |

## Capability rules

- Agents must declare their role and scope before work.
- Agents must not claim capability for areas they cannot inspect or safely modify.
- Agents must stop and report if repository evidence is incomplete.
- Agents must not work outside allowed files.
- Agents must not autonomously merge trust-critical changes.
- Agents must keep agent check-in and agent checkout records concise, evidence-based, and tied to task barcodes when available.
- Agents must preserve do-not-repeat rules by checking the task ledger and project state before proposing repeated work.

## Human-supervised validation boundaries

Trust-kernel, schema, workflow, records, signing, federation, policy, runtime-sensitive, and governance-enforcement changes require human-supervised validation.

No agent may autonomously merge trust-critical changes. Agent recommendations, bot reports, and automation outputs are advisory unless validated by repository-defined checks and human review.
