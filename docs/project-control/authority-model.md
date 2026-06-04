# Authority Model

Documentation-only authority model for HC-TRUST-LAYER. This document consolidates repository evidence about HC:// authority boundaries, role responsibilities, review expectations, and advisory agent limits.

## 1. Purpose

This document provides a single project-control reference for authority questions in HC-TRUST-LAYER.

It describes how source-of-truth authority, validation authority, release authority, trust-kernel authority, governance authority, role authority, human-supervised validation authority, and advisory agent authority should be interpreted from existing repository evidence.

This document is advisory and documentation-only. It does not create approval authority, merge authority, release authority, security certification, production readiness, forensic certainty, truth finality, or autonomous governance.

## 2. Authority Boundary

Repository evidence remains authoritative.

No individual, founder, maintainer, reviewer, CODEOWNER, contributor, agent, bot, or future automation is above repository evidence.

Roles may have different responsibilities, permissions, authority scopes, and review obligations. Evidence requirements, audit expectations, protected-path boundaries, and human-supervised validation expectations apply consistently regardless of role.

This document does not override:

- merged repository files;
- protected repository evidence;
- repository-defined checks;
- PR records, commits, review notes, or human review decisions;
- protected-path and trust-kernel boundary documents;
- governance and constitutional documents;
- release governance and release checklist documents;
- project-control operating documents;
- machine-readable indexes;
- `hc_context` advisory files;
- agent, bot, or chat outputs.

Human-supervised validation remains required for sensitive trust-kernel-impacting work.

## 3. Source-of-Truth Authority

The repository is the source of truth for architecture, policy baselines, implementation status, verification documentation, and reviewable project-control evidence.

Source-of-truth authority belongs to repository evidence, not to a person, role title, agent summary, external interpretation, or unmerged assertion.

When claims conflict, reviewers and contributors should prefer the strongest available repository evidence and surface any uncertainty rather than silently resolving it through personal or agent interpretation.

## 4. Validation Authority

Validation authority is the authority to determine whether a proposed change has been checked against repository-defined expectations.

Validation authority remains distributed across:

- repository-defined checks;
- reviewer inspection;
- protected-surface assessment;
- trust-kernel impact review;
- human-supervised validation where required;
- audit trail evidence captured in PRs, commits, review notes, and project-control records.

Passing a check does not create truth finality, security certification, release authority, or production readiness. Failing, skipped, or unavailable checks must be reported without implying success.

## 5. Release Authority

Release authority is currently implied rather than fully formalized.

Release governance and release checklist documents may describe expected release scope, evidence, signoff, tag, release-note, changelog, correction, supersession, or retirement practices. They do not independently create merge authority, release authority, approval authority, security certification, production readiness, forensic certainty, truth finality, or autonomous governance.

A release should be treated as reviewable repository evidence only to the extent it is supported by commits, tags, release notes, changelog entries, checks, PR records, and human review decisions.

## 6. Trust-Kernel Authority

Trust-kernel authority concerns boundaries that affect HC:// verification integrity, provenance continuity, canonical record assumptions, protected-path routing, policy interpretation, signing semantics, federation behavior, validator logic, schema contracts, or related audit trail expectations.

Trust-kernel authority does not belong to a single role or advisory document. It is bounded by repository evidence, trust-kernel boundary documentation, protected-path rules, repository-defined checks, reviewer oversight, and human-supervised validation where required.

This document does not redefine the trust kernel. The trust-kernel definition remains distributed across multiple files and should be reviewed through the dedicated trust-kernel and protected-surface documentation.

## 7. Governance Authority

Governance authority is the authority to propose, review, record, supersede, or retire governance guidance through repository-recognized processes.

Governance documents may describe decision models, RFC expectations, review criteria, impact classifications, protected-surface assessments, and evidence requirements. They do not create hidden approval authority, merge authority, enforcement authority, truth finality, or autonomous governance.

Governance proposals that affect or reinterpret protected surfaces, trust-kernel boundaries, policy evaluation, workflow governance, schema governance, validator governance, signing governance, federation governance, or canonical record boundaries must surface expected human-supervised validation needs.

## 8. Constitutional Authority

Constitutional authority describes durable repository principles such as evidence precedence, no hidden authority, role equality before repository evidence, auditability, and limits on unsupported claims.

