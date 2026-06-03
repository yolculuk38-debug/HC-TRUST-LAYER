# HC Decision Registry v0.1

Advisory, documentation-only registry model for preserving HC-TRUST-LAYER decision memory across HC:// repository operations.

## 1. Purpose

The HC Decision Registry preserves institutional memory for significant project decisions without creating new governance authority or changing repository behavior. It records:

- what was decided;
- why it was decided;
- what evidence supported it;
- what review history exists;
- what validation history exists;
- what later superseded it;
- whether it was retired.

Use this registry model to make historical decisions easier to find, audit, revisit, and explain during human-supervised validation, reviewer handoff, and future HC Control Center or HC Guide Bot workflows.

## 2. Authority Boundary

The HC Decision Registry is advisory only.

It is not:

- approval authority;
- merge authority;
- governance enforcement;
- security validation;
- production-readiness validation;
- truth-finality validation;
- a canonical record surface;
- a schema-backed governance object;
- automation;
- a substitute for repository-defined checks, reviewer oversight, or human-supervised validation.

Decision entries do not modify runtime, workflow, schema, validator, record, policy, federation, signing, or trust-kernel behavior. A decision entry may describe a decision, but implementation authority remains with repository evidence, approved changes, required checks, and reviewer oversight.

## 3. Source-of-Truth Model

The registry follows this source-of-truth priority when evidence conflicts:

1. Merged repository files and protected repository evidence.
2. Repository-defined checks and validation outputs.
3. PR records, commits, review notes, and human review decisions.
4. Project-control documentation, including Project State, Task Ledger, Active Work Registry, Next Actions, and Governance Change Protocol.
5. Decision Registry entries as advisory historical memory.
6. `hc_context`, chat memory, bot summaries, and external summaries as advisory context that may be stale.

A registry entry must not override repository evidence. If an entry conflicts with higher-priority evidence, mark the entry as needing review, supersession, or retirement rather than treating the registry entry as final.

## 4. Decision ID Format

Decision IDs use documentation-native identifiers:

```text
HC-DEC-YYYY-NNN
```

Example:

```text
HC-DEC-2026-001
```

Rules:

- `HC-DEC` identifies the entry as an advisory decision-registry item.
- `YYYY` is the calendar year in which the decision entry was opened.
- `NNN` is a three-digit sequence number for that year.
- IDs should not be reused after rejection, supersession, or retirement.
- IDs are documentation labels only and do not create canonical records, schema-backed objects, governance tokens, or security artifacts.

## 5. Decision Lifecycle

A decision entry may move through these stages:

1. Open a Draft entry when a decision needs persistent institutional memory.
2. Attach repository evidence, related PRs, review notes, and validation notes when available.
3. Move to Evidence Needed if support is incomplete or unclear.
4. Move to Under Review when reviewers are actively assessing scope, evidence, and implications.
5. Move to Validation Pending when human-supervised validation or repository-defined checks remain unresolved.
6. Move to Accepted, Accepted with Limits, Deferred, or Rejected after review.
7. Move to Superseded when a later decision replaces or narrows the entry.
8. Move to Retired when the decision is no longer active and should not guide future work.

Lifecycle changes should cite repository evidence and preserve the audit trail. Do not use lifecycle updates to imply approval, merge authority, security validation, production readiness, or truth-finality.

## 6. Decision States

| State | Meaning |
| --- | --- |
| Draft | Initial advisory entry. Evidence, review, or scope may be incomplete. |
| Evidence Needed | The entry lacks sufficient repository evidence to support the stated decision. |
| Under Review | Reviewers are assessing evidence, implications, and boundaries. |
| Validation Pending | Required checks, reviewer confirmation, or human-supervised validation remain unresolved. |
| Accepted | The decision is accepted within the documented authority boundary and supporting evidence. |
| Accepted with Limits | The decision is accepted only within explicitly stated scope, assumptions, or constraints. |
| Deferred | The decision is postponed and should not be treated as active guidance. |
| Rejected | The proposed decision was not accepted. Keep the entry for audit trail continuity. |
| Superseded | A later decision replaces, narrows, or materially changes this entry. |
| Retired | The decision is no longer active and should not guide future work. |

## 7. Evidence Model

Each decision entry should list the evidence that supported the decision. Evidence may include:

- repository files;
- PR numbers;
- commit hashes;
- check outputs;
- review comments;
- task-ledger references;
- project-control documentation;
- human-supervised validation notes;
- known evidence gaps.

