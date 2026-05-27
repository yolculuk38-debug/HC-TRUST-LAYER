# Runtime Policy and Enforcement Architecture

## Scope and posture

This document defines an advisory runtime policy and enforcement model for HC-TRUST-LAYER and HC://.

It describes how the operational runtime, validator orchestration, observability layer, federation review routing, and public verification gateway coordinate policy decisions while preserving human-supervised validation.

This is architecture guidance only. It does not claim production readiness, autonomous authority, or unreviewed enforcement finality.

## Objectives

- classify runtime violations into consistent decision classes
- apply bounded, auditable trust-state impact updates
- route high-sensitivity cases to federation review
- preserve provenance and audit trail continuity
- enforce continuity snapshot controls before public exposure changes

## Runtime policy domains

The runtime policy evaluator consumes normalized signals from:

1. operational runtime event stream
2. validator orchestration outcomes
3. observability layer anomaly and integrity signals
4. federation review routing metadata
5. public verification gateway exposure controls

Each signal is evaluated as advisory input until human-supervised validation confirms trust-kernel-impacting outcomes.

## Policy evaluation lifecycle

## 1) Signal intake

- collect runtime events, validator outcomes, and observability signals
- bind events to agent context and canonical record references where available
- stamp each signal with provenance source, confidence level, and timestamp

## 2) Normalization and pre-checks

- normalize signal format for policy evaluation
- deduplicate correlated events within a bounded evaluation window
- verify continuity snapshot availability for affected entities

## 3) Violation classification

Signals are mapped into one of three classes:

### Soft policy violations

Low-severity deviations with limited trust-kernel risk and no immediate canonical boundary concern.

Typical handling:
- advisory downgrade
- localized trust degradation
- increased observability sampling

### Hard policy violations

High-severity deviations that indicate integrity or provenance instability and require immediate containment.

Typical handling:
- escalation
- quarantine
- continuity snapshot enforcement
- public exposure restriction

### Federation-triggering violations

Violations that exceed local adjudication boundaries and require federation review routing.

Typical handling:
- federation review routing activation
- quarantine or exposure restriction while review is pending
- trust degradation with explicit reviewer handoff

## 4) Decision synthesis

The policy evaluator computes a decision package containing:

- violation class
- trust-score delta proposal
- enforcement actions
- escalation level
- federation review requirement
- continuity snapshot requirement
- reviewer handoff note

## 5) Enforcement staging

The runtime stages decisions in two lanes:

- **automatic advisory lane:** low-risk, reversible actions (for example advisory downgrade)
- **human-supervised lane:** trust-kernel-impacting or federation-triggering actions requiring explicit reviewer validation

## 6) Audit trail persistence

All decision packages and resulting actions must preserve:

- provenance references
- decision rationale
- enforcement timestamps
- actor attribution (runtime component or reviewer)
- continuity snapshot identifiers

## 7) Post-decision observation

- monitor for recurrence or escalation within a rolling window
- emit observability events for policy feedback loops
- trigger follow-up review when repeated soft violations accumulate

## Violation model separation summary

| Class | Severity posture | Default runtime action | Reviewer requirement |
|---|---|---|---|
| Soft policy violation | Cautionary | Advisory downgrade + bounded trust degradation | Recommended when repeated |
| Hard policy violation | Containment | Escalation + quarantine + exposure restriction | Required |
| Federation-triggering violation | Cross-boundary | Federation review routing + protective controls | Required |

## Trust-score impact model

Trust-score impact remains advisory until human-supervised validation confirms trust-kernel-impacting outcomes.

### Impact inputs

- violation class
- recurrence frequency within evaluation window
- signal confidence from observability and validator orchestration
- continuity snapshot presence/absence
- federation review pending state

### Baseline delta ranges

- soft violation: `-2` to `-8`
- hard violation: `-10` to `-25`
- federation-triggering violation: `-15` to `-35`

### Modifiers

- recurrence multiplier: up to `1.5x`
- missing continuity snapshot penalty: `-5`
- validated remediation recovery credit: `+3` to `+10`

### Floors and guards

