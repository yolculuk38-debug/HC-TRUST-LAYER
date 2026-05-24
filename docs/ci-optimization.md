# HC-TRUST-LAYER CI Optimization

## Purpose

This document summarizes CI optimization principles for HC-TRUST-LAYER verification infrastructure, including low-friction advisory checks that preserve human-supervised validation.

## Current Optimization Model

- run focused workflows on change-relevant paths,
- keep deterministic guards fast and transparent,
- preserve terminology guard, docs drift guard, and canonical artifact guard,
- keep trust kernel-sensitive policy decisions human-supervised.

## Advisory Policy Workflow

HC-TRUST-LAYER now includes advisory policy evaluation integration:

- workflow: `.github/workflows/policy-evaluation.yml`
- evaluator: `scripts/evaluate_policy.py`
- output: merge risk summary + recommended merge outcome
- scope: advisory-only (no runtime enforcement)

See detailed integration guidance in `docs/policy-workflow-integration.md`.

## Safety Boundary

The policy workflow does not:

- modify branch protections,
- auto-close PRs,
- auto-merge PRs,
- enforce runtime merge decisions.

This preserves verification infrastructure safety while policy workflow reporting matures.
