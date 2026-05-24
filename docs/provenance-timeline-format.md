# HC-TRUST-LAYER HC:// Provenance Timeline Format (MVP-1)

## Purpose

This document defines a documentation-only provenance timeline format for human-readable chronology views in HC-TRUST-LAYER and HC:// MVP-1.

## Timeline Overview

The provenance timeline should present verification-relevant chronology in a simple, ordered sequence.

Each timeline entry should prefer:

- timestamp context
- event category
- short meaning summary
- evidence pointer availability note

## First Seen Concepts

The timeline should identify first-seen moments for artifacts or references within displayed scope.

First-seen markers help users understand when an artifact entered the visible provenance context.

## Snapshot Chronology

Timeline entries should include trust snapshot events:

- snapshot creation time
- snapshot scope summary
- linkage to related provenance references

## Validator Review Chronology

The timeline should include validator review events with:

- validator identity reference
- review timestamp
- summary outcome label

## Replay Chronology

Replay-related chronology should show when replay warning signals first appeared and whether later events changed interpretation.

## Dispute Chronology

Dispute events should be visible in timeline sequence:

- dispute initiated
- dispute updated
- dispute resolved or unresolved-state continuation

## Federation Verification Chronology

When federation-relevant verification context exists in displayed scope, timeline entries should show chronology markers without implying live federation guarantees.

## Audit Continuity Concepts

Timeline formatting should preserve audit trail continuity interpretation by showing ordered history and clearly labeling missing or unknown intervals.

## Related References

- `docs/trust-result-standard.md`
- `docs/verification-status-ux.md`
- `docs/replay-warning-standard.md`
- `docs/provenance-viewer.md`
