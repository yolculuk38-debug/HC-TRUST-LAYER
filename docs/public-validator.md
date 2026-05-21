# HC:// Public Validator Core

## Purpose

The HC:// Public Validator Core provides portable and explainable proof validation outside GitHub.

It validates:
- exported proof structures
- revision integrity
- witness validity
- provenance references
- trust passport presence
- verification levels
- conflict signals

## Design Principles

- no automatic trust
- deterministic validation
- explainable decisions
- layered evidence
- adversarial-aware validation
- public verifiability

## Decisions

Possible outputs:
- VERIFIED
- PARTIAL
- REVIEW_REQUIRED
- INVALID
- UNTRUSTED

## Validation Flow

proof -> validator -> explainable decision

## Long-Term Direction

This validator is designed to become:
- browser verifier
- mobile verifier
- offline validator
- SDK/API verification core
- federated trust validation layer
