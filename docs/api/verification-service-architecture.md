# Verification Service Architecture Foundation

## Purpose and Scope

The verification service provides a modular public API layer for HC-TRUST-LAYER consumers that need canonical verification, trust lookup, revision history, witness summaries, and federation provenance. This document defines foundation-level behavior only and avoids production deployment assumptions.

The architecture in this phase is designed to:
- preserve backward compatibility with existing CLI/SDK workflows,
- establish canonical endpoint contracts,
- normalize verification semantics across subsystems,
- and keep transport and storage implementations replaceable.

## Service Responsibilities

The verification service is responsible for:
- exposing read-oriented verification APIs,
- normalizing verification and provenance state values,
- composing responses from explorer, validator, and federation inputs,
- returning deterministic schema-compatible payloads,
- and providing implementation boundaries for future scaling and security controls.

The service is not responsible in this phase for write operations, asynchronous queue orchestration, external auth integration, or deployment policy decisions.

## Subsystem Interaction Model

### Explorer Interaction

Explorer integration is read-oriented. The service consults explorer indexes to resolve record identifiers and locate candidate artifacts.

Rules:
- explorer indexes are treated as discovery sources, not verification authority,
- generated artifacts remain outside canonical API state unless validator/federation checks corroborate them,
- canonical lookup follows stable record ID resolution before any derived artifact expansion.

### Validator Interaction

Validators provide integrity and state assertions for records and revisions.

The API layer:
- submits canonical record IDs and optionally revision hints,
- consumes validator status outputs,
- maps validator outputs to normalized API states,
- and records verification timestamp at response assembly time.

### Federation Interaction

Federation connectors provide distributed source summaries and optional corroboration metadata.

The API layer:
- aggregates per-source federation outcomes,
- normalizes source states using the shared verification-state enum,
- and reports federation status independent from trust score confidence.

### Provenance Lookup Behavior

Provenance lookup composes witness and revision information into a stable response fragment.

Required provenance fields:
- witness count,
- revision state,
- federation state,
- verification timestamp,
- provenance status,
- integrity status.

## Canonical Endpoints

The following endpoints define first-phase canonical read APIs:

- `GET /verify/{record_id}`
  - full verification result with provenance and source summary.
- `GET /trust/{record_id}`
  - trust score and rationale-oriented summary.
- `GET /history/{record_id}`
  - revision chain and current revision state.
- `GET /witness/{witness_id}`
  - witness summary, status, and optional metadata.
- `GET /federation/{record_id}`
  - federated source summary for record-level lookup.

## Verification State Normalization

All route responses use the same canonical states:
- `verified`
- `suspicious`
- `disputed`
- `revoked`
- `superseded`
- `unavailable`

Normalization goals:
- avoid subsystem-specific status drift,
- maintain compatibility with existing HC-TRUST-LAYER terminology,
- and keep client logic deterministic.

## Explorer/API Compatibility Notes

- Explorer index usage must remain deterministic and record-id first.
- Generated artifacts are non-canonical until corroborated by verification flows.
- Canonical lookup rules prioritize explicit record IDs over inferred links.
- API responses should indicate unavailable state rather than invent inferred certainty.

## API Security Notes

Security behavior in this foundation phase includes:
- replay-safe verification assumptions at the request/response contract level,
- malformed request handling through deterministic error surfaces,
- verification integrity boundaries between discovery and assertion subsystems,
- trust score limitation disclosure (scores are advisory and context-dependent).

## Future Scalability Notes

The architecture is intentionally modular to support future additions:
- rate limiting policies at endpoint and actor levels,
- federation caching strategies for repeated provenance lookups,
- distributed verification execution across validator domains,
- async validation workflows for high-latency sources,
- external integration adapters for downstream ecosystems.

## Modularity and Compatibility Requirements

- Backward compatibility must be preserved for existing public interfaces.
- No assumptions are made about production infra, auth topology, or deployment targets.
- Route, model, and integration layers must remain independently replaceable.
- Language should remain implementation-oriented and avoid hype framing.
