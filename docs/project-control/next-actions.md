# Next Actions

This file lists safe next work for HC-TRUST-LAYER. All entries are advisory, repository-state based, and limited to report-only inspection unless explicitly re-scoped by a human supervisor.

Do not claim production readiness, truth finality, security guarantees, or autonomous governance. Do not introduce workflow behavior from this file.

## Priority order

| Priority | Next safe task | Mode | Risk | Allowed inspection scope | Why it is next |
| --- | --- | --- | --- | --- | --- |
| 1 | PR risk labeler Tier-1 sync review | REPORT ONLY | Governance-enforcement and protected path routing risk | `.github/workflows/pr-risk-labeler.yml`, `CODEOWNERS`, trust-kernel protected path documentation, recent related PR evidence; no edits | Confirms whether PR risk labeling reflects current Tier-1 review boundaries before any behavior proposal. |
| 2 | safe auto-merge Tier-1 restriction review | REPORT ONLY | Governance-enforcement and autonomous merge risk | `.github/workflows/safe-auto-merge.yml`, branch protection documentation, CODEOWNERS references, recent related PR evidence; no edits | Confirms whether safe auto-merge restrictions remain aligned with protected path boundaries and advisory-only semantics. |
| 3 | HC Guide Bot design review | REPORT ONLY | Agent guidance and onboarding scope risk | `agents/`, `docs/project-control/`, `docs/trust-pr-engine.md`, `docs/trust-impact-analysis.md`, `docs/trust-review-workflow.md`; no edits | Defines a future shift guide and onboarding assistant without creating uncontrolled automation. |
| 4 | GitHub Project Board and label taxonomy plan | REPORT ONLY | Governance planning and contributor routing risk | `.github/labels.md`, issue templates, project documentation, current roadmap and governance docs; no edits | Establishes a repository-state based plan for work order labels, board columns, and review routing. |
| 5 | `hc_context` machine-readable state proposal | REPORT ONLY | Machine-readable project memory and provenance risk | `protocol-graph.json`, `verification-map.json`, `trust-kernel-index.json`, project-control docs, verification map docs; no edits | Prepares a TREX-like machine-readable project memory proposal while preserving advisory-only semantics. |

## Report-only rules

- Inspect only within the allowed inspection scope.
- Do not modify runtime code, schemas, validators, workflows, CODEOWNERS, records, policy files, federation files, trust-kernel index files, `protocol-graph.json`, `verification-map.json`, or scripts.
- Cross-check current repository evidence before proposing any follow-up task.
- Record do-not-repeat findings in the task ledger when a future docs-only update is explicitly authorized.
- Escalate trust-kernel-sensitive, governance-enforcement, runtime-sensitive, schema, workflow, records, signing, federation, or policy findings for human-supervised validation.
