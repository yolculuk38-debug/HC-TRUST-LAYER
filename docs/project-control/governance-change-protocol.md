# Governance Change Protocol

Advisory protocol for proposing, reviewing, deciding, superseding, and retiring governance-oriented documentation in HC-TRUST-LAYER.

## 1. Purpose

This protocol describes a documentation-only path for proposed changes to repository rules, governance rules, operating rules, protected-path definitions, trust-kernel boundaries, operating standards, and future HC governance guidance.

It supports auditable discussion of how governance guidance can be proposed, reviewed, accepted, accepted with limits, rejected, deferred, superseded, or retired without creating automation, enforcement, runtime behavior, workflow behavior, or governance authority.

## 2. Authority Boundary

- Repository evidence is authoritative.
- Human-supervised validation remains authoritative where required.
- Agent output is advisory.
- Governance documentation is not governance enforcement.
- Governance documentation is not merge authority.
- Governance documentation is not security validation.
- Governance documentation is not production-readiness validation.
- Governance documentation is not truth-finality validation.

This protocol does not grant approval power, reviewer power, maintainer power, merge authority, security-validation authority, or autonomous governance authority.

## 3. Governance Principles

- HC-TRUST-LAYER remains the source of truth for HC:// architecture, policy baselines, implementation status, verification documentation, provenance, and audit trail evidence.
- Governance guidance must preserve canonical terminology, including verification map, trust kernel, protocol graph, agent context, canonical record, and human-supervised validation.
- Governance changes must be scoped, reversible, reviewable, and supported by repository evidence.
- Human-supervised validation is required where repository rules require it, especially for trust-kernel-impacting or protected-surface changes.
- Agent output may assist review, drafting, evidence collection, or risk surfacing, but it does not decide governance outcomes.
- Governance documentation may clarify expectations, but it does not enforce rules by itself.
- Governance documentation may describe review expectations, but it does not approve merges.
- Governance documentation may identify security-sensitive topics, but it does not validate security.
- Governance documentation may describe readiness criteria, but it does not establish production readiness.
- Governance documentation may preserve evidence and decision history, but it does not establish truth finality.

No individual, role, agent, founder, maintainer, reviewer, operator, governance actor, contributor, or future automation is above repository evidence, review requirements, protected-path boundaries, or human-supervised validation requirements.

Different roles may have different responsibilities, authority scopes, permissions, and review obligations. Governance requirements, evidence requirements, protected-path boundaries, audit requirements, and validation expectations apply consistently regardless of role.

### 3.1 Auditability Principle

No role is exempt from auditability.

No individual, founder, maintainer, reviewer, operator, governance actor, contributor, agent, or future automation is above:

- repository evidence;
- review requirements;
- protected-path boundaries;
- human-supervised validation requirements.

Different roles may have different responsibilities, permissions, authority scopes, and review obligations. Governance requirements, evidence requirements, protected-path boundaries, audit requirements, and validation expectations apply consistently regardless of role.

Auditability in this protocol is advisory and evidence-oriented. It does not create governance enforcement, approval authority, merge authority, runtime behavior, or automation.

### 3.2 Transparency Principle

Governance legitimacy depends on:

- transparency;
- traceability;
- evidence;
- reviewability.

Opaque governance structures, undocumented decision paths, hidden rule changes, or non-reviewable authority create trust risk.

Governance changes should remain:

- discoverable;
- reviewable;
- attributable;
- historically traceable.

Repository evidence should provide the traceability needed to inspect governance changes without relying on chat memory, hidden context, or non-reviewable authority.

### 3.3 Accountability Principle

Authority and responsibility must remain linked.

Actions, decisions, approvals, exceptions, and governance changes should be attributable to identifiable evidence and review history.

Mistakes should be:

- documented;
- reviewed;
- corrected;
- used for continuous improvement.

The objective is not the absence of mistakes, but the existence of traceable accountability, reviewability, and corrective mechanisms.

Accountability language in this protocol remains advisory. It does not introduce governance enforcement, automation, approval authority, merge authority, or a replacement for repository evidence and human-supervised validation.

## 4. Source-of-Truth Model

When governance guidance conflicts with repository evidence, use this priority order:

1. Merged repository files and protected repository evidence.
2. Repository-defined checks and validation outputs.
3. PR records, commits, review notes, and human review decisions.
4. Protected-path rules, trust-kernel boundaries, and canonical record boundaries documented in-repo.
5. Project-control documents, including HC Control Center, Active Work Registry, Project State, Task Ledger, and Next Actions.
6. Advisory agent context and external summaries.

Governance proposals must identify their evidence layer and must not override stronger repository evidence with weaker advisory context.

