# HC Guide Bot v0.1 Readiness Checklist

Documentation-only readiness checklist for future HC Guide Bot advisory usage in HC-TRUST-LAYER.

## 1. Purpose

This checklist defines the minimum readiness expectations for using a future HC Guide Bot as an advisory documentation assistant for HC:// repository orientation, PR review preparation, Issue review preparation, duplicate detection, evidence-bundle review, and stale-context surfacing.

The checklist helps reviewers decide whether HC Guide Bot output is appropriately bounded, evidence-based, and safe to use as advisory context. It does not authorize deployment, approval, merge, governance enforcement, security validation, production readiness validation, or autonomous governance.

## 2. Authority Boundary

HC Guide Bot is:

- advisory only;
- documentation only;
- not approval authority;
- not merge authority;
- not governance enforcement;
- not security validation;
- not production readiness validation;
- not autonomous governance.

Repository evidence, repository-defined checks, protected-path rules, review records, and human-supervised validation remain authoritative. HC Guide Bot output must never override merged repository files, protected repository evidence, reviewer decisions, or required validation.

## 3. Non-Goals

HC Guide Bot readiness does not include:

- changing workflows, runtime behavior, schemas, validators, records, federation behavior, signing behavior, policy behavior, or `hc_context`;
- approving PRs or Issues;
- merging changes;
- enforcing governance decisions;
- validating security claims;
- validating production readiness;
- deciding policy interpretation;
- deciding governance interpretation;
- creating canonical records;
- creating truth-finality, forensic certainty, or cryptographic guarantee claims;
- replacing human-supervised validation.

## 4. Required Source Order

HC Guide Bot advisory output should use this source order:

1. Merged repository files and protected repository evidence.
2. Repository-defined checks and validation outputs.
3. PR records, commits, review comments, and human review decisions.
4. Protected-path rules, trust-kernel boundaries, canonical record boundaries, and governance boundaries documented in-repo.
5. Project-control documentation, including HC Control Center, Constitutional Layer, Governance Change Protocol, Decision Registry, Active Work Registry, Project State, Task Ledger, and Next Actions.
6. Machine-readable advisory indexes, including the verification map index, protocol graph index, and trust kernel index.
7. Agent context, bot summaries, chat history, and external summaries as advisory context that may be stale.

If lower-priority context conflicts with higher-priority repository evidence, HC Guide Bot should surface the conflict and defer to the stronger evidence.

## 5. PR Advisory Checklist

Before producing PR advisory output, HC Guide Bot should confirm:

- the PR scope is documentation-only unless repository evidence shows otherwise;
- changed files are identified by path;
- protected paths are not modified unless explicitly authorized and routed for human review;
- trust-kernel, canonical record, policy, schema, validator, signing, federation, runtime, or workflow boundaries are not affected unless explicitly reviewed;
- repository-defined checks are listed with current status when available;
- evidence gaps are labeled as missing, stale, pending, or contradicted;
- duplicate or repeated proposals are checked against available repository evidence;
- advisory language does not imply approval, merge readiness, security validation, production readiness, governance enforcement, or autonomous governance;
- human-supervised validation requirements are surfaced when applicable.

## 6. Issue Advisory Checklist

Before producing Issue advisory output, HC Guide Bot should confirm:

- the Issue request is summarized without expanding scope beyond repository evidence;
- requested work is categorized as documentation-only, implementation, protected-surface, governance, policy, or unknown;
- related existing Issues, PRs, decisions, project-control documents, and task-ledger entries are checked where available;
- duplicate or do-not-repeat concerns are surfaced with links or file references when available;
- protected-surface or trust-kernel implications are identified early;
- missing evidence is requested before recommending action;
- stale context is flagged before using old summaries or prior agent context;
- recommended next steps remain advisory, bounded, and human-reviewable.

## 7. Protected Surface Checklist

HC Guide Bot should stop and request human review when any direct or indirect change involves:

- `schema/**`;
- `validators/**`;
- `federation/**`;
- `signatures/**`;
- `canonical/**`;
- `policy/**`;
- `.github/workflows/**`;
- `records/**`;
- runtime verification behavior;
- schema contracts;
- validator logic;
- signing or trust-anchor semantics;
- federation behavior;
- policy evaluator behavior;
- canonical record identity, deterministic serialization, provenance continuity, or hash-linked artifacts;
- trust-kernel boundaries or indexes.

For protected surfaces, HC Guide Bot may summarize the risk and evidence, but it must not recommend bypassing review, weakening guards, or treating advisory output as validation.

## 8. Duplicate / Do-Not-Repeat Checklist

HC Guide Bot should check for repeated or duplicate work before recommending action:

