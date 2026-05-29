# Contribution Traceability Policy

## Status and Scope

- advisory_only=true
- public_safe=true
- human_final_authority=true
- governance_protected=true
- traceability_first=true
- documentation-only policy
- no runtime behavior changes
- no validator changes
- no schema changes
- no workflow changes
- no security policy changes

This policy is an advisory documentation baseline for HC-TRUST-LAYER and HC:// contribution history. It does not create ownership, governance authority, release authority, validator authority, signing authority, or automated approval rights.

## Purpose

The purpose of this policy is to create a permanent and auditable traceability path for ideas, documents, issues, pull requests, reviews, checks, merges, and releases.

The baseline traceability chain is:

```text
Idea
→ Document
→ Issue
→ PR
→ Checks
→ Review
→ Merge
→ Release
```

This chain helps reviewers reconstruct how a concept moved from proposal to implementation history without treating contribution activity as control over HC:// governance, trust-kernel boundaries, canonical record surfaces, or release decisions.

## Traceability Principles

1. **Traceability first**: every meaningful contribution should preserve enough references for later review of intent, scope, checks, review discussion, merge outcome, and release context.
2. **Human final authority**: repository checks, agent output, sponsorship, and support are advisory unless accepted through human-supervised validation and reviewer oversight.
3. **Contribution is not control**: making, funding, proposing, reviewing, or supporting a contribution does not grant control over HC-TRUST-LAYER, HC:// governance, trust-kernel decisions, signing logic, validator behavior, federation behavior, policy enforcement, or canonical record boundaries.
4. **Sponsor is not owner**: a sponsor may help fund, prioritize, describe, or support work, but sponsorship does not transfer ownership of repository decisions, documents, code paths, governance outcomes, release timing, or canonical record authority.
5. **Support is not governance authority**: public support, organizational support, issue comments, review comments, or external endorsement do not create governance authority unless recognized by repository-defined governance processes.
6. **Public-safe references**: traceability records should use public issue, PR, review, check, merge, and release references where possible and must not expose secrets, tokens, private keys, private credentials, or non-public security material.
7. **Minimal and auditable scope**: traceability should make the contribution path easy to review without requiring unrelated refactors, uncontrolled architecture expansion, or unsupported production claims.
8. **Boundary preservation**: traceability records must not imply changes to runtime behavior, validators, schemas, workflows, security policy, governance enforcement, signing logic, federation behavior, or policy evaluator behavior unless those changes are explicitly implemented, reviewed, and validated in-repo.

## Contribution Lifecycle

A contribution is any proposed or accepted change to repository-facing materials, including documentation, examples, tests, scripts, code, review materials, or release notes.

The preferred lifecycle is:

1. **Idea**: a concept is captured with intent, scope, expected value, known constraints, and affected HC:// areas.
2. **Document**: the idea is mapped to a repository document, design note, future concept, process note, or implementation plan.
3. **Issue**: the document or idea receives an issue reference that records discussion, scope, risk class, out-of-scope boundaries, and expected checks.
4. **PR**: implementation or documentation work is proposed in a pull request with clear references to the source document and issue.
5. **Checks**: applicable automated checks run, such as terminology guard, docs drift guard, canonical artifact guard, and relevant test subsets.
6. **Review**: reviewers evaluate scope, terminology, governance relationship, audit trail continuity, and boundary impact.
7. **Merge**: an accepted PR is merged by authorized maintainers according to repository process.
8. **Release**: release notes or release artifacts reference the merged work when the contribution becomes part of a release boundary.

The lifecycle preserves implementation history while keeping final decisions under human-supervised validation.

## Required References

Traceable contributions should record the following references when available:

- **Contribution identifiers**: stable labels, slugs, document headings, branch names, PR titles, or repository-local identifiers that connect related artifacts.
- **Issue references**: issue number, issue title, scope summary, risk notes, affected documentation or HC:// areas, and any explicit out-of-scope boundaries.
- **PR references**: PR number, PR title, commit range, changed files, linked issue, linked document, and stated non-goals.
- **Check references**: check names, command names, CI run links when public, pass/fail state, and documented limitations for checks that could not run.
- **Review references**: reviewer comments, approvals, requested changes, unresolved concerns, governance notes, and human-supervised validation notes.
- **Merge references**: merge commit, squash commit, merge date, merge actor, and any merge queue or branch protection context available in repository history.
- **Release references**: release tag, release notes entry, changelog entry, distribution artifact reference, or explicit note that the contribution has not yet reached a release.

