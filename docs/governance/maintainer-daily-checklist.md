# HC:// Maintainer Daily Governance Checklist

This checklist helps HC-TRUST-LAYER maintainers perform fast, repeatable, human-supervised validation of pull requests without weakening governance controls.

Scope boundaries:

- Documentation-only governance guidance.
- No autonomous governance claims.
- No canonical schema, validator, signing, federation, policy, or runtime behavior changes.

## Daily flow

Use this short sequence for each active pull request:

1. **Check open pull requests** and identify current review priority by risk and trust-kernel proximity.
2. **Inspect governance preflight result** (for example `check_pr_governance`) and confirm no governance blockers are reported.
3. **Inspect unresolved conversations** and treat unresolved governance comments as merge-blocking until intentionally resolved.
4. **Confirm required checks are green** (CI, required status checks, and branch protection expectations).
5. **Check Dependabot and security alerts** for newly introduced or unresolved high-risk findings in changed scope.
6. **Review protected path changes** (schema, validators, federation, signatures, canonical, policy, workflow controls) and route for elevated review when touched.
7. **Decide outcome:** merge, hold, or request fix with explicit rationale preserved in the audit trail.

## Safe to merge checklist

Mark as safe to merge only when all of the following are true:

- Governance preflight reports no blocking findings.
- Required checks are green and current for the PR head commit.
- No unresolved review conversations remain.
- PR scope and labels match actual changed files.
- No unreviewed trust-kernel-impacting change is present.
- Dependabot/security posture for changed scope is acceptable.
- At least one human-supervised validation pass is recorded for consequential changes.

## Must stop and review checklist

Stop and perform deeper review when any of the following appears:

- Governance preflight returns warnings or unclear boundary signals.
- Review discussion shows unresolved disagreement about trust interpretation.
- Protected paths are modified, even if the diff appears small.
- Required checks are flaky, stale, or rerun against a different commit state.
- Security alerts, dependency risk, or provenance continuity questions are unresolved.
- PR description, risk labels, or impact notes are incomplete for changed scope.

## Do not merge checklist

Do not merge when any condition below is present:

- Required checks are failing or missing.
- Governance preflight indicates unresolved blocking conditions.
- Unresolved governance conversations remain open.
- Changes bypass required reviewer or branch protection expectations.
- Trust-kernel-impacting behavior is changed without explicit human-supervised validation.
- The PR introduces or implies autonomous governance authority.
- Security-sensitive changes are requested to merge without required review depth.

## Maintainer decision logging

When deciding **merge / hold / request fix**, keep the decision short and auditable:

- decision state
- key blocker or approval reason
- requested next action
- reviewer/maintainer attribution

This preserves provenance and audit trail continuity for HC:// governance operations in HC-TRUST-LAYER.