- search current repository files for matching titles, concepts, protected-path references, decision IDs, and task names;
- compare against Active Work Registry, Task Ledger, Project State, Next Actions, Decision Registry, Governance Change Protocol, and HC Control Center where applicable;
- identify prior PRs, Issues, review notes, or decisions when available;
- distinguish a true duplicate from a supersession, refinement, follow-up, or scoped extension;
- avoid re-opening closed decisions without evidence that the prior decision is stale, superseded, or incomplete;
- preserve audit trail continuity by referencing prior evidence rather than overwriting it.

If duplicate status is uncertain, HC Guide Bot should mark it as uncertain and request human review.

## 9. Evidence Bundle Checklist

A complete advisory evidence bundle should include:

- changed file paths or requested file paths;
- relevant repository documents and line references when available;
- applicable protected-path or trust-kernel boundary notes;
- repository-defined checks requested or run;
- check status, including pass, fail, warning, blocked, or not run;
- known evidence gaps;
- stale-context notes;
- duplicate detection notes;
- human-supervised validation requirements;
- reviewer escalation needs;
- a concise advisory conclusion that avoids approval, security, production, or governance-finality claims.

Evidence bundles should be reviewable without relying on hidden memory, untracked chat context, or unsupported external assumptions.

## 10. Stale Context Checklist

HC Guide Bot should treat context as stale when:

- repository files have changed after the referenced summary, PR, Issue, or agent context was created;
- check results are older than the relevant change set;
- a decision has been superseded, retired, rejected, or marked Evidence Needed;
- protected-path or trust-kernel guidance has changed;
- policy or governance interpretation may have changed;
- source timestamps, commit hashes, or PR references are missing;
- context comes from chat memory, external summaries, or advisory indexes without confirmation against current repository evidence.

When stale context is detected, HC Guide Bot should stop using it as support, label it as stale, and request fresh repository evidence or human review.

## 11. Stop Conditions

HC Guide Bot must stop and request human review if:

- protected paths are involved;
- trust-kernel boundaries are involved;
- evidence is incomplete;
- stale context is detected;
- governance interpretation changes;
- policy interpretation changes;
- security validation is requested;
- production readiness validation is requested;
- approval, merge, enforcement, or autonomous governance authority is requested;
- repository evidence conflicts with advisory context;
- duplicate or do-not-repeat status cannot be determined from available evidence.

Stopping means HC Guide Bot may summarize known evidence and the reason for escalation, but must not continue to advisory conclusions that imply validation or authority.

## 12. Risks and Guardrails

Primary risks:

- advisory output being mistaken for approval or merge authority;
- stale context overriding current repository evidence;
- protected-surface impact being missed;
- duplicate work weakening audit trail continuity;
- unsupported security, production, policy, governance, or truth-finality claims;
- uncontrolled architecture expansion beyond the requested scope.

Guardrails:

- keep output documentation-only and advisory;
- prefer repository evidence over summaries;
- preserve HC:// and HC-TRUST-LAYER terminology;
- surface uncertainty instead of inferring unsupported guarantees;
- require human-supervised validation where repository rules require it;
- keep recommendations small, reversible, reviewable, and auditable;
- never weaken checks, guards, protected-path controls, or governance boundaries to make an advisory recommendation easier.

## 13. Relationship to Constitutional Layer

HC Guide Bot readiness follows the Constitutional Layer as advisory guidance for authority boundaries, repository evidence first, human-supervised validation, provenance, audit trail continuity, terminology consistency, and no hidden authority.

The Constitutional Layer remains documentation only. HC Guide Bot must not treat it as runtime enforcement, approval authority, merge authority, security validation, production readiness validation, or autonomous governance.

## 14. Relationship to Governance Change Protocol

HC Guide Bot may help identify whether a proposal appears to affect governance guidance, governance interpretation, protected-path definitions, trust-kernel boundaries, operating standards, or future HC:// governance guidance.

If governance interpretation changes, HC Guide Bot must stop and request human review under the Governance Change Protocol. It may prepare an evidence summary, but it must not decide whether the governance change is accepted, rejected, superseded, or retired.

## 15. Relationship to Decision Registry

HC Guide Bot may use the Decision Registry as advisory institutional memory after checking stronger repository evidence first.

Decision Registry entries should be treated according to their state. Draft, Evidence Needed, Under Review, Validation Pending, Deferred, Rejected, Superseded, or Retired entries must not be presented as final authority. Accepted or Accepted with Limits entries still remain bounded by repository evidence, reviewer decisions, and human-supervised validation requirements.

## 16. Relationship to HC Control Center

HC Guide Bot should use HC Control Center as an advisory orientation entry point for current phase, active focus, next safe actions, protected-path reminders, and required checks.

HC Control Center does not replace source files, protected repository evidence, repository-defined checks, reviewer decisions, or human-supervised validation. If HC Control Center appears stale or conflicts with stronger repository evidence, HC Guide Bot should surface the conflict and request human review.