Constitutional authority is evidence-bound. It may guide interpretation of governance and project-control materials, but it does not bypass merged repository files, protected repository evidence, repository-defined checks, human review decisions, or human-supervised validation requirements.

Constitutional documents are not runtime enforcement, merge approval, release approval, security certification, forensic certainty, production readiness, truth finality, or autonomous governance.

## 9. Operational Authority

Operational authority covers day-to-day repository work such as scoping tasks, preparing documentation, collecting evidence, running checks, proposing PRs, reviewing diffs, and recording outcomes.

Operational authority is limited by:

- task scope;
- protected-path rules;
- trust-kernel boundaries;
- repository-defined checks;
- reviewer obligations;
- human-supervised validation requirements;
- audit trail expectations.

Operational guidance may help contributors act consistently, but it does not create approval authority, merge authority, release authority, or truth finality.

## 10. Role Authority Model

Roles in HC-TRUST-LAYER can differ in responsibility, access, review expectations, and operational permissions.

Role authority is always evidence-bound and reviewable:

- no role is above repository evidence;
- no role bypasses protected-path boundaries;
- no role bypasses repository-defined checks;
- no role bypasses human-supervised validation where required;
- no role turns advisory output into authoritative repository evidence without reviewable support;
- no role creates security certification, production readiness, forensic certainty, truth finality, or autonomous governance by assertion.

## 11. Founder / Project Steward Role

The founder or project steward may provide strategic direction, prioritize work, define project-control needs, request reviews, and require human-supervised validation for sensitive trust-kernel-impacting work.

Founder / project steward authority must remain evidence-bound and reviewable. It does not sit above repository evidence, does not silently override protected-path or trust-kernel boundaries, and does not create approval authority, merge authority, release authority, security certification, production readiness, forensic certainty, truth finality, or autonomous governance by role status alone.

## 12. Maintainer Role

Maintainers may coordinate repository work, review PRs, apply labels, steward project-control documentation, assess scope, request checks, and help maintain audit trail continuity.

Maintainer authority does not create truth finality. Maintainers must remain bound by repository evidence, protected-path expectations, repository-defined checks, review obligations, and human-supervised validation requirements for sensitive trust-kernel-impacting work.

## 13. Reviewer Role

Reviewers may inspect proposed changes, compare claims against repository evidence, request revisions, confirm check outcomes, and identify protected-surface or trust-kernel impacts.

Reviewer authority does not create security certification. A reviewer approval or comment is part of the review record, but it does not independently create production readiness, forensic certainty, truth finality, autonomous governance, release authority, or a bypass around required validation.

## 14. CODEOWNER Role

CODEOWNER status may route review obligations for files, directories, or protected surfaces.

CODEOWNER status does not bypass human-supervised validation. It does not place a CODEOWNER above repository evidence, repository-defined checks, protected-path boundaries, trust-kernel boundaries, or governance expectations.

CODEOWNER review should be treated as part of the audit trail, not as automatic security certification, production readiness, forensic certainty, truth finality, release authority, or autonomous governance.

## 15. Contributor Role

Contributors may propose changes, prepare documentation, run checks, collect evidence, and respond to review.

Contributor authority is limited to the submitted proposal and supporting evidence. Contributors must preserve HC-TRUST-LAYER and HC:// terminology, avoid unsupported authority claims, respect protected-path rules, and report checks accurately.

## 16. AI-Assisted Contributor Role

AI-assisted contributors, including Codex, ChatGPT, Copilot, external AI agents, and similar tools, may help draft, inspect, summarize, and propose changes.

AI-assisted output is advisory unless reviewed and supported by repository evidence. Agent, bot, and chat outputs do not create approval authority, merge authority, release authority, security certification, production readiness, forensic certainty, truth finality, autonomous governance, or validated repository facts by themselves.

AI-assisted contributors must preserve auditability by reporting changed files, checks run, limitations, protected-path status, and relevant evidence.

## 17. Future HC Guide Bot / HC Control Bot Role

Future HC Guide Bot or HC Control Bot behavior should remain advisory unless repository evidence and human review define a narrower validated role.

A future bot may orient contributors, summarize evidence, identify gaps, suggest next actions, prepare bounded reports, and support low-friction operations. It must not claim approval authority, merge authority, release authority, security certification, production readiness, forensic certainty, truth finality, or autonomous governance.

Future automation must remain bounded, explainable, reversible, human-reviewable, and subordinate to repository evidence, repository-defined checks, protected-path boundaries, trust-kernel documentation, and human-supervised validation requirements.

