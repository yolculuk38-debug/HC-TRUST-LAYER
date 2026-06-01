# Changelog

All notable changes to HC-TRUST-LAYER will be documented in this file.

The format follows Keep a Changelog style, and this project uses reviewable release notes to preserve HC:// provenance, audit trail clarity, and human-supervised validation boundaries.

## [Unreleased]

### Added

- Developer onboarding documentation for Python 3.11+, virtual environment setup, dependency installation, pytest, linting, optional type checking, and contribution flow.
- Security threat model documentation covering repository contribution paths, CI/CD risks, verification package manipulation, and human review limits.

### Changed

- Pending.

### Fixed

- Pending.

### Security

- Added threat model coverage for CI/CD risks, workflow secrets, generated trust artifacts, verification package manipulation, and human review limits.

## [0.1.0] - Initial Release

### Added

- Verification workflow.
- Trust-layer prototype.
- Documentation.
- Testing infrastructure.
- Protected pull request workflow for release and protocol-facing updates.
- CodeQL and Dependabot coverage to improve visibility into code quality and dependency posture.
- Validation pipeline for repeatable repository-level verification.
- Real record validation examples and checks for concrete record flows.
- Safer normalization flow to reduce inconsistent canonicalization behavior.
- Documentation set for QR verification, witness layer, and trust interpretation.
- Visible verification demo flow (`record → hash → QR → verify → trust explanation`) for first-time users.
- Limitations and trust model clarification to prevent overclaiming verification scope.
- Architecture roadmap and glossary to align language, scope, and future protocol direction.

### Security

- Initial verification controls.
