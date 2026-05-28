# HC-TRUST-LAYER Governance Decision Matrix

## Purpose

This matrix provides a concise governance view for HC:// maintainers to classify pull requests (PRs) and determine whether automation can assist merge flow.

Governance in this document is advisory and control-layer only. It does not change runtime behavior, validator behavior, signing/security workflows, schema contracts, or canonical record boundaries.

## Governance Priority Rule

When any rule conflict exists, use:

`manual-review > auto-merge`

Manual-review requirements always override automation eligibility.

## Decision Matrix

| PR category | Risk level | Auto-merge eligibility | Human review requirement | Rationale |
| --- | --- | --- | --- | --- |
| Generic docs-only PRs | Low | Eligible when checks pass and no protected boundary is touched | Recommended (maintainer spot-check) | Non-governance documentation updates are generally low risk, but maintainers should confirm terminology, provenance clarity, and no hidden trust-kernel impact. |
| Governance-policy documentation PRs (`docs/governance/**`, automation policy docs, governance routing docs) | Medium | Not eligible by default | Required (explicit human-supervised validation) | Governance-policy documentation can change review routing and governance interpretation, and must align with `docs/governance/pr-risk-label-taxonomy.md` medium-risk expectations. |
| Tests-only PRs | Low to Medium | Eligible when scoped to non-behavioral test updates and checks pass | Required for scope confirmation | Test updates can indirectly change release confidence; reviewer confirms no runtime, schema, or policy behavior change is implied. |
| Dependency updates | Medium | Conditionally eligible for patch-level, low-impact updates after checks pass | Required | Dependency drift can affect supply chain and transitive behavior; human-supervised validation confirms bounded risk and rollback readiness. |
| Workflow changes | Medium to High | Not eligible by default | Required | CI/governance workflow edits can alter enforcement and audit trail expectations; maintainers must validate control integrity. |
| Schema changes | High | Not eligible | Required (explicit human-supervised validation) | Schema surfaces are canonical record boundaries and require deliberate review for compatibility, determinism, and provenance continuity. |
| Validator/runtime changes | High | Not eligible | Required (explicit human-supervised validation) | Validator and runtime logic are trust-kernel-impacting and must not be merged through automation-only paths. |
| Federation changes | High | Not eligible | Required (explicit human-supervised validation) | Federation behavior affects protocol graph trust relationships and cross-domain verification routing. |
| Policy changes | High | Not eligible | Required (explicit human-supervised validation) | Policy evaluator changes can alter decision paths and must preserve audit trail continuity with reviewer oversight. |
| Signing/security changes | Critical | Never eligible | Required (explicit security-focused human-supervised validation) | Signing keys, trust anchors, and security workflows are high-sensitivity controls that must always remain under direct human oversight. |

## Operating Notes

- Automation may assist labeling, checklist verification, and report generation.
- Automation must remain bounded, explainable, reversible, and human-reviewable.
- This matrix does not authorize unrestricted autonomous merge.
- This matrix does not claim autonomous governance, production trust guarantees, or forensic certainty.
