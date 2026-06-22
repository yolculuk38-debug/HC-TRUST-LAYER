# HC GitHub Signal Watch Live Signal Map

> Status: documentation-only planning note
> Scope: GitHub-visible signal mapping before live ingestion
> Authority: advisory only; humans remain final decision makers
> Network access: not enabled for the current phase
> Repository mutation: not authorized

## Purpose

This note documents the next practical HC GitHub Signal Watch step for HC-TRUST-LAYER: map GitHub-visible signals into advisory-only human actions before adding any live network ingestion, repository automation, issue creation, PR comments, labels, reviewer assignment, approvals, or merge behavior.

The map keeps Signal Watch bounded to local, public-safe triage. It does not create production readiness, truth guarantees, forensic certainty, certification authority, identity finality, or autonomous governance authority.

## Current status

Signal Watch is currently report-only.

Current supported inputs and outputs:

- It can process operator-provided JSON signals.
- It can process local GitHub Changelog fixture signals.
- It can produce `recommended_human_actions`.
- It does not fetch live GitHub data.

Current boundaries:

```text
advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
network_access=false
repository_mutation=false
approval_authority=false
merge_authority=false
```

## Signal source map

| Source | Example signal | Impact | Risk default | Recommended human action | Automation boundary |
| --- | --- | --- | --- | --- | --- |
| GitHub Home notification | GitHub Home shows a repository notification, security notice, community event, or platform prompt visible to the operator. | May affect repository triage, visibility, workflow review, security review, or onboarding review depending on the notification. | Medium until the operator classifies the source and repository impact. | Record the signal in a manual JSON input or shift note, classify impact, and route to the relevant human review path before any repository change. | Advisory-only classification; no live fetch, issue creation, PR comment, label, reviewer, approval, merge, or repository mutation. |
| GitHub Changelog item | Changelog item mentions Actions runtime, security scanning, Dependabot, Copilot, repository permissions, or collaboration behavior. | May affect workflow assumptions, dependency review, security scanning, bot behavior, or contributor governance. | Low for unrelated product news; medium for repository operations; high when security, permissions, or blocking workflow behavior is plausibly affected. | Compare the item to HC-TRUST-LAYER workflow, dependency, security, and governance boundaries; record no-action when repo operations are not affected. | Fixture/local report only in the current phase; no live RSS fetching or automatic follow-up. |
| Dependabot PR | Dependabot opens a pip, GitHub Actions, or security update pull request. | May affect dependencies, workflows, runtime compatibility, or vulnerability response. | Medium by default; high for security updates, major updates, or breaking-change notes. | Inspect dependency policy, release notes, changed files, checks, comments, review threads, and compatibility before a human decides. | Report and recommendation only; no auto-merge, auto-approval, reviewer assignment, labels, or PR comments. |
| CodeQL / code scanning alert | Code scanning reports a new alert, baseline warning, neutral advisory, or changed annotation. | May affect security review, code quality triage, or release confidence. | High for new or blocking security findings; medium for baseline or neutral warnings needing context. | Human reviewer inspects alert details, affected paths, baseline context, and required checks before deciding whether follow-up is needed. | No alert dismissal, issue creation, code change, approval, or merge authority. |
| Workflow warning / deprecation | GitHub Actions warns about a deprecated runtime, action version, runner image, permission behavior, or syntax. | May affect CI reliability, workflow execution, or future repository checks. | Medium by default; high when checks are blocked or an enforcement date is near. | Inspect workflow and action versions, runner assumptions, permissions, check annotations, and documented migration path before proposing a workflow change. | Signal Watch does not edit workflows, pin actions, rerun jobs, or mutate repository state. |
| First external star / watcher / fork / contributor | First external visibility or contributor activity appears in GitHub Home, notifications, repository insights, or a pull request. | Public visibility and onboarding expectations increase; safety language and contributor boundaries matter more. | Low by default; medium if contributor activity touches protected paths or governance-sensitive areas. | Review README, onboarding, demo safety language, issue templates, contribution boundaries, and public-safe claims. | No automatic welcome comment, issue creation, labels, reviewer assignment, trust claim, or governance change. |
| Bot / agent / Copilot behavior change | GitHub announces or surfaces a change in Copilot, bots, agent modes, automated comments, or repository assistance behavior. | May affect agent governance, supply-chain review, contributor expectations, or automation boundaries. | Medium by default; high if write access, PR behavior, approval behavior, or security-sensitive automation could be affected. | Review agent governance docs, automation boundaries, permission assumptions, and supply-chain risk before changing repository practice. | No agent authority expansion, no automatic comments, no approvals, no merges, and no repository mutation. |

## Decision rules

- Security or blocking signals require human review before any repository action.
- Workflow or runtime deprecation signals require workflow and action version inspection before any proposed workflow change.
- Dependabot signals require dependency policy review, changed-file inspection, release-note review when relevant, and check review.
- Community visibility signals require onboarding, safety language, demo language, and contribution-boundary review.
- Unrelated GitHub product news is recorded as no-action unless repository operations are affected.

## Next implementation sequence

1. Add a manual signal template for operator-collected GitHub Home, notification, PR, check, Changelog, and community signals.
2. Bridge Signal Watch output into the HC Check Digest as advisory evidence only.
3. Add an issue or PR suggestion dry-run that writes local report text only.
4. Consider an optional `workflow_dispatch`-only live RSS report after separate review, with read-only behavior and no repository mutation.
5. Do not add automatic issue or PR creation until a separate governance review explicitly authorizes the scope.

## Required safety markers

```text
advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
network_access=false
repository_mutation=false
approval_authority=false
merge_authority=false
```

## Explicit non-goals

This document does not authorize or add:

- code changes;
- workflow changes;
- GitHub API integration;
- live RSS fetching;
- issue creation;
- PR comments;
- labels, reviewers, approvals, merges, or repository mutation;
- runtime, schema, validator, record, hash, QR, policy, signing, federation, or canonical artifact changes.
