# Public Validator Demo Fixture Records

> **Status:** documentation-only demo fixtures  
> **Scope:** local Public Validator adapter planning inputs  
> **Authority:** advisory-only; human review remains required  
> **Production readiness:** not claimed

These fixtures show how HC:// Public Validator examples can be represented as structured local demo inputs. They are fictional, public-safe, and intended for documentation and local adapter planning only.

These fixtures are not canonical HC:// records, not schema definitions, not validator outputs, not signed payloads, not generated artifacts, and not evidence that any real-world product, building, article, QR label, issuer, or claim is true.

## Shared Fixture Boundaries

Every fixture below preserves the same review boundary:

- `advisory_only: true`
- `public_safe: true`
- `truth_guarantee: false`
- `human_review_required: true`
- `warnings` is always present as a list.
- `missing_evidence` is always present as a list.
- `conflicting_evidence` is always present as a list.
- `source_chain` is always present as a list.
- `responsibility_chain` is always present as a list.
- `chain_of_custody` is present where custody continuity is part of the demo scenario.

The fixtures are designed to help future local-only Public Validator demo work show provenance signals, evidence gaps, and review boundaries without claiming certification, legal authority, safety, truth, forensic certainty, or production readiness.

## 1. Imported Banana / Food Provenance Fixture

This fixture models a public-safe food provenance demo input. It does not certify food safety, origin truth, freshness, import legality, regulatory compliance, or fitness for consumption.

```yaml
record_id: HC-DEMO-PV-FIXTURE-FOOD-0001
record_type: public_validator_demo_fixture
status: demo_fixture_advisory_only
scenario: imported_banana_food_provenance
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
  inspector_reference: DEMO-ORIGIN-INSPECTION-REF
  evidence_status: present
  notes: Demo origin inspection metadata is visible, but issuer authority is not independently confirmed.
destination_inspection:
  location: Demo Destination Intake Facility
  inspection_date: 2026-04-16
  inspector_reference: DEMO-DESTINATION-INSPECTION-REF
  evidence_status: partial
  notes: Demo destination intake metadata is visible, but intake image evidence is not attached.
lab_method:
  method_name: demo pesticide residue screening method
  method_reference: DEMO-LAB-METHOD-FOOD-01
  lab_reference: DEMO-LAB-FOOD-22
  evidence_status: present
  notes: Method metadata is included for provenance review only and does not assert lab accreditation or safety certification.
device_used:
  device_id: DEMO-DEVICE-GC-001
  device_type: demo chromatography device reference
  calibration_reference: DEMO-CALIBRATION-2026-03
  evidence_status: present
operator_role: Demo lab operator
approver_role: Demo human review approver

source_chain:
  - Demo grower cooperative harvest note
  - Demo packhouse lot record
  - Demo export inspection note
  - Demo carrier handoff note
  - Demo destination intake note
  - Demo lab method summary
responsibility_chain:
  - Demo grower cooperative
  - Demo packhouse operator
  - Demo export broker
  - Demo carrier
  - Demo destination intake reviewer
  - Demo human review approver
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
  - step: sample_to_lab
    custodian: Demo Lab Intake Technician
    timestamp: 2026-04-16T13:10:00Z
    evidence_status: present
evidence:
  - type: demo_lot_record
    reference: DEMO-LOT-0187-RECORD
    evidence_status: present
  - type: demo_inspection_summary
    reference: DEMO-ORIGIN-INSPECTION-REF
    evidence_status: present
  - type: demo_lab_method_summary
    reference: DEMO-LAB-METHOD-FOOD-01
    evidence_status: present
missing_evidence:
  - Independent confirmation of origin inspection issuer authority
  - Destination intake image evidence
  - Complete transport temperature log
conflicting_evidence:
  - Destination intake count differs from export count by two cartons.
warnings:
  - Advisory demo fixture only; not a food safety certification.
  - Visible provenance is incomplete and requires human review.
  - Conflicting carton count should be reviewed before relying on this demo record shape.
```

## 2. Building / Concrete Provenance Fixture

