# Signed Validator Identity

> **Status:** Research
>
> **Exploratory / Non-Canonical Notice:** This document is exploratory and non-canonical. It does not define production behavior, modify active HC:// protocol requirements, change active runtime behavior, or change active governance behavior.

## Research Question

Could future HC:// validator identities be represented with signed metadata while preserving clear trust anchor boundaries and avoiding unsupported security claims?

## Concept

Signed validator identity research may explore how a validator could publish identity metadata, operational scope, contact or stewardship information, and key lifecycle notes. The research goal is accountable provenance for validator operators, not automatic trust.

Potential metadata areas:

- validator display name and operator scope;
- public review contact or stewardship reference;
- supported validation capabilities;
- key lifecycle status;
- revocation or retirement notes; and
- links to audit trail records when active documentation supports them.

## Boundary Notes

This document does not modify signing logic, trust anchors, schemas, validators, federation logic, runtime behavior, or governance enforcement. It does not claim that signed identities are implemented, secure by default, or production-ready.

## Open Questions

- Which identity fields are necessary and which are optional?
- How should key rotation and retirement be documented without affecting current signing assumptions?
- What review is required before validator identity data becomes active protocol metadata?
- How should identity provenance appear in public verification without misleading authority claims?

## Promotion Considerations

Promotion would require reviewer escalation for signing and trust anchor semantics, schema impact review, security review, human-supervised validation, and clear updates to active documentation. Until then, this concept remains separate from active TODOs.
