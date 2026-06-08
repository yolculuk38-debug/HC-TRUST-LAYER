# HC Control Bot Issue Routing Boundary

This document defines the safety boundary for any future HC Control Bot issue routing support.

It is documentation only. It does not enable issue comments, pull request comments, labels, assignments, workflow changes, approvals, request-changes behavior, merge behavior, LLM behavior, or autonomous authority.

## Purpose

HC Control Bot may later help maintainers orient issues and pull requests toward likely review areas.

This support must remain advisory. The bot may suggest possible routing categories, but it must not apply labels, assign owners, close issues, approve pull requests, or decide priority.

## Current status

Current HC Control Bot baseline:

- advisory-only
- non-LLM
- deterministic
- path-metadata based
- report-only
- artifact/log based
- human-supervised

Current behavior does not include issue routing.

## Operating model

Issue routing support must preserve the HC operating model:

```text
AI accelerates.
CI checks.
Governance classifies.
Audit records.
Humans make final decisions.
```

The bot may suggest where a maintainer should look. Humans decide routing, ownership, priority, and outcome.

## Allowed advisory routing suggestions

A future issue routing mode may suggest likely review areas such as:

- runtime/API review;
- validator review;
- schema review;
- records and canonical artifact review;
- governance review;
- policy review;
- public validator or explorer review;
- documentation drift review;
- workflow or automation safety review;
- security/threat-model review;
- project-control review.

These suggestions are review aids only.

## Disallowed behavior

Issue routing support must not:

- apply labels;
- remove labels;
- assign people or teams;
- remove assignees;
- close issues;
- reopen issues;
- lock conversations;
- mark work as accepted or rejected;
- prioritize work automatically;
- approve pull requests;
- request changes;
- merge pull requests;
- certify correctness;
- certify security;
- certify production readiness;
- certify objective truth;
- override maintainers.

## Suggested routing categories

A future advisory note may mention possible categories, but must keep them non-authoritative.

Examples:

| Observed signal | Possible advisory route |
| --- | --- |
| `.github/workflows/**` | Workflow or automation safety review |
| `src/hc_runtime/**` | Runtime/API review |
| `validators/**` | Validator review |
| `schema/**` | Schema compatibility review |
| `records/**` | Canonical record boundary review |
| `docs/governance/**` | Governance review |
| `policy/**` | Policy review |
| `federation/**` | Federation or trust-anchor review |
| `docs/project-control/**` | Operating-layer review |

The final routing decision belongs to human maintainers.

## Safe routing language

Acceptable:

```text
This issue may be relevant to runtime/API review. A maintainer should confirm the correct route.
```

Unsafe:

```text
This issue is assigned to runtime and must be handled there.
```

Acceptable:

```text
Possible labels for human consideration: governance, docs, runtime.
```

Unsafe:

```text
The bot applied labels and finalized issue classification.
```

## Evidence source disclosure

Any future routing suggestion should disclose what triggered the suggestion.

For v0.1-style behavior, valid trigger sources include:

```text
Changed file metadata only.
Path pattern match.
Protected path match.
Governance-adjacent path match.
```

A routing suggestion must not imply semantic understanding of intent, priority, security impact, or correctness unless a later reviewed implementation explicitly supports that scope.

## Label boundary

Labels are governance and workflow signals.

A future HC Control Bot mode may suggest labels in plain text for human consideration, but must not apply or remove labels unless a separate reviewed governance decision grants that authority.

For the current safety model, label authority remains human-controlled.

## Assignment boundary

Assignments create ownership signals.

A future HC Control Bot mode may suggest possible reviewer areas, but must not assign users or teams unless a separate reviewed governance decision grants that authority.

For the current safety model, assignment authority remains human-controlled.

## Priority boundary

Priority affects project direction.

The bot may identify that an issue touches protected or governance-adjacent surfaces, but it must not decide priority, severity, roadmap order, or release inclusion.

## Downstream automation boundary

No workflow or automation should treat routing suggestions as executable commands, label instructions, assignment instructions, approval signals, rejection signals, merge signals, or governance decisions.

Routing suggestions are human-readable advisory notes only.

## Failure and disablement rule

If routing support applies labels, assigns users, closes issues, decides priority, repeatedly creates noisy output, or is used as command input by another workflow, maintainers should disable routing mode and review the incident before re-enabling it.

## Implementation readiness checklist

Before enabling issue routing support, maintainers should confirm:

- authority policy is on `main`;
- report-only workflow is stable;
- report interpretation guide exists;
- advisory comment boundary exists if comments are used;
- evidence prompt boundary exists if prompts are used;
- no label, assignment, close, reopen, approve, request-changes, or merge permission is required;
- no LLM behavior is introduced;
- no PR branch code is executed;
- routing suggestions disclose trigger source;
- routing suggestions avoid final classification language;
- downstream workflows do not parse routing suggestions as commands.

## Boundary

This document does not authorize issue routing implementation.

It only defines the safety boundary that must be satisfied before any future issue routing support is proposed.
