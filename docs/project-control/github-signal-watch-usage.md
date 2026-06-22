# HC GitHub Signal Watch Usage

> Status: operator usage note
> Scope: local and workflow report-only signal review
> Authority: advisory only
> Production readiness: not claimed

## Purpose

This note shows how an operator can run the local HC GitHub Signal Watch report added in `scripts/hc_signal_watch_report.py`.

The script helps turn GitHub Home, GitHub Changelog, dependency, workflow, code scanning, and community visibility signals into a small advisory report.

It does not call GitHub, fetch external network resources, mutate repository state, approve pull requests, merge pull requests, change labels, or change reviewer assignments.

## Baseline local report

Run from the repository root:

```bash
python scripts/hc_signal_watch_report.py --format md
```

Expected behavior:

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

The baseline report checks local repository readiness:

- Signal Watch policy file exists;
- Active Work Registry links the policy;
- Dependabot configuration exists;
- GitHub Actions weekly updates are configured;
- pip weekly updates are configured;
- GitHub Actions dependency grouping is configured.

## Scheduled workflow report

`.github/workflows/hc-signal-watch-report.yml` runs the same local report script in a report-only GitHub Actions workflow.

It can run from:

- `workflow_dispatch` for manual operator checks;
- a daily schedule;
- pull requests that change the workflow, Signal Watch script, related policy docs, the Active Work Registry, or Dependabot configuration.

Expected workflow boundary:

```text
permissions: contents: read
network_access: no explicit external fetch step
repository_mutation: false
approval_authority: false
merge_authority: false
issue_or_comment_creation: false
label_or_reviewer_mutation: false
```

Expected artifacts:

```text
hc-signal-watch-report.json
hc-signal-watch-report.md
```

The workflow report is advisory evidence only. It does not replace live PR review, code scanning review, dependency review, GitHub Home inspection, GitHub Changelog inspection, or human-supervised validation.

## Operator-provided signal input

When a signal is visible in GitHub Home, GitHub Changelog, repository notifications, a pull request, or a check annotation, an operator can write a small local JSON file.

Example `tmp/hc-signals.json`:

```json
[
  {
    "source": "GitHub Home",
    "title": "First external star on the repository"
  },
  {
    "source": "GitHub Changelog",
    "title": "Actions runtime deprecation notice for Node",
    "url": "https://example.invalid/changelog-item"
  },
  {
    "source": "Pull Request",
    "title": "Dependabot opened a pip dependency update"
  }
]
```

Run:

```bash
python scripts/hc_signal_watch_report.py --signals tmp/hc-signals.json --format md
```

The output classifies each signal as advisory evidence and recommends an action such as:

- inspect onboarding and public safety language;
- inspect workflow action versions and warnings;
- inspect dependency update policy;
- record as no action when there is no HC-relevant match.

## Dry-run issue/PR suggestion text

Operators can convert the local JSON report `recommended_human_actions` into copy-ready dry-run suggestion text. This is local-only text generation. It does not create GitHub issues, PRs, comments, labels, reviewer requests, approvals, merges, workflow runs, or repository state changes.

Example dry-run flow:

```bash
python scripts/hc_signal_watch_report.py --signals tmp/hc-signals.json --format json > tmp/hc-signal-watch-report.json
python scripts/hc_signal_watch_suggest.py tmp/hc-signal-watch-report.json --format md
```

The suggestion output keeps `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, and `human_review_required=true`. Human review remains required before any repository action.

## GitHub Changelog fixture signal input

The report can also include normalized local fixture signals produced by `scripts/hc_signal_watch_rss_ingest.py`. This input is local fixture-only and report-only. It reads a saved JSON output file and does not fetch a live RSS feed, call the network, mutate the repository, create issues or comments, change labels or reviewers, approve pull requests, or merge pull requests.

Example local fixture flow:

```bash
python scripts/hc_signal_watch_rss_ingest.py examples/hc-signal-watch/github-changelog-rss-fixture.xml > tmp/github-changelog-signals.json
python scripts/hc_signal_watch_report.py --changelog-signals tmp/github-changelog-signals.json --format md
```

The report preserves fixture signal fields such as `source`, `title`, `url`, `published`, `category`, `impact`, `risk`, `recommended_action`, `classification_reason`, `matched_keywords`, `evidence_gap`, `automation_boundary`, and `dedupe_key` when they are present in the normalized JSON. Human review remains required before any repository action.

For a full end-to-end local fixture demo that generates both JSON and Markdown reports in a temporary output directory, see [HC Signal Watch GitHub Changelog Fixture Demo](github-signal-watch-fixture-demo.md).

For a concise end-to-end operator flow from manual JSON signal or live RSS dry-run to advisory report and dry-run suggestions, see [HC Signal Watch Operator Quickstart](github-signal-watch-operator-quickstart.md).


## Manual live GitHub Changelog RSS dry-run

`.github/workflows/hc-signal-watch-live-rss-dry-run.yml` provides an optional manual-only Signal Watch dry-run for the GitHub Changelog RSS feed. It runs only from `workflow_dispatch`; it has no schedule and no pull request trigger.

The workflow fetches `https://github.blog/changelog/feed/` by default, or an explicit operator-supplied workflow input URL. It writes normalized Signal Watch JSON and Markdown report files as artifacts only:

