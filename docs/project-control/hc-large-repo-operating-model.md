# HC Large-Repo Operating Model

Status: advisory operating model.

This document adapts large GitHub and open-source repository practices to HC-TRUST-LAYER project control. It is a permanent review guide for combining ownership hints, Git trace evidence, PR gates, protected surfaces, provenance records, advisory security metrics, release audit references, and Codex handoff discipline.

## Status and scope

This model is:

- advisory only;
- public-safe;
- evidence-oriented;
- designed for human-supervised repository review;
- bounded by `advisory_only=true` and `truth_guarantee=false`.

This model is not:

- production certification;
- legal truth;
- identity finality;
- forensic certainty;
- automatic merge authority;
- certification authority;
- autonomous governance authority;
- guaranteed correctness.

A passing inventory, check, score, or assistant summary does not make a change ready to merge by itself. Human final authority remains required.

## World / large-repo practice summary

Large GitHub and open-source repositories commonly combine several control layers. HC-TRUST-LAYER can reuse the pattern while preserving HC:// boundaries.

| Practice | Common large-repo purpose | HC boundary |
| --- | --- | --- |
| CODEOWNERS | Maps paths to responsible reviewers or teams so changes route to people who understand that area. | A CODEOWNERS-like `owner_role` is a review responsibility hint, not identity proof or merge authority. |
| Rulesets / protected branch checks | Require CI, policy checks, or review gates before protected branches accept changes. | Checks are governance gates and evidence inputs. They do not create legal truth, production certification, or autonomous approval. |
| PR review | Provides human review, comment resolution, changed-file inspection, and merge readiness judgment before merge. | Review remains human-supervised. AI comments and CI reports are advisory until accepted by authorized reviewers. |
| Artifact provenance / attestations | Records where build outputs, reports, packages, or other artifacts came from. | Provenance explains evidence origin. It does not guarantee real-world truth unless governance and review verify the evidence. |
| Scorecard-like metrics | Surface advisory repository health signals, such as branch protection, pinned actions, dependency hygiene, or token permissions. | Metrics are warning signals and prioritization aids, not final security truth or certification. |
| Release audit | Aligns changelog entries, task ledger references, PRs, checks, merge commits, and release artifacts. | Release evidence must remain auditable and human-reviewed. A release audit is not legal truth or identity finality. |

## HC adapted model

### HC Large-Repo Operating Model

1. **Ownership**
   - CODEOWNERS-like `owner_role`.
   - Question: Who is responsible for reviewing this area?
   - Boundary: ownership means review responsibility, not authorship, approval, legal identity, or automatic merge authority.

2. **Actor Trace**
   - Git metadata:
     - `last_commit_author_name`
     - `last_commit_committer_name`
   - Question: Who last touched this file?
   - Boundary: Git metadata is evidence from repository history. It is not identity finality.

3. **Time Trace**
   - `last_commit_iso`
   - Question: When was it touched?
   - Boundary: timestamp evidence helps review order and audit context. It is not a complete chronology outside the repository.

4. **Change Trace**
   - `last_commit_sha`
   - `last_commit_subject`
   - Question: What changed?
   - Boundary: the commit subject is a summary. Reviewers should inspect the diff, PR, checks, and linked evidence.

5. **PR Gate**
   - `last_commit_pr_number`
   - CI/check status
   - Question: Which PR and which checks?
   - Boundary: a PR number and check state support auditability. They do not replace review, comment resolution, or protected-surface judgment.

6. **Protected Surface**
   - Workflows, records, schema, validators, policy, signatures, and federation are higher risk and require separate review.
   - Boundary: protected surfaces must not be auto-cleaned, auto-rewritten, or changed from inventory evidence alone.

7. **Provenance**
   - Artifact/report source.
   - Question: Where was the evidence generated?
   - Boundary: provenance records source and generation context. It is not legal truth, production certification, or a guarantee that the artifact is complete.

8. **Advisory Boundary**
   - `advisory_only=true`
   - `truth_guarantee=false`
   - Record evidence is not legal or final truth.
   - Evidence is advisory unless verified by governance and human review.

9. **Human Final Authority**
   - AI assists.
   - CI reports.
   - Governance constrains.
   - Audit records.
   - Human final authority remains.

## Practical examples

- **Wrong test file changed:** the repository inventory should show the test file path, actor trace, PR number when available, commit SHA, commit subject, commit time, and linked source or commit URL when available. The finding should route to review; it should not auto-rewrite tests.
- **Workflow changed:** workflow paths should show `protected_surface=true` and route to `protected-surface-reviewer` or equivalent human review. CI evidence is useful, but workflow changes remain governance-sensitive.
- **Record/schema changed:** records and schemas must never be auto-cleaned, reformatted, or rewritten from inventory output alone. Treat the inventory as a review index, not as authority to mutate canonical or provenance-bearing material.
- **Release change:** changelog entries, task ledger references, PR numbers, required checks, merge evidence, and release audit records should align before reviewers treat the release as ready. Misalignment should be reported as an audit finding.
- **Codex PR:** an issue records intent, Codex proposes implementation, and PR checks plus human review decide merge readiness. Codex output is advisory and must not approve, reject, close, merge, request reviewers, assign users, or add labels unless explicitly authorized by repository governance.

## What HC has now

Completed references provide the current evidence base:

- #967 repository inventory ledger;
- #968 improved test-anchor detection;
- #970 category Markdown views;
- #973 actor and PR trace evidence.

These references support review visibility. They do not add autonomous authority, protected implementation changes, or truth guarantees.

## What remains parked

The following items remain parked unless explicitly authorized, designed, reviewed, and validated:

- real CODEOWNERS enforcement;
- new ruleset changes;
- artifact attestation implementation;
- Scorecard integration;
- release attestation;
- fully autonomous issue -> Codex -> PR bridge;
- any authority-changing automation.

## Next safe steps

Safe next steps should remain docs/report/test/sample work unless explicitly authorized:

1. Review inventory artifacts.
2. Review test inventory evidence.
3. Review branch-count evidence.
4. Design a CODEOWNERS proposal before implementation.
5. Design a provenance/attestation proposal before implementation.

Do not change workflows, records, schema, validators, policy, signatures, federation, generated artifacts, protected indexes, or authority-changing automation as part of these safe steps.

## Boundary language

Use these boundaries when summarizing this model:

- Trust the record, not the narrative.
- Beyan değil, kayıt esastır.
- Evidence is advisory unless verified by governance and human review.
- `truth_guarantee=false` stays explicit.
- `advisory_only=true` stays explicit.
- Human final authority remains required.
