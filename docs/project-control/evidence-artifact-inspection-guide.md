# Evidence Artifact Inspection Guide

Status: advisory operator guide.

This guide explains how a human reviewer should locate, download, and inspect governance evidence artifacts before proposing cleanup, branch changes, workflow or ruleset changes, release actions, protected-path changes, or authority-impacting automation for HC-TRUST-LAYER.

It closes the operator read-path gap after the generated governance evidence artifact review completed in #985: repository tools and workflows may generate advisory evidence, but a human reviewer still needs to inspect the actual GitHub Actions artifacts, platform evidence, current repository files, and PR diff before any next step.

Baseline boundary:

- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`
- generated artifacts are advisory evidence, not canonical records
- CI green is evidence, not trust authority
- human final authority remains required

## Short operator flow

1. Open the relevant PR workflow run or the relevant `main` workflow run in GitHub Actions.
2. Confirm the run branch and commit SHA before trusting any artifact contents.
3. Download or inspect the named artifact from the run summary.
4. Compare artifact contents with current repository files and, for PR work, the PR diff.
5. Record evidence gaps instead of inventing missing values.
6. Escalate to human review before any cleanup, branch cleanup, workflow or ruleset change, release action, protected-path change, generated-artifact rewrite, or authority-changing automation.

## Repository inventory artifacts

Expected artifact names and files may include:

- `hc-repo-inventory.json`
- `hc-repo-inventory.md`
- category Markdown views when generated, such as source, tests, docs, workflows, protected paths, latest changes, and review-needed views

Before using repository inventory evidence, check:

- the GitHub Actions workflow run that generated the artifact;
- the branch and commit SHA recorded by the run and artifact;
- the artifact name and file names downloaded from the run;
- generation time or run time;
- protected-path classification;
- review-needed entries;
- actor and PR trace fields where present;
- whether the reported file paths still exist in the current repository state.

Boundary: inventory artifacts identify review questions. They do not authorize deleting, archiving, moving, renaming, or de-prioritizing files, especially in protected or trust-kernel-adjacent paths.

## Test inventory evidence

When reviewing test inventory evidence, inspect both the generated output and the current repository files.

Check for:

- exact test anchors that name a file, symbol, command, or behavior directly;
- prefix-style anchors that cover grouped file or module names;
- reference-based anchors from documentation, fixtures, or supporting tests;
- whether the referenced test files still exist;
- whether relevant local or CI test runs are current for the branch and commit under review.

Boundary: missing anchors are review questions, not rewrite authority. A missing or weak anchor may justify a follow-up proposal, but it does not prove that code is unused, unsafe, or ready for removal.

## Branch-count evidence

Use GitHub platform evidence or a reliable full remote branch listing when reviewing branch-count evidence.

Check:

- the GitHub branch UI for visible active branches;
- a full remote branch listing when available;
- branch names, last commit dates, and whether a branch has an open PR;
- whether stale-looking branches are protected, historical, release-related, or tied to unresolved review.

Boundary: branch count does not authorize branch deletion, archival, renaming, or forced cleanup. Branch cleanup requires human review and repository-maintainer action.

## Ruleset readiness reports

Ruleset readiness evidence may come from:

- `scripts/check_ruleset_readiness.py` output;
- `docs/governance/github-ruleset-readiness.md`;
- workflow or local report output;
- live GitHub repository settings where a maintainer can inspect them.

Check:

- the report target, branch, and commit SHA;
- the command or workflow that produced the output;
- whether reported checks match current repository configuration;
- whether live GitHub branch protection or ruleset settings confirm or contradict the report;
- any protected-path or governance-control impact.

Boundary: readiness output does not prove actual branch protection or ruleset enforcement. It is advisory evidence for human review, not authority to change workflows, settings, permissions, or merge rules.

## Scorecard advisory signals

Scorecard evidence should be treated as public-safe advisory signal evidence.

Check:

- the Scorecard JSON artifact;
- run date;
- branch and commit SHA;
- repository target;
- signal names and values;
- warnings, unavailable signals, or platform-dependent limitations;
- whether any cited signal is backed by repository evidence.

Boundary: Scorecard output is advisory signal evidence only. It is not certification, production readiness, legal truth, forensic certainty, guaranteed correctness, or approval authority.

## Release audit reports

Release audit evidence may include JSON and Markdown artifacts produced for human release review.

Check:

- release audit JSON and Markdown artifact names;
- branch and commit SHA;
- PR references;
- changed files;
- changelog and task-ledger evidence;
- missing evidence fields;
- `human_review_required=true`;
- whether any proposed release action is separate from report generation.

Boundary: a release audit report does not publish releases, create tags, modify changelogs, or create release authority. Missing evidence must be recorded as a review gap or blocker, not silently filled in.

## Hard boundaries

Do not use any evidence artifact or CI result to perform cleanup, source rewrite, branch cleanup, workflow change, ruleset change, release action, protected-path change, generated-artifact rewrite, label, assignment, reviewer request, approval, rejection, close action, auto-merge, bot authority expansion, or other authority-changing automation.

Do not claim production readiness, certification, legal truth, forensic certainty, identity finality, guaranteed correctness, signing implementation, witness authority, C2PA ingestion, OpenTimestamps verification, federation, or dispute/governance implementation from these artifacts.

## Safe next action

The safe next action is to record a small, reviewable evidence note or scoped proposal that identifies:

- the workflow run or platform page inspected;
- branch and commit SHA;
- artifact names;
- observed gaps or uncertainties;
- whether human review is required before any action.

Keep the result advisory, public-safe, and reversible. Preserve HC:// and HC-TRUST-LAYER terminology and human-supervised validation boundaries.
