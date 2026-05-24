# HC-TRUST-LAYER Trust Decay and Risk History Foundation

## Status

- documentation foundation only
- no production trust scoring implementation
- no trust score algorithm in this phase
- no validator behavior changes in this phase
- no schema changes in this phase
- no workflow changes in this phase

## Purpose

This document defines a foundation for future trust decay and risk history handling in HC-TRUST-LAYER.

The goal is to prepare verification infrastructure for historical trust-sensitive signals while preserving human-supervised validation and explicit audit trail reasoning.

HC:// verification outputs must remain explainable, provenance-linked, and reviewable by humans.

## Why Static Trust Is Not Enough

Static trust can miss repeated warning patterns and long-horizon reliability drift.

A trust state that never changes can hide:
- repeated warning accumulation
- unresolved validation failure history
- replay indicator recurrence
- persistent provenance completeness gaps
- federation synchronization instability

HC-TRUST-LAYER therefore needs explicit risk history and trust decay concepts so future policy evaluator and trust graph decisions can account for historical context.

## Trust Decay Overview

Trust decay is the principle that trust should not be permanent by default.

Future HC-TRUST-LAYER trust decay models should:
- reduce confidence when warning patterns recur
- reduce trust state after revocations
- increase review requirements for repeated failures
- preserve human-supervised validation as final authority
- avoid any automatic truth determination

Trust decay is a governance and verification infrastructure concept, not objective truth scoring.

## Risk History Overview

Risk history is a structured historical record of warning and failure context tied to canonical verification artifacts.

Risk history should preserve:
- time-ordered event context
- provenance references
- validator and witness participation context
- policy evaluator outcomes
- audit trail linkage

This enables future trust graph interpretation without introducing opaque scoring authority.

## Historical Dimensions for Future Evaluation

### Validator Behavior History

Future models may track validator consistency, stale-state patterns, and revoked-signature handling quality.

### Witness Reliability History

Future models may track witness reference quality, contradiction frequency, and unresolved dispute participation.

### Repeated Warning Patterns

Future models may detect warning recurrence windows and escalation cadence rather than treating each warning as isolated.

### Validation Failure History

Future models may accumulate repeated validation failures and classify them for increased human-supervised review.

### Replay Indicator History

Future models may track suspicious replay patterns across HC:// provenance contexts and trust graph lineage edges.

### Provenance Completeness History

Future models may capture missing-source trends, partial provenance snapshots, and unresolved provenance fields.

### Federation Trust History

Future models may evaluate failed federation sync frequency, stale mirror relationships, and federation dispute carryover.

### Policy Violation History

Future models may track repeated terminology and policy violations as risk history context for future policy evaluator decisions.

## Future Risk Signals (Not Yet Implemented)

The following are potential future risk signals for HC-TRUST-LAYER:

- repeated validation failures
- malformed verification packages
- inconsistent witness references
- revoked signatures
- stale validator state
- suspicious replay patterns
- generated artifact boundary violations
- terminology/policy violations
- failed federation sync
- unresolved dispute status
- source repository drift

These signals are design inputs only and do not currently produce autonomous trust outcomes.

## Trust Decay Principles

HC-TRUST-LAYER trust decay principles for future phases:

1. trust should not be permanent by default
2. warnings should affect future evaluation
3. revocations should reduce trust state
4. repeated failures should increase review requirements
5. human-supervised validation remains required
6. no automatic truth determination

## Possible Future Outcomes (Conceptual)

Potential future trust/risk routing states:

- **normal**
- **watch**
- **degraded**
- **restricted**
- **blocked**
- **revoked**

These outcomes are conceptual vocabulary for future governance and policy evaluator alignment. They are not active runtime scoring states in this phase.

## Risks and Safety Concerns

Any future trust decay or risk history layer must address:

- unfair trust decay
- false positives
- validator poisoning
- coordinated reports
- opaque scoring risk
- privacy concerns
- over-automation risk

Mitigations must prioritize transparent reasoning, provenance evidence, and human-supervised validation.

## Non-Goals

This foundation explicitly does **not** introduce:

- production trust scoring
- automatic banning
- truth scoring
- autonomous model authority
- autonomous governance

## Related Documents

- Policy evaluator foundation: `docs/policy-evaluator.md`
- Trust graph foundation: `docs/trust-graph.md`
- Verification levels model: `docs/verification-levels.md`
- Signing architecture foundation: `docs/signing-architecture.md`
- Public verification API architecture draft: `docs/public-verification-api.md`
- Federation roadmap and architecture: `docs/federation-architecture.md`
- Message/content provenance foundation: `docs/message-content-provenance.md`
