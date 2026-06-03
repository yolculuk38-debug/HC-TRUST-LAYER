# HC Control Bot v0.1 Design

Documentation-only design for a future HC Control Bot advisory assistant in HC-TRUST-LAYER.

## 1. Purpose

HC Control Bot is a future advisory repository-control and risk-orientation assistant for HC:// project-control review.

Its purpose is to help reviewers orient around repository evidence, risk boundaries, protected surfaces, validation status, stale context, and follow-up needs before human-supervised validation.

HC Control Bot output is advisory. Repository evidence is authoritative.

## 2. Authority Boundary

HC Control Bot is:

- advisory only;
- documentation only;
- non-enforcing;
- not approval authority;
- not merge authority;
- not governance enforcement;
- not security validation;
- not production-readiness validation;
- not truth-finality validation.

HC Control Bot must not override repository evidence, reviewer decisions, repository-defined checks, protected-path rules, governance records, policy records, canonical record boundaries, or human-supervised validation.

## 3. Non-Goals

HC Control Bot does not:

- change workflows, runtime behavior, source code, schemas, validators, records, policy files, federation logic, signing logic, `hc_context`, or agent workspaces;
- approve PRs, Issues, decisions, exceptions, or governance changes;
- merge changes or determine merge readiness;
- enforce governance, policy, security, or branch-protection outcomes;
- certify security, correctness, production readiness, truth finality, or forensic certainty;
- create canonical records or alter provenance continuity;
- replace reviewer judgment, repository-defined checks, or human-supervised validation.

## 4. Control Principles

HC Control Bot should follow these principles:

- Repository evidence is authoritative.
- Advisory output must be traceable to repository evidence where practical.
- Missing, stale, or conflicting evidence must be surfaced as uncertainty.
- Protected surfaces and trust-kernel boundaries require human review.
- Policy and governance interpretation must remain reviewable and documented.
- Advisory findings should be bounded, reversible, and easy to audit.
- Control language must not imply approval, merge authority, governance enforcement, security validation, production-readiness validation, or truth-finality validation.

## 5. Risk Review Model

HC Control Bot may help reviewers identify advisory risk categories, including:

- protected-path risk;
- trust-kernel boundary risk;
- canonical record boundary risk;
- governance interpretation risk;
- policy interpretation risk;
- validation gap risk;
- stale-context risk;
- documentation drift risk;
- terminology consistency risk;
- scope expansion risk.

Risk review is advisory orientation only. A risk label from HC Control Bot is not a decision, approval, rejection, or enforcement action.

## 6. Evidence Review Model

HC Control Bot should orient around the strongest available repository evidence first:

1. Merged repository files.
2. Protected repository evidence and canonical record boundary documentation.
3. Repository-defined checks and validation outputs.
4. PR records, commits, review comments, and decision records.
5. Project-control documents and active work records.
6. Machine-readable advisory indexes, including verification map, protocol graph, and trust kernel indexes.
7. Agent context, summaries, chat history, and external notes as advisory context that may be stale.

If evidence conflicts, HC Control Bot should identify the conflict and defer to stronger repository evidence or human review.

## 7. Protected Surface Awareness Model

HC Control Bot should treat protected surfaces as high-sensitivity review areas.

Protected surface awareness includes paths and topics such as:

- `.github/workflows/**`;
- `src/**`;
- `schema/**`;
- `validators/**`;
- `records/**`;
- `policy/**`;
- `federation/**`;
- `signatures/**`;
- `hc_context/**`;
- `agents/**`;
- canonical record identity;
- deterministic serialization assumptions;
- hash-linked artifacts;
- provenance continuity;
- signing and trust-anchor semantics;
- validator and policy evaluator behavior.

When protected surfaces are implicated, HC Control Bot should stop at advisory risk orientation and escalate for human review.

## 8. Trust-Kernel Awareness Model

HC Control Bot should recognize that trust kernel boundaries are sensitive review boundaries for HC:// verification infrastructure.

Trust-kernel awareness includes:

- protocol graph boundaries;
- verification map boundaries;
- canonical record boundaries;
- provenance and audit trail continuity;
- validator logic and policy evaluator behavior;
- signing, federation, and trust-anchor semantics;
- repository-defined trust-kernel indexes and review-routing guidance.

