# Federation Risk Checklist

Metadata:

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- Runtime behavior change: none.
- Schema mutation: none.
- Validator logic mutation: none.
- Signing logic mutation: none.
- Federation logic mutation: none.
- Canonical artifact mutation: none.
- Human final authority: required.

## Purpose

This checklist helps reviewers evaluate HC:// validator federation synchronization proposals without changing runtime behavior, validator logic, signing semantics, federation behavior, schema contracts, policy evaluator behavior, or canonical record boundaries.

Federation peers are advisory. Local validators remain authoritative for local validation state, audit trail interpretation, and human-supervised validation routing.

## Required review boundaries

- [ ] The proposal is documentation-only or has a separate approved implementation scope.
- [ ] No protected paths are modified without explicit approval.
- [ ] No remote validator is described as overriding local validation state.
- [ ] No production readiness, truth guarantee, forensic certainty, or autonomous governance finality is claimed.
- [ ] Signature validation remains required for every inbound federation event.
- [ ] Immutable audit preservation is maintained for accepted, rejected, stale, replayed, and conflicting events.
- [ ] Human-supervised validation remains the escalation path for trust-kernel-impacting uncertainty.

## Replay attacks

- [ ] Federation messages include nonce or challenge metadata.
- [ ] Message identifiers are unique per source validator and sync scope.
- [ ] Timestamps and freshness windows are documented.
- [ ] Signatures cover the complete message body, including replay-protection fields.
- [ ] Replayed or late messages are preserved as audit trail warnings, not silently accepted.

## Forged validator claims

- [ ] Validator identity evidence is explicit.
- [ ] Unknown or unverifiable validator keys are rejected or marked as advisory-only risk inputs.
- [ ] Signature failures are preserved in the audit trail.
- [ ] Validator reputation or trust score changes do not bypass signature validation.
- [ ] Human review is required for unexpected validator identity transitions.

## Stale trust propagation

- [ ] Trust score events include issued and expiration timestamps.
- [ ] Receiving validators compare peer freshness against local policy.
- [ ] Stale scores remain historical context and do not override local state.
- [ ] Large or unexplained trust score shifts are escalated for human-supervised validation.
- [ ] Downstream displays preserve stale or degraded-state warnings.

## Witness spoofing

- [ ] Witness events identify the original witness source and propagating validator.
- [ ] Witness propagation includes signature references and provenance context.
- [ ] Witness observations are not merged into a single untraceable claim.
- [ ] Conflicting witness claims are recorded as separate evidence branches.
- [ ] Spoofing indicators route to human-supervised validation before user-facing trust interpretation changes.

## Federation partition scenarios

- [ ] Peer unavailability is recorded as degraded federation context.
- [ ] Missing federation input is not replaced with fabricated defaults.
- [ ] Local validation can continue only within local evidence limits.
- [ ] Partition recovery preserves pre-partition and post-partition audit trail continuity.
- [ ] Divergent peer state after recovery is treated as conflict evidence until reviewed.

## Reviewer outcome

Use this checklist to classify federation risk before merge:

| Outcome | Meaning | Required action |
| --- | --- | --- |
| Low documentation risk | Clarifies advisory architecture only. | Run terminology, docs drift, and canonical artifact checks. |
| Review-required risk | Affects trust interpretation language or user-facing confidence. | Add human-supervised validation notes and reviewer routing. |
| Escalation risk | Touches schema contracts, validator logic, signing semantics, federation behavior, policy evaluator behavior, or canonical record boundaries. | Stop and request explicit approval before implementation. |

## Related architecture

See `docs/runtime/validator-federation-sync.md` for the advisory federation synchronization architecture and examples.