Evidence requirements:

- Prefer repository-native evidence over chat memory or external summaries.
- Identify whether evidence is merged, pending, stale, contradicted, or missing.
- Do not claim cryptographic, policy, forensic, security, production, or truth guarantees unless implemented and validated in repository evidence.
- Preserve provenance and audit trail continuity when evidence changes.

## 8. Review Model

Decision entries should document review history without replacing reviewer authority. Review notes should include:

- reviewers or review groups when known;
- review dates or PR references;
- concerns raised;
- scope limits;
- follow-up work;
- unresolved questions;
- decision-state changes.

A registry entry may summarize review history, but it does not approve a PR, merge a change, enforce governance, or bypass required review. Review history should surface uncertainty rather than infer unsupported guarantees.

## 9. Human-Supervised Validation Model

Human-supervised validation remains required for non-trivial trust-kernel-impacting changes and any change where repository rules require explicit reviewer oversight.

A decision entry should document:

- whether human-supervised validation was required;
- who or what review process supplied validation when known;
- what checks or artifacts supported validation;
- whether validation was partial, scoped, pending, or absent;
- any limits on the decision that follow from validation gaps.

A registry entry is not human-supervised validation by itself. It may preserve validation history, but it must not claim security validation, production-readiness validation, truth-finality validation, or autonomous governance finality.

## 10. Supersession Model

Supersession records when a later decision replaces, narrows, clarifies, or invalidates an earlier decision.

A supersession note should identify:

- superseded decision ID;
- superseding decision ID;
- reason for supersession;
- evidence supporting the change;
- effective date when known;
- residual limits or migration notes.

Supersession does not delete the earlier decision. The earlier entry remains part of the audit trail and should move to Superseded unless it is also retired.

## 11. Retirement Model

Retirement records that a decision is no longer active guidance.

A retirement note should identify:

- retired decision ID;
- reason for retirement;
- evidence supporting retirement;
- date or PR reference when known;
- whether any follow-up work remains;
- whether a superseding decision exists.

Retirement does not erase history. Retired entries remain available for institutional memory and audit trail continuity.

## 12. Decision Entry Template

Use this template for future entries:

```markdown
### HC-DEC-YYYY-NNN — <short decision title>

- State: <Draft | Evidence Needed | Under Review | Validation Pending | Accepted | Accepted with Limits | Deferred | Rejected | Superseded | Retired>
- Opened: <YYYY-MM-DD or unknown>
- Last updated: <YYYY-MM-DD or unknown>
- Decision: <what was decided>
- Rationale: <why it was decided>
- Authority boundary: <advisory only / scope limits / no approval or merge authority>
- Evidence:
  - <repository file, PR, commit, check, review note, or evidence gap>
- Review history:
  - <reviewer, review process, PR reference, or unresolved review gap>
- Human-supervised validation history:
  - <validation note, scoped validation, pending validation, or not required>
- Supersedes: <decision ID or none>
- Superseded by: <decision ID or none>
- Retirement status: <active / retired / retirement pending>
- Related project-control references:
  - <HC Control Center, Active Work Registry, Project State, Task Ledger, Next Actions, Governance Change Protocol, HC_BOOTSTRAP, AGENTS.md, HC Guide Bot, future HC Control Bot>
- Notes: <limits, risks, unresolved questions, or follow-up>
```

## 13. Decision Index

No decision entries are recorded in this v0.1 registry page yet. Future entries should be indexed here for quick lookup.

| Decision ID | Title | State | Opened | Last updated | Primary evidence |
| --- | --- | --- | --- | --- | --- |
| _None yet_ | _No advisory decision entries have been added._ | _N/A_ | _N/A_ | _N/A_ | _N/A_ |

## 14. Supersession Index

Use this index to connect superseded and superseding decisions.

| Superseded decision | Superseding decision | Reason | Evidence |
| --- | --- | --- | --- |
| _None yet_ | _N/A_ | _N/A_ | _N/A_ |

## 15. Retirement Index

Use this index to list retired decisions and preserve the reason they should no longer guide active work.

| Retired decision | Retirement reason | Retirement evidence | Follow-up |
| --- | --- | --- | --- |
| _None yet_ | _N/A_ | _N/A_ | _N/A_ |

## 16. Relationship to HC Control Center

The HC Control Center is the single-entry operator orientation page. The Decision Registry may support that orientation by preserving historical decisions, but it does not replace the HC Control Center, repository evidence, checks, review notes, or human-supervised validation.

