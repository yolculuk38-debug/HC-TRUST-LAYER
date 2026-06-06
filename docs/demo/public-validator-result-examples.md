# Public Validator Result Examples

> **Status:** demo / explanatory examples  
> **Scope:** documentation-only public validator result shapes  
> **Authority:** advisory-only; human review remains final  
> **Production readiness:** not claimed

These examples show how HC:// Public Validator results can present records, evidence, gaps, conflicts, and provenance signals for real-world scenarios without claiming truth finality, production readiness, legal authority, or autonomous final authority for automated systems.

The examples are fictional and public-safe. They are not canonical records, not signed payloads, not generated artifacts, not certification outputs, and not evidence that any real-world item, building, article, issuer, QR code, or claim is true.

## Shared Output Posture

Every example below preserves the same review boundary:

- `advisory_only: true`
- `public_safe: true`
- `truth_guarantee: false`
- `human_review_required: true`
- `warnings` always exists as a list.
- `missing_evidence` always exists as a list.
- `conflicting_evidence` always exists as a list.
- `source_chain` always exists as a list.
- `responsibility_chain` always exists as a list.
- `chain_of_custody` exists where custody continuity is part of the scenario.

HC-TRUST-LAYER can help make provenance signals visible. Humans remain responsible for interpreting context, requesting additional evidence, escalating disputes, and making final decisions.

## 1. Imported Banana / Food Provenance

This example shows a public-safe result for an imported food provenance review. It does not certify food safety, regulatory compliance, origin truth, freshness, import legality, or fitness for consumption.

```yaml
scenario: imported_banana_food_provenance
record_id: HC-DEMO-PV-FOOD-0001
result_label: NEEDS_HUMAN_REVIEW
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true

batch_id: DEMO-BANANA-BATCH-2026-04
lot_id: DEMO-LOT-0187
sample_id: DEMO-SAMPLE-FOOD-44A
origin_inspection:
  location: Demo Export Inspection Point
  inspection_date: 2026-04-12
  inspector_reference: DEMO-ORIGIN-INSPECTOR-REF
  status_signal: present
  notes: Origin inspection record is visible, but issuer authority is not independently confirmed in this example.
destination_inspection:
  location: Demo Destination Intake Facility
  inspection_date: 2026-04-16
  inspector_reference: DEMO-DEST-INSPECTOR-REF
  status_signal: partial
  notes: Destination intake record is visible, but photo evidence is not attached.
lab_method:
  method_name: demo pesticide residue screen
  method_reference: DEMO-LAB-METHOD-FOOD-01
  lab_reference: DEMO-LAB-REF-22
  status_signal: present
  notes: Method metadata is present; this example does not assert lab accreditation or safety certification.
device_used:
  device_id: DEMO-DEVICE-GC-001
  calibration_reference: DEMO-CAL-2026-03
  status_signal: present
chain_of_custody:
  - step: harvest_to_packhouse
    custodian: Demo Packhouse Operator
    timestamp: 2026-04-10T09:20:00Z
    evidence_status: present
  - step: packhouse_to_export_inspection
    custodian: Demo Export Broker
    timestamp: 2026-04-12T08:05:00Z
    evidence_status: present
  - step: export_to_destination_intake
    custodian: Demo Carrier
    timestamp: 2026-04-15T18:40:00Z
    evidence_status: partial
source_chain:
  - Demo packhouse lot record
  - Demo export inspection note
  - Demo destination intake note
  - Demo lab method summary
responsibility_chain:
  - Demo grower cooperative
  - Demo packhouse operator
  - Demo export broker
  - Demo carrier
  - Demo destination intake reviewer
missing_evidence:
  - Independent confirmation of issuer authority for origin inspection
  - Destination intake photo evidence
  - Complete transport temperature log
conflicting_evidence:
  - Destination intake count differs from export count by two cartons
warnings:
  - Advisory result only; does not certify food safety or legal import status.
  - Visible provenance is incomplete and requires human review.
  - Conflicting carton count should be resolved before relying on the record.
```

## 2. Building / Concrete Provenance

This example shows a public-safe result for construction material provenance review. It does not certify building safety, structural integrity, code compliance, occupancy readiness, contractor performance, or legal approval.

