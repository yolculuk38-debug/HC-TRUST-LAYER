# HC:// Governance Framework

## Merge Authority
- Maintainers designated in repository governance are responsible for final merge approval.
- Security- or protocol-critical changes require at least two independent approvals.

## Validator Roles
- Validators evaluate records against protocol and policy requirements.
- Validator decisions must be signed and auditable.
- Validator misconduct may result in temporary or permanent trust penalties.

## Federation Participation
- Federation participants must publish node identity and verification policy metadata.
- Participants must support deterministic verification export/import interfaces.

## Moderation Principles
- Moderation actions must be evidence-backed, proportional, and reversible through review.
- Content actions are separated from cryptographic verification history.

## Dispute Handling
- Disputed records enter `disputed` or `quarantined` status depending on risk.
- Dispute dossiers must include claims, evidence, and signed adjudication outcomes.

## Emergency Freeze Policy
- Emergency freeze may be applied for active abuse, key compromise, or replay attack events.
- Freeze actions must be logged with timestamp, actor, and scope.
- Unfreeze requires post-incident review.

## Review Escalation Flow
1. Initial validator review.
2. Secondary validator review for contested outcomes.
3. Governance council escalation for unresolved disputes.
4. Final published ruling with audit trace.

## Trust and Reputation Principles
- Reputation is earned through consistent, auditable, and policy-compliant behavior.
- Trust scoring is transparent at the signal category level.
- Revocation and recovery pathways must be explicitly defined and logged.
