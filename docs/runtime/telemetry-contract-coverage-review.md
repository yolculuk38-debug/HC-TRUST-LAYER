# Telemetry Contract Coverage Review

## Executive Summary

This report reviews telemetry contract coverage for the HC:// advisory runtime after PR #483, PR #519, and PR #627. The review is REPORT ONLY and does not modify runtime code, tests, schemas, validators, workflows, governance rules, records, hashes, QR artifacts, generated artifacts, signing, federation, or policy.

Decision: **TELEMETRY CONTRACT SUFFICIENT**.

The telemetry contract is sufficiently hardened for the current v0.1.0 advisory runtime scope. The three telemetry endpoints expose consistent advisory metadata, preserve public-safe posture, avoid truth-guarantee claims, keep degraded state visible, and have targeted regression coverage for deterministic payload shape, queue edges, redaction, degraded runtime behavior, escalation queue behavior, and `human_review_required` bool algebra.

This is not a production-readiness finding. It is an advisory coverage finding limited to the inspected runtime telemetry surfaces and tests.

## Current Telemetry Contract

### Current telemetry endpoints

The runtime exposes these telemetry endpoints from `src/hc_runtime/routes/health.py`:

1. `/telemetry/health`
   - Returns the shared telemetry base payload.
   - Reflects degraded status when a `runtime_recovery_mode` runtime event exists.

2. `/telemetry/runtime`
   - Returns the shared telemetry base payload.
   - Adds `events_total` and `degraded_events` integer counters.

3. `/telemetry/queues`
   - Returns the shared telemetry base payload.
   - Adds `verification_queue`, `escalation_queue`, `replay_warning_queue`, and `degraded_queue_handling`.
   - Queue fields currently expose redacted queue item lists, not counts.

### Current response contract shape

The shared telemetry base currently returns these keys, in deterministic insertion order:

1. `status`
2. `runtime_mode`
3. `advisory_only`
4. `runtime_stage`
5. `verification_mode`
6. `public_safe`
7. `traceable`
8. `truth_guarantee`
9. `warnings`
10. `human_review_required`
11. `degraded`
12. `degraded_reasons`

Endpoint-specific extensions are:

- `/telemetry/runtime`: `events_total`, `degraded_events`
- `/telemetry/queues`: `verification_queue`, `escalation_queue`, `replay_warning_queue`, `degraded_queue_handling`

### `advisory_only` handling

All telemetry endpoints inherit `advisory_only=true` from the shared telemetry base. Tests assert this metadata across normal telemetry, degraded telemetry, runtime telemetry, queues telemetry, and broader public response contracts.

### `public_safe` handling

All telemetry endpoints inherit `public_safe=true` from the shared telemetry base. Queue payloads are populated through `RuntimeQueueStore`, whose enqueue methods apply public-payload redaction before storing queue items. PR #519 added telemetry-specific tests that seed secret-like queue inputs and assert that token, credential, API-key, private-key, and related markers do not appear in serialized telemetry output.

### `truth_guarantee` handling

All telemetry endpoints inherit `truth_guarantee=false` from the shared telemetry base. Existing runtime response contract tests also assert that public runtime builders and route surfaces avoid objective-truth language.

### Warnings behavior

Telemetry warnings are deterministic:

- Clean runtime state returns `warnings=[]`.
- Degraded runtime state returns a single public-safe degraded runtime warning.
- The current telemetry base does not add queue-only warnings for replay or escalation queues unless degraded runtime state is also present.

This behavior is covered by telemetry tests across clean, degraded, replay-warning queue, escalation queue, verification queue, and mixed degraded/replay/escalation states.

### Degraded runtime behavior

Degraded telemetry is driven by recorded runtime events whose `event_type` is `runtime_recovery_mode`. When at least one degraded runtime event exists:

- `status="degraded"`
- `degraded=true`
- `degraded_reasons=["runtime_recovery_mode"]`
- `warnings` contains the degraded runtime advisory warning
- `human_review_required=true`
- `/telemetry/runtime` increments `degraded_events`
- `/telemetry/queues` preserves `degraded_queue_handling=true`

The behavior is visible and does not silently downgrade to a clean status.

### Escalation behavior

Escalation behavior is endpoint-scoped:

- `/telemetry/queues` passes `escalation_required=bool(QUEUE_STORE.escalation_queue)` to the telemetry base.
- Therefore `/telemetry/queues` sets `human_review_required=true` when escalation queue items exist, even if warnings are empty.
- `/telemetry/health` and `/telemetry/runtime` do not currently incorporate escalation queue state unless degraded runtime warnings are present.

This is acceptable for the current contract because escalation queue visibility is intentionally queue telemetry scope, but it is a compatibility point to preserve in future changes.

### `human_review_required` behavior

PR #627 made the telemetry base bool algebra explicit:

`human_review_required = bool(warnings) OR escalation_required`

Current behavior:

- Clean state: `false`
- Degraded state: `true` because warnings are present
- Escalation queue present on `/telemetry/queues`: `true` because `escalation_required=true`
- Replay-warning queue alone: `false` unless it also creates warnings or escalation queue state

This is deterministic and sufficiently covered for current telemetry scope.

### Deterministic payload guarantees

The current contract is deterministic at these levels:

- shared telemetry key insertion order
- runtime endpoint extension order
- queue endpoint extension order
- stable advisory metadata values
- stable warning list behavior for clean and degraded states
- integer runtime counters for runtime telemetry
- redacted queue item list shape for queue telemetry