```yaml
scenario: building_concrete_provenance
record_id: HC-DEMO-PV-CONCRETE-0001
result_label: PARTIAL_TRACE
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true

project_id: DEMO-PROJECT-27
building_asset_id: DEMO-BUILDING-ASSET-A12
concrete_batch_id: DEMO-CONCRETE-BATCH-5509
sample_id: DEMO-SAMPLE-CONCRETE-CYL-03
lab_method:
  method_name: demo compressive strength test
  method_reference: DEMO-ASTM-LIKE-METHOD-PLACEHOLDER
  lab_reference: DEMO-CONCRETE-LAB-04
  status_signal: present
  notes: Method metadata is shown for provenance review only and does not assert accreditation or code compliance.
test_result:
  result_type: demo compressive strength value
  value: 38 MPa
  test_age_days: 28
  status_signal: present
  notes: Result is a fictional example and not a safety certification.
contractor:
  name: Demo Concrete Contractor
  role: batch supplier and placement support
supervising_authority:
  name: Demo Site Review Authority
  role: human-supervised review reference
  authority_status: not_legally_asserted
chain_of_custody:
  - step: batch_creation
    custodian: Demo Concrete Plant
    timestamp: 2026-03-03T06:30:00Z
    evidence_status: present
  - step: transport_to_site
    custodian: Demo Mixer Truck Operator
    timestamp: 2026-03-03T07:15:00Z
    evidence_status: present
  - step: field_sample_collection
    custodian: Demo Field Technician
    timestamp: 2026-03-03T08:05:00Z
    evidence_status: partial
  - step: lab_receipt
    custodian: Demo Concrete Lab
    timestamp: 2026-03-04T10:10:00Z
    evidence_status: present
source_chain:
  - Demo batch ticket
  - Demo site placement note
  - Demo sample receipt form
  - Demo lab result summary
responsibility_chain:
  - Demo concrete plant
  - Demo mixer truck operator
  - Demo contractor
  - Demo field technician
  - Demo lab reviewer
  - Demo supervising authority reviewer
missing_evidence:
  - Field sampling photo evidence
  - Complete curing condition log
  - Independent supervising authority sign-off
conflicting_evidence: []
warnings:
  - Advisory result only; does not certify building safety, code compliance, or legal authority.
  - Missing curing and sampling evidence may affect interpretation.
  - Human-supervised review is required before any consequential use.
```

## 3. News Source Provenance

This example shows a public-safe result for news source provenance review. It does not certify truth, journalistic quality, defamation risk, legality, editorial independence, or public-interest value.

```yaml
scenario: news_source_provenance
record_id: HC-DEMO-PV-NEWS-0001
result_label: REVIEW_WITH_CAUTION
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true

publisher: Demo Public Newsroom
reporter: Demo Reporter Name
editor: Demo Editor Name
original_source:
  source_type: public agency statement
  source_reference: DEMO-AGENCY-STATEMENT-2026-02
  status_signal: present
referenced_sources:
  - source_type: public meeting transcript
    source_reference: DEMO-MEETING-TRANSCRIPT-01
    status_signal: present
  - source_type: anonymous interview
    source_reference: DEMO-ANON-INTERVIEW-REF
    status_signal: redacted_public_summary_only
independent_confirmation:
  status_signal: partial
  confirmed_by:
    - Demo Secondary Outlet Summary
  notes: Independent confirmation is partial and should not be treated as truth certification.
correction_history:
  - correction_date: 2026-02-21
    correction_summary: Demo correction changed a date reference in the article.
    status_signal: present
opinion_or_analysis_marker:
  marked: true
  marker_text: analysis
source_chain:
  - Demo original agency statement
  - Demo public meeting transcript
  - Demo newsroom article record
  - Demo correction note
responsibility_chain:
  - Demo reporter
  - Demo editor
  - Demo publisher
  - Human reviewer
missing_evidence:
  - Full public evidence for redacted anonymous interview context
  - Direct confirmation from every named party referenced in the article
conflicting_evidence:
  - One referenced timeline differs from the public meeting transcript by one day
warnings:
  - Advisory result only; does not certify news truth or editorial quality.
  - Anonymous or redacted source material limits public review.
  - Opinion or analysis marker should be shown clearly to readers.
  - Human judgment is required for context, fairness, and reliance decisions.
```

## 4. QR Spoof / Non-Canonical Link Warning

This example shows a public-safe result for a scanned QR URL that does not match the expected canonical HC:// reference location. It does not establish criminal intent, legal liability, issuer fraud, or forensic certainty.

```yaml
scenario: qr_spoof_non_canonical_link_warning
record_id: HC-DEMO-PV-QR-0001
result_label: NON_CANONICAL_LINK_WARNING
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true

scanned_url: https://example.invalid/hc/demo-redirect/HC-DEMO-PV-QR-0001
canonical_url: hc://demo/public-validator/HC-DEMO-PV-QR-0001
issuer: Demo Issuer Name
payload_hash: DEMO_HASH_PLACEHOLDER_NOT_A_REAL_HASH
signed_payload_status:
  status_signal: not_verified_in_demo
  notes: This example does not validate a signature or signed payload.
qr_integrity:
  status_signal: warning
  observed_issue: scanned URL is not the canonical HC:// reference shown in the demo record.
source_chain:
  - Demo QR scan observation
  - Demo expected canonical URL reference
  - Demo public validator warning output
responsibility_chain:
  - Demo issuer
  - Demo QR publisher
  - Human reviewer
missing_evidence:
  - Verified signed payload
  - Issuer-controlled redirect policy
  - Evidence that scanned URL was intentionally substituted
conflicting_evidence:
  - Scanned URL differs from canonical URL
warnings:
  - Advisory result only; does not prove spoofing, fraud, legal liability, or malicious intent.
  - Non-canonical URL requires human review before relying on the QR result.
  - Do not treat placeholder hash text as a real hash or signature.
```

## Interpretation Boundary

These examples are meant to make review posture visible:

- HC shows record identifiers, source chains, responsibility chains, evidence availability, gaps, conflicts, and warnings.
- HC does not turn incomplete or disputed evidence into truth finality.
- HC does not replace food inspectors, building officials, editors, courts, regulators, issuers, or other responsible humans.
- HC does not grant autonomous final authority to automated systems.
- HC does not claim production readiness from these documentation examples.

Human reviewers remain the final decision makers for real-world reliance, escalation, correction, approval, rejection, or further investigation.