- trust degradation is bounded by policy floor thresholds
- score restoration requires documented remediation evidence
- no automatic return to pre-violation state without reviewer confirmation for hard or federation-triggering classes

## Escalation thresholds

Escalation uses cumulative score and event patterns:

- **Level 0 (observe):** soft violation, low recurrence
- **Level 1 (operator review):** repeated soft violations or single hard violation
- **Level 2 (trust-kernel reviewer):** high-confidence hard violation, quarantine active
- **Level 3 (federation review):** federation-triggering violation or unresolved Level 2 breach beyond window

Threshold examples:

- escalate to Level 1 after `3` soft violations in `24h`
- escalate to Level 2 when trust-score delta exceeds `-20` in `24h`
- escalate to Level 3 when federation-triggering criteria are met or quarantine exceeds defined local resolution window

## Enforcement action definitions

### Escalation

Routes the decision package to the required reviewer lane with context-complete provenance and audit trail links.

### Federation review

Creates a federation review routing record with violation summary, trust impact proposal, and continuity snapshot references.

### Quarantine

Temporarily isolates affected runtime entities from normal trust propagation paths until reviewer disposition.

### Advisory downgrade

Lowers verification confidence presentation while preserving availability for supervised review.

### Public exposure restriction

Reduces or masks public verification gateway exposure for affected entities pending review outcome.

### Trust degradation

Applies bounded trust-score reduction based on class and modifiers, with reversible recovery path through validated remediation.

### Continuity snapshot enforcement

Requires continuity snapshot capture and integrity reference linkage before any high-impact decision is finalized.

## Runtime enforcement examples

## Example A: Soft violation handling

- observability detects intermittent metadata mismatch with low confidence
- policy classifies as soft policy violation
- runtime applies advisory downgrade and `-4` trust-score delta
- if repeated three times in `24h`, escalation advances to Level 1 for operator review

## Example B: Hard violation with quarantine

- validator orchestration reports deterministic replay inconsistency
- policy classifies as hard policy violation
- runtime initiates quarantine, public exposure restriction, and continuity snapshot enforcement
- decision package is routed to Level 2 trust-kernel reviewer for human-supervised validation

## Example C: Federation-triggering route

- cross-boundary provenance conflict appears across federation-linked verification paths
- policy classifies as federation-triggering violation
- runtime applies protective trust degradation and routes federation review request
- public verification gateway remains restricted until reviewer disposition and continuity confirmation

## Policy decision flow diagrams

## High-level lifecycle

```text
[Signal Intake]
      |
      v
[Normalization + Pre-checks]
      |
      v
[Violation Classification]
  | soft | hard | federation-triggering
      |
      v
[Decision Synthesis]
      |
      v
[Enforcement Staging]
  | advisory lane | human-supervised lane
      |
      v
[Audit Trail Persistence]
      |
      v
[Post-decision Observation]
```

## Escalation and routing flow

```text
[Violation Classified]
      |
      v
[Compute Trust Delta + Threshold Check]
      |
      +--> if Level 0: observe + advisory downgrade
      |
      +--> if Level 1: operator review queue
      |
      +--> if Level 2: quarantine + trust-kernel reviewer queue
      |
      +--> if Level 3: federation review routing + exposure restriction
```

## Continuity snapshot enforcement flow

```text
[High-impact Decision Candidate]
      |
      v
[Snapshot Present?] -- no --> [Capture Snapshot] --> [Link Provenance + Audit Trail]
      | yes
      v
[Proceed to Human-supervised Validation]
      |
      v
[Finalize Advisory Outcome]
```

## Alignment map

- **operational runtime:** event intake, staging, enforcement execution
- **validator orchestration:** violation evidence and deterministic consistency signals
- **observability layer:** anomaly telemetry, recurrence detection, confidence weighting
- **federation review routing:** Level 3 adjudication and cross-boundary reviewer handoff
- **public verification gateway:** advisory downgrade display and exposure restriction controls

## Safeguards

- preserve advisory-only positioning for machine decisions
- require human-supervised validation for trust-kernel-impacting dispositions
- preserve canonical record boundaries and provenance continuity
- keep actions reversible and auditable where possible
- avoid unsupported claims about autonomous governance finality or guaranteed outcomes
