# Governance Review Conversation Resolution (Advisory)

## Purpose

This document defines governance review conversation resolution rules for HC:// pull request flow in HC-TRUST-LAYER.

The goal is to preserve human-supervised validation, clear audit trail continuity, and explicit maintainer accountability for review outcomes.

## Scope and Safety Boundary

This governance clarification is documentation-only.

- No runtime verification behavior changes.
- No canonical schema changes.
- No validator weakening.
- No signing or security workflow changes.
- No unrestricted auto-merge behavior.
- No autonomous governance claims.

## Merge Blocking Rule for Unresolved Conversations

Unresolved pull request review conversations are merge-blocking in governance-controlled PR flow.

Maintainers must treat unresolved review conversations as open governance state until each conversation is reviewed and intentionally resolved.

## Required Maintainer Review Behavior

For each review conversation, maintainers must complete this sequence:

1. Inspect the review comment and related context.
2. Decide whether the comment is valid for the proposed change scope.
3. Apply a fix or update when the comment is valid.
4. Resolve the conversation only after the review step is complete and any required update is applied.

If a comment is not valid, maintainers should record rationale in the conversation before resolution so the audit trail remains attributable and inspectable.

## Governance Checkpoint Comment Classes

The following governance comments must be treated as human-supervised checkpoints:

- risk classification
- auto-merge eligibility
- protected paths
- policy inconsistency

These checkpoint classes require deliberate maintainer review and must not be treated as routine noise.

## Auto-Merge Constraint

Auto-merge must not bypass unresolved governance review conversations.

If a governance checkpoint conversation remains unresolved, merge must remain blocked until human-supervised review is completed and the conversation is explicitly resolved.

## Audit Trail and Review Continuity

Maintainers and reviewers should preserve review chronology so governance decisions remain inspectable across:

- review comment intake
- validation decision
- update or non-update rationale
- explicit conversation resolution

This preserves provenance and canonical record alignment for governance oversight without implying autonomous governance authority.

## Relationship to Existing Governance Docs

Use this document with:

- `docs/governance/pr-governance-preflight.md`
- `docs/governance/branch-protection-enforcement-baseline.md`
- `docs/governance/governance-preflight-workflow.md`
- `docs/governance/governance-structure-map.md`

Together, these references support consistent HC:// and HC-TRUST-LAYER governance review hygiene.