## 5. Governance Change Lifecycle

A governance change should move through these steps when applicable:

1. **Propose** the change with a clear scope, rationale, affected files, and protected-surface assessment.
2. **Collect evidence** from repository files, existing checks, prior PRs, review notes, and task-ledger links when applicable.
3. **Classify impact** across governance controls, operating rules, trust-kernel boundaries, protected-path definitions, and related HC:// documentation.
4. **Review** the change through the applicable repository review path.
5. **Validate** the change with human-supervised validation when required by trust-kernel, protected-surface, policy, workflow, schema, validator, signing, federation, or governance-control impact.
6. **Decide** using one of the governance decision outcomes in this protocol.
7. **Record** the decision with enough evidence for later audit trail review.
8. **Monitor for supersession or retirement** when repository evidence changes.

## 6. RFC Model

A governance RFC is an advisory proposal format for non-trivial governance guidance. It may be a document, issue, PR description, or structured review note.

A governance RFC should include:

- title and short summary;
- task or issue reference;
- proposed governance change;
- affected repository areas;
- protected-surface assessment;
- expected review requirements;
- expected human-supervised validation requirements;
- evidence bundle;
- known risks and guardrails;
- proposed decision outcome;
- retirement or supersession conditions when known.

RFCs are not governance approval, merge approval, enforcement, or autonomous governance. They are advisory records that support review.

## 7. Decision Record Model

A governance decision record should preserve the decision and evidence without overstating authority.

A decision record should include:

- decision title;
- decision outcome;
- task, issue, or PR reference;
- commit hash when available;
- changed files;
- affected governance surfaces;
- review notes;
- checks run;
- validation notes;
- limits, conditions, or follow-up requirements;
- supersession or retirement references when applicable.

Decision records are repository evidence only to the extent they are merged or otherwise captured through repository-recognized review artifacts.

## 8. Evidence Requirements

An evidence bundle should include:

- task or issue reference;
- PR reference;
- commit hash when available;
- changed files;
- checks run;
- review notes;
- validation notes;
- task-ledger linkage when applicable.

If evidence is missing, the proposal or decision should mark the gap explicitly and avoid approval, production-readiness, security-validation, truth-finality, or autonomous governance claims.

## 9. Review Requirements

Governance changes should receive review appropriate to their scope and risk.

Review should confirm:

- the change is documentation-only unless explicitly authorized otherwise;
- affected files are within authorized scope;
- protected paths are not modified unless explicitly requested;
- trust-kernel boundaries are not altered without required review and human-supervised validation;
- terminology is consistent with HC-TRUST-LAYER and HC:// usage;
- authority claims remain advisory and bounded;
- evidence supports the proposed decision outcome;
- follow-up work is separated from the current change when needed.

## 10. Human-Supervised Validation Requirements

Human-supervised validation must be considered and documented for governance changes that affect or reinterpret:

- trust-kernel boundaries;
- governance controls;
- protected-path definitions;
- policy interpretation;
- workflow governance;
- schema governance;
- validator governance;
- signing governance;
- federation governance.

When a proposal affects these areas, the decision record should identify the affected surface, the expected validation path, known risks, and whether validation is complete, pending, limited, or not applicable.

This protocol does not perform human-supervised validation. It only describes when that validation must be surfaced.

## 11. Protected-Surface Assessment Model

Every governance proposal should include a protected-surface assessment.

The assessment should state whether the proposal affects:

- `.github/workflows/**` workflow behavior;
- `src/**` runtime behavior;
- `schema/**` schema contracts;
- `validators/**` validator logic;
- `records/**` canonical record or provenance continuity;
- `policy/**` policy evaluator behavior or interpretation;
- `federation/**` federation behavior;
- `signatures/**` signing or trust anchor semantics;
- trust-kernel indexes or trust-kernel review routing;
- `hc_context/**` advisory agent context;
- `agents/**` agent workspace behavior.

If the proposal changes only governance documentation, the assessment should say so directly and confirm that no protected path was modified.

## 12. Governance Roles and Responsibilities

Governance participants may include contributors, operators, maintainers, reviewers, founders, agents, governance actors, and future automation.

Responsibilities may differ by role:

- Contributors may propose scoped governance changes and provide evidence.
- Operators may maintain shift-level awareness and surface conflicts or stale context.
- Reviewers may evaluate evidence, scope, terminology, and protected-surface impact.
- Maintainers may apply repository-recognized merge and branch-protection procedures.
- Founders or governance actors may provide domain direction within repository-defined boundaries.
- Agents may draft, summarize, inspect, and report, but their output remains advisory.
- Future automation may assist with bounded checks or reports only when authorized and reviewable.

