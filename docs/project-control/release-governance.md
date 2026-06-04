# Release Governance

Documentation-only release governance model for HC-TRUST-LAYER. This document describes how v0.1.0 and future HC:// releases should be scoped, reviewed, evidenced, approved, tagged, published, audited, corrected, superseded, or retired.

## 1. Purpose

Release governance gives contributors and reviewers a shared advisory model for release preparation and review.

It helps define:

- release scope;
- required release evidence;
- release signoff expectations;
- version, tag, release-note, and changelog ownership;
- trust-kernel and protected-surface review routing;
- audit trail expectations;
- correction, supersession, retirement, and incident handling.

Repository evidence is authoritative. Release governance is advisory and documentation-only. v0.1.0 should be framed as early-stage advisory HC:// verification infrastructure unless repository evidence says otherwise.

## 2. Authority Boundary

Release governance does not create authority beyond repository evidence, reviewer decisions, and repository-defined checks.

A release document does not create merge authority.
A release document does not create approval authority.
A release document does not create security certification.
A release document does not create production readiness.
A release document does not create forensic certainty.
A release document does not create truth finality.
A release document does not create autonomous governance.

Release governance does not override:

- merged repository files;
- protected repository evidence;
- repository-defined checks;
- PR review decisions;
- human-supervised validation requirements;
- protected-path rules;
- trust-kernel boundaries;
- canonical record boundaries;
- policy, signing, federation, schema, validator, workflow, runtime, or record governance documented elsewhere in the repository.

Human-supervised validation remains required for sensitive trust-kernel-impacting release content.

## 3. Release Governance Principles

Release governance should remain:

- **Evidence-led:** repository files, commits, tags, release notes, changelog entries, checks, and review records provide the release basis.
- **Documentation-first:** release preparation should clarify scope and evidence before implying operational readiness.
- **Minimal and auditable:** each release should have a bounded scope, traceable changes, and a clear audit trail.
- **Protected-surface aware:** releases should identify whether protected paths or protected concepts are affected.
- **Human-supervised:** sensitive trust-kernel-impacting release content requires reviewer oversight and human-supervised validation.
- **Non-final:** releases can be corrected, superseded, or retired when repository evidence changes.
- **No unsupported claims:** release materials must avoid production-readiness, security-certification, forensic-certainty, truth-finality, or autonomous-governance claims unless implemented and validated in-repo.

## 4. Release Authority Model

Release authority should be treated as a reviewer-controlled repository process, not as an output of this document.

A release authority model should identify:

- who may propose a release;
- who may approve release scope;
- who may approve release notes;
- who may create or move tags;
- who may publish release artifacts;
- who may approve corrections, supersession, or retirement;
- which checks and evidence are required before each action.

Until formalized elsewhere, release authority is currently implied rather than fully formalized. Operators should not infer authority from advisory project-control documents, agent context, or release templates.

## 5. Release Scope Approval

Release scope approval should happen before tagging or publication.

A release scope proposal should include:

- target release version;
- release objective;
- included commits or PRs;
- excluded or deferred work;
- changed files summary;
- protected-path status;
- trust-kernel impact status;
- known limitations;
- required checks;
- expected reviewers or approvers;
- human-supervised validation status when sensitive trust-kernel-impacting content is included.

Scope approval means reviewers agree that the release candidate may continue through the documented release path. It does not create merge authority, approval authority, security certification, production readiness, forensic certainty, truth finality, or autonomous governance.

## 6. Release Evidence Package

Each release should collect a release evidence package before tag creation or publication.

The release evidence package should include:

- release version;
- release candidate commit;
- tag name;
- release notes path;
- changelog section;
- changed files summary;
- checks run;
- protected-path status;
- trust-kernel impact status;
- human-supervised validation status;
- known limitations;
- approver / reviewer evidence.

Evidence should be traceable to repository files, commits, PRs, tags, checks, review records, and release notes. If evidence is missing, the release package should state the gap directly and avoid unsupported authority or readiness claims.

## 7. Release Signoff Model

Release signoff should confirm that reviewers have inspected the release evidence package and that unresolved gaps are documented.

A release signoff should cover:

- release version and tag name;
- release candidate commit;
- release notes and changelog location;
- changed files and release scope;
- required checks and outcomes;
- protected-path status;
- trust-kernel impact status;
- human-supervised validation status;
- known limitations and follow-up work;
- reviewer or approver evidence.

