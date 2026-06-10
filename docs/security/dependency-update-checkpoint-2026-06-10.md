# Dependency Update Checkpoint — 2026-06-10

Status: checkpoint record.

This document records the first dependency update wave after Python dependency monitoring was enabled for HC-TRUST-LAYER.

## Purpose

The goal of this checkpoint is to preserve the audit trail for why dependency monitoring was expanded, which Dependabot pull requests appeared, how they were reviewed, and which safety boundaries were preserved.

## Precondition

Before Python dependency monitoring was enabled, the repository added:

```text
docs/security/dependency-update-policy.md
docs/security/python-dependency-monitoring-readiness.md
docs/security/python-dependency-declaration-review.md
```

The dependency update policy was also updated to reference Python declaration consistency review.

## Dependabot configuration change

Python dependency monitoring was enabled with a conservative scope:

```text
package ecosystem: pip
directory: /
schedule: monthly
open pull request limit: 2
```

Auto-merge was not enabled.

Human review remains required.

## Pull requests processed

The following dependency pull requests were reviewed and merged:

| PR | Dependency | Change | Area | Result |
| --- | --- | --- | --- | --- |
| #775 | `actions/checkout` | `4` to `6` | GitHub Actions | merged |
| #776 | `actions/upload-artifact` | `4` to `7` | GitHub Actions | merged |
| #778 | `actions/setup-python` | `5` to `6` | GitHub Actions | merged |
| #777 | `jsonschema` | `4.17.3` to `4.25.1` | Python schema/validator-adjacent | merged after manual review |
| #779 | `qrcode[pil]` | `7.4.2` to `8.2` | Python QR-adjacent | merged after manual review |

## Review boundaries applied

### GitHub Actions updates

The GitHub Actions dependency updates were reviewed as workflow-adjacent changes.

The reviewed workflow changes preserved the HC Control Bot safety pattern:

```text
trusted base revision checkout
persist-credentials: false
no PR branch code execution as trust authority
```

### Python dependency updates

The Python dependency updates were reviewed against the dependency declaration consistency rule.

For `jsonschema` and `qrcode[pil]`, both declaration locations were updated consistently:

```text
requirements.txt
pyproject.toml
```

## Manual review escalations

`jsonschema` was treated as schema/validator-adjacent.

`qrcode[pil]` was treated as QR-adjacent.

Both were kept under human review before merge.

## Preserved safety boundaries

This update wave did not intentionally change:

- HC advisory-only semantics;
- `truth_guarantee` semantics;
- schema files;
- validator files;
- record contents;
- signing behavior;
- federation behavior;
- policy behavior;
- generated artifacts;
- QR record semantics.

## Observations

Enabling Python dependency monitoring immediately produced a small backlog of dependency PRs.

This confirms that dependency monitoring should remain conservative:

```text
monthly cadence
low open PR limit
manual review for runtime, schema, validator, QR, workflow, policy, or generated-artifact adjacent changes
```

## Follow-up note

Dependabot surfaced a warning about future support expectations around Python 3.9.

This checkpoint does not change Python version support policy.

A separate report-only review should be opened before any Python version support change is made.

## Final boundary

Dependency updates improve freshness.

Dependency updates do not prove safety.

Trust the record, not the narrative.