References should be sufficient for a reviewer to reconstruct what changed, why it changed, who reviewed it, which checks were considered, and when it entered the repository history.

## Governance Relationship

Contribution traceability supports governance review but does not replace governance.

Required distinctions:

- **Contribution ≠ Control**: a contribution creates reviewable history; it does not create control rights.
- **Sponsor ≠ Owner**: a sponsor may be acknowledged as a contributor or supporter; sponsorship does not create ownership over HC-TRUST-LAYER decisions.
- **Support ≠ Governance Authority**: support signals may inform prioritization; they do not override repository-defined governance authority.

Governance-protected areas remain protected by existing repository rules and reviewer oversight. Changes affecting trust-kernel boundaries, canonical record surfaces, validators, schemas, signing logic, federation behavior, policy interpretation, or security-sensitive workflows require explicit review and human-supervised validation before merge.

## Audit Relationship

Traceability records are part of the audit trail for contribution history. They help answer:

- where the idea originated;
- which document described the proposal;
- which issue scoped the work;
- which PR implemented the change;
- which checks were run;
- which review decisions were recorded;
- which merge introduced the change; and
- which release first included or referenced the change.

This policy does not claim forensic certainty, truth guarantees, autonomous dispute resolution, or production readiness. It defines a reviewable audit path for repository history.

## Documentation Relationship

Documentation is the preferred first-class surface for clarifying ideas before implementation. Documents may describe proposed, future, advisory, or accepted concepts, but their status must remain clear.

Documentation references should:

- preserve HC-TRUST-LAYER and HC:// terminology;
- identify whether content is advisory, future-facing, implemented, or release-bound;
- avoid implying runtime behavior unless it exists in repository implementation and tests;
- connect future concepts to issue and PR history before implementation claims are made; and
- preserve IP, brand, and idea-use boundaries without claiming ownership through contribution.

## Future Workspace Relationship

Future concepts become traceable implementation history when they move through the documented chain from future-facing documentation to issue scoping, PR implementation, review, merge, and release.

The future workspace may hold concepts that are not yet implemented. A future concept becomes part of implementation history only when a linked issue and PR produce reviewed, merged changes. Until then, the concept remains advisory and should not be described as runtime behavior, validator behavior, schema behavior, governance enforcement, signing behavior, federation behavior, or release behavior.

Future workspace references should make clear:

- the future concept identifier or document path;
- the issue that scoped implementation readiness;
- the PR that introduced implementation or documentation changes;
- the checks and reviews used for validation;
- the merge reference that entered repository history; and
- the release reference, if and when release inclusion occurs.

## Examples

### Future concept flow

```text
Future Idea
→ docs/future
→ Issue
→ PR
→ Review
→ Merge
→ Release
```

Example traceability record:

- **Future Idea**: `future-verification-note`
- **Document**: `docs/future/future-verification-note.md`
- **Issue**: `#123`, scoped as documentation-first with no runtime behavior change
- **PR**: `#124`, linked to the issue and document
- **Checks**: terminology guard, docs drift guard, canonical artifact guard
- **Review**: human reviewer confirms advisory scope and no trust-kernel behavior impact
- **Merge**: merge commit records the accepted documentation change
- **Release**: release notes reference the documentation policy if included in a release

### Sponsorship without authority

A sponsor may request or fund a documentation improvement and may be listed in issue context when appropriate. The sponsor does not own the resulting document, PR, review decision, merge decision, release decision, HC:// governance outcome, or canonical record boundary.

Traceability should record the sponsor relationship only when public-safe and relevant to context. It must not convert sponsorship into governance authority.

### Support without governance authority

Community support on an issue may indicate interest or priority. Support does not approve implementation, bypass checks, override reviewers, grant signing authority, or create autonomous governance finality.

Traceability should preserve support context as discussion history while routing final decisions through repository-defined review and human-supervised validation.
