# HC Control Bot Label Allowlist Policy

This policy defines the governance requirements for any future HC Control Bot label behavior.

## Status

Label application is not active by this policy.

This document only defines the minimum rules that must exist before label behavior can be enabled.

## Purpose

Labels may help maintainers triage pull requests faster.

Labels must not become a decision authority.

## Allowed label categories

A future implementation may only use labels from a strict allowlist.

Initial candidate categories:

- area:runtime
- area:schema
- area:validator
- area:records
- area:governance
- area:project-control
- area:generated-artifact
- risk:workflow

## Label source

Labels must be derived from deterministic changed file path metadata.

The bot must not infer labels from PR title, PR body, commit messages, or contributor instructions.

## Required governance before activation

Before label behavior is enabled, a separate governance PR must define:

1. exact label allowlist
2. exact path-to-label mapping
3. denied labels
4. conflict behavior
5. audit/logging behavior
6. rollback procedure
7. test plan
8. human approval requirement

## Denied behavior

The bot must not use labels to:

- approve a pull request
- reject a pull request
- bypass protected path review
- bypass CODEOWNERS
- bypass branch protection
- imply production readiness
- imply truth guarantee
- replace maintainer review

## Conflict rule

If label signals conflict, the bot should prefer conservative output.

A conflicting label set must not become an automated decision.

## Human authority

Labels are routing metadata only.

Human maintainers retain final authority.