Different responsibilities do not remove equal governance obligations. Evidence requirements, review requirements, protected-path boundaries, and validation expectations apply consistently regardless of role.

## 13. Governance Decision Outcomes

Governance changes should use one of these outcomes:

- **Draft**: The proposal is incomplete or exploratory and is not ready for review.
- **Under Review**: The proposal is being evaluated against repository evidence, scope, risk, and validation requirements.
- **Accepted**: The proposal is accepted as written through the applicable repository review path.
- **Accepted with Limits**: The proposal is accepted only within stated scope, conditions, time limits, or follow-up requirements.
- **Rejected**: The proposal is declined, with reasons recorded when available.
- **Deferred**: The proposal is parked pending evidence, validation, priority, dependency, or reviewer availability.
- **Superseded**: The proposal or decision is replaced by later repository evidence or a later accepted decision.
- **Retired**: The proposal or guidance is no longer active and is preserved only for historical audit trail context.

No outcome grants autonomous governance, production readiness, security validation, or truth-finality validation.

## 14. Retirement and Supersession Process

Governance guidance may be superseded or retired when repository evidence changes, scope becomes obsolete, a later decision replaces it, or reviewers determine that the guidance should no longer be active.

A supersession or retirement record should include:

- the prior guidance or decision being superseded or retired;
- the new controlling evidence or reason for retirement;
- changed files;
- PR reference and commit hash when available;
- review notes;
- validation notes when required;
- any remaining limits or follow-up tasks.

Retired guidance should not be deleted automatically. Preserve historical context unless an explicit repository-approved deletion is requested.

## 15. Relationship to HC Control Center

HC Control Center remains an advisory orientation page for repository status, safe task scoping, and evidence collection. This protocol may inform governance-change discussions, but it does not replace HC Control Center, alter its authority boundary, or turn it into enforcement.

## 16. Relationship to Active Work Registry

The Active Work Registry remains an advisory shift-level coordination snapshot. Governance proposals may link to it for current-work context, but the registry does not approve governance changes, override Project State, or replace review and human-supervised validation.

## 17. Relationship to Project State

Project State remains the advisory repository status and focus reference for current phase, active focus, parked work, and protected-path reminders. Governance proposals should cite Project State when relevant and should not silently override it.

## 18. Relationship to Task Ledger

The Task Ledger remains the task history, completed-reference, closed-reference, and do-not-repeat source. Governance proposals and decision records should link to the Task Ledger when a task barcode, completed PR, superseded item, or deferred item is relevant.

## 19. Relationship to Next Actions

Next Actions remains the priority queue for safe next work. Governance proposals should not create new active work or reorder priorities unless the requested scope explicitly authorizes that documentation update and supporting evidence exists.

## 20. Relationship to HC_BOOTSTRAP

`HC_BOOTSTRAP.md` remains the first operational bootstrap checklist for repository-native handoff. This protocol supports governance-change evidence collection after bootstrap orientation; it does not replace the bootstrap sequence.

## 21. Relationship to AGENTS.md

`AGENTS.md` remains the repository-wide contributor and agent guide. Governance changes that affect repository rules, agent behavior rules, protected-path expectations, or human-supervised validation expectations should treat `AGENTS.md` as a high-sensitivity governance reference and should not modify it without explicit scope and review.

## 22. Relationship to HC Guide Bot

HC Guide Bot is future advisory orientation support. It may summarize this protocol, point to repository evidence, and surface gaps, but it must not claim approval authority, merge authority, governance enforcement, security validation, production readiness, autonomous governance, or truth-finality validation.

## 23. Risks and Guardrails

Risks:

- Governance documentation could be mistaken for enforcement.
- Advisory records could be mistaken for approval or merge authority.
- Stale governance guidance could conflict with stronger repository evidence.
- Agent-generated summaries could omit protected-surface or validation requirements.
- Role names could be mistaken for exemption from governance obligations.

Guardrails:

- State authority boundaries in governance documents.
- Keep changes small, reversible, and reviewable.
- Preserve HC-TRUST-LAYER and HC:// terminology.
- Require evidence bundles for non-trivial decisions.
- Surface protected-surface impact before review.
- Require human-supervised validation where repository rules require it.
- Record limits, deferrals, supersession, and retirement explicitly.
- Do not use governance documents to bypass checks, protected paths, reviewer oversight, or validation expectations.

## 24. Non-Goals

- No workflow changes.
- No runtime changes.
- No schema changes.
- No validator changes.
- No record changes.
- No policy changes.
- No federation changes.
- No signing changes.
- No trust-kernel behavior changes.
- No automation.
- No governance enforcement.
- No autonomous governance.
