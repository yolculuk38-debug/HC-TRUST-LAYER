# HC GitHub Signal Watch Usage

> Status: operator usage note
> Scope: local report-only signal review
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

## Required manual live checks

The script is local and cannot replace live GitHub inspection.

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

This usage note does not:

- authorize automatic merge;
- authorize automatic approval;
- replace live PR review;
- replace CI;
- replace CodeQL or dependency review;
- guarantee truth, security, correctness, production readiness, or forensic certainty;
- change workflows, branch protection, runtime behavior, schemas, validators, records, policy enforcement, federation, signing, or canonical artifacts.

## Next possible step

A future implementation may add a scheduled report-only workflow that runs the local script and uploads a markdown artifact.

That future step must remain advisory-only and must be reviewed separately before workflow changes are introduced.