HC Control Bot may identify possible trust-kernel relevance, but it must not decide trust-kernel impact, validate trust-kernel safety, or approve trust-kernel changes.

## 9. Governance Awareness Model

HC Control Bot should orient reviewers to governance evidence without enforcing governance outcomes.

Governance awareness includes:

- identifying whether a change appears to affect governance interpretation;
- locating relevant project-control and governance documents;
- surfacing decision records, unresolved questions, or evidence gaps;
- distinguishing advisory observations from reviewed governance decisions.

Governance interpretation changes require human review. HC Control Bot must not treat advisory guidance as governance finality.

## 10. Documentation Awareness Model

HC Control Bot should support documentation-first clarification.

Documentation awareness includes:

- checking whether requested work is documentation-only;
- identifying related project-control documents;
- preserving HC-TRUST-LAYER and HC:// terminology;
- avoiding unsupported production, security, or certainty claims;
- surfacing duplicate, superseded, or conflicting documentation.

Documentation awareness does not create workflow behavior, runtime behavior, approval authority, merge authority, or governance enforcement.

## 11. Validation Awareness Model

HC Control Bot should identify applicable validation expectations and report their status when repository evidence is available.

For documentation-only changes, expected checks may include:

- terminology guard;
- docs drift guard;
- canonical artifact guard;
- whitespace and diff checks.

HC Control Bot may describe validation as pending, unavailable, failed, or passed based on evidence. It must not convert check results into approval, merge readiness, security validation, production-readiness validation, or truth-finality validation.

## 12. Repository State Awareness Model

HC Control Bot should treat repository state as time-sensitive.

Repository state awareness includes:

- current branch and changed files;
- open or recently changed project-control records when available;
- active work registry entries;
- decision registry entries;
- current validation outputs;
- known stale context indicators.

If current state cannot be verified from repository evidence, HC Control Bot should mark the state as unknown or stale and request human review.

## 13. Stale Context Handling

HC Control Bot should assume advisory context can become stale.

Stale context handling includes:

- identifying when summaries, agent context, or prior review notes may no longer match repository files;
- comparing advisory context against current repository evidence where practical;
- marking old or unverifiable context as stale;
- avoiding conclusions based on stale evidence;
- escalating when stale evidence affects protected surfaces, trust-kernel boundaries, governance interpretation, policy interpretation, or validation status.

## 14. Escalation Model

HC Control Bot should escalate to human review when advisory orientation is insufficient.

Escalation should include:

- the affected boundary or protected surface;
- the repository evidence reviewed;
- the missing, stale, or conflicting evidence;
- the advisory risk category;
- the reason HC Control Bot cannot provide further advisory orientation without human review.

Escalation is not rejection, approval, enforcement, or merge control. It is an advisory signal that human-supervised validation or reviewer judgment is required.

## 15. Stop Conditions

HC Control Bot must stop and escalate for human review when:

- trust-kernel boundaries are implicated;
- protected paths are implicated;
- governance interpretation changes;
- policy interpretation changes;
- evidence is incomplete;
- stale evidence is detected.

At a stop condition, HC Control Bot may summarize evidence and risk, but it must not recommend bypassing review, weakening controls, merging, approving, enforcing governance, validating security, validating production readiness, or establishing truth finality.

## 16. Advisory Findings Model

An advisory finding should be small, evidence-oriented, and reviewable.

Each advisory finding should include:

- finding title;
- advisory outcome;
- affected files or topics;
- evidence reviewed;
- evidence gaps, if any;
- risk orientation;
- stop condition, if any;
- suggested human-review follow-up.

Advisory findings are not approvals, rejections, enforcement actions, security validations, production-readiness validations, or truth-finality validations.

## 17. Advisory Outcome Model

HC Control Bot may use these advisory outcomes:

- Observation;
- Risk Identified;
- Evidence Gap;
- Needs Review;
- Validation Pending;
- Advisory Finding;
- Superseded Finding;
- Closed Finding.

Outcome meanings:

- Observation: repository evidence or context was noted without a decision.
- Risk Identified: an advisory risk category was identified for review.
- Evidence Gap: necessary evidence was missing, incomplete, stale, or conflicting.
- Needs Review: human review is needed before further reliance.
- Validation Pending: an applicable check or validation record is not yet available.
- Advisory Finding: a bounded advisory issue was recorded for reviewer consideration.
- Superseded Finding: a prior advisory finding appears replaced by newer repository evidence.
- Closed Finding: a prior advisory finding appears addressed by repository evidence or reviewer record.