This fixture models a public-safe construction material provenance demo input. It does not certify building safety, structural integrity, code compliance, occupancy readiness, contractor performance, or legal approval.

```yaml
record_id: HC-DEMO-PV-FIXTURE-CONCRETE-0001
record_type: public_validator_demo_fixture
status: demo_fixture_advisory_only
scenario: building_concrete_provenance
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true

project_id: DEMO-PROJECT-27
building_asset_id: DEMO-BUILDING-ASSET-A12
concrete_batch_id: DEMO-CONCRETE-BATCH-5509
sample_id: DEMO-SAMPLE-CONCRETE-CYL-03
lab_method:
  method_name: demo compressive strength test method
  method_reference: DEMO-CONCRETE-METHOD-01
  lab_reference: DEMO-CONCRETE-LAB-04
  evidence_status: present
  notes: Method metadata is included for provenance review only and does not assert accreditation or code compliance.
test_result_reference:
  result_reference: DEMO-CONCRETE-RESULT-28DAY-03
  result_type: demo compressive strength reference
  test_age_days: 28
  evidence_status: present
  notes: The referenced result is fictional demo data and is not a safety certification.
contractor:
  name: Demo Concrete Contractor
  role: batch supplier and placement support
supervising_authority:
  name: Demo Site Review Authority
  role: human-supervised review reference
  authority_status: not_legally_asserted

source_chain:
  - Demo concrete plant batch ticket
  - Demo mixer truck dispatch note
  - Demo field sample collection note
  - Demo lab receipt note
  - Demo test result reference
responsibility_chain:
  - Demo concrete plant
  - Demo mixer truck operator
  - Demo field technician
  - Demo concrete lab reviewer
  - Demo supervising authority reviewer
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
    custodian: Demo Concrete Lab Intake
    timestamp: 2026-03-04T10:00:00Z
    evidence_status: present
evidence:
  - type: demo_batch_ticket
    reference: DEMO-CONCRETE-BATCH-5509-TICKET
    evidence_status: present
  - type: demo_sample_collection_note
    reference: DEMO-SAMPLE-CONCRETE-CYL-03
    evidence_status: partial
  - type: demo_test_result_reference
    reference: DEMO-CONCRETE-RESULT-28DAY-03
    evidence_status: present
missing_evidence:
  - Independent confirmation of sample collection witness
  - Complete curing condition log
  - Signed supervising authority review note
conflicting_evidence:
  - Field sample timestamp is later than one dispatch note timestamp and requires human review.
warnings:
  - Advisory demo fixture only; not a building safety or code compliance certification.
  - Demo result references must not be treated as proof of structural integrity.
  - Chain-of-custody contains partial field sample evidence.
```

## 3. News Source Provenance Fixture

This fixture models a public-safe news provenance demo input. It does not certify article truth, publisher reliability, legal status, journalistic quality, editorial independence, or absence of misinformation.

```yaml
record_id: HC-DEMO-PV-FIXTURE-NEWS-0001
record_type: public_validator_demo_fixture
status: demo_fixture_advisory_only
scenario: news_source_provenance
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true

publisher: Demo Daily Ledger
reporter_role: Demo staff reporter
editor_role: Demo assigning editor
original_source:
  source_type: demo_public_meeting_note
  reference: DEMO-MEETING-NOTE-2026-05-02
  evidence_status: present
referenced_sources:
  - source_type: demo_press_statement
    reference: DEMO-PRESS-STATEMENT-01
    evidence_status: present
  - source_type: demo_public_dataset_summary
    reference: DEMO-DATASET-SUMMARY-04
    evidence_status: partial
independent_confirmation:
  status: partial
  references:
    - DEMO-INDEPENDENT-CONFIRMATION-REQUEST-01
  notes: One independent confirmation request is visible, but final confirmation is not attached.
correction_history:
  status: present
  entries:
    - date: 2026-05-04
      summary: Demo correction note updates a date reference.
opinion_or_analysis_marker: news_analysis_labeled

source_chain:
  - Demo public meeting note
  - Demo reporter interview note
  - Demo press statement
  - Demo public dataset summary
  - Demo correction note
responsibility_chain:
  - Demo staff reporter
  - Demo assigning editor
  - Demo publisher review desk
  - Demo human reviewer
evidence:
  - type: demo_original_source_note
    reference: DEMO-MEETING-NOTE-2026-05-02
    evidence_status: present
  - type: demo_referenced_source
    reference: DEMO-PRESS-STATEMENT-01
    evidence_status: present
  - type: demo_correction_history
    reference: DEMO-CORRECTION-NOTE-01
    evidence_status: present
missing_evidence:
  - Final independent confirmation response
  - Full context for the public dataset summary
conflicting_evidence:
  - Demo press statement and demo meeting note use different date wording for the same event.
warnings:
  - Advisory demo fixture only; not a truth rating or news certification.
  - Source provenance is partial and requires human editorial review.
  - Opinion or analysis marker should remain visible to public reviewers.
```