## 18. Human-Supervised Validation Authority

Human-supervised validation is required for sensitive trust-kernel-impacting work and for changes that affect or reinterpret high-sensitivity boundaries.

Human-supervised validation authority is not the same as unchecked personal discretion. It should be tied to repository evidence, review notes, checks, impact assessments, and explicit validation status.

Human-supervised validation should identify:

- affected protected paths or protected concepts;
- affected trust-kernel boundaries;
- expected decision-path differences when policy interpretation is involved;
- checks run and check limitations;
- review participants or review artifacts;
- validation status, such as complete, limited, pending, deferred, or not applicable.

## 19. Authority Conflict Resolution

When authority claims conflict, resolve them by evidence precedence rather than role status.

Conflict handling should:

1. identify the claim and affected authority surface;
2. collect repository evidence;
3. classify protected-path, trust-kernel, canonical record, policy, signing, federation, schema, validator, workflow, release, and governance impact as applicable;
4. run applicable repository-defined checks;
5. request reviewer input where needed;
6. require human-supervised validation where sensitive trust-kernel impact exists;
7. record the outcome in PR records, commits, review notes, or project-control documents as appropriate;
8. leave unresolved gaps explicit rather than silently normalizing them.

## 20. Authority Hierarchy

Use the following authority hierarchy when evidence conflicts:

1. Repository evidence.
2. Protected repository evidence.
3. Repository-defined checks.
4. PR records, commits, review notes, and human review decisions.
5. Human-supervised validation where required.
6. Protected-path and trust-kernel boundary documents.
7. Governance and constitutional documents.
8. Release governance and release checklist documents.
9. Project-control operating documents.
10. Machine-readable indexes.
11. `hc_context` advisory files.
12. Agent / bot / chat outputs.

Lower layers may assist interpretation, but they must not override higher layers. Machine-readable indexes and `hc_context` files are advisory navigation aids unless stronger repository evidence gives them specific authority.

## 21. Known Authority Gaps

Known authority gaps include:

- Validation authority remains distributed.
- Release authority is currently implied rather than fully formalized.
- Trust-kernel definition is distributed across multiple files.
- Some protected-path and risk-classification definitions may be stale or narrower than current trust-kernel documentation.
- Founder / maintainer / reviewer / CODEOWNER authority hierarchy needs clearer operational mapping.
- `records/archive` vs `records/archived` remains unresolved elsewhere and should not be silently normalized by this document.

These gaps should be surfaced in future governance or project-control work rather than resolved by inference in this document.

## 22. Risks and Guardrails

Authority ambiguity can create trust risk when roles, agents, documents, checks, or release artifacts are treated as stronger than repository evidence supports.

Guardrails:

- keep authority claims evidence-bound;
- report checks accurately;
- preserve audit trail continuity;
- keep protected-path and trust-kernel boundaries visible;
- require human-supervised validation for sensitive trust-kernel-impacting work;
- avoid production-readiness, security-certification, forensic-certainty, truth-finality, or autonomous-governance claims;
- avoid silently normalizing unresolved terminology, path, or authority gaps;
- keep PRs small, scoped, reversible, and reviewable.

## 23. Related Documents

- `AGENTS.md`
- `HC_BOOTSTRAP.md`
- `docs/project-control/hc-control-center.md`
- `docs/project-control/agent-operating-model.md`
- `docs/project-control/release-governance.md`
- `docs/project-control/trust-kernel-boundary.md`
- `docs/project-control/validation-architecture.md`
- `docs/project-control/governance-change-protocol.md`
- `docs/project-control/hc-constitutional-layer.md`
- `docs/project-control/project-state.md`
- `docs/project-control/task-ledger.md`
- `docs/project-control/active-work-registry.md`
- `docs/project-control/decision-registry.md`
- `docs/project-control/hc-guide-bot-readiness.md`
- `docs/project-control/hc-control-bot.md`
- `docs/project-control/v0.1.0-release-checklist.md`
- `docs/trust-impact-analysis.md`
- `docs/trust-review-workflow.md`
- `docs/verification-map.md`
- `docs/protocol-graph-index.md`
- `docs/verification-map-index.md`
- `docs/trust-kernel-index.md`
- `protocol-graph.json`
- `verification-map.json`
- `trust-kernel-index.json`
- `hc_context` advisory files
