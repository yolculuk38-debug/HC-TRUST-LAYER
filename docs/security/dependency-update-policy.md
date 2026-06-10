# Dependency Update Policy

Status: advisory policy.

This document defines how HC-TRUST-LAYER treats dependency update suggestions from Dependabot and similar tooling.

## Purpose

Dependency update tooling can help keep repository infrastructure current, but it must not become an autonomous trust authority.

HC-TRUST-LAYER uses dependency update tooling as an advisory signal only.

## Current Dependabot scope

Current repository configuration is intentionally minimal:

```text
package ecosystem: github-actions
directory: /
schedule: weekly
open pull request limit: 5
```

This means Dependabot currently watches GitHub Actions dependencies only.

## Authority model

Dependabot may:

- open dependency update pull requests;
- describe changed dependency versions;
- provide compatibility or release-note context;
- request rebase or recreate actions when explicitly instructed by a maintainer.

Dependabot must not be treated as:

- merge authority;
- release authority;
- security authority by itself;
- trust anchor;
- replacement for human review;
- replacement for CI or repository governance.

## Review requirements

Every dependency update pull request should be reviewed as a normal repository change.

Maintainers should check:

- changed dependency name;
- old and new versions;
- affected workflow or package file;
- whether protected paths are touched;
- whether release notes mention breaking changes;
- whether CI passes;
- whether HC Control Bot or equivalent advisory checks report path risk;
- whether the change affects runtime, validation, governance, records, signing, federation, policy, or generated artifacts.

## Auto-merge boundary

Auto-merge should remain disabled by default for dependency updates.

A dependency update may be merged only after human maintainer review.

This is especially important for:

- GitHub Actions runtime changes;
- Python dependency changes;
- security-sensitive packages;
- validation or schema-adjacent packages;
- workflow permission changes;
- generated artifact tooling.

## Python dependency updates

Python dependency updates are not currently enabled in `.github/dependabot.yml`.

Before enabling Python dependency monitoring, the repository should define:

- target files to monitor;
- update cadence;
- whether security-only updates should be separated from routine updates;
- test requirements;
- review boundaries for runtime/API behavior;
- maximum open pull request limits.

## Python declaration consistency

Before Python dependency monitoring is expanded, maintainers should review the current declaration reports:

```text
docs/security/python-dependency-monitoring-readiness.md
docs/security/python-dependency-declaration-review.md
```

Future Python dependency pull requests should confirm that both dependency declaration locations were checked and that duplicated versions remain aligned when applicable.

This protects the project from drift between CI installation behavior and package metadata.

## Safe operating rule

For HC-TRUST-LAYER, dependency tooling should follow this sequence:

```text
Dependency tool proposes.
CI tests.
Advisory bots report.
Human maintainer reviews.
Human maintainer merges or rejects.
```

## Final boundary

Dependency freshness is useful.

Dependency freshness is not proof of safety.

Trust the record, not the narrative.