The deterministic key-order regression test in `tests/test_hc_runtime_app.py` protects the current order for all three telemetry endpoints.

## Existing Test Coverage

### Existing telemetry tests

Telemetry coverage currently includes:

- endpoint availability and shared advisory metadata checks for `/telemetry/health`, `/telemetry/runtime`, and `/telemetry/queues`
- degraded telemetry visibility without hidden fallback
- deterministic telemetry response key order
- queue edge coverage for clean state, degraded state, replay-warning queue, escalation queue, verification queue, and mixed degraded/replay/escalation state
- runtime counter type and degraded counter assertions
- queue field shape assertions for redacted queue item lists
- public-safe telemetry redaction checks for secret-like queue inputs
- explicit `human_review_required` bool algebra checks

### Coverage added by PR #483

PR #483 (`7ccbc46`) added the first major telemetry hardening pass. It introduced the shared telemetry base, degraded runtime event detection, degraded status/warnings/reasons, and endpoint-specific telemetry extensions. It also added app-level tests for degraded telemetry visibility and deterministic telemetry response key order, and extended response-contract expectations for degraded telemetry metadata.

Coverage impact:

- established shared advisory telemetry metadata
- made degraded runtime telemetry visible
- added deterministic response key-order coverage
- added degraded telemetry assertions across all three telemetry endpoints

### Coverage added by PR #519

PR #519 (`65586ee`) added `tests/runtime/test_telemetry_payload_contract.py`, a dedicated telemetry payload contract suite.

Coverage impact:

- covered all three telemetry endpoints through a shared helper
- parameterized queue/runtime edge states
- asserted advisory metadata, public-safe posture, traceability, and no truth guarantee
- asserted degraded warnings and degraded reasons
- asserted runtime counter types and values
- asserted queue field list shape and expected queue item counts
- asserted public-safe telemetry redaction against common secret-like markers

### Coverage added by PR #627

PR #627 (`e34e504`) documented and tested deterministic `human_review_required` bool algebra in telemetry.

Coverage impact:

- made `human_review_required = bool(warnings) OR escalation_required` explicit in the telemetry base
- added clean, degraded, and escalation queue test cases for the bool algebra
- preserved advisory-only and public-safe posture while clarifying when human review is required

## Remaining Gaps

The remaining gaps are non-blocking for the current advisory telemetry contract:

1. **No typed telemetry schema model.** The contract is enforced through route construction and tests, not through a typed response model.
2. **Queue telemetry exposes redacted queue item lists.** This is intentional in current tests, but consumers expecting counts could be affected if they rely on older behavior.
3. **Endpoint-scoped escalation awareness.** `/telemetry/queues` accounts for escalation queue state; `/telemetry/health` and `/telemetry/runtime` do not include escalation queue state unless degraded warnings are also present.
4. **Replay-warning queue alone does not force `human_review_required=true`.** Current tests encode this behavior. If operators later want replay queue presence to require review at telemetry level, that should be a separate contract change.
5. **No restart or continuity replay edge coverage inside telemetry-specific tests.** Related runtime suites cover replay and continuity behavior, but the next focused PR should cover replay / continuity edge cases against telemetry-visible state.

## Risk Assessment

### Backward compatibility risks

- The most important compatibility risk is the current `/telemetry/queues` shape: queue fields are lists of redacted queue items, not counts. Current telemetry tests explicitly assert lists and count them with `len(...)`, so future changes from lists to counts would be a breaking contract change.
- The key-order contract is now tested. Reordering shared telemetry keys or endpoint extension keys would break tests and should be treated as an intentional contract update.
- `human_review_required` on `/telemetry/health` and `/telemetry/runtime` remains tied to warnings, not queue escalation state. Consumers should use `/telemetry/queues` for queue-driven escalation visibility.

### Security observations

- Telemetry payloads preserve `advisory_only=true`, `public_safe=true`, and `truth_guarantee=false`.
- Queue stores redact public payloads at enqueue time before telemetry exposes queue contents.
- Telemetry redaction tests cover representative secret-like tokens, API keys, credentials, GitHub-style tokens, AWS-style access key markers, and private-key markers.
- No reviewed telemetry surface claims production readiness, autonomous governance finality, forensic certainty, live federation guarantees, or objective truth.
- Because queue telemetry returns item lists, continued redaction coverage is important whenever queue item fields expand.

## Final Recommendation

Decision: **TELEMETRY CONTRACT SUFFICIENT**.

Telemetry contract hardening is complete for the current advisory runtime scope after PR #483, PR #519, and PR #627. The current implementation and tests sufficiently cover advisory-only posture, public-safe posture, truth-guarantee avoidance, warnings visibility, degraded runtime behavior, queue telemetry behavior, escalation-driven human review on queue telemetry, deterministic key order, and secret redaction.

No runtime, code, test, schema, validator, workflow, governance, record, hash, QR artifact, generated artifact, signing, federation, or policy patch is recommended in this PR.

## Recommended Next PR

Next PR: **#629 replay / continuity edge-case tests**.

Recommended scope:

- Add targeted replay / continuity edge-case tests that confirm telemetry-visible runtime state remains advisory-only, public-safe, deterministic, and human-reviewable when replay warnings and continuity warnings interact.
- Keep the PR test-only unless the tests reveal a real contract defect.
- Do not modify protected paths unless a human reviewer explicitly approves a follow-up fix.