## 4. QR Spoof / Non-Canonical Link Fixture

This fixture models a public-safe QR and link provenance demo input. It highlights a non-canonical link condition for local adapter planning, but it does not claim fraud, malicious intent, legal liability, signature validity, issuer authority, or forensic certainty.

```yaml
record_id: HC-DEMO-PV-FIXTURE-QR-0001
record_type: public_validator_demo_fixture
status: demo_fixture_advisory_only
scenario: qr_spoof_non_canonical_link
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true

scanned_url: https://demo.example.invalid/public-validator/banana-batch-0187
canonical_url: hc://demo/public-validator/banana-batch-0187
issuer:
  name: Demo Label Issuer
  issuer_reference: DEMO-ISSUER-QR-01
  issuer_authority_status: not_independently_confirmed
payload_hash:
  value: not_provided_demo_placeholder
  hash_status: not_verified
  notes: No real hash is asserted in this documentation-only fixture.
signed_payload_status:
  status: not_verified
  notes: This fixture does not include or validate a signed payload.
qr_integrity:
  status: non_canonical_link_detected_in_demo_input
  scanned_url_matches_canonical_url: false
  notes: Local fixture fields show that the scanned URL differs from the expected HC:// canonical URL.

source_chain:
  - Demo QR label scan observation
  - Demo expected HC:// canonical reference
  - Demo issuer reference note
responsibility_chain:
  - Demo label issuer
  - Demo scanner operator
  - Demo human reviewer
chain_of_custody:
  - step: label_issued
    custodian: Demo Label Issuer
    timestamp: 2026-04-11T10:30:00Z
    evidence_status: partial
  - step: label_scanned
    custodian: Demo Scanner Operator
    timestamp: 2026-04-16T15:45:00Z
    evidence_status: present
evidence:
  - type: demo_scanned_url_observation
    reference: DEMO-SCANNED-URL-OBSERVATION-01
    evidence_status: present
  - type: demo_canonical_url_reference
    reference: DEMO-CANONICAL-HC-REFERENCE-01
    evidence_status: present
  - type: demo_issuer_reference
    reference: DEMO-ISSUER-QR-01
    evidence_status: partial
missing_evidence:
  - Independently verified issuer authority
  - Signed payload evidence
  - Real payload hash verification
  - Original QR artifact image
conflicting_evidence:
  - Scanned URL differs from the expected HC:// canonical URL in this demo fixture.
warnings:
  - Advisory demo fixture only; not a fraud finding or forensic determination.
  - Non-canonical link condition requires human review before any reliance.
  - This fixture does not validate signatures, generate QR artifacts, or fetch remote URLs.
```

## What These Fixtures Do Not Claim

These fixtures do not claim:

- production readiness;
- certification, legal authority, regulatory approval, or compliance status;
- food safety, building safety, article truth, or QR authenticity;
- forensic certainty, fraud determination, malicious intent, or liability;
- signature validity, issuer authority, federation status, or policy approval;
- canonical HC:// record status.

They are safe local demo inputs for planning a future Public Validator demo adapter or static demo page. Any future implementation should remain local-only unless a later reviewed PR explicitly changes that scope.
