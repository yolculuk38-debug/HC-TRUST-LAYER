# HC GitHub Signal Watch Policy

> Status: advisory-only project-control policy
> Scope: GitHub ecosystem, dependency, security, repository-visibility, and platform-change signals
> Authority: report-only; humans remain final decision makers
> Production readiness: not claimed

## Purpose

HC GitHub Signal Watch defines how HC-TRUST-LAYER should notice GitHub-side signals that can affect repository safety, maintainability, onboarding, or governance.

The goal is to reduce human manual tracking burden while preserving the HC boundary:

```text
AI speeds review.
CI checks evidence.
Governance defines limits.
Audit preserves records.
Humans make final decisions.
```

This policy does not add automatic merge authority, automatic approval authority, branch-protection authority, issue-closing authority, reviewer-request authority, or repository-governance authority.

## Signals to watch

The signal watch surface includes:

- repository-wide open pull requests, not only user-authored pull requests;
- Dependabot version and security update pull requests;
- GitHub Actions dependency version drift;
- pip dependency version drift;
- workflow warnings and deprecation notices;
- CodeQL, code scanning, and neutral baseline warnings;
- dependency review findings for manifest and lockfile changes;
- HC Control Bot advisory comments and artifacts;
- GitHub Changelog items tagged or related to Actions, Application Security, Supply Chain Security, Platform Governance, Copilot, and Collaboration Tools;
- repository visibility signals such as stars, watchers, forks, first external followers, and first-time contributor activity;
- repository setting or permission changes that can affect write access, pull request behavior, bot-created pull requests, workflow execution, or code scanning.

## Mandatory repository check before saying "repo clean"

Do not claim that the repository is clean by checking only user-authored pull requests.

Before saying `open PR yok`, `repo temiz`, `checks temiz`, or `sürüm güncel`, an operator or agent must check:

```text
repo:yolculuk38-debug/HC-TRUST-LAYER is:pr is:open
```

The check must include bot-authored pull requests, especially Dependabot pull requests.

## Dependency update policy

Dependency updates must be classified before merge:

| Update type | Default handling |
| --- | --- |
| Patch | Merge can proceed after diff, comments, threads, reviews, checks, annotations, and advisory notes are clean. |
| Minor | Merge can proceed after release notes and runtime/API impact are checked. |
| Major or breaking-note update | Do not merge blindly. Read release notes, inspect repository usage, confirm runtime/API tests, and report risk before merge. |
| Security update | Prioritize review, but keep human final authority and required checks. |

`Most recent` is not enough. The target is:

```text
most recent safe and compatible version
```

## Check review is more than green status

A green checkmark is not sufficient by itself.

For each pull request, inspect:

1. PR info and head SHA;
2. changed files;
3. diff;
4. issue comments;
5. inline review threads;
6. review submissions;
7. required checks;
8. advisory and neutral checks;
9. check annotations and warnings;
10. CodeQL or code scanning baseline warnings;
11. HC Control Bot advisory comments and artifacts;
12. protected-path impact;
13. duplicate PR or branch risk;
14. merge result;
15. repository-wide open pull request search after merge.

## GitHub Changelog triage

GitHub Changelog and platform-news items are advisory signals. They must be triaged with this decision table:

| Changelog topic | HC action |
| --- | --- |
| Actions runtime, runner, action-version, or deprecation change | Check workflow actions and runner assumptions. |
| Dependabot, dependency review, package ecosystem, or advisory database change | Check dependency update policy and `dependabot.yml`. |
| CodeQL, code scanning, secret scanning, or application security change | Check security workflows, annotations, and baseline status. |
| Pull request permission, write-access, fork, bot-created PR, or approval behavior change | Check governance boundary and contributor-risk model. |
| Copilot, agent, or automation behavior change | Check agent supply-chain threat model and report-only boundaries. |
| Stars, watchers, forks, followers, first external contributor activity | Check onboarding, README, demo safety language, issue templates, and contribution boundaries. |
| Unrelated product news | Record as no action unless it affects repository operations. |

## Community signal triage

External attention is a repository health signal, not vanity data.

When the repository receives a new star, watcher, fork, follower, or first-time contributor activity, the advisory interpretation should be:

```text
public visibility increased
onboarding surface matters more
safety language must remain clear
contributor path should be understandable
no production or truth guarantee claims should be introduced
```

Recommended first response is review-only:

- check README and demo entry points;
- check `CONTRIBUTING.md` or equivalent onboarding path if present;
- check issue templates if contributor traffic increases;
- check whether public-safe demo language remains visible;
- do not change governance authority without explicit human review.

## External practice model

This policy borrows proven ideas without copying authority models blindly:

- Dependabot opens update pull requests and can group related updates to reduce noise.
- Dependency review helps understand manifest and dependency changes before merge.
- CodeQL/code scanning provides security-analysis alerts but must be interpreted with baseline and neutral-status context.
- OpenSSF Scorecard-style checks are useful as advisory evidence, not final approval authority.
- Renovate-style dependency dashboards show the value of central update visibility and approval workflows, especially for major or risky updates.

HC-TRUST-LAYER keeps the simpler GitHub-native path first:

```text
Dependabot + GitHub checks + HC advisory reports + human final authority
```

Renovate-style dashboards, scheduled changelog ingestion, and automated issue creation can be considered later only after this policy is validated.

## Report format

A signal report should use this compact shape:

```text
Signal: <dependency / action / code scanning / changelog / community / governance>
Source: <PR, check, changelog item, repository event, or artifact>
Impact: <none / docs / dependency / workflow / runtime / governance / security>
Risk: <low / medium / high>
Recommended action: <none / inspect / docs PR / config PR / workflow PR / human review>
Automation boundary: advisory-only; no automatic approval or merge
Evidence gap: <missing evidence or none>
```

## Non-goals

This policy does not:

- create automatic merge authority;
- create automatic approval authority;
- replace human review;
- replace CI checks;
- guarantee objective truth, security, production readiness, or correctness;
- change workflows, branch protection, permissions, runtime behavior, schemas, validators, records, policy, federation, signing, or canonical artifacts;
- treat social signals as proof of trust.

## Initial operating rule

Until a dedicated signal-watch workflow exists, every shift must begin with:

```text
1. repo-wide open PR search
2. Dependabot PR check
3. security / code scanning / check annotation review for active PRs
4. workflow warning review for active PRs
5. GitHub Changelog scan for Actions, Application Security, Supply Chain Security, Platform Governance, Copilot, and Collaboration Tools items
6. community visibility signal review when visible in GitHub Home or repository notifications
```

Every merge completion must end with:

```text
1. merged PR verification
2. repository-wide open PR search
3. remaining dependency/security/platform signals listed or explicitly marked as none found
```
