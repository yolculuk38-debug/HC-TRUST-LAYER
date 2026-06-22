# HC GitHub Signal Watch Manual Signal Template

> Status: documentation-only operator template
> Scope: manual, GitHub-visible Signal Watch inputs
> Authority: advisory only; human review remains required
> Network access: not used
> Repository mutation: not authorized

## Purpose

Signal Watch accepts operator-collected GitHub-visible signals and converts them into advisory-only human actions for HC-TRUST-LAYER review.

Operators can use this template when a signal is visible in GitHub Home, GitHub Changelog, a Dependabot pull request, CodeQL or code scanning output, workflow warnings, repository notifications, or community visibility surfaces.

The manual input is public-safe triage material. It does not create production readiness, truth guarantees, forensic certainty, certification authority, identity finality, legal truth, or autonomous governance authority. Human final authority remains required before any repository action.

## Required JSON shape

Create a local JSON file such as `tmp/hc-signals.json` with an array of signal objects:

```json
[
  {
    "source": "GitHub Home | GitHub Changelog | Dependabot PR | CodeQL | Workflow warning | Repository notification",
    "title": "...",
    "url": "...",
    "note": "..."
  }
]
```

Field guidance:

- `source`: where the operator saw the signal.
- `title`: short human-readable summary.
- `url`: optional public or repository-visible URL when available.
- `note`: optional operator context, limited to observable facts and review needs.

## Ready-to-copy templates

Copy one or more objects into `tmp/hc-signals.json`, then replace placeholder values with the operator-observed signal details.

### GitHub Changelog Actions/runtime deprecation

```json
[
  {
    "source": "GitHub Changelog",
    "title": "Actions runtime deprecation notice for <runtime-or-action>",
    "url": "<github-changelog-url>",
    "note": "Operator observed a GitHub Changelog item that may affect workflow runtime, action versions, runner assumptions, or future check behavior. Human review should inspect repository workflows before proposing any change."
  }
]
```

### Dependabot dependency update

```json
[
  {
    "source": "Dependabot PR",
    "title": "Dependabot opened <ecosystem> dependency update for <package-or-action>",
    "url": "<dependabot-pr-url>",
    "note": "Operator observed a Dependabot update. Human review should inspect changed files, release notes when relevant, dependency policy, checks, comments, and review threads before any merge decision."
  }
]
```

### CodeQL/code scanning warning

```json
[
  {
    "source": "CodeQL",
    "title": "Code scanning warning for <alert-or-annotation-summary>",
    "url": "<code-scanning-or-check-url>",
    "note": "Operator observed a CodeQL or code scanning warning. Human review should inspect alert details, affected paths, baseline context, and required checks before deciding whether follow-up is needed."
  }
]
```

### Workflow warning/check annotation

```json
[
  {
    "source": "Workflow warning",
    "title": "Workflow warning or check annotation for <workflow-or-job>",
    "url": "<workflow-run-or-check-url>",
    "note": "Operator observed a workflow warning or check annotation. Human review should inspect the workflow, action versions, runner assumptions, permissions, and documented migration path before proposing any workflow change."
  }
]
```

### First external star/watcher/fork/contributor

```json
[
  {
    "source": "GitHub Home",
    "title": "First external <star-watcher-fork-or-contributor> observed",
    "url": "<repository-or-notification-url>",
    "note": "Operator observed new external visibility or contributor activity. Human review should inspect onboarding, public-safe language, contribution boundaries, and protected-path expectations."
  }
]
```

### Copilot/agent/platform behavior change

```json
[
  {
    "source": "GitHub Changelog",
    "title": "Copilot, agent, or platform behavior change for <feature-or-surface>",
    "url": "<github-changelog-or-notification-url>",
    "note": "Operator observed a platform behavior change that may affect agent governance, automation boundaries, supply-chain review, contributor expectations, or repository assistance behavior. Human review remains required before changing repository practice."
  }
]
```

### Unrelated product news/no-action signal

```json
[
  {
    "source": "GitHub Changelog",
    "title": "Unrelated GitHub product news: <summary>",
    "url": "<github-changelog-url>",
    "note": "Operator observed product news with no apparent HC-TRUST-LAYER repository impact. Record as no-action unless later human review identifies a workflow, dependency, security, governance, or public-safety connection."
  }
]
```

## Local command example

Run the report locally from the repository root:

```bash
python scripts/hc_signal_watch_report.py --signals tmp/hc-signals.json --format md
```

The command reads the local JSON file and prints an advisory Markdown report. It does not call GitHub, fetch live RSS, create issues or comments, change labels or reviewers, approve pull requests, merge pull requests, or mutate repository state.

## Expected output fields

Signal Watch report output should include advisory fields such as:

- `impact`
- `risk`
- `recommended_action`
- `evidence_gap`
- `recommended_human_actions`
- `automation_boundary`

Use these fields as triage aids only. They are not proof of truth, security, correctness, or readiness.

## Safety markers

Expected safety boundary for this manual flow:

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

This template does not authorize or add:

- code changes;
- workflow changes;
- GitHub API calls;
- live RSS fetching;
- issue creation;
- PR comments;
- labels, reviewers, approvals, merges, or repository mutation;
- changes to schemas, validators, records, hashes, QR artifacts, policy, signing logic, federation logic, source code, tests, or generated artifacts.

## Next step

The next implementation PR should add a dry-run issue/PR suggestion generator from Signal Watch report output.