The HC Control Center may point operators to the Decision Registry when historical context is needed.

## 17. Relationship to Active Work Registry

The Active Work Registry tracks shift-level active, blocked, parked, and recently completed work. The Decision Registry preserves decision history over a longer horizon.

Use the Active Work Registry for current coordination snapshots. Use the Decision Registry for durable advisory memory after a decision needs historical tracking.

## 18. Relationship to Project State

Project State remains the repository-native shift handoff summary for current phase, active focus, parked work, and source-of-truth priority. The Decision Registry must not override Project State.

When a decision affects current phase interpretation or active focus, Project State should remain the primary project-control source and the decision entry should cite it as evidence or context.

## 19. Relationship to Task Ledger

The Task Ledger records task history, completed or closed PR references, and do-not-repeat notes. The Decision Registry may cite Task Ledger entries as evidence or review history, but it should not duplicate the full task ledger.

If a decision entry conflicts with the Task Ledger, treat the conflict as an evidence gap requiring review.

## 20. Relationship to Next Actions

Next Actions provides the priority queue for safe future work. The Decision Registry may explain why a future action exists or why a past action was deferred, accepted, rejected, superseded, or retired.

A decision entry does not authorize a next action unless the appropriate reviewer direction, repository checks, and human-supervised validation requirements are also satisfied.

## 21. Relationship to Governance Change Protocol

The Governance Change Protocol governs how governance-related changes should be proposed, reviewed, and validated. The Decision Registry may preserve governance decision history, but it does not enforce governance, approve governance changes, or bypass the protocol.

Governance-impacting entries should clearly identify affected boundaries, expected evidence, review history, validation status, and any limits.

## 22. Relationship to HC_BOOTSTRAP

`HC_BOOTSTRAP.md` provides first-step operational orientation for repository-native handoff. The Decision Registry can serve as a follow-up evidence source when bootstrap readers need historical context for a decision.

Bootstrap guidance remains an orientation layer and should not be displaced by decision entries.

## 23. Relationship to AGENTS.md

`AGENTS.md` remains the repository-wide contributor and agent guide for terminology, behavior rules, protected paths, safe task boundaries, and required checks. The Decision Registry must preserve HC-TRUST-LAYER and HC:// terminology and must not weaken `AGENTS.md` requirements.

If a decision entry appears to conflict with `AGENTS.md`, treat `AGENTS.md` and higher-priority repository evidence as authoritative and mark the decision entry for review.

## 24. Relationship to HC Guide Bot

The future HC Guide Bot may use the Decision Registry as advisory context for answering orientation questions, surfacing stale evidence, and routing users to repository evidence.

The HC Guide Bot should not treat registry entries as approval, merge authority, governance enforcement, security validation, production-readiness validation, or truth-finality validation.

## 25. Relationship to future HC Control Bot

A future HC Control Bot may use the Decision Registry to summarize historical decision context, identify superseded or retired decisions, and help operators prepare reviewable evidence bundles.

Any future bot use must remain bounded, explainable, reversible, and human-reviewable. The registry does not authorize uncontrolled automation or autonomous governance finality.

## 26. Risks and Guardrails

Risks:

- stale entries may mislead operators;
- advisory notes may be mistaken for approval authority;
- incomplete evidence may create false confidence;
- duplicated history may drift from PR records, commits, checks, or review notes;
- broad decision language may imply unsupported production, security, policy, forensic, or truth guarantees.

Guardrails:

- keep entries concise, evidence-linked, and scoped;
- identify missing or stale evidence explicitly;
- preserve source-of-truth priority;
- use Accepted with Limits when scope constraints matter;
- move replaced entries to Superseded rather than deleting them;
- move inactive entries to Retired rather than treating them as active guidance;
- never use this registry to bypass checks, reviewer oversight, protected-path rules, or human-supervised validation.

## 27. Non-Goals

The HC Decision Registry does not:

- create canonical records;
- create schema-backed governance objects;
- create automation;
- change runtime behavior;
- change workflow behavior;
- change schema behavior;
- change validator behavior;
- change record behavior;
- change policy behavior;
- change federation behavior;
- change signing behavior;
- change trust-kernel behavior;
- approve PRs;
- merge changes;
- enforce governance;
- validate security;
- validate production readiness;
- validate truth finality;
- replace repository-defined checks, reviewer oversight, or human-supervised validation.
