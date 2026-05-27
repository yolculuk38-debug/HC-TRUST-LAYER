# Reference Runtime Skeleton Plan (HC://)

This document defines the first reference runtime skeleton plan for HC:// within HC-TRUST-LAYER.

The scope is documentation-only and advisory. It does not modify canonical record surfaces, validator logic, federation logic, or workflow controls.

## Purpose and Scope

The plan combines three aligned skeletons:

1. reference runtime API skeleton
2. public verification gateway skeleton
3. validator runtime service skeleton

The goal is to provide a minimal, reviewable runtime shape that supports human-supervised validation, preserves audit trail continuity, and keeps public responses advisory-only.

## 1) Reference Runtime API Skeleton

### API purpose

The reference runtime API exposes minimal verification and routing interfaces that connect public verification entrypoints, validator runtime services, and trust-kernel review boundaries.

### Public-safe endpoints

Public-safe endpoints should return advisory verification summaries only, with no private data exposure and no hidden trust-state mutation.

### Validator endpoints

Validator endpoints should accept validation intake requests and execute bounded verification hooks under human-supervised validation expectations.

### Federation endpoints

Federation endpoints should support review routing and inter-organization escalation handoff without asserting autonomous governance finality.

### Audit/history endpoints

Audit/history endpoints should return auditable event history slices suitable for public-safe visibility and reviewer follow-up.

### Recovery endpoints

Recovery endpoints should support reconstruction requests for continuity and traceability workflows without modifying canonical record definitions.

### Telemetry endpoints

Telemetry endpoints should provide minimal runtime health and operational status signals for observability.

## 2) Public Verification Gateway Skeleton

### QR verification entrypoint

The gateway should accept QR-derived verification requests and normalize them into a public-safe verification query.

### Record lookup route

The gateway should resolve record identifiers through bounded lookup logic and route unresolved identifiers to safe failure pathways.

### Hash verification route

The gateway should submit record and digest context for integrity verification hooks in the validator runtime service.

### Trust-state response route

The gateway should return advisory trust-state outputs with explicit non-guarantee language and escalation cues.

### Advisory response route

The gateway should return concise public-safe advisory summaries that preserve HC:// terminology and uncertainty boundaries.

### Audit/history response route

The gateway should expose audit/history views that include event continuity context and non-canonical artifact boundaries where relevant.

### Failure response route

The gateway should return public-safe failure responses that avoid authority inflation and avoid leaking private runtime state.

## 3) Validator Runtime Service Skeleton

### Validation intake

Accept normalized verification requests from the gateway and attach request provenance metadata for downstream audit trail continuity.

### Schema validation hook

Run schema validation hooks against request payload shapes defined by runtime API contracts, without changing canonical schemas.

### Hash/integrity verification hook

Run hash and integrity checks against supplied evidence pointers and produce bounded verification outcomes.

### Trust-state decision hook

Route validated inputs through a decision hook aligned with the verification decision engine model to produce advisory trust-state outputs.

### Escalation routing hook

Route uncertain, high-risk, or policy-sensitive outcomes to human-supervised validation paths.

### Federation routing hook

Route qualified cross-domain review requests to federation interfaces while preserving provenance and audit trail continuity.

### Continuity event hook

Create auditable continuity events for each major verification step, including request intake, decision outcomes, escalation, and failure handling.

## 4) Minimal Endpoint Examples

These example routes define a minimal reference skeleton surface:

- `GET /verify/{record_id}`
- `GET /verify/{record_id}/history`
- `POST /runtime/validate`
- `POST /runtime/trust-state`
- `POST /federation/review`
- `POST /recovery/reconstruct`
- `GET /telemetry/health`

## 5) Minimal Runtime Flow

Minimal request flow:

QR request  
→ public gateway  
→ validator runtime  
→ decision engine  
→ event store  
→ public-safe response

This flow is intentionally minimal and advisory so reviewers can inspect trust-kernel boundaries before any implementation expansion.

## 6) Safeguards

The reference skeleton must preserve the following safeguards:

- advisory-only response
- no truth guarantee
- no private data exposure
- no hidden trust-state mutation
- auditable event creation
- public-safe failure responses

## 7) Future Implementation Notes

Potential implementation direction (non-binding):

- FastAPI reference runtime
- static gateway compatibility
- JSON response contracts
- event-store integration
- validator plugin architecture
- federation transport layer

Any non-trivial trust-kernel-impacting implementation should be routed through explicit human-supervised validation and repository-defined checks before merge.

## Alignment References

This skeleton plan aligns with:

- `docs/core/runtime-api-contract-architecture.md`
- `docs/core/minimal-reference-runtime-architecture.md`
- `docs/core/public-qr-verification-gateway.md`
- `docs/core/verification-decision-engine-model.md`
- `docs/core/runtime-storage-contracts-and-event-store-schema.md`
- `docs/core/reference-operational-data-flow.md`

## Non-Goals

- No production-readiness claim
- No canonical schema change
- No validator behavior change
- No workflow control change
- No federation logic change
