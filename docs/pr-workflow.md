# Pull Request Workflow Guide

> **Documentation Status**
> - **status:** GUIDE
> - **scope:** Contributor guidance for opening, validating, reviewing, and closing Pull Requests in HC-TRUST-LAYER.
> - **canonical relevance:** Advisory workflow guidance only; does not change canonical records, schemas, validators, signing, federation, policy, protected paths, or trust-kernel indexes.
> - **runtime relevance:** None; this guide does not change runtime verification behavior.

## 1. Purpose

This guide helps contributors open small, reviewable Pull Requests for HC-TRUST-LAYER while preserving HC:// verification boundaries, provenance expectations, and audit trail clarity.

Repository evidence is authoritative. A PR should explain what repository files, checks, documentation, or issue context support the change. Do not replace in-repository architecture notes, implementation status, validation outputs, or documented boundaries with assumptions from outside the repository.

A PR is a review request, not proof that a capability is implemented, validated, or accepted. AI-assisted contributions are advisory and require review. Human-supervised validation remains required for sensitive trust-kernel-impacting changes.

## 2. Before Opening a PR

Before opening a PR:

1. Read the relevant repository documents for the affected area.
2. Confirm the change is in scope for HC-TRUST-LAYER and HC:// verification infrastructure.
3. Keep the branch focused on one purpose.
4. Confirm the diff does not include unrelated formatting, generated output, local environment files, or protected-path changes.
5. Run the required checks for the touched scope.
6. Prepare a PR description that states what changed, what did not change, and what evidence supports the change.

If the change may affect runtime verification behavior, schemas, validators, records, signing, federation, policy, trust-kernel indexes, or governance controls, stop and ask before expanding the PR.

## 3. Small PR Principle

Prefer small, scoped, reviewable PRs.

A good PR should be:

- focused on one issue, document, workflow clarification, or implementation concern
- easy to review from the changed files alone
- easy to revert without disrupting unrelated work
- explicit about validation performed
- clear about any protected or trust-kernel-sensitive surfaces that were not touched

Avoid combining documentation cleanup, behavior changes, dependency updates, workflow changes, and policy changes in one PR. Split unrelated work into separate PRs so reviewers can preserve audit trail clarity and human-supervised validation boundaries.

## 4. Issue First vs Direct PR

Open an issue first when the work:

- changes trust-kernel-sensitive behavior or review boundaries
- affects protected paths or canonical record assumptions
- changes policy interpretation, federation behavior, signing semantics, schemas, validators, or records
- introduces a new architecture direction or unclear ownership boundary
- needs maintainer agreement before implementation
- contains security-sensitive uncertainty that should not be discussed in a public PR

A direct PR is usually acceptable for:

- typo fixes
- broken links
- contributor guidance improvements
- documentation-only clarification aligned with existing repository evidence
- small examples that do not change protocol behavior
- narrow navigation improvements

If there is uncertainty, open an issue or ask maintainers before starting implementation.

## 5. Docs-Only PRs

Docs-only PRs may update explanatory Markdown, navigation, or contributor guidance when they do not change runtime behavior, protected paths, schemas, validators, records, policy, federation, signing, trust-kernel indexes, or GitHub Actions.

For docs-only PRs:

- keep language concise, professional, and evidence-based
- preserve HC:// and HC-TRUST-LAYER terminology
- avoid new guarantees or implementation claims
- link to related repository documents instead of duplicating large sections
- run the documentation checks listed in this guide
- state clearly in the PR description that the change is docs-only

Docs-only does not mean review-free. It means the declared scope is non-behavioral and should be validated against documentation, terminology, and canonical artifact guardrails.

## 6. Trust-Kernel-Sensitive PRs

A PR is trust-kernel-sensitive when it directly or indirectly affects review, interpretation, provenance, audit trail continuity, canonical record boundaries, policy routing, validator behavior, signing assumptions, federation behavior, or runtime verification outcomes.

Trust-kernel-sensitive PRs must:

- identify the affected HC:// surfaces
- explain the expected decision-path or validation differences
- preserve audit trail continuity
- identify affected policy rules when policy interpretation changes
- include relevant tests and repository-defined checks
- avoid unsupported claims about guarantees or readiness
- receive human-supervised validation before merge

Human-supervised validation remains required for sensitive trust-kernel-impacting changes.

## 7. Protected Paths

Protected paths require explicit authorization and review routing. Do not modify them unless the task or maintainer direction clearly requests the change.

Protected or sensitive paths include:

- `.github/workflows/**`
- `schema/**`
- `validators/**`
- `records/**`
- `policy/**`
- `federation/**`
- `signatures/**`
- `canonical/**`
- trust-kernel indexes
- `hc_context/**`
- `agents/**`

Also treat runtime verification behavior, signing and trust anchor semantics, validator logic, policy evaluator behavior, federation behavior, and canonical record identity as sensitive even when the file path is not listed above.

## 8. Validation Requirements

Validation should match the touched scope.

For documentation-only PRs, run:

```bash
python scripts/check_terminology.py
python scripts/check_docs_drift.py
python scripts/check_canonical_artifacts.py
git diff --check
```

For code, validator, schema, policy, signing, federation, record, or workflow changes, run the documentation checks plus the relevant test or validation subset for the affected surface.

If a check cannot run, document the reason in the PR. Do not imply that skipped, blocked, or unavailable checks passed.

## 9. Required Checks

Before requesting review, confirm applicable guardrails are complete:

