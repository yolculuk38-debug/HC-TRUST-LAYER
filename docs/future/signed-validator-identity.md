# Signed Validator Identity

> **Status:** Research
>
> **Research-only notice:** This document is future-facing and research-only. It is not implemented. It does not modify runtime behavior, validators, schemas, federation behavior, signing logic, or governance enforcement.
>
> **Boundary warning:** Research ≠ implementation. Identity ≠ authority. Validator ≠ governance. Federation ≠ consensus. Human final authority remains required.

## Problem Statement

HC:// may eventually need a documented way to describe validator identity without implying that an identity alone creates trust, authority, consensus, or governance power.

Current HC-TRUST-LAYER documentation separates provenance, verification map review, trust kernel boundaries, protocol graph navigation, and human-supervised validation. Future validator identity research must preserve those boundaries while exploring whether signed identity metadata could help reviewers understand who operates a validator, how identity continuity is maintained, and how key lifecycle events are documented.

## Motivation

A future signed validator identity model could make validator provenance easier to review by documenting identity continuity, identity rotation history, revocation awareness, and operator stewardship context.

The motivation is reviewability, not automatic trust. A signed validator identity concept should help human reviewers and future tooling reason about trust boundaries, provenance continuity, and federation trust relationships without creating unsupported production guarantees or bypassing human-supervised validation.

## Validator Identity Concepts

A future validator identity may describe a validator-facing identity record for an operator, service, or review-controlled validator role. Research topics include:

- **validator identity:** a stable identifier or descriptor used to discuss a validator across review records;
- **validator provenance:** documented origin, stewardship, and audit trail references for the validator identity;
- **identity continuity:** evidence that a validator identity remains connected to prior reviewed identity records;
- **identity rotation:** a documented transition from one identity key, descriptor, or stewardship reference to another;
- **revocation awareness:** visibility into retired, revoked, superseded, or disputed identity material;
- **trust boundaries:** clear separation between identity evidence, validation output, governance decisions, and policy interpretation; and
- **federation trust relationships:** documented relationships among validators or reviewing parties without implying consensus.

Identity metadata must not be treated as authority by itself. A validator identity can support provenance review, but it cannot replace policy review, governance review, security review, or human final authority.

## Identity Lifecycle

A future identity lifecycle model may include these research stages:

1. **Draft identity record:** proposed validator identity metadata is prepared for review.
2. **Reviewer-visible provenance:** operator scope, stewardship references, audit trail links, and intended validator role are documented.
3. **Activation proposal:** reviewers evaluate whether the identity should become part of an active implementation plan.
4. **Continuity maintenance:** identity updates preserve traceability to earlier reviewed records.
5. **Rotation or retirement:** identity material is replaced, retired, or superseded with documented reasoning.
6. **Revocation awareness:** revoked, compromised, disputed, or invalid identity material is clearly marked for reviewers.

This lifecycle is a research structure only. It does not create active HC:// lifecycle rules, validator requirements, schemas, signing behavior, federation behavior, or governance enforcement.

## Key Rotation Concepts

Future key rotation research may examine how validator identity records could document key transition events while preserving audit trail continuity.

Potential concepts include:

- linking old and new identity material through reviewer-visible provenance;
- documenting the reason for rotation, such as scheduled maintenance, operator change, suspected compromise, or retirement;
- preserving identity continuity without silently transferring trust;
- requiring explicit human-supervised validation before any active trust-kernel-impacting use; and
- distinguishing cryptographic possession from governance authority.

Key rotation concepts in this document do not add cryptographic enforcement, change signing logic, or define production key management requirements.

## Revocation Concepts

Future revocation research may examine how HC:// documentation or tooling could represent revoked, superseded, disputed, compromised, or retired validator identity material.

Revocation awareness should make identity risk visible without claiming automatic enforcement. Research questions include how to display revocation status, how to preserve provenance for revoked material, and how to prevent stale identity data from misleading reviewers.

Revocation awareness is not governance finality. A revocation marker may inform review, but it does not by itself prove wrongdoing, remove authority, create consensus, or enforce policy.

