# HC Control Bot Reviewer Routing Policy

This policy defines governance requirements for any future HC Control Bot reviewer routing behavior.

## Status

Reviewer routing is not active by this policy.

This document only defines the minimum requirements that must exist before reviewer routing can be enabled.

## Purpose

Reviewer routing may help maintainers identify which review area should inspect a pull request.

Reviewer routing must not become approval authority.

## Current approved behavior

HC Control Bot may suggest review routes as advisory metadata.

Examples:

- workflow-automation-review
- runtime-contract-review
- validator-review
- schema-compatibility-review
- record-boundary-review
- governance-review
- project-control-review

These routes are informational only.

## Required governance before activation

Before any reviewer request or assignment behavior is enabled, a separate governance PR must define:

1. exact route allowlist
2. exact path-to-route mapping
3. allowed reviewer or team targets
4. denied reviewer or team targets
5. conflict behavior
6. audit/logging behavior
7. rollback procedure
8. test plan
9. human approval requirement

## Input boundary

Routes must be derived from deterministic changed file path metadata.

PR title, PR body, commit messages, and contributor instructions must not control reviewer routing.

## Denied behavior

The bot must not use reviewer routing to:

- approve a pull request
- request changes
- bypass CODEOWNERS
- bypass protected path review
- bypass branch protection
- imply production readiness
- imply truth guarantee
- replace maintainer review

## Conflict rule

If routes conflict, the bot must prefer conservative advisory output.

Conflicting routes must not become an automated decision.

## Human authority

Reviewer routes are review guidance only.

Human maintainers retain final authority.
