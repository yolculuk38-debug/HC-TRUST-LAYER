# Public Verification Explorer MVP

This directory contains a static, read-only HC:// Public Verification Explorer MVP foundation for HC-TRUST-LAYER.

## Scope

- Provides a browser-only verification screen in `docs/explorer/index.html`.
- Attempts to load generated explorer index data from `generated/explorer_index.json` when available, with static fallback paths for local review.
- Supports exact search by `record_id` and `content_hash`.
- Displays status and verification fields already present in the loaded index.
- Preserves advisory-only boundaries: `advisory_only=true`, `truth_guarantee=false`, and `human_final_authority=true`.

## Boundaries

The explorer is a navigation and review aid. It does not modify runtime behavior, schemas, validators, signing logic, workflows, policy routing, governance controls, or canonical records. Generated explorer index data is non-canonical and must not be treated as a canonical record.

A QR or explorer result is not proof of final truth. Human-supervised validation remains the final authority for HC:// review decisions.

## Empty and error states

If no index can be loaded, or if the index is malformed, the page shows a deterministic unavailable state and performs no write operation.
