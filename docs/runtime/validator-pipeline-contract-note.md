# Validator Pipeline Contract Note

This note records the current validator pipeline response surface for future hardening.

## Current top-level fields

- record_id
- canonical_bridge
- schema_result
- hash_result
- trust_assignment
- escalation

## Current nested areas

The pipeline currently separates:

- canonical lookup bridge result
- schema result
- hash result
- trust assignment warnings
- escalation routing result

## Hardening direction

A future test-only change should lock the nested response fields for each area.

That test should be small and should not change runtime behavior.

## Boundary

The pipeline remains advisory-only.

It does not provide a truth guarantee.
