# Governance Evidence Review Checklist

Status: advisory operator checklist.

Use this checklist to review generated repository evidence before proposing any cleanup, branch deletion, source archival, workflow change, or authority-changing automation. It supports HC-TRUST-LAYER governance review without replacing human judgment.

Generated artifacts are advisory evidence, not canonical records. CI green is useful evidence, but CI green is not trust authority. Human final authority remains required for governance decisions.

Baseline boundary:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- human final authority remains required

## One-open-PR discipline

Operators should keep governance automation work scoped to one open PR for the same task or evidence-review scope. Before opening a new PR, confirm that no open PR already covers the same repository evidence, cleanup proposal, workflow proposal, or authority boundary.

If an overlapping PR exists, continue review in that PR or record the blocker instead of opening a duplicate PR.

## Source inventory evidence review checklist

Use generated source inventory artifacts as starting evidence only. Before any cleanup or archival proposal, confirm:

1. the artifact was generated from the expected repository branch and commit;
2. the reported file paths still exist or the report clearly identifies removed paths;
3. import, reference, documentation, and test anchors were reviewed directly in the repository;
4. protected paths and trust-kernel-adjacent files were excluded from cleanup by default;
5. source files without obvious references were marked review-needed, not deletion-ready;
6. generated classifications were not treated as proof of inactivity;
7. human reviewers recorded the reason for any proposed keep, move, archive, or removal decision.

Do not delete, move, archive, or de-prioritize source files from generated inventory output alone.

## Ruleset readiness report review checklist

Use ruleset readiness reports to identify governance-readiness gaps. Before proposing branch protection, ruleset, workflow, or authority changes, confirm:

1. the report target, branch, and commit are clear;
2. reported checks match current repository configuration;
3. missing or failing checks were verified from repository or platform evidence where available;
4. advisory findings were separated from required governance blockers;
5. any proposed ruleset change preserves human review and does not grant autonomous bot authority;
6. any protected-path impact is explicitly identified for human review;
7. CI status is treated as evidence, not as final trust authority.

Do not change workflows, branch protection, review authority, merge authority, or bot permissions from readiness output alone.

## Scorecard advisory signal review checklist

Use Scorecard advisory signals as public-safe risk indicators, not as objective truth or certification. Before citing Scorecard output in a governance proposal, confirm:

1. the Scorecard run date, repository target, branch, and commit are documented;
2. each referenced signal is mapped to repository evidence or a known limitation;
3. low or high scores are treated as review prompts, not automatic pass/fail decisions;
4. noisy, unavailable, or platform-dependent signals are marked uncertain;
5. proposed follow-up work stays scoped, reversible, and human-reviewable;
6. no statement implies production readiness, legal truth, forensic certainty, certification authority, or guaranteed correctness.

Do not use Scorecard output to approve, reject, merge, close, or auto-label PRs without explicit human review.

## Release audit report review checklist

Use release audit reports to prepare human release review. Before any release, tag, changelog, or authority proposal, confirm:

1. the report target, branch, commit, and command are recorded;
2. changelog, task ledger, PR reference, and changed-file evidence were inspected directly;
3. missing evidence is listed as a review blocker or follow-up, not silently ignored;
4. release readiness language remains advisory and does not claim production readiness;
5. `human_review_required=true` remains preserved where release action is discussed;
6. `merge_ready` or similar generated fields are not treated as final authority;
7. any release action remains separate from generated report creation unless explicitly approved by human reviewers.

Do not publish releases, create tags, rewrite release evidence, or claim release authority from generated audit output alone.

## Human review gate before authority-changing action

No cleanup, branch deletion, source archival, workflow change, ruleset change, bot permission change, merge-rule change, release action, or other authority-changing automation may proceed without human review.

Generated artifacts may support review, but they must not create autonomous governance authority. Repository maintainers retain final judgment, and HC:// and HC-TRUST-LAYER terminology must remain advisory, evidence-preserving, and human-supervised.