```text
hc-signal-watch-live-rss-dry-run.json
hc-signal-watch-live-rss-dry-run.md
```

Expected live dry-run boundary:

```text
advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
repository_mutation=false
issue_comment_automation=false
label_reviewer_mutation=false
approval_authority=false
merge_authority=false
```

The workflow includes a bounded job timeout and script-level fetch timeout. Fetch or parse errors are reported as safe dry-run failures in the artifacts instead of creating issues, pull request comments, labels, reviewer requests, approvals, merges, or repository mutations. Human review remains required before any repository action.

The future issue-based visibility model for this dry-run is defined in [HC Signal Watch Console Issue Model](github-signal-watch-console-issue-model.md). That model is documentation only here; it does not implement issue comment automation. Any future workflow that posts or updates the fixed console issue would be issue-comment automation and a GitHub issue state mutation, while repository files and branches remain unchanged. The fixed console issue must be human-created before any future workflow may update it.

Routine live RSS dry-run status should remain in Actions summaries and artifacts as the current public-safe evidence view unless a genuinely private/admin-only notification channel is separately designed and reviewed. The future private/admin-only operator queue is separately documented in [HC Signal Watch Operator Notification Queue](github-signal-watch-operator-notification-queue.md), with setup requirements in [HC Signal Watch Private Inbox Setup Contract](github-signal-watch-private-inbox-setup.md), and is not implemented here. The preferred next-direction boundary is documented in [HC Signal Watch Admin Notification Boundary](github-signal-watch-admin-notification-boundary.md); public issue comments are not the default channel for internal operational Signal Watch updates.

## Required manual live checks

The script and workflow are local/report-only and cannot replace live GitHub inspection.

Before saying `repo temiz`, `checks temiz`, `açık PR yok`, or `sürüm güncel`, the operator must still check:

```text
repo:yolculuk38-debug/HC-TRUST-LAYER is:pr is:open
```

Also inspect:

- Dependabot pull requests;
- comments;
- inline review threads;
- review submissions;
- check annotations;
- neutral or advisory checks;
- CodeQL or code scanning baseline warnings;
- HC Control Bot advisory comments and artifacts;
- workflow warnings;
- GitHub Changelog items with repository impact.

## Output interpretation

Use the report as a triage aid:

| Field | Meaning |
| --- | --- |
| `impact` | Area that might be affected: dependency, workflow, security, automation, community, or none. |
| `risk` | Advisory priority, not a security proof. |
| `recommended_action` | Next human-reviewed action. |
| `automation_boundary` | Confirms no automatic approval or merge. |
| `evidence_gap` | Missing context or no matching HC-relevant signal. |

## Safe usage examples

Community visibility signal:

```text
Signal: First external star on the repository
Impact: community
Recommended action: inspect onboarding and public safety language
```

Workflow/runtime signal:

```text
Signal: Actions runtime deprecation notice for Node
Impact: workflow
Recommended action: inspect workflow action versions and warnings
```

Dependency signal:

```text
Signal: Dependabot opened a pip dependency update
Impact: dependency
Recommended action: inspect dependency update policy
```

## Non-goals

This usage note and workflow do not:

- authorize automatic merge;
- authorize automatic approval;
- replace live PR review;
- replace CI;
- replace CodeQL or dependency review;
- guarantee truth, security, correctness, production readiness, or forensic certainty;
- create issues or comments;
- change labels or reviewers;
- change workflows beyond the report-only workflow documented here;
- change branch protection, runtime behavior, schemas, validators, records, policy enforcement, federation, signing, or canonical artifacts.

## Parked next steps

The following remain parked for separate review:

- repository-mutating live GitHub Changelog RSS ingestion;
- automatic issue creation;
- automatic PR comments;
- dependency dashboard issue;
- any workflow that writes to repository or PR state.
