# Release Automation Plan

This document describes the current manual release process and a proposed automation plan for **HC:// TRUST LAYER**.

## Scope

- Publication automation remains planned; the installed-wheel validation job below is implemented.
- The installed-wheel job validates and preserves artifacts; it does not publish them.
- It does **not** create a release.
- It does **not** change schema definitions.

## Current Manual Release Process

Today, releases are prepared manually with the following sequence:

1. Merge the release PR into the default branch.
2. Ensure all required GitHub Actions checks are green.
3. Update `VERSION` and `CHANGELOG.md` with the intended release information, merge those changes, and wait for the installed-wheel gate on that exact main commit.
4. Create a GitHub Release entry.
5. Tag the version in Git (for example `v0.1.1`) and publish.

This process works, but relies on maintainers to remember each step and keep release metadata consistent.

## Proposed Future Automation

The target state is a guarded release pipeline that automates repeatable validation while keeping human control for publication.

### Planned Automation Controls

- **Auto-generate release notes** from merged PRs and categorized commits.
- **Require changelog updates** before a release can proceed.
- **Verify `VERSION` matches the release tag** (for example, `VERSION=0.2.0` must match tag `v0.2.0`).
- **Block release if validation fails**, including metadata mismatches or missing release notes/changelog requirements.
- **Keep manual approval for final publish**, so a maintainer explicitly confirms the final release action.

### Why Keep Manual Approval

A manual final approval step reduces risk for experimental and trust-critical infrastructure by preserving human review at the publication boundary.

## Release Types

### Patch Release

- Purpose: backward-compatible fixes and documentation/validation improvements.
- Typical version movement: `x.y.Z` (increment patch number).
- Example: `v0.1.0` → `v0.1.1`.

### Minor Release

- Purpose: backward-compatible features and protocol improvements.
- Typical version movement: `x.Y.0` (increment minor number, reset patch).
- Example: `v0.1.3` → `v0.2.0`.

### Experimental Release

- Purpose: publish unstable or trial capabilities for early feedback.
- Typical convention: pre-release tags (for example `v0.3.0-rc.1`, `v0.3.0-beta.1`) or clearly labeled release notes.
- Notes: should explicitly declare constraints, risk level, and migration expectations.

### Security Release

- Purpose: urgent fixes for vulnerabilities or integrity-impacting issues.
- Typical behavior: accelerated review and publication timeline.
- Notes: should include clear remediation notes, impact statement, and upgrade guidance.

## Suggested Implementation Phases

1. Add release validation jobs (dry-run mode first).
2. Enforce changelog and version/tag checks as required gates.
3. Add release note generation.
4. Keep final publish behind maintainer approval.

This phased approach allows validation hardening without disrupting existing manual release operations.

## Implemented installed-wheel validation

`.github/workflows/installed-wheel.yml` builds one wheel, installs it in a fresh
Python 3.14 environment and runs `scripts/smoke_installed_distribution.py` with
`-I` outside the checkout. It checks the installed archive hash, packaged schema,
console command, SDK/CLI agreement, actual file bytes, failure exit codes and
runtime imports. Both PR and main triggers include `VERSION` and `CHANGELOG.md`,
so release-metadata-only commits also produce their own tested artifact.
No server or registry publication is started.

A successful run uploads `tested-wheel-<source commit>` containing that exact
wheel and `verification.json`. The report records the wheel SHA-256, tested
source commit, interpreter/distribution versions and completed checks. A PR run
uses GitHub's test merge commit; release handoff must use the successful main
run at the actual release commit. Artifacts expire after 14 days. If the artifact
is absent, run validation again and inspect its new report before handoff.

For a manual release, obtain the matching successful run's artifact, recompute
the wheel SHA-256 and compare it with `verification.json`, then attach that same
wheel. Do not rebuild between testing and publication. A changed/rebuilt wheel
needs a new installation test and report. This does not grant release approval
or replace independent review, signing or provenance attestations.
