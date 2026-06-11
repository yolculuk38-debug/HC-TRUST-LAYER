# Public Validator MVP Specification

> **Mode:** documentation-only MVP specification  
> **Scope:** smallest public-safe HC:// validator journey  
> **Posture:** advisory-only, local-only first, human-supervised  
> **Boundary:** no runtime, validator, schema, record, hash, QR, signing, federation, policy, workflow, backend, database, account, or production hosting change

## Purpose

This page is the official small Public Validator MVP specification for the current planning gap identified in the Public Validator MVP readiness review.

The MVP helps a public reader inspect demo-safe HC:// verification signals. It does not prove truth, establish legal authority, certify security, provide forensic certainty, operate federation, or replace human review.

## MVP Posture

Every MVP result and public-facing explanation must preserve this posture:

```yaml
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
human_final_authority: true
processing_model: local_only_first
```

Required interpretation:

- `advisory_only=true`: output is a review aid, not a final decision.
- `public_safe=true`: output must not expose secrets, private data, protected review notes, or restricted evidence.
- `truth_guarantee=false`: passing local checks does not prove real-world truth.
- `human_review_required=true`: a visible human review checkpoint is required before reliance.
- `human_final_authority=true`: human reviewers preserve final interpretation and escalation authority.
- `processing_model=local_only_first`: the MVP should run from local demo inputs, local commands, or local runtime surfaces before any hosted service is considered.

The MVP must not claim production readiness, legal authority, security certification, forensic certainty, live federation, autonomous governance, autonomous enforcement, or objective truth verification.

## Smallest User Journey

The official smallest MVP journey is:

```text
README.md
→ docs/demo/mini-public-validator-demo.md
→ demo-safe input
→ local runtime `POST /verify/{record_id}` endpoint
→ advisory public-safe result
→ human review checkpoint
```

User-facing steps:

1. Open `README.md` for repository orientation.
2. Follow `docs/demo/mini-public-validator-demo.md` for the public-safe demo flow.
3. Use only the official demo-safe input type defined below.
4. Run the official local runtime `POST /verify/{record_id}` route with a demo-safe `qr_input` payload.
5. Read the advisory public-safe result.
6. Stop at the human review checkpoint before treating the result as reliable for any consequential use.

## Official Executable MVP Path

The official executable MVP path is the local HC:// runtime route:

```text
POST /verify/{record_id}
```

Use this route only in a local runtime environment with a demo-safe `qr_input` payload. The request body shape is:

```json
{
  "qr_input": "hc://HC-DEMO-2026-0001 hash:advisory demo-public-safe"
}
```

Example local invocation when the reference runtime is already running locally:

```sh
curl -s -X POST "http://127.0.0.1:8000/verify/HC-DEMO-2026-0001" \
  -H "Content-Type: application/json" \
  -d '{"qr_input":"hc://HC-DEMO-2026-0001 hash:advisory demo-public-safe"}'
```

Executable path requirements:

- `record_id` must identify a demo-safe HC:// review target.
- `qr_input` must be demo-safe, public-safe, and non-secret.
- The route is local-only first and does not require a hosted backend.
- The response remains advisory and public-safe, with human review required before reliance.
- A route response is not a production, truth, legal, security, forensic, signing, federation, or autonomous authority result.

## Official MVP Input Type

The only official MVP input type is a demo HC:// record, proof, or package.

Input requirements:

- demo HC:// record/proof/package only;
- no secrets;
- no private data;
- no live external network dependency;
- no hosted backend requirement;
- no mutation of canonical records, schemas, validators, signing material, federation material, policy, workflows, or generated artifacts.

Example demo-safe input shape:

```yaml
input_type: demo_hc_record_package
record_id: HC-DEMO-2026-0001
record_type: public_validator_demo
purpose: explanatory_flow_only
source: local_demo
contains_secrets: false
contains_private_data: false
requires_external_network: false
requires_hosted_backend: false
```

## Official MVP Result Shape

Every MVP result must use this top-level shape, even when some checks are `UNKNOWN` or `NOT_RUN`:

```yaml
record_id: HC-DEMO-2026-0001
status: NEEDS_REVIEW
schema_status: NOT_RUN
hash_status: NOT_RUN
provenance_status: UNKNOWN
warnings:
  - Demo result only; human review required before reliance.
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
human_final_authority: true
next_steps:
  - Review warnings.
  - Inspect available public-safe evidence.
  - Escalate incomplete, disputed, ambiguous, or consequential results to a human reviewer.
```