Release signoff is not autonomous governance. Release signoff does not replace repository review, required checks, protected-surface review, or human-supervised validation.

## 8. Release Checklist

Before tagging or publishing a release, reviewers should confirm:

- [ ] Release version is identified.
- [ ] Release candidate commit is identified.
- [ ] Tag name is identified.
- [ ] Release notes path is identified.
- [ ] Changelog section is identified.
- [ ] Changed files summary is prepared.
- [ ] Required checks are run or documented as unavailable.
- [ ] Protected-path status is documented.
- [ ] Trust-kernel impact status is documented.
- [ ] Human-supervised validation status is documented.
- [ ] Known limitations are documented.
- [ ] Reviewer or approver evidence is captured.
- [ ] Release claims avoid production-readiness, security-certification, forensic-certainty, truth-finality, and autonomous-governance language unless supported by repository evidence.

## 9. Version Ownership

Version ownership should define who may propose, reserve, approve, and publish a release version.

Version ownership should document:

- version naming convention;
- relationship between release branches, commits, and tags;
- rules for pre-release identifiers;
- rules for patch, minor, and major versions;
- reviewer expectations for version changes;
- correction, supersession, or retirement handling.

Version ownership is not yet fully documented for HC-TRUST-LAYER. Until it is formalized, version changes should be treated as reviewer-controlled repository actions.

## 10. Tag Ownership

Tag ownership should define who may create, update, delete, or retire release tags.

Tag handling should document:

- tag name;
- tagged commit;
- tag creation evidence;
- tag protection or review expectations when available;
- correction process if a tag is incorrect;
- supersession or retirement notes when applicable.

Tags are high-sensitivity release markers because they can shape external interpretation of repository state. A tag must not imply production readiness, security certification, forensic certainty, truth finality, or autonomous governance unless repository evidence supports that claim.

## 11. Release Notes Ownership

Release notes ownership should identify who prepares, reviews, approves, and publishes release notes.

Release notes should include:

- release version;
- release candidate commit;
- tag name;
- summary of changes;
- protected-path status;
- trust-kernel impact status;
- validation and check summary;
- known limitations;
- links to changelog and review evidence;
- correction, supersession, or retirement notes when applicable.

Release notes should frame v0.1.0 as early-stage advisory HC:// verification infrastructure unless repository evidence says otherwise.

## 12. Changelog Requirements

A release should have a changelog section or equivalent release-history entry.

The changelog section should identify:

- release version;
- release date when known;
- release candidate commit or final tag;
- notable documentation, governance, verification map, protocol graph, implementation, or protected-surface changes;
- known limitations;
- correction or supersession references when applicable.

The changelog should not overstate readiness, certification, certainty, finality, or autonomous governance.

## 13. Trust-Kernel Release Review

A trust-kernel release review is required when release content affects, reinterprets, or appears to alter trust-kernel boundaries.

Reviewers should assess whether release content affects:

- runtime verification behavior;
- schema contracts;
- validator logic;
- canonical record handling;
- provenance continuity;
- deterministic serialization assumptions;
- hash-linked artifacts;
- record identity;
- policy interpretation or routing;
- signing or trust-anchor semantics;
- federation behavior;
- protected workflow behavior;
- machine-readable trust-kernel indexes.

Human-supervised validation remains required for sensitive trust-kernel-impacting release content. A trust-kernel release review should document affected surfaces, expected decision-path differences when applicable, checks run, reviewer evidence, and unresolved limitations.

## 14. Protected-Surface Release Review

A protected-surface release review should document whether release content modifies or reinterprets protected paths or protected concepts.

Protected-surface review should identify:

- protected paths changed, if any;
- protected concepts affected, if any;
- whether the release is documentation-only;
- whether runtime, schema, validator, record, policy, federation, signing, workflow, or source-code behavior changed;
- whether trust-kernel indexes or `hc_context` changed;
- required reviewer routing;
- required checks;
- human-supervised validation status.

If protected paths are not modified, the release package should state that status clearly. If protected paths are modified, the release package should identify reviewer escalation and validation evidence.

## 15. Human-Supervised Validation Requirements

Human-supervised validation remains required for sensitive trust-kernel-impacting release content.

