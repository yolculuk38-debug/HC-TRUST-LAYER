# HC:// Production Risk Checklist

This checklist identifies security and operational risks that must be reviewed before HC:// Runtime can be considered production-ready in HC-TRUST-LAYER.

This document is documentation-only. It does not modify runtime code, validators, signing logic, schemas, workflows, federation logic, policy files, or canonical records. It does not claim production readiness.

## Production Readiness Boundaries

Production readiness does not permit:

- Changing canonical records outside approved canonical record procedures.
- Bypassing signature validation.
- Bypassing audit requirements.
- Bypassing human review boundaries.
- Remote authority override of repository-defined trust-kernel, validator, federation, policy, or governance decisions.

Each risk below requires detection, mitigation, escalation, and recovery evidence before production approval.

## Secret Exposure

### Detection

- Secret scanning flags credentials, signing material, tokens, or private configuration in repository content, logs, audit events, telemetry, backups, or reports.
- Runtime monitoring detects unexpected authentication failures, credential use from unknown locations, or anomalous operator activity.
- Human review identifies accidental disclosure in PRs, screenshots, generated artifacts, or support material.

### Mitigation

- Revoke and rotate exposed secrets immediately.
- Remove disclosed material from operational surfaces and follow repository-approved cleanup procedures.
- Confirm logs, audit events, and verification packages redact secret values.
- Review least-privilege access and reduce unnecessary secret scope.

### Escalation path

Escalate to security maintainers, runtime owners, and governance reviewers. If signing material may be affected, include trust-kernel reviewers and require human-supervised validation before restoring normal operation.

### Recovery expectations

Recovery must include documented rotation evidence, access review, audit trail annotation, affected-surface review, and confirmation that no canonical records were changed to hide or repair the exposure.

## Validator Compromise

### Detection

- Validator health checks report unexpected version, capability, timeout, or integrity changes.
- Verification outputs diverge from expected validator behavior or produce unsupported positive claims.
- Audit events show unusual validator routing, repeated failures, or unexplained state transitions.

### Mitigation

- Isolate the affected validator and disable its production decision path without deleting audit evidence.
- Re-run verification with known-good validators where repository procedures permit.
- Preserve suspicious inputs, outputs, logs, and provenance references for review.
- Confirm no signature validation or human review boundary was bypassed.

### Escalation path

Escalate to validator maintainers, security maintainers, runtime owners, and trust-kernel reviewers. Governance reviewers must approve any return to service after compromise.

### Recovery expectations

Recovery must include validator replacement or repair evidence, version and capability verification, audit trail continuity review, and documented human-supervised validation of restored behavior.

## Replay Attacks

### Detection

- Replay or duplicate detection surfaces repeated record identifiers, timestamps, signatures, request fingerprints, or verification package references.
- Runtime metrics show repeated validation requests with suspicious timing or source patterns.
- Audit trail review identifies reused evidence presented as new provenance.

### Mitigation

- Return explicit replay or duplicate warning states without converting warnings into positive verification claims.
- Rate limit repeated attempts and preserve audit-visible evidence.
- Require fresh validation evidence where applicable.
- Maintain separation between replay warnings and canonical record mutation.

### Escalation path

Escalate persistent or high-impact replay attempts to runtime, security, and audit reviewers. Include trust-kernel reviewers if replay handling affects verification decision paths.

### Recovery expectations

Recovery must document affected records or packages, replay indicators, mitigations applied, and any reviewer decisions. Audit trail continuity must be preserved.

## Federation Desynchronization

### Detection

- Federation peers report different state, delayed updates, conflicting witness data, or inconsistent verification map references.
- Monitoring detects peer timeout, stale synchronization markers, or unexpected peer identity changes.
- Audit events show unresolved disagreement between local and remote federation state.

### Mitigation

- Treat desynchronized federation state as warning or degraded, not as authority to override local trust-kernel decisions.
- Pause affected peer synchronization where necessary.
- Preserve local audit evidence and peer-state snapshots for review.
- Reconcile only through documented federation procedures and human review.

