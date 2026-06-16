# Source Module Purpose Index — 2026-06-16

Status: advisory source-surface index.

This document classifies the `src/` implementation surface so HC-TRUST-LAYER code can be reviewed by trust boundary instead of by file-name guesswork.

## Boundary

- advisory_only=true
- public_safe=true
- truth_guarantee=false
- CI/checks are evidence, not trust authority.
- Human final authority remains required.
- This index is documentation only.
- This index does not modify runtime behavior, validators, schemas, records, QR data, hash data, workflows, tests, or generated artifacts.
- No module is moved, renamed, deleted, disabled, or consolidated by this document.

## Source operating rule

`src/` should contain active implementation only. Planning, roadmap, governance explanation, and historical narrative belong in `docs/` unless they are code comments needed to preserve runtime safety boundaries.

Implementation should be reviewed by trust boundary:

```text
runtime entry -> validator pipeline -> canonical bridge -> schema/hash checks -> QR/public validator -> redaction/events/state -> advisory response
```

## Active source layers

| Layer | Purpose | Review posture |
|---|---|---|
| Runtime service layer | FastAPI/runtime entry points and advisory runtime responses. | Runtime contract changes require tests. |
| Telemetry layer | Health, runtime, and queue telemetry with explicit advisory/public-safe markers. | Response keys must stay deterministic. |
| Validator pipeline layer | Advisory pipeline hooks for canonical bridge, schema, hash, trust assignment, and escalation routing. | No truth guarantee. Human review stays visible. |
| Canonical bridge layer | Lookup and compare local canonical records where configured. | Missing, malformed, and mismatch states must remain visible. |
| Schema/hash layer | Local schema-like checks and SHA-256 content-hash comparison. | Must not imply final correctness beyond recorded evidence. |
| QR safety layer | QR parsing, record bridge, spoof protection, and public validator QR boundaries. | Security-adjacent. High review before consolidation. |
| Public validator layer | Local/demo public verification behavior and public-safe result formatting. | Demo/local first unless explicit deployment PR changes scope. |
| Redaction layer | Public-safe redaction helper behavior. | Must not regress public-safe output behavior. |
| Event/state layer | Runtime event store, queue store, replay/degraded visibility. | Append-only and traceable behavior must be preserved. |
| Package verification layer | Local verification package hash/proof checks and CLI-facing verification behavior. | Advisory-only local verification; no production guarantee. |

## Known module anchors

These source anchors were verified from current repository content during this indexing pass:

| Path | Class | Purpose |
|---|---|---|
| `src/hc_runtime/runtime.py` | `ACTIVE_IMPLEMENTATION` | Advisory runtime components, validator pipeline hooks, canonical bridge, schema/hash hook routing, trust assignment, escalation routing. |
| `src/hc_runtime/routes/health.py` | `ACTIVE_IMPLEMENTATION` | Health and telemetry routes for advisory runtime prototype, including `/health`, `/telemetry/health`, `/telemetry/runtime`, and `/telemetry/queues`. |
| `src/hc_runtime/state.py` | `ACTIVE_IMPLEMENTATION` | Shared runtime stores used by telemetry and runtime behavior. |
| `src/hc_runtime/redaction.py` | `ACTIVE_IMPLEMENTATION` | Public-safe redaction helper layer used by runtime behavior. |
| `src/hc_runtime/events.py` | `ACTIVE_IMPLEMENTATION` | Runtime event store and traceability layer. |
| `src/hc_runtime/decision_engine.py` | `ACTIVE_IMPLEMENTATION` | Trust-state decision helper layer. |
| `src/hc_runtime/canonical_record_loader.py` | `ACTIVE_IMPLEMENTATION` | Canonical record loading and malformed record boundary. |
| `src/hc_runtime/qr_spoof_protection.py` | `ACTIVE_IMPLEMENTATION` | QR spoof and canonical-source risk inspection. |

This is not an exhaustive file inventory. It is the first source-purpose map. Future PRs may add a generated or complete source inventory if needed.

## Runtime contract guardrails

Runtime and API behavior must preserve:

- `advisory_only=true` where applicable;
- `public_safe=true` where applicable;
- `truth_guarantee=false` where applicable;
- deterministic response keys where tests expect them;
- visible warnings for degraded, replay, missing, malformed, or mismatch states;
- no hidden fallback that makes unsafe states look verified;
- no production-readiness claim from local/demo runtime behavior.

## Source cleanup rules

Do not change source modules from visual clutter alone.

A source cleanup or consolidation PR requires:

1. exact files listed;
2. current tests identified;
3. protected-path risk checked;
4. behavior-preserving intent stated;
5. targeted tests updated or run;
6. no advisory/public/truth boundary weakening;
7. post-merge audit if behavior changes.

## Immediate next index work

1. `scripts/` tool purpose index.
2. generated/reference artifact index.
3. historical/evidence index.
4. public/demo docs index.
5. optional complete source inventory if GitHub file listing is needed later.

## Final rule

Source code must stay boring, deterministic, and evidence-oriented.

```text
small modules
explicit warnings
stable contracts
no hidden authority
no trust overclaim
```
