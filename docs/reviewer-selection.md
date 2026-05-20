# Reviewer Selection Principles (HC:// TRUST LAYER)

> Status: **Experimental / Trust Infrastructure Preparation**

This document defines how reviewer selection should be structured for future trust infrastructure while preserving existing validation and workflow behavior.

## Independent Review Pools

HC:// uses structured reviewer pools to reduce single-source interpretation risk.

- AI reviewer pool: model-diverse interpretation support.
- Human reviewer pool: contextual judgment and forensic reasoning.
- Institutional reviewer pool: process and methodology oversight.

Independent pools support multi-perspective verification without changing immutable verification records.

## Mixed AI + Human Review

For high-impact records, mixed review composition is preferred:

- AI reviewers provide scalable cross-record and discrepancy analysis.
- Human reviewers provide domain judgment, nuance handling, and dispute interpretation.
- Institutional reviewers provide governance and process accountability signals.

This mixed model improves resilience against blind spots from any single reviewer class.

## No Unrestricted Reviewer Injection

Reviewer participation must be controlled and auditable.

- Reviewers are listed through explicit registry updates.
- Unrestricted or random reviewer injection is not allowed.
- Reviewer status and eligibility should be visible before trust interpretation.

## Append-Only Review Philosophy

Review history should be append-only for accountability.

- New reviews are added as new entries.
- Historical reviews are retained, even when disputed, revoked, or superseded.
- Corrections are represented as additional events, not silent deletions.

## Reviewer Transparency

Each reviewer profile should expose structured metadata:

- identity (`reviewer_id`, `display_name`, `reviewer_type`)
- capability context (`specialization`)
- eligibility context (`status`, `independence_level`)
- optional verification metadata (`public_key_optional`)
- governance context (`notes`)

Transparent reviewer metadata supports external scrutiny and reproducible trust interpretation.

## Experimental Scope Note

Reviewer registry entries are experimental and do not imply endorsement or autonomous governance.