- terminology guard
- docs drift guard
- canonical artifact guard
- whitespace and patch hygiene check
- relevant unit, integration, validator, schema, or policy checks when the touched scope requires them
- protected-path review when the diff includes sensitive surfaces

Do not weaken guards, policy checks, validation logic, or CI configuration to make a PR pass unless the PR is explicitly about changing those guardrails and has reviewer approval.

## 10. Human-Supervised Validation

Human-supervised validation is required whenever a PR could affect sensitive trust-kernel behavior or interpretation.

Human-supervised validation means qualified maintainers or reviewers examine the evidence, diff, expected impact, validation outputs, and repository-defined boundaries before accepting the change. Automation and AI assistance can support review, but they do not replace reviewer judgment.

AI-assisted contributions are advisory and require review.

## 11. PR Description Expectations

A useful PR description should include:

- a concise summary of what changed
- changed files or affected areas
- issue link, if applicable
- whether the PR is docs-only or behavior-impacting
- protected-path confirmation
- trust-kernel impact statement
- validation commands run and results
- checks that could not run, with reasons
- screenshots for perceptible web UI changes when applicable
- explicit note of any sensitive surfaces intentionally not changed

For AI-assisted PRs, disclose that assistance was used and make clear that repository evidence and reviewer validation remain authoritative.

## 12. Review Expectations

Reviewers should be able to determine:

- whether the PR matches its stated scope
- whether terminology is consistent
- whether repository evidence supports the change
- whether protected paths or trust-kernel-sensitive areas are touched
- whether validation is complete for the scope
- whether claims are appropriately limited
- whether the PR can be safely reverted if needed

Review may request smaller scope, additional checks, clearer evidence, updated wording, or explicit human-supervised validation before merge.

## 13. Common Reasons PRs Are Delayed

PRs are commonly delayed when they:

- mix unrelated changes
- omit required checks or check output
- change protected paths without prior agreement
- make claims not supported by repository evidence
- introduce terminology drift
- alter behavior while describing the PR as docs-only
- require security, policy, validator, signing, federation, schema, record, or trust-kernel review
- lack enough context for reviewers to evaluate provenance or audit trail impact
- depend on external assumptions instead of repository evidence

## 14. Common Reasons PRs Are Closed

PRs may be closed when they:

- modify protected paths without authorization
- bypass or weaken validation guardrails without approval
- introduce production readiness, security certification, forensic certainty, truth finality, or autonomous governance claims
- attempt to change sensitive trust-kernel behavior without human-supervised validation
- include unsafe security details that belong in private reporting
- are too broad to review safely
- conflict with documented HC:// boundaries or repository evidence
- include generated, unrelated, or non-reviewable changes

Closure does not necessarily reject the underlying idea. Maintainers may ask for a smaller PR, an issue-first discussion, private security reporting, or a revised evidence-based proposal.

## 15. AI-Assisted PRs

AI-assisted PRs are welcome when they remain bounded, reviewable, and evidence-based.

Contributors using AI assistance should:

- review every changed line before submission
- verify paths, links, commands, and terminology
- avoid broad rewrites unless explicitly requested
- disclose material AI assistance in the PR description
- keep outputs advisory and subject to repository review
- avoid claiming that AI output validates security, policy, truth, or governance conclusions

AI-assisted contributions are advisory and require review.

## 16. What Not To Claim

Do not claim production readiness, security certification, forensic certainty, truth finality, or autonomous governance.

Also avoid claiming:

- objective-truth finality
- complete dispute automation
- live federation guarantees
- cryptographic guarantees not backed by repository tests and documentation
- policy guarantees not backed by repository tests and documentation
- validation status for checks that were not run
- implementation status that is not supported by repository evidence

Use careful language such as "supports review," "provides evidence for," "documents expected behavior," or "requires human-supervised validation" when those phrases match the repository evidence.

## 17. When To Stop and Ask

Stop and ask maintainers before continuing when:

- the diff touches protected paths
- the change may affect trust-kernel-sensitive behavior
- the change alters runtime verification behavior, schemas, validators, records, policy, federation, signing, workflows, trust-kernel indexes, `hc_context`, or agents
- repository evidence conflicts or is incomplete
- a check fails and the fix would require weakening a guardrail
- the PR would need security-sensitive details in public
- the scope keeps expanding beyond the original task
- you are unsure whether a claim is supported

When in doubt, preserve the current behavior, document the uncertainty, and ask for human-supervised review.

## 18. Related Documents

- [`README.md`](../README.md) — repository overview and contribution entrypoint.
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — contribution expectations and merge policy.
- [`docs/contributor-start-here.md`](contributor-start-here.md) — beginner contributor orientation.
- [`docs/issue-workflow.md`](issue-workflow.md) — issue routing, duplicate checks, and private reporting guidance.
- [`docs/pr-scope-boundaries.md`](pr-scope-boundaries.md) — advisory PR scope and protected-surface guidance.
- [`docs/verification-map.md`](verification-map.md) — verification map orientation.
- [`docs/protocol-graph-index.md`](protocol-graph-index.md) — protocol graph navigation aid.
- [`docs/trust-kernel-index.md`](trust-kernel-index.md) — advisory trust kernel routing index.
- [`docs/limitations-and-risks.md`](limitations-and-risks.md) — limitations and risk boundary language.
- [`SECURITY.md`](../SECURITY.md) — security and vulnerability reporting path.
