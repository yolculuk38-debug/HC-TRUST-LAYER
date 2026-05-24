# External Verification Packages (Experimental)

Status:
- implemented: external package schema and sample bundle scaffolding.
- experimental: `/verify/export/{record_id}` route returns preview package structures.
- planned: deterministic signing profile and validator import profile.
- research: third-party portability profiles for public archive systems.

## Purpose

External verification packages provide portable bundles so independent parties can inspect provenance and integrity evidence outside a live runtime.

## Package scope

A package currently includes:
- provenance metadata
- revision references
- witness references
- integrity hash references
- federation source references

## Trust limitations

This format currently defines shape, not final security guarantees. Consumers must treat these bundles as pre-standard experimental artifacts.

## Distributed verification direction

The package model is designed for future validator-network compatibility by keeping references modular and source-attributed.

## Non-production warning

Do not treat exported package previews as cryptographically complete proofs yet.

> Trust the record, not the narrative.
