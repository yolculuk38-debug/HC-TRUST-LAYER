# HC:// Threat Model Master Map

This document defines a single master threat model map for HC:// in HC-TRUST-LAYER.

Scope boundaries:

- Documentation-only threat model map.
- Advisory-only verification posture is preserved.
- Human-supervised validation remains required.
- No canonical schema changes.
- No validator or guard weakening.
- No claims of perfect security or impossible guarantees.

## Purpose

Consolidate known trust and security risks across verification, governance, AI validators, human reviewers, sponsors, federation, audit history, public UX, and generated artifacts into one auditable navigation surface.

## Security posture baseline

HC:// is designed for layered risk reduction, not perfect security.

- uncertainty must remain visible
- no single actor should silently control verification outcomes
- security posture must evolve with attacks
- transparency, accountability, and inspectability remain mandatory

## Master threat category map

| Threat category | Risk description | Affected layer | Current mitigation | Future mitigation | Public warning state |
|---|---|---|---|---|---|
| fake verified records | Non-canonical or tampered artifacts are presented as trusted outcomes. | verification, canonical record boundary | Canonical boundary checks, provenance checks, reviewer confirmation. | Wider multi-party canonical cross-check tooling and stronger operator diagnostics. | `POSSIBLE SPOOF`, `REVIEW REQUIRED` |
| fake validator identity | A malicious actor claims validator authority without trusted identity continuity. | AI validators, verification | Validator identity references and traceability requirements. | Stronger validator attestation lifecycle and rotation transparency. | `VALIDATOR TRACE MISSING` |
| fake AI approval | Fabricated "AI approved" claims are used to bypass human review boundaries. | AI validators, public UX | Advisory-only AI outputs and explicit state labeling. | Standardized signed AI output envelopes and public verifier checks. | `AI CLAIM UNVERIFIED`, `REVIEW REQUIRED` |
| unauthenticated AI analysis | AI-generated analysis appears in workflow without authenticated source context. | AI validators, governance | Authenticated AI validator access documentation and reviewer gatekeeping. | Mandatory authenticated AI provenance fields in operator workflows. | `UNAUTHENTICATED AI ANALYSIS` |
| bribed or biased human reviewer | Reviewer judgment is distorted by incentives, coercion, or undisclosed conflict. | human reviewers, governance | Human-supervised validation, escalation rules, review trace expectations. | Conflict-disclosure workflow hardening and diversified reviewer routing. | `CONFLICT DETECTED`, `PUBLIC REVIEW ESCALATED` |
| compromised maintainer | Privileged maintainer identity or channel is abused to alter trust interpretation. | maintainers, governance | Branch protections, review requirements, audit visibility expectations. | Faster compromise playbooks and federation-backed incident cross-checking. | `POSSIBLE COMPROMISE`, `EMERGENCY INTEGRITY REVIEW` |
| sponsor influence | Sponsor pressure attempts to shape outcomes beyond declared review boundaries. | governance, sponsorship | Accountability documentation and no hidden authority baseline. | Sponsor firewall policy checklist and stricter disclosure templates. | `SPONSOR CONFLICT REVIEW REQUIRED` |
| hidden override | Trust-impacting override is applied without explicit visibility. | governance, maintainers | Override visibility expectations and audit trail continuity guidance. | Mandatory override event registry and independent reviewer acknowledgements. | `OVERRIDE DETECTED` |
| silent policy rewrite | Policy interpretation shifts without visible rationale and review continuity. | governance, policy interpretation | Policy traceability expectations and escalation guidance. | Stronger policy-diff alerts with required rationale + reviewer signoff. | `POLICY CONFLICT DETECTED` |
| deleted evidence | Verification-relevant evidence is removed, reducing challengeability. | audit history, evidence preservation | Continuity-gap warnings and evidence preservation guidance. | Broader snapshot redundancy and recovery-path automation with oversight. | `EVIDENCE MISSING`, `CONTINUITY GAP DETECTED` |
| continuity gap | Lineage/provenance continuity is incomplete, broken, or unresolved. | audit history, verification | Continuity checks and caution-state expectations. | Continuous continuity-drift dashboards and federation mirror comparison. | `CONTINUITY GAP DETECTED`, `HISTORY INCOMPLETE` |
| forged audit trail | Audit events are fabricated or tampered to hide real actions. | audit history, governance | Immutable-style state history model and traceability guidance. | Independent audit witnessing and cross-source consistency proofs. | `AUDIT TRAIL INCONSISTENT` |
| replayed artifact | Previously valid outputs are replayed in a new context to fake fresh validity. | verification, AI validators | Replay-awareness guidance and context checks. | Stronger nonce/time-bound validation metadata and replay detectors. | `REPLAY SUSPECTED` |
| QR spoofing | Malicious QR content mimics trusted verification destinations or flows. | public UX, verification | QR security model, route checks, anti-spoof warnings. | Improved mobile warning UX and signed route manifests. | `POSSIBLE SPOOF` |
| fake public verification page | Impersonated verification pages mislead users about trust outcomes. | public UX | Public verification boundary docs and caution-state signaling. | Public authenticity indicators and dispute shortcut UX. | `PAGE AUTHENTICITY UNVERIFIED` |
| federation divergence | Federated participants show materially different trust states without reconciliation. | federation, governance | Federated oversight model and divergence visibility expectations. | Automated federation divergence alerts and structured reconciliation workflow. | `FEDERATION DIVERGENCE` |
| generated artifact confusion | Non-canonical generated artifacts are mistaken for canonical truth. | generated artifacts, public UX | Generated artifact boundary guidance and advisory language. | Stronger artifact watermarking and UI-level canonical/non-canonical labels. | `NON-CANONICAL ARTIFACT`, `REVIEW REQUIRED` |
| social engineering misuse | Attackers exploit trust language, UX ambiguity, or authority assumptions to mislead users. | public UX, governance, human reviewers | Transparency-first wording and challenge/dispute pathways. | Operator/user anti-abuse drills, clearer warning taxonomies, and education surfaces. | `SOCIAL ENGINEERING RISK` |

