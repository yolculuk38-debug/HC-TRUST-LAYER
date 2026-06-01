# HC-TRUST-LAYER Project Status

HC-TRUST-LAYER is maintained as the canonical repository for HC:// verification infrastructure, provenance documentation, and review-boundary guidance. Current work is focused on keeping the trust kernel reviewable, preserving canonical record validation, and improving documentation and validation coverage without making production-readiness claims.

## Completed infrastructure milestones

- Developer onboarding documentation has been established for contributor and agent workflows.
- Threat model documentation has been added to clarify risk boundaries and review expectations.
- A changelog is present for tracking repository-facing changes.
- CI cleanup and scoped validation work have improved guardrail focus for documentation, examples, and repository checks.
- Example JSON validation scope has been corrected so example validation remains bounded to the intended files.
- Workflow security review documentation has been added to support human-supervised validation of workflow changes.

## Current working principles

- Prefer small, scoped PRs that are easy to review and revert.
- Treat workflow changes as human-supervised and security-sensitive.
- Require explicit review for schema and protocol changes.
- Do not delete tests to hide failures or bypass validation.
- Keep canonical records strictly validated and preserve canonical record boundaries.

## Next candidate tasks

- Branch protection review.
- Verification package standard review.
- Trust score schema review.
- Runtime/API contract stabilization.
- Public explorer hardening.
