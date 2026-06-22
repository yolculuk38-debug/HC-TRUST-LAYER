# HC Signal Watch Operator Quickstart

> Status: operator quickstart
> Scope: manual signal input and live RSS dry-run review
> Authority: advisory only
> Production readiness: not claimed

## Purpose

This quickstart shows the safe end-to-end HC Signal Watch operator flow:

```text
manual JSON signal
→ Signal Watch report
→ recommended_human_actions
→ dry-run suggestion text
→ human final decision
```

HC Signal Watch is a triage aid for HC-TRUST-LAYER operations. It preserves HC:// review boundaries by producing public-safe advisory evidence and copy-ready dry-run suggestions without mutating repository state.

## Safety boundaries

Expected boundary values for this workflow:

```text
advisory_only=true
public_safe=true
truth_guarantee=false
human_review_required=true
repository_file_branch_mutation=false
issue_comment_automation=true
automatic_issue_creation=false
automatic_pr_creation=false
issue_text_command_parsing=false
label_reviewer_mutation=false
approval_authority=false
merge_authority=false
```

For local report and suggestion-only flows, `issue_comment_automation=false` still applies. For the gated workflow latest-status comment on `#1082`, the value is `issue_comment_automation=true`. These values mean Signal Watch output is not a final decision. A human operator must inspect the evidence, repository context, open pull requests, checks, and review state before taking any action.

## Manual JSON signal flow

Create a local signal file from a GitHub Home item, GitHub Changelog item, repository notification, pull request, check annotation, or other operator-observed public signal.

Example `tmp/hc-signals.json`:

```json
[
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

Generate a JSON report for artifact-style review:

```bash
python scripts/hc_signal_watch_report.py --signals tmp/hc-signals.json --format json > tmp/hc-signal-watch-report.json
```

Generate a Markdown report for terminal or copy/paste review:

```bash
python scripts/hc_signal_watch_report.py --signals tmp/hc-signals.json --format md
```

Review `recommended_human_actions` in the JSON report. Treat the field as a human-reviewed queue of possible next steps, not as authorization to create issues, open pull requests, comment, label, approve, or merge.

## Dry-run suggestion text

Convert the JSON report into copy-ready issue/PR suggestion text:

```bash
python scripts/hc_signal_watch_suggest.py tmp/hc-signal-watch-report.json --format md
```

The suggestion output is dry-run text only. It may help an operator draft an issue or pull request, but it does not create one. A human operator remains responsible for deciding whether action is needed, editing the text, and performing any repository operation through normal review paths.

## Manual live RSS dry-run workflow

For a manually triggered live GitHub Changelog RSS dry-run, use GitHub Actions:

```text
Actions → HC Signal Watch Live RSS Dry Run → Run workflow
```

The workflow fetches the GitHub Changelog RSS feed, normalizes candidate signals, and uploads advisory artifacts only. It does not create issues, open pull requests, comment, label, request reviewers, approve, merge, or otherwise mutate repository state.

Expected artifacts:

```text
hc-signal-watch-live-rss-dry-run.json
hc-signal-watch-live-rss-dry-run.md
```

Use the JSON artifact for structured review and the Markdown artifact for operator-readable triage. If the workflow reports a fetch or parse error, treat it as a safe dry-run failure and inspect the artifact before deciding whether to retry or investigate manually.

Treat the Actions summary and artifacts as the current public-safe evidence view, not as private/admin-only notifications. The same-repo review console is `#1082`, titled `HC Signal Watch Console`, as recorded in [HC Signal Watch Console Issue Binding](github-signal-watch-console-issue-binding.md). For actionable P0/P1/P2 Signal Watch reports on safe main-branch contexts, the separate `console-comment` job may update one controlled latest-status comment on `#1082`. Pull request report runs remain read-only and do not receive issue-write permission. No second repository is required for the current model. Optional private/admin-only notifications remain future and parked, as described in [HC Signal Watch Private Inbox Setup Contract](github-signal-watch-private-inbox-setup.md).

## Future console issue model

A future same-repo issue-based visibility model is documented in [HC Signal Watch Same-Repo Console Mode](github-signal-watch-same-repo-console-mode.md) and [HC Signal Watch Console Issue Model](github-signal-watch-console-issue-model.md). The model defines the fixed, human-created `HC Signal Watch Console` issue, currently `#1082`, for public-safe advisory latest-status summaries only. The implemented latest-status path is issue-comment automation and a GitHub issue state mutation, while repository files and branches remain unchanged. The GitHub Actions run plus JSON and Markdown artifacts remain the evidence source for human review. A notification is not an obligation; trust the record, not the assistant.

## Interpretation guide

Use Signal Watch priorities as triage hints:

| Priority | Operator interpretation |
| --- | --- |
| P0/P1/P2 | Inspect promptly. If `#1082` has a latest-status notification, open the linked Actions run and artifacts before deciding on any next step. |
| P3 | Review repository context before deciding whether any action is needed. |
| P4/no-action | Record only unless repository operations are affected. |

Signal Watch priorities are advisory. They do not prove security impact, correctness, or operational urgency.

## Non-goals

This quickstart does not authorize or provide:

- automatic issue creation;
- automatic PR creation;
- uncontrolled comments outside the single gated `#1082` latest-status comment;
- labels or reviewers;
- approvals;
- merges;
- truth, security, correctness, production readiness, or forensic certainty guarantees.

## Human final decision

Before taking action, the operator should inspect current repository state, open pull requests, checks, review comments, relevant workflow logs, and any referenced public source. The final decision remains human-supervised and must follow normal HC-TRUST-LAYER review boundaries.