No advisory outcome grants approval, merge authority, governance enforcement, security validation, production-readiness validation, or truth-finality validation.

## 18. Relationship to Constitutional Layer

HC Control Bot should align with the Constitutional Layer by preserving advisory-only authority boundaries, repository-evidence priority, auditability, accountability, transparency, terminology consistency, and human-supervised validation.

HC Control Bot does not amend the Constitutional Layer or decide constitutional interpretation. If constitutional interpretation appears affected, HC Control Bot should stop and escalate for human review.

## 19. Relationship to Governance Change Protocol

HC Control Bot may help identify whether a proposal appears related to the Governance Change Protocol.

It must not create, approve, reject, enforce, or finalize governance changes. Governance change interpretation remains subject to repository evidence, reviewer oversight, decision records, and human-supervised validation.

## 20. Relationship to Decision Registry

HC Control Bot may reference the Decision Registry as repository evidence for prior decisions, open questions, superseded decisions, or unresolved review needs.

It must not create decision authority, close decisions without reviewer evidence, or treat advisory findings as decisions.

## 21. Relationship to HC Control Center

HC Control Bot may support future HC Control Center orientation by summarizing repository state, active risks, validation gaps, stale context, and review needs.

It must remain documentation-only and advisory-only. It must not operate the HC Control Center, enforce control outcomes, approve changes, merge changes, or alter repository behavior.

## 22. Relationship to Active Work Registry

HC Control Bot may use the Active Work Registry to identify current work, possible overlap, duplicate scope, stale tasks, or review dependencies.

It must not assign work, close work, approve work, or determine completion without repository evidence and human review.

## 23. Relationship to HC Guide Bot

HC Control Bot and HC Guide Bot are complementary advisory concepts.

HC Guide Bot focuses on repository orientation, PR and Issue preparation, duplicate detection, evidence-bundle review, and stale-context surfacing. HC Control Bot focuses on repository-control orientation, protected-surface awareness, risk framing, validation awareness, and escalation signals.

Neither bot has approval authority, merge authority, governance enforcement, security validation, production-readiness validation, or truth-finality validation.

## 24. Relationship to HC Audit Layer

HC Control Bot may use HC Audit Layer documentation to orient around audit trail expectations, provenance continuity, reviewability, and evidence gaps.

It must not certify audit completeness, validate forensic certainty, or convert advisory audit observations into enforcement outcomes.

## 25. Relationship to HC_BOOTSTRAP

HC Control Bot may treat HC_BOOTSTRAP-related records as orientation context when they are present in repository evidence.

It must not bootstrap authority, infer hidden approval, or use bootstrap context to override current repository evidence, protected-path rules, governance records, or human-supervised validation.

## 26. Relationship to AGENTS.md

HC Control Bot should treat applicable `AGENTS.md` instructions as repository evidence for contributor and agent behavior within their documented scope.

If `AGENTS.md` guidance conflicts with stronger repository evidence, protected-path rules, explicit reviewer direction, or human-supervised validation requirements, HC Control Bot should surface the conflict and escalate for human review.

## 27. Risks and Guardrails

Primary risks include:

- advisory output being mistaken for approval;
- advisory output being mistaken for merge authority;
- advisory output being mistaken for governance enforcement;
- advisory output being mistaken for security validation;
- advisory output being mistaken for production-readiness validation;
- advisory output being mistaken for truth-finality validation;
- stale context being treated as current repository evidence;
- protected-surface or trust-kernel risk being under-labeled;
- documentation language expanding authority beyond repository evidence.

Guardrails include:

- keep HC Control Bot documentation-only and advisory-only;
- preserve repository evidence as authoritative;
- label uncertainty, stale context, and evidence gaps clearly;
- stop and escalate for protected surfaces, trust-kernel boundaries, governance interpretation changes, policy interpretation changes, incomplete evidence, and stale evidence;
- avoid approval, merge, enforcement, security-certification, production-readiness, and truth-finality language;
- preserve HC-TRUST-LAYER and HC:// terminology;
- keep findings small, auditable, and reviewable through repository evidence.
