# Public Validator Demo Quickstart

> **Status:** documentation-only quickstart for a deterministic local demo runner
> **Scope:** public-safe HC:// Public Validator demo output
> **Authority:** advisory-only; humans remain final decision makers
> **Production readiness:** not claimed

## Overview

This quickstart helps a new user run the local HC:// Public Validator demo and read the JSON output quickly.

The demo runner is [`scripts/run_public_validator_demo.py`](../../scripts/run_public_validator_demo.py). It prints deterministic, public-safe fixture results for the demo scenarios described in the [Public Validator Static Demo](public-validator-static-demo.md), the [Public Validator Static Viewer MVP](public-validator-static-viewer.html), the [Public Validator Demo Links](public-validator-demo-links.md), and the [Public Validator Demo Fixtures](fixtures/public-validator-demo-fixtures.md).

The runner is local-only. It does not make external network calls, contact live HC:// services, fetch remote evidence, validate signatures, or certify real-world claims.

## Static browser viewer

Open [`docs/demo/public-validator-static-viewer.html`](public-validator-static-viewer.html) in a browser to view the same public-safe demo scenario shape as a static HC result card. The viewer accepts static query-string demo entry links for the bundled scenarios: `public-validator-static-viewer.html?scenario=banana`, `public-validator-static-viewer.html?scenario=building`, `public-validator-static-viewer.html?scenario=news`, and `public-validator-static-viewer.html?scenario=qr-spoof`. Unsupported or missing scenario values fall back to the `banana` demo scenario.

The compact link-pattern reference is [`docs/demo/public-validator-demo-links.md`](public-validator-demo-links.md). It records the current scenario-link and demo `record_id` boundaries, including that `record_id` query-string support is not yet implemented.

The viewer also includes a demo Record ID input. Supported fixture IDs map to bundled scenarios only: `HC-DEMO-PV-FIXTURE-FOOD-0001` maps to `banana`, `HC-DEMO-PV-FIXTURE-CONCRETE-0001` maps to `building`, `HC-DEMO-PV-FIXTURE-NEWS-0001` maps to `news`, and `HC-DEMO-PV-FIXTURE-QR-0001` maps to `qr-spoof`. Unsupported IDs show a public-safe warning and do not trigger any backend, external service, canonical record lookup, database lookup, production verification, truth verification, QR authenticity check, or signed payload verification.

The viewer is demo-only, local-only, deterministic, and does not use a backend, external network calls, external dependencies, or a build step. Query-string and Record ID selection are navigation conveniences only; they do not prove QR authenticity, validate signed payloads, certify any real-world claim, or turn fixture results into canonical records.

## What this demo does

This demo:

- prints a deterministic JSON result for one selected public validator scenario;
- shows how a public-safe validation summary might expose provenance, responsibility, evidence, missing evidence, conflicts, and warnings;
- lets users type supported demo `record_id` values to select matching bundled fixture scenarios;
- keeps the output advisory-only and human-review-required;
- uses local fixture data only;
- helps reviewers compare the command-line output with the static demo documentation.

## What this demo does NOT do

This demo does not:

- claim production readiness;
- certify food safety, origin truth, import legality, freshness, or fitness for consumption;
- certify building safety, structural integrity, code compliance, occupancy readiness, or legal approval;
- certify article truth, publisher reliability, misinformation status, editorial independence, or legal status;
- make a fraud finding, forensic determination, legal determination, or QR authenticity certification;
- grant autonomous agent authority or replace human reviewer judgment;
- validate real signatures, verify live hashes, fetch remote URLs, perform external network checks, or look up canonical records by Record ID;
- modify schemas, validators, runtime endpoints, workflows, governance rules, records, generated artifacts, signing, federation, or policy.

## Requirements

- Python 3.
- A local checkout of the HC-TRUST-LAYER repository.
- Run commands from the repository root.
- No network access is required for the demo runner.

## How to run

From the repository root, run the demo script with one supported scenario name:

```bash
python scripts/run_public_validator_demo.py banana
python scripts/run_public_validator_demo.py building
python scripts/run_public_validator_demo.py news
python scripts/run_public_validator_demo.py qr-spoof
```

The script prints JSON to standard output. The output is deterministic for each scenario, so repeated runs of the same command should produce the same result unless the fixture definitions are intentionally changed in a later PR.

## Result fixtures

The runner reads demo-only result fixture exports from [`docs/demo/fixtures/results/`](fixtures/results/): [`banana.json`](fixtures/results/banana.json), [`building.json`](fixtures/results/building.json), [`news.json`](fixtures/results/news.json), and [`qr-spoof.json`](fixtures/results/qr-spoof.json). These JSON files are public-safe demo fixtures only; they are not canonical records, generated artifacts, production validator output, certifications, or legal authority.

## Available scenarios

