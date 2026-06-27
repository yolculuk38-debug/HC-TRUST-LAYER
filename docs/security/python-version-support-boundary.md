# Python Version Support Boundary Audit

Status: advisory documentation.

This document records the current Python package support boundary before any change to package metadata is considered.

## Current observed packaging value

The current observed packaging value is:

```text
requires-python = ">=3.14"
```

## Scope of this PR

This PR does not change Python support.

This PR does not change packaging behavior.

This PR does not change dependencies.

This PR does not change CI, runtime, or test behavior.

This document is advisory only. It does not create a compatibility guarantee, release guarantee, or HC:// trust guarantee.

## Risk summary

Python `>=3.14` may create install friction for contributors and package consumers whose environments use older supported Python versions.

Changing the support boundary without an audit may create false compatibility claims if runtime, API, dependency, or test behavior has not been checked.

Runtime, API, and test behavior must be checked before widening Python support to an earlier baseline.

## Decision options

Maintainers can consider one of these options in a later implementation PR:

- Keep `>=3.14` temporarily.
- Move to `>=3.11` after test and CI verification.
- Move to `>=3.12` after test and CI verification.
- Defer package publishing posture until runtime support is clearer.

## Evidence checklist for a future implementation PR

A future implementation PR should preserve evidence that:

- `pyproject.toml` was reviewed.
- CI Python version was reviewed.
- dependency compatibility was reviewed.
- runtime/import tests were reviewed.
- public validator/demo tests were reviewed.
- packaging build metadata was reviewed.
- no unsupported compatibility claim was introduced.

## Recommendation

Do not change `requires-python` in this PR.

Open a later implementation PR only after compatibility evidence exists.

Human review remains required before any Python support boundary change is accepted.