## Provenance Relationship

Validator identity research is connected to provenance because identity records can help explain where validator claims came from, who stewarded them, and how they changed over time.

A future validator provenance model should preserve:

- traceability from validator identity metadata to supporting review artifacts;
- clear separation between identity evidence and validation outcomes;
- continuity across identity rotation and retirement events;
- audit trail references that reviewers can inspect; and
- explicit warnings when provenance is incomplete, disputed, or research-only.

Validator provenance must not imply forensic certainty, production readiness, or automatic truth guarantees.

## Federation Relationship

Future federation trust relationships may reference validator identities to describe how independent validators, review groups, or ecosystem participants recognize each other for review coordination.

This document does not modify federation behavior. Federation references in a future identity model must avoid consensus claims unless consensus behavior is implemented, documented, tested, and reviewed elsewhere in HC-TRUST-LAYER.

Federation ≠ consensus. Federation trust relationships may support visibility into cross-party review boundaries, but they do not create automatic acceptance, governance finality, or shared authority.

## Governance Relationship

Validator identity may inform governance review, but identity is not governance. A validator identity record should not grant decision rights, policy authority, merge authority, or enforcement power.

Any future governance use would require a separate implementation plan, affected-rule analysis, security review, audit trail continuity plan, and human-supervised validation before merge.

Human final authority remains required for trust-kernel-impacting decisions.

## Security Considerations

Future signed validator identity work would need explicit security review before active use. Research considerations include:

- impersonation and look-alike validator identity risks;
- key compromise, stale keys, and undocumented key reuse;
- misleading continuity claims during identity rotation;
- revocation ambiguity or delayed revocation visibility;
- over-trusting identity metadata as authority;
- confusing validator participation with governance approval;
- federation relationship spoofing or reputation laundering;
- audit trail gaps across operator changes; and
- unsafe promotion from research notes into active runtime, schema, signing, federation, or governance behavior.

Security review must confirm that proposed identity mechanisms preserve trust boundaries and do not weaken existing HC:// guardrails.

## Open Questions

- What minimum metadata is needed for validator identity without expanding authority claims?
- How should validator provenance be represented without modifying schemas?
- What evidence is required to establish identity continuity across identity rotation?
- How should revocation awareness be displayed without implying automatic enforcement?
- Which trust boundaries must be visible to public verification users?
- How should federation trust relationships be documented without implying consensus?
- What reviewer roles are required before any signed identity mechanism can leave research status?
- How should disputed, compromised, or retired identity material remain visible for audit trail continuity?

## Non-Goals

This document does not:

- implement signed validator identity;
- modify runtime behavior;
- modify validators;
- modify schemas;
- modify workflows;
- modify federation behavior;
- modify signing logic;
- modify governance enforcement;
- modify governance rules;
- add cryptographic enforcement;
- define production key management requirements;
- create production readiness claims;
- create truth guarantees, forensic certainty claims, or autonomous governance finality;
- grant authority to any validator identity; or
- replace human-supervised validation.

## Promotion Criteria

This research track may only advance through an explicit promotion path:

Future → Candidate → Issue → Security Review → Implementation Plan → PR → Review → Merge

Promotion requires, at minimum:

1. identification of affected active documents, protocol graph references, verification map references, and trust kernel boundaries;
2. explicit impact analysis for validators, schemas, signing logic, federation behavior, governance enforcement, runtime behavior, and canonical record surfaces;
3. affected policy or governance rule analysis if any interpretation or routing behavior would change;
4. security review covering identity spoofing, key lifecycle, revocation awareness, provenance continuity, and federation trust relationships;
5. implementation planning that separates documentation, schema, validator, signing, federation, and governance changes into reviewable scopes;
6. relevant terminology, docs drift, canonical artifact, and test checks reported without bypassing guardrails; and
7. human-supervised validation before any trust-kernel-impacting merge.

Until promotion is completed through that path, signed validator identity remains future-facing, research-only, and non-implemented.
