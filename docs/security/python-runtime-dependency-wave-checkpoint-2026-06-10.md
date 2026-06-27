# Python Runtime Dependency Wave Checkpoint — 2026-06-10

Status: checkpoint record.

## Historical/report-only boundary

This document is a historical/report-only checkpoint. It records Python, dependency, CI, test, or release observations from the review moment when it was written. It should not be read as the current Python support baseline, dependency baseline, workflow runtime baseline, or live CI/test evidence. Current package metadata must be confirmed from `pyproject.toml`. Current pinned install/test dependencies must be confirmed from `requirements.txt`. Current workflow runtime versions must be confirmed from `.github/workflows/**`. Current CI/test evidence must be confirmed from live GitHub Actions and current PR/release evidence.

This document records the Python runtime dependency update wave that followed the increase of Python Dependabot cadence.

## Purpose

The goal of this checkpoint is to preserve the audit trail for runtime-adjacent Python dependency updates, the review boundaries applied, and the HC safety semantics that were preserved.

## Trigger

Python Dependabot monitoring was increased from a conservative monthly cadence to a weekly cadence with a higher open pull request limit.

That cadence change allowed Dependabot to surface additional runtime-adjacent Python updates.

## Pull requests processed

The following Dependabot pull requests were reviewed and merged:

| PR | Dependency | Change | Area | Result |
| --- | --- | --- | --- | --- |
| #782 | `fastapi` | `0.115.14` to `0.128.8` | runtime/API-adjacent | merged after manual review |
| #783 | `anyio` | `4.9.0` to `4.12.1` | async runtime/test-adjacent | merged after manual review |
| #784 | `pydantic` | `2.11.7` to `2.13.4` | response/model-validation-adjacent | merged after manual review |

## Declaration consistency

Each update preserved dependency declaration consistency between:

```text
requirements.txt
pyproject.toml
```

The wave did not intentionally introduce divergent dependency versions between runtime test dependencies and project dependency declarations.

## Review boundaries applied

These updates were not treated as ordinary low-risk dependency bumps.

They were reviewed as runtime-adjacent because they can influence:

- API request/response behavior;
- async execution behavior;
- test client behavior;
- model validation behavior;
- response contract behavior;
- runtime exception behavior.

## Auto-merge boundary

Auto-merge was not used as the authority for these updates.

The dependency PRs were handled under human review.

Safe auto-merge failures or skipped auto-merge results for these PRs are expected and acceptable when the PR is intentionally treated as manual-review.

## Preserved HC safety semantics

This wave did not intentionally change:

- advisory-only behavior;
- `truth_guarantee = false` semantics;
- public-safe runtime boundaries;
- schema files;
- validator logic;
- record contents;
- signing behavior;
- federation behavior;
- governance policy;
- generated artifacts;
- QR semantics.

## Python 3.9 warning

Dependabot surfaced warnings about future support expectations around Python 3.9.

This checkpoint does not change Python version support policy.

A separate report-only review is required before changing:

- `requires-python`;
- CI Python version expectations;
- runtime support policy;
- dependency support policy.

## Operational observation

Increasing Python Dependabot cadence produced runtime-adjacent updates immediately.

This confirms that Python dependency monitoring must remain human-supervised.

Recommended ongoing rule:

```text
Dependabot may propose dependency updates.
HC governance and human review decide whether they are safe to merge.
```

## Final boundary

Dependency freshness is useful.

Dependency freshness is not a trust guarantee.

Trust the record, not the narrative.

Historical Python, dependency, CI, and test evidence reports must be read in sequence with later migration checkpoints, dependency-wave checkpoints, current `pyproject.toml`, current `requirements.txt`, current workflow files, and live GitHub Actions evidence.