## Threat-to-defense mapping

| Defense control | Purpose in HC:// |
|---|---|
| canonical boundaries | Prevent non-canonical artifacts from being interpreted as canonical record truth. |
| audit continuity | Preserve attributable chronology for trust-impacting events and state changes. |
| immutable-style state history | Reduce silent tampering risk through append-style continuity expectations. |
| federation cross-checking | Surface divergence and concentrated-control risk via independent comparisons. |
| AI validator authentication | Reduce fake or unauthenticated AI approval claims in verification workflows. |
| reviewer accountability | Keep consequential review decisions challengeable and attributable. |
| public disputes/challenges | Preserve public challenge pathways when claims are contested or unclear. |
| evidence preservation | Limit silent evidence disappearance and preserve continuity-under-failure signals. |
| sponsor firewall | Reduce sponsor pressure leakage into verification outcome interpretation. |
| maintainer accountability | Prevent hidden privileged authority and require visible override traceability. |
| verification result states | Keep uncertainty, conflict, spoof risk, and escalation needs visible. |

## Prioritization map

### Immediate foundation risks

- fake verified records
- fake validator identity
- fake AI approval
- unauthenticated AI analysis
- generated artifact confusion

### Operational core risks

- bribed or biased human reviewer
- compromised maintainer
- sponsor influence
- hidden override
- silent policy rewrite
- replayed artifact

### Federation-scale risks

- federation divergence
- forged audit trail
- continuity gap
- deleted evidence

### Public adoption risks

- QR spoofing
- fake public verification page
- social engineering misuse

## Interpretation and governance reminders

- HC:// security posture is layered and adaptive; it is not an absolute-security claim.
- Uncertainty must remain explicit in verification result states and review workflows.
- No single actor (maintainer, reviewer, validator, sponsor, or federation participant) should silently control verification outcomes.
- The threat model must evolve as attacks, incentives, and adversarial behaviors evolve.
- Human-supervised validation remains mandatory for non-trivial consequential trust interpretation.

## Implementation notes

- This map does not modify canonical records, schema contracts, validator logic, signing semantics, federation runtime behavior, policy evaluator behavior, or workflow security controls.
- This map is a documentation-first consolidation artifact for risk routing, review planning, and public accountability communication.

## Related documents

- `HC_CONSTITUTION.md`
- `docs/FOUNDATION_STATUS.md`
- `docs/accountability-defense-layer.md`
- `docs/maintainer-accountability-model.md`
- `docs/evidence-preservation-recovery-model.md`
- `docs/federated-oversight-model.md`
- `docs/HC_CONTROL_PANEL.md`
- `docs/verification-result-states.md`
- `docs/anti-spoofing-foundations.md`
- `docs/authenticated-ai-validator-access.md`
- `docs/governance/validator-ethics-and-conduct.md`