Field requirements:

| Field | Requirement |
| --- | --- |
| `record_id` | Identifies the demo HC:// record, proof, or package boundary under review. |
| `status` | Uses the official status taxonomy below. |
| `schema_status` | Reports local schema or shape check status when executed. |
| `hash_status` | Reports local hash or integrity check status when executed. |
| `provenance_status` | Reports public-safe provenance evidence status when available. |
| `warnings` | Lists missing, partial, ambiguous, conflicting, or advisory-boundary cautions. |
| `advisory_only` | Must be `true`. |
| `public_safe` | Must be `true`. |
| `truth_guarantee` | Must be `false`. |
| `human_review_required` | Must be `true` and visible in the result. |
| `human_final_authority` | Must be `true`; human reviewers preserve final authority. |
| `next_steps` | Gives review-oriented next actions, not autonomous decisions. |

## Status Taxonomy

The MVP uses these statuses for `status`, `schema_status`, `hash_status`, and `provenance_status` where applicable:

| Status | Meaning |
| --- | --- |
| `VERIFIED` | Local checks passed within the MVP scope. This does not prove truth, legal authority, safety, forensic certainty, or production readiness. |
| `NEEDS_REVIEW` | Human review is required before reliance because the result is incomplete, ambiguous, disputed, consequential, or otherwise not final. |
| `REVIEW_REQUIRED` | Same public meaning as `NEEDS_REVIEW`; use when a surface needs a stronger mandatory-review label. |
| `INVALID` | A local shape, hash, proof, or package check failed. Human review may still be needed to interpret impact. |
| `UNKNOWN` | There is insufficient public-safe evidence to determine the check result. |
| `NOT_RUN` | The check was not executed. |

Required status rule: `VERIFIED` means local checks passed only. It must never mean objective truth, production approval, legal certification, safety certification, forensic certainty, federation acceptance, or autonomous authority.

## Component Reuse Map

This specification maps existing components without changing them:

| Existing surface | MVP reuse role |
| --- | --- |
| `docs/demo/mini-public-validator-demo.md` | Public-facing demo entry and explanatory flow. |
| `src/hc_runtime` routes | Official executable MVP path through local `POST /verify/{record_id}` with a demo-safe `qr_input` payload. |
| `src/hc_trust` helpers | Local helper candidates for shape, hash, proof, provenance, and package checks. |
| `src/public_validator.py` | Adjacent reusable public validator helper surface. |
| `src/public_validator_api.py` | Adjacent reusable public validator API payload helper surface. |
| `src/public_verification_response.py` | Adjacent reusable public verification response formatting surface. |
| `src/verification_cli.py` | Adjacent local command candidate for package-oriented demos; not the official executable MVP path. |
| `examples/` | Demo-safe examples and explanatory fixtures when public-safe and non-canonical. |
| `schema/` | Reference material for record-shape boundaries; this specification does not modify schemas. |

## Known Helper/API Gap

Existing public validator helper/API surfaces may emit `VERIFIED` or trusted-like results without the full runtime advisory/public-safe posture fields defined here.

Until aligned, those helper/API surfaces are adjacent reusable surfaces, not the complete official MVP result contract by themselves. A complete MVP result must visibly include `advisory_only=true`, `public_safe=true`, `truth_guarantee=false`, `human_review_required=true`, and `human_final_authority=true`.

## Human Review Checkpoint

Every MVP journey ends with a human review checkpoint.

A human reviewer must decide whether the available public-safe evidence, local check results, provenance context, warnings, and missing information are sufficient for the intended use. High-impact, disputed, ambiguous, incomplete, or externally consequential uses require escalation through the appropriate human-supervised review path.

## Non-Goals and Deferred Work

This documentation-only MVP specification does not add, modify, or require:

- runtime code;
- validators;
- tests;
- schemas;
- canonical records;
- hashes;
- QR artifacts;
- generated artifacts;
- signing;
- federation;
- policy;
- workflows;
- governance rules;
- backend services;
- databases;
- authentication or accounts;
- rate limiting;
- CAPTCHA or WAF controls;
- production or public hosting.

These items remain deferred unless explicitly approved in a later scoped change.

## Review Boundary

This page is a planning and specification document only. It does not modify runtime behavior, canonical artifacts, trust-kernel paths, validator semantics, schema definitions, records, signatures, federation behavior, policy, workflows, or generated outputs.