Release reviewers should document human-supervised validation status as one of:

- **Not applicable:** no sensitive trust-kernel-impacting content is included.
- **Required and pending:** sensitive content is included, but validation has not been completed.
- **Completed with evidence:** validation evidence is linked or summarized.
- **Blocked:** validation could not be completed, with the reason documented.

A release must not use advisory release governance to bypass validation requirements.

## 16. Release Audit Trail

A release audit trail should make later review possible without relying on chat memory, hidden context, or unsupported summaries.

The audit trail should include:

- release version;
- release candidate commit;
- tag name;
- release notes path;
- changelog section;
- changed files summary;
- checks run and outcomes;
- protected-path status;
- trust-kernel impact status;
- human-supervised validation status;
- known limitations;
- approver / reviewer evidence;
- correction, supersession, retirement, or incident references when applicable.

Audit trail records should distinguish repository evidence from advisory analysis.

## 17. Release Rollback and Correction

Release rollback and correction should be explicit, documented, and reviewer-controlled.

A correction package should include:

- affected release version and tag;
- reason for correction;
- affected files or release artifacts;
- corrected commit, tag, release notes, or changelog entry;
- protected-path and trust-kernel impact status;
- checks run;
- reviewer evidence;
- known limitations after correction.

Rollback or correction does not erase prior audit trail evidence. Prior release evidence should remain traceable, with correction notes explaining what changed and why.

## 18. Post-Release Review

Post-release review should confirm whether release evidence matched the final published state.

Reviewers should check:

- final tag points to the expected commit;
- release notes and changelog match the release scope;
- changed files summary remains accurate;
- checks are recorded accurately;
- protected-path and trust-kernel impact status remain accurate;
- known limitations are visible;
- follow-up issues or tasks are captured;
- incident, correction, supersession, or retirement needs are identified.

Post-release review should not imply production readiness, security certification, forensic certainty, truth finality, or autonomous governance.

## 19. Release Incident Handling

A release incident occurs when release evidence, tag state, release notes, changelog content, approval status, protected-surface status, or trust-kernel impact status is materially wrong, incomplete, misleading, or stale.

Incident handling should:

- preserve the audit trail;
- identify affected release materials;
- identify the repository evidence that conflicts with the release claim;
- classify protected-surface and trust-kernel impact;
- document immediate containment steps;
- document correction, supersession, or retirement actions;
- document required checks and human-supervised validation status;
- preserve reviewer evidence.

Incident handling must not create autonomous governance or unsupported finality claims.

## 20. Known Release Governance Gaps

Known gaps:

- Release authority is currently implied rather than fully formalized.
- Release evidence package is not yet standardized.
- Release signoff process is not yet standardized.
- Version, tag, changelog, and release-note ownership need clearer documentation.
- Release rollback and post-release review need explicit release-specific handling.

These gaps should be treated as follow-up governance work. They do not block documentation-only release-governance clarification, but they should be visible in release planning and review.

## 21. Risks and Guardrails

Risks:

- release notes may overstate repository maturity;
- tags may be interpreted as readiness claims;
- missing evidence may hide protected-surface impact;
- trust-kernel-impacting changes may be released without adequate validation;
- release corrections may obscure prior audit trail evidence;
- advisory governance language may be mistaken for approval authority.

Guardrails:

- keep release scope small and reviewable;
- state known limitations directly;
- separate repository evidence from advisory interpretation;
- avoid unsupported readiness, certification, certainty, finality, and autonomous-governance claims;
- document checks that were run and checks that could not run;
- escalate sensitive trust-kernel-impacting release content for human-supervised validation;
- preserve correction, supersession, retirement, and incident evidence.

## 22. Related Documents

- `AGENTS.md`
- `HC_BOOTSTRAP.md`
- `docs/project-control/hc-control-center.md`
- `docs/project-control/hc-audit-layer.md`
- `docs/project-control/governance-change-protocol.md`
- `docs/project-control/trust-kernel-boundary.md`
- `docs/project-control/project-state.md`
- `docs/project-control/task-ledger.md`
- `docs/project-control/active-work-registry.md`
- `docs/project-control/shift-change-checklist.md`
- `docs/verification-map.md`
- `docs/protocol-graph-index.md`
- `docs/trust-kernel-index.md`