### Escalation path

Escalate to federation maintainers, runtime owners, security reviewers, and governance reviewers. Trust-kernel reviewers must be included if peer disagreement affects verification outcomes.

### Recovery expectations

Recovery must include reconciliation evidence, peer identity review, audit trail notes, and confirmation that remote authority override did not occur.

## Audit Corruption

### Detection

- Audit integrity checks detect missing, altered, unordered, or unverifiable audit entries.
- Monitoring reports audit write failures, storage errors, or unexpected retention gaps.
- Human review finds inconsistent provenance references or generated artifacts treated as canonical records.

### Mitigation

- Freeze affected audit-dependent operations if integrity cannot be established.
- Preserve available logs, backups, verification packages, and operator reports.
- Restore from verified backups only through documented recovery procedures.
- Clearly disclose audit gaps or uncertainty in reviewer-facing material.

### Escalation path

Escalate to audit maintainers, security reviewers, runtime owners, and governance reviewers. Include canonical record boundary reviewers if corruption risks confusion with canonical records.

### Recovery expectations

Recovery must include integrity assessment, restore evidence, gap disclosure, provenance continuity review, and explicit confirmation that canonical records were not changed to mask audit corruption.

## Trust Score Abuse

### Detection

- Monitoring or review identifies abnormal trust score changes, repeated self-reinforcing inputs, unexplained weight shifts, or inconsistent score explanations.
- Audit events show suspicious routing, repeated attempts to influence score-related inputs, or missing rationale.
- Reviewer feedback identifies misleading interpretation of advisory trust signals.

### Mitigation

- Treat suspicious trust score outputs as warning or degraded until reviewed.
- Preserve input evidence and score rationale for audit review.
- Do not allow trust score changes to bypass validator checks, signature validation, or human review.
- Adjust score interpretation only through documented policy and governance review.

### Escalation path

Escalate to policy, governance, security, and trust-kernel reviewers. Runtime owners must be included if abuse affects operational availability or output shape.

### Recovery expectations

Recovery must include affected-output review, audit trail updates, policy decision documentation where applicable, and human-supervised validation before restored trust score use.

## Witness Manipulation

### Detection

- Witness submissions show repeated identities, inconsistent signatures, suspicious timing, or conflicting provenance claims.
- Federation or validator checks detect witness disagreement, stale witness data, or unverifiable witness references.
- Audit trail review identifies witness evidence reused outside its documented context.

### Mitigation

- Mark suspicious witness evidence as warning, degraded, or rejected according to repository-defined rules.
- Preserve witness inputs, signatures, and provenance references for review.
- Prevent witness evidence from overriding canonical records, validators, or human review boundaries.
- Require additional review before relying on disputed witness material.

### Escalation path

Escalate to witness-layer maintainers, security reviewers, federation reviewers where relevant, and trust-kernel reviewers when witness evidence affects verification decisions.

### Recovery expectations

Recovery must document witness evidence status, reviewer decisions, affected verification outputs, and audit trail continuity. Disputed witness material must not be silently removed from review context.

## Operational Failures

### Detection

- Monitoring detects runtime outage, high error rate, latency spike, validator unavailability, audit write failure, backup failure, or rate limit saturation.
- Operator reports identify unexpected behavior during deployment, rollback, recovery, or maintenance.
- Audit trail review shows incomplete event capture or unclear operational state.

### Mitigation

- Follow documented runbooks for rollback, emergency freeze, degraded operation, and recovery.
- Preserve logs, audit events, deployment metadata, and operator actions.
- Avoid changing canonical records, schemas, validators, signing logic, federation logic, security workflows, policy files, or GitHub Actions as an emergency shortcut.
- Communicate known limitations and current advisory status to reviewers.

### Escalation path

Escalate to runtime owners, operations maintainers, security reviewers when applicable, and governance reviewers for production-impacting failures or emergency freezes.

### Recovery expectations

Recovery must include root-cause notes, audit trail review, restored health checks, backup or rollback evidence where applicable, and explicit human review before returning to normal operation.
