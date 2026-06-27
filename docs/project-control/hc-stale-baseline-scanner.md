# HC Stale Baseline Scanner

The HC stale baseline scanner is a deterministic, local, report-only helper for HC-TRUST-LAYER baseline review.
It scans documentation for stale-looking Python, dependency, and CI baseline references that may otherwise be mistaken for current active baseline guidance.

## What it checks

The scanner observes current baseline signals from local repository files:

- `pyproject.toml` `requires-python`
- dependency pins in `pyproject.toml`
- dependency pins in `requirements.txt`
- Python versions in `.github/workflows/**/*.yml` and `.github/workflows/**/*.yaml`

It then scans `docs/**/*.md` for stale-looking references such as older Python versions, dependency pins, or workflow/runtime evidence.
Matches are reported as either historical-safe or missing-boundary findings.
A documentation file is treated as historical-safe when it contains an explicit boundary note such as `Historical/report-only boundary`, `historical/report-only`, or wording that says the evidence should not be read as the current baseline.

## What it does not do

The scanner does not rewrite old audit records, edit files, create pull requests, comment on issues, apply labels, request reviewers, approve changes, merge changes, call an LLM, use the GitHub API, or make network calls.
It is advisory-only and does not provide truth, security, legal, identity, approval, or merge authority.

## Why old audit records are not rewritten

Historical HC:// and HC-TRUST-LAYER evidence may contain older Python versions, dependency pins, workflow runtimes, or CI/test observations.
Those values can be valid audit records for their review moment even when they are no longer the active baseline.
Rewriting old evidence would weaken provenance continuity and make the review trail harder to audit.
The scanner therefore reports stale-looking references and boundary status without changing historical documents.

## Review boundary

The current baseline must still be confirmed from `pyproject.toml`, `requirements.txt`, workflow files, and live GitHub Actions when live CI status is relevant.
Local CI/check output is evidence, not trust authority.
Human review remains final for HC-TRUST-LAYER governance and release decisions.
