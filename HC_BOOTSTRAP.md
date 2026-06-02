# HC Operating Layer Bootstrap v0.1

`HC_BOOTSTRAP.md` is the first operational entrypoint for HC-TRUST-LAYER contributors, including humans, ChatGPT, Codex, Copilot, future AI agents, the future HC Guide Bot, and the future HC Control Bot.

This file provides repository-native handoff guidance for HC:// project state, task history, role boundaries, evidence expectations, and do-not-repeat rules. It is a bootstrap checklist, not an authority source. It does not grant approval authority, introduce runtime or workflow behavior, or support claims of autonomous governance, security guarantees, truth finality, or production readiness.

## Startup sequence

Before proposing, assigning, or performing work, complete this read order. Keep the repository evidence open for reference while scoping the task:

1. Read `AGENTS.md` first for repository-wide contributor and agent rules.
2. Read `docs/project-control/project-state.md` for the current phase, known status, and active focus areas.
3. Read `docs/project-control/agent-operating-model.md` for roles, authority levels, scope limits, and validation boundaries.
4. Read `docs/project-control/task-ledger.md` for completed work, closed work, task barcodes, evidence notes, and do-not-repeat rules.
5. Read `docs/project-control/next-actions.md` for safe report-only next work.

Repository state is the source of truth. Do not rely on chat memory alone. Do not override repository evidence with assumptions from prior conversations, external memory, or tool suggestions.

## Operating principles

- Preserve advisory-only semantics for agent output, bot guidance, operating notes, and planning recommendations.
- Do not repeat merged, superseded, abandoned, closed, conflicted, or do-not-reuse work.
- Require human-supervised validation for trust-kernel-sensitive changes and protected path boundary changes.
- Do not claim production readiness, truth finality, security guarantees, forensic certainty, or autonomous governance.
- Stop and report when repository evidence is incomplete, inconsistent, stale, or outside the allowed scope before editing.

## Shift-ledger model

HC-TRUST-LAYER treats project work like a traceable production line for handoff clarity, evidence bundling, and review routing. The model is advisory and repository-state based; it does not create automation, approval authority, or governance finality.

| Production-line concept | HC Operating Layer equivalent | Operating use |
| --- | --- | --- |
| Work order | Issue or task request | Explains why work is being proposed. |
| Operator | Human contributor or agent | Identifies who inspected, drafted, edited, or reviewed. |
| Machine | Tool | Identifies what was used to inspect, edit, validate, report, or prepare a PR. |
| Production batch | Pull request | Groups proposed repository changes for review. |
| Task barcode | PR number and commit hash | Connects work to a traceable repository record and commit history. |
| Quality control | CI checks, repository guards, and review | Cross-checks the proposed batch before human acceptance. |
| Shift ledger | Task ledger | Records task history, evidence pointers, and do-not-repeat notes. |
| Shift handoff summary | Project state | Summarizes current phase, known status, and active focus. |
| Machine-readable project memory | Future `hc_context` JSON | Proposed TREX-like state for cross-checkable project memory. |
| Shift guide | Future HC Guide Bot | Advisory onboarding and routing assistant. |
| Risk/control officer | Future HC Control Bot | Advisory boundary, risk, and evidence reviewer. |
| Supervisor decision gate | Human review | Required decision point for trust-critical acceptance. |

## Agent check-in

Before starting work, each agent should provide a concise check-in:

- role and authority level;
- task or work order, including issue or PR reference when available;
- mode, such as report only, docs only, tests only, or implementation when explicitly authorized;
- allowed files and inspection scope;
- protected path boundaries and files that must not be touched;
- expected evidence bundle and planned checks;
- known repository evidence gaps or assumptions.

If requested work conflicts with the allowed scope, protected path boundaries, or available repository evidence, the agent should stop and report the conflict before editing.

## Agent checkout

Before handing off work, each agent should provide a concise checkout that can be cross-checked against repository state:

- changed files, if any;
- task barcode, including PR number and commit hash when available;
- checks run and whether each passed, warned, failed, or could not run;
- evidence bundle contents, including changed files and checks;
- confirmation that protected paths were not modified, when applicable;
- unresolved risks, uncertainty, or human-supervised validation still required;
- next recommended action, if any.

## Evidence cross-checking

A task should not be treated as complete from a single signal. Cross-check evidence across repository layers where available, and keep conclusions advisory when evidence is partial or unresolved:

- task or issue reference;
- PR record;
- commit hash;
- changed files;
- checks run;
- review or human-supervised validation notes;
- task ledger update when applicable;
- human-supervised validation outcome when required.

If evidence is missing or inconsistent, keep the result advisory, identify the missing layer, and avoid claiming completion.
