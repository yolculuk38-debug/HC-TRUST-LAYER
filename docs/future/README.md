# Future Architecture Workspace

> **Exploratory / Non-Canonical Notice**
>
> Documents in `docs/future/` are exploratory and non-canonical. They do not define production behavior, modify active HC:// protocol requirements, change active runtime behavior, or change active governance behavior. They are a curated research workspace for long-term ideas that may never be promoted.

## Purpose

The future architecture workspace separates long-term HC:// research ideas from active protocol, runtime, security, governance, and verification map documentation.

Use this directory to discuss possible directions without mixing them into active TODOs or implementation commitments. Existing `docs/drafts/` content remains in place and is not moved, deleted, or reclassified by this workspace.

## Status Vocabulary

Future documents must use one of these statuses:

- **Idea** — an early concept with unresolved assumptions and no implementation commitment.
- **Research** — an idea being investigated through notes, comparison, constraints, or reviewer discussion.
- **Candidate** — a researched concept that may be proposed for active documentation after impact analysis.
- **Promoted** — a concept that has moved out of `docs/future/` into active documentation through review.
- **Archived** — a concept retained for provenance but no longer under active consideration.

## Promotion Rules

A future concept may move into active HC:// documentation only when all of the following are true:

1. The target active document is identified.
2. The expected impact on protocol requirements, runtime behavior, governance behavior, security posture, and trust kernel boundaries is documented.
3. The change is reviewed through human-supervised validation.
4. Relevant terminology, docs drift, canonical artifact, and scope checks are run and reported.
5. Any affected verification map, protocol graph, or trust kernel routing references are updated in the same reviewed change.
6. The promoted content removes the exploratory and non-canonical labels only where the active document explicitly supports that status.

Promotion must be explicit. A document living in `docs/future/` is never active by implication.

## Workspace Boundaries

This workspace does not:

- define production behavior;
- modify active HC:// protocol requirements;
- change active runtime behavior;
- change active governance behavior;
- alter validators, schemas, signing logic, federation logic, policy enforcement, or workflows;
- create implementation commitments; or
- replace `docs/drafts/`, active architecture documentation, verification map entries, or protocol graph references.

## Current Future Notes

- [Trust Ladder](trust-ladder.md)
- [Validator Federation](validator-federation.md)
- [Signed Validator Identity](signed-validator-identity.md)
- [Trust Exchange](trust-exchange.md)
- [Ecosystem Roadmap](ecosystem-roadmap.md)