| Scenario command | Scenario label in output | Public demo focus |
| --- | --- | --- |
| `banana` | `imported_banana_food_provenance` | Food provenance with missing evidence and a carton-count conflict. |
| `building` | `building_concrete_provenance` | Building/concrete provenance with partial field sample evidence. |
| `news` | `news_source_provenance` | News source provenance with incomplete confirmation and wording conflict. |
| `qr-spoof` | `qr_spoof_non_canonical_link` | QR/link review where the scanned URL differs from the expected HC:// canonical reference. |

## Example command

```bash
python scripts/run_public_validator_demo.py banana
```

## Example output

The exact key order is sorted by the script for readability. This excerpt shows the main fields a new user should inspect:

```json
{
  "advisory_only": true,
  "conflicting_evidence": [
    "Destination intake count differs from export count by two cartons."
  ],
  "evidence": [
    {
      "evidence_status": "present",
      "reference": "DEMO-LOT-0187-RECORD",
      "type": "demo_lot_record"
    }
  ],
  "human_review_required": true,
  "missing_evidence": [
    "Independent confirmation of origin inspection issuer authority"
  ],
  "public_safe": true,
  "record_id": "HC-DEMO-PV-FIXTURE-FOOD-0001",
  "responsibility_chain": [
    "Demo grower cooperative",
    "Demo packhouse operator"
  ],
  "scenario": "imported_banana_food_provenance",
  "source_chain": [
    "Demo grower cooperative harvest note",
    "Demo packhouse lot record"
  ],
  "status": "needs_human_review",
  "truth_guarantee": false,
  "warnings": [
    "Advisory demo result only; not a food safety certification."
  ]
}
```

## How to read the result

Use these fields as a quick reading guide:

- `record_id`: Fixture record identifier for the demo result. It is not a production record, signed payload, or certification.
- `scenario`: Internal scenario label selected by the command.
- `status`: Demo review posture. Current scenarios return `needs_human_review` to show that a person must review the evidence before relying on the result.
- `advisory_only`: Safety marker showing the output is informational and not authoritative.
- `public_safe`: Safety marker showing the fixture output is intended for public demo display and avoids private or sensitive evidence details.
- `truth_guarantee`: Safety marker. `false` means the result does not guarantee truth, safety, compliance, legality, authenticity, or completeness.
- `human_review_required`: Safety marker. `true` means human review remains required before any real-world reliance.
- `source_chain`: Public-facing list of demo source references that shaped the result.
- `responsibility_chain`: Public-facing list of demo roles or participants associated with the scenario.
- `evidence`: Structured list of visible demo evidence entries, usually with `type`, `reference`, and `evidence_status`.
- `missing_evidence`: Evidence or confirmations not available in the fixture output.
- `conflicting_evidence`: Public-safe conflicts that require review before relying on the scenario result.
- `warnings`: Scenario-specific reminders about limits, incomplete provenance, conflicts, and non-certification.

## Safety markers

Every scenario includes these safety markers:

```yaml
advisory_only: true
public_safe: true
truth_guarantee: false
human_review_required: true
```

Read them together:

- The output is advisory and public-safe.
- The output does not provide a truth guarantee.
- Human review is required.
- The result must not be presented as production validation, food certification, building certification, news certification, legal certification, fraud determination, or autonomous agent authority.

## Human review reminder

HC-TRUST-LAYER supports evidence-preserving, human-supervised validation. The demo runner helps users see how provenance and review boundaries might be displayed, but humans remain the final decision makers.

Before relying on any real HC:// validation workflow, a human reviewer must inspect the available evidence, missing evidence, conflicts, warnings, governance context, and applicable domain requirements.

## Troubleshooting

### `python: command not found`

Use the Python executable available in your environment, for example:

```bash
python3 scripts/run_public_validator_demo.py banana
```

### `invalid choice`

Use one of the supported scenario names:

```bash
python scripts/run_public_validator_demo.py banana
python scripts/run_public_validator_demo.py building
python scripts/run_public_validator_demo.py news
python scripts/run_public_validator_demo.py qr-spoof
```

### File path errors

Run the command from the repository root. The script path is relative to the root:

```bash
python scripts/run_public_validator_demo.py banana
```

### Output looks incomplete

The output is intentionally public-safe and fixture-based. Missing or conflicting evidence is part of the demo. It does not fetch additional evidence from the network.

## Recommended next step

After trying the static viewer and running the local demo, compare the JSON output with the static public result examples in [`docs/demo/public-validator-static-demo.md`](public-validator-static-demo.md). For the current checkpoint review, read [`docs/demo/public-validator-demo-checkpoint.md`](public-validator-demo-checkpoint.md). A recommended follow-up PR is **#651 Public Validator demo navigation polish**, kept documentation/demo-only unless explicitly scoped otherwise.
