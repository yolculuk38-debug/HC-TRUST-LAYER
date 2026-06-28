# Demo / Example Boundary Review

## 1. Purpose

This document is an advisory, documentation-only review of observed HC-TRUST-LAYER demo, example, and fixture boundaries.

It supports backlog item 4-5, “demo/example boundary review,” after the core package boundary review, test taxonomy review, public API / CLI boundary review, and generated/canonical artifact ownership review. It clarifies which observed paths appear to be demo-only material, examples, fixtures, public validator demo outputs, simulated scenarios, or areas needing maintainer confirmation.

This review does not modify code, tests, workflows, scripts, schemas, validators, records, generated or canonical artifacts, demo fixtures, runtime behavior, API behavior, CLI behavior, public validator behavior, QR behavior, package metadata, CI behavior, or governance authority.

## 2. HC boundary

- `advisory_only=true`.
- `public_safe=true`.
- `truth_guarantee=false`.
- `human_review_required=true` for repository and governance decisions.
- Demos, examples, and fixtures are learning and validation aids, not trust authority.
- Demo outputs do not establish legal truth, identity finality, forensic certainty, certification, production readiness, or real-world verification.
- The human maintainer remains the final authority.

HC-TRUST-LAYER demo and example material should be interpreted as bounded evidence for learning, local validation, documentation review, and negative-path demonstration only. No demo, example, fixture, static viewer, public explorer page, QR scenario, browser/mobile flow, or verification package example should be treated as autonomous governance authority, a real-world record, or guaranteed correctness unless a separate human-reviewed PR explicitly promotes that surface with tests, provenance, and boundary documentation.

## 3. Review method

This review inspected observed repository paths by name and apparent role. It does not invent files or directories and does not assert hidden maintainer intent. If a requested category was not observed, it is marked as `not observed`.

Observed categories reviewed:

- `docs/demo/**`;
- `docs/demo/fixtures/**`;
- public validator demo docs;
- public validator static viewer docs;
- QR spoof demo and scenario references;
- banana, building, news, and QR spoof scenario references;
- browser/mobile demo flow docs where observed;
- public explorer/static viewer demo docs where observed;
- verification package examples where observed;
- relationship to `docs/project-control/public-api-cli-boundary-review.md`;
- relationship to `docs/project-control/generated-canonical-artifact-ownership-review.md`;
- relationship to `docs/project-control/test-taxonomy-review.md`.

This review is conservative. It only documents observed documentation and example boundaries and does not inspect, alter, regenerate, move, rename, or validate demo fixture contents beyond path/name-level classification.

## 4. Demo/example classification table

| Path / demo group | Observed role | Demo/example/fixture status | Public audience | Trust sensitivity | Boundary label needed | Related tests/checks observed | Notes |
|---|---|---|---|---|---|---|---|
| `docs/demo/` | Public validator and local lookup demo documentation. | demo-only; public-safe; advisory-only | Public demo users, reviewers, maintainers. | medium | Yes: public demos must remain advisory-only. | Test taxonomy references public validator demo runner, static viewer, browser, and mobile checks. | Demo docs should keep boundary language before commands and sample output. |
| `docs/demo/fixtures/` | Public validator, local lookup, QR parser, and result fixture material. | fixture; demo-only; public-safe; advisory-only | Public demo users, reviewers, maintainers. | medium | Yes: fixtures are not real records. | Test taxonomy references fixture and demo runner coverage. | Fixture promotion to records requires separate human review. |
| `docs/demo/fixtures/results/banana.json` | Banana public validator result fixture. | fixture; simulated scenario; public-safe | Public demo users and reviewers. | medium | Yes: not a real food record or safety certification. | Public validator demo runner coverage observed by test taxonomy. | Scenario name observed as `banana`. |
| `docs/demo/fixtures/results/building.json` | Building/concrete public validator result fixture. | fixture; simulated scenario; public-safe | Public demo users and reviewers. | medium | Yes: not building safety, code, occupancy, or legal approval. | Public validator demo runner coverage observed by test taxonomy. | Scenario name observed as `building`. |
| `docs/demo/fixtures/results/news.json` | News provenance public validator result fixture. | fixture; simulated scenario; public-safe | Public demo users and reviewers. | medium | Yes: not news truth, editorial quality, or certification. | Public validator demo runner coverage observed by test taxonomy. | Scenario name observed as `news`. |
| `docs/demo/fixtures/results/qr-spoof.json` | QR spoof / non-canonical link result fixture. | fixture; simulated scenario; advisory-only | Public demo users and reviewers. | high | Yes: negative-path spoofing demo must be visibly simulated. | QR spoof and public validator demo checks are referenced by test taxonomy. | Warning output must not be read as legal, forensic, or fraud finality. |
| `docs/demo/fixtures/demo-qr-links.json` | Demo QR/link entry mappings. | fixture; demo-only; public-safe | Public demo users and reviewers. | high | Yes: QR links are pointers, not proof. | QR parser and public validator checks are referenced by test taxonomy. | QR output needs pointer/payload boundary. |
| `docs/demo/fixtures/qr-payload-parser/` | QR payload parser example inputs. | fixture; example-only; public-safe | Maintainers, reviewers, demo operators. | high | Yes: parser examples do not prove QR authenticity. | QR payload parser tests are referenced by test taxonomy. | Includes malformed, missing-field, unknown-field, matching, and mismatched examples by filename. |
| `docs/demo/fixtures/local-validator-output/` | Golden output examples for local validator lookup. | generated example; fixture; advisory-only | Public demo users and reviewers. | medium | Yes: output fixtures are examples, not production API responses. | Local lookup and public validator checks observed by docs and test taxonomy. | Must remain separated from canonical records. |
| `docs/demo/public-validator-static-viewer.html` | Static public validator demo viewer. | demo-only; public-safe; advisory-only | Public demo users and reviewers. | medium | Yes: static viewer is not live validation. | Static viewer contract and smoke checks are referenced by test taxonomy. | Public-facing output could be mistaken for real verification if labels are omitted. |
| `docs/demo/public-validator-static-demo.md` | Narrative static demo with banana, building, news, and QR spoof examples. | demo-only; simulated scenario; public-safe | Public demo users and reviewers. | medium | Yes: scenario outputs are not real-world verification. | Static viewer and demo runner checks referenced by test taxonomy. | Strong boundary language is already visible by path review. |
| `docs/demo/public-validator-result-examples.md` | Explanatory result examples for public validator scenarios. | example-only; simulated scenario; public-safe | Public demo users and reviewers. | medium | Yes: examples are fictional and advisory. | Public validator response/demo checks referenced by test taxonomy. | Covers banana, building, news, and QR spoof style examples. |
| `docs/demo/public-validator-demo-quickstart.md` | Public validator local demo runner quickstart. | demo-only; advisory-only | Public demo users, reviewers, maintainers. | medium | Yes: commands must not imply production verification. | Public validator demo runner test referenced by test taxonomy. | Copy-paste commands should be preceded by boundary language. |
| `docs/demo/public-validator-local-lookup-quickstart.md` | Local record ID lookup quickstart and output examples. | example-only; demo-only; advisory-only | Public demo users and reviewers. | high | Yes: local lookup is not canonical lookup or truth verification. | Local lookup and public validator checks observed by docs and taxonomy. | References `records/pending/example.json`; this review does not inspect or modify records. |
| `docs/demo/public-validator-local-record-lookup-boundary.md` | Boundary document for local Record ID lookup demo. | advisory-only; public-safe | Public demo users and maintainers. | high | Already boundary-focused; keep explicit. | Static viewer and local lookup checks are referenced. | Distinguishes fixture matching from production/API/canonical lookup. |
| `docs/demo/public-validator-demo-links.md` | Static viewer scenario and Record ID demo links. | demo-only; public-safe | Public demo users and reviewers. | medium | Yes: links select fixtures only. | Static viewer smoke/contract checks referenced. | QR-style navigation must not imply QR authenticity. |
| `docs/demo/public-validator-demo-qr-entry.md` | Public-safe QR/link entry flow documentation. | demo-only; simulated scenario | Public demo users and reviewers. | high | Yes: QR entry is not proof by itself. | QR and public validator checks referenced by test taxonomy. | Keep QR as pointer/payload language. |
| `docs/demo/public-validator-demo-checkpoint.md` | Checkpoint for public validator demo docs, viewer, runner, and fixtures. | advisory-only; public-safe | Maintainers and reviewers. | medium | Already boundary-focused; keep explicit. | Names static viewer, runner, and fixture alignment. | Useful maintainer checkpoint for current demo state. |
| `docs/demo/mini-public-validator-demo.md` | Minimal explanatory public validator result shape. | example-only; demo-only | Public demo users and reviewers. | low | Yes: shape example is not a live validation result. | Public response checks referenced by taxonomy. | Useful concise example boundary. |
| `docs/demo/public-validator-local-demo-adapter-plan.md` | Local adapter planning document. | advisory-only; example/demo planning | Maintainers and reviewers. | medium | Yes: plan is not implementation authority. | not observed by name in checks | Needs maintainer confirmation before any promotion. |
| `docs/demo-flow.md`, `docs/demo-index.md`, `docs/demo-verification-flow.md` | Top-level demo navigation and flow docs. | demo-only; public-safe | Public demo users and reviewers. | medium | Yes: flow docs should avoid production claims. | Browser/mobile demo checks are referenced by test taxonomy. | Browser/mobile documentation is observed at top-level docs path. |
| `docs/explorer/` and `docs/public-explorer-mvp.md` | Public explorer/static viewer documentation and static explorer surface. | demo-only or MVP-bound; public-safe; needs maintainer confirmation | Public viewers, reviewers, maintainers. | medium | Yes: explorer views are navigation/evidence, not authority. | Public verification explorer smoke and MVP checks are referenced by test taxonomy. | Public Explorer appears future-facing/MVP-bounded by path and names. |
| `docs/verification-package-*.md`, `docs/external-verification-packages.md`, `docs/mvp-1-verification-package-viewer.md` | Verification package docs and examples. | example-only; advisory-only; needs maintainer confirmation | Maintainers, reviewers, integrators. | high | Yes: package examples are not canonical records. | Verification package tests/checks referenced by test taxonomy. | Package export/validation remains evidence only. |
| `examples/verification-package/` and `examples/verification-packages/` | Verification package example directories. | example-only; generated example where applicable; not canonical | Maintainers, reviewers, demo operators. | high | Yes: examples must not be promoted to canonical records silently. | Verification package checks referenced by test taxonomy. | Observed outside allowed edit scope; not modified. |
| `records/` demo relationship | Real record examples or canonical-adjacent records may exist by repo map. | real record not observed in this review | Maintainers and reviewers. | critical | Needs maintainer confirmation before linking demo examples to real records. | Canonical artifact checks observed. | This PR does not inspect or modify records. |
| Live backend public validator demo service | not observed | not observed | not observed | not observed | Needs maintainer confirmation if added. | not observed | Static/local documentation observed; live service deployment not observed. |
| Production QR certification flow | not observed | not observed | not observed | not observed | Needs maintainer confirmation if added. | not observed | QR spoof and QR payload examples are observed only as demo/test-adjacent material. |

## 5. Demo scenario table

| Scenario | Apparent purpose | Expected output category | Must not be interpreted as | Human review requirement | Notes |
|---|---|---|---|---|---|
| `banana` | Imported food provenance demonstration. | Public validator demo result; simulated scenario; fixture output. | Food safety certification, origin truth, import legality, product authenticity, regulatory approval, legal truth, or production verification. | Required before any consequential use. | Observed in public validator static demo, result examples, fixture results, and demo links. |
| `building` | Construction material or concrete provenance demonstration. | Public validator demo result; simulated scenario; fixture output. | Building safety certification, structural integrity finding, code compliance, occupancy readiness, contractor approval, legal truth, or production verification. | Required before any consequential use. | Observed in public validator static demo, result examples, fixture results, and demo links. |
| `news` | News source provenance demonstration. | Public validator demo result; simulated scenario; fixture output. | News truth rating, editorial certification, defamation/legal conclusion, public-interest judgment, source identity finality, or production verification. | Required before any consequential use. | Observed in public validator static demo, result examples, fixture results, and demo links. |
| `qr-spoof` | QR spoof / non-canonical link negative-path demonstration. | Public validator warning demo; simulated negative-path fixture output. | Criminal intent, issuer fraud, legal liability, forensic certainty, QR authenticity certification, identity finality, or production verification. | Required before escalation or public claims. | Observed in public validator static demo, result examples, fixture results, and demo links. |
| Public validator static viewer scenarios | Browser-readable local scenario selection. | Static demo output; public-safe advisory output. | Live backend lookup, canonical record lookup, truth verification, signature verification, QR cryptography, or production API behavior. | Required for consequential interpretation. | Observed in `docs/demo/public-validator-static-viewer.html` and related docs. |
| Browser/mobile demo flow | Public-facing demo flow documentation and runtime checks by name. | Demo/integration output; advisory-only. | Production mobile/browser verification, guaranteed security, identity finality, or legal truth. | Required before public reliance. | Top-level demo flow docs are observed; browser/mobile tests are referenced by test taxonomy. |
| Public explorer/static viewer | Public navigation/explorer demonstration or MVP-bound surface. | Static/public explorer demo output; advisory evidence view. | Canonical authority, live federation status, complete provenance truth, production explorer readiness, or certification. | Required before treating as public contract. | `docs/explorer/` and `docs/public-explorer-mvp.md` observed. |
| Verification package examples | Package shape and local verifier examples. | Example-only package output; generated example where applicable. | Canonical record, signed proof, production export guarantee, legal truth, or complete verification package authority. | Required before promotion or reuse as authoritative evidence. | Verification package docs and example directories are observed. |

## 6. Boundary findings

Paths that appear demo-only include `docs/demo/**`, the public validator static viewer, public validator demo quickstarts, public validator demo links, QR entry docs, top-level demo flow docs, and the static public validator scenario material. These paths are public-facing and should keep visible advisory-only language near scenario selection, copy-paste commands, and sample outputs.

Paths that appear examples include public validator result examples, mini public validator examples, verification package docs, verification package example directories under `examples/`, and explanatory local lookup outputs. These examples help reviewers understand output shape and evidence boundaries, but they do not create canonical records, legal truth, production APIs, or validation authority.

Paths that appear fixtures include `docs/demo/fixtures/**`, especially local validator output fixtures, QR payload parser inputs, demo QR links, and public validator scenario result JSON files for `banana`, `building`, `news`, and `qr-spoof`. These fixtures should remain visibly separated from `records/**` and should not be promoted to real records without a separate PR, tests, provenance review, and human approval.

Public-facing demo outputs include the public validator static viewer, public validator static demo, public validator result examples, public validator demo links, local lookup quickstart outputs, public explorer/static viewer documentation, browser/mobile demo flow docs, and verification package examples. These outputs may be useful for learning and review, but they can be misunderstood when fields such as `valid`, `verified`, `record_id`, hash/digest status, QR match status, warnings, provenance, or scenario names are read without boundary context.

Demo outputs most likely to be misunderstood as real verification include public validator scenario results, QR spoof warnings, Record ID fixture matches, static viewer selections, public explorer pages, local lookup results, and verification package example summaries. These examples need clear “not a real record,” “not production verification,” “not legal truth,” and “human review required” language wherever users encounter outputs before context.

Areas needing maintainer confirmation include any future promotion of demo fixtures into records, any stable public validator demo contract, any public explorer production boundary, any browser/mobile demo readiness claim, any QR spoof warning wording used outside simulated negative-path demos, and any verification package example promoted into a canonical record or public contract.

Existing tests appear to cover demo separation and fixture safety by name through public validator demo runner tests, static viewer contract and smoke tests, public verification explorer checks, browser validator checks, mobile verification flow checks, QR parser and QR spoof protection checks, QR public validator and QR record bridge checks, and verification package checks as summarized in the test taxonomy. This review does not prove complete coverage and does not run the full test suite; maintainers should confirm whether the tests fully cover demo separation, fixture safety, QR spoofing, static viewer behavior, public explorer behavior, browser/mobile demos, and the public validator demo runner before treating those boundaries as stable.

## 7. Recommended HC demo/example rules

- Demo fixtures must be visibly separated from real records.
- Demo outputs must never claim legal truth, identity finality, certification, or production readiness.
- QR demo output must treat QR as pointer/payload, not proof by itself.
- Public validator demo output must remain advisory and public-safe.
- Spoofing demos must be clearly labeled as simulated negative-path examples.
- Example verification packages must not be promoted to canonical records without separate human review.
- Demo docs should include boundary language before copy-paste commands or sample outputs.
- Any promotion from demo/example to production/public contract requires a separate PR, tests, and human review.
- Demo screenshots, static viewers, and public explorer examples must not expose secrets, tokens, private paths, or internal-only context.

## 8. Ideal vs current practical state

### Ideal

- Every demo, example, and fixture has a visible boundary label.
- Demo data is clearly separated from real records.
- Sample outputs include `advisory_only`, `public_safe`, `truth_guarantee`, and `human_review_required` wording where relevant.
- Spoofing and negative-path demos are unmistakably simulated.
- Demo commands and static viewers avoid production claims.
- Public examples link back to boundary docs.

### Current practical next step

- Document observed demo/example boundaries first.
- Do not change demo files or outputs in this PR.
- Propose small follow-up PRs for missing labels, wording, or tests.

## 9. Real-world analogy

A bank training receipt or sandbox transaction is not a real ledger transaction. An e-devlet demo screen is not an official citizen record. An SSL/TLS test certificate or staging environment lock does not prove the production site’s claims. C2PA, W3C Verifiable Credentials, and OpenTimestamps examples are useful evidence demos only when clearly tied to source and context.

HC-TRUST-LAYER demos should follow the same rule: demo evidence is useful for learning and testing, not final truth.

## 10. Follow-up items

- 4-5b optional: add visible demo/example boundary labels where missing.
- 4-5c optional: add or tighten demo output wording in public validator docs.
- 4-5d optional: add QR spoof / negative-path demo wording checklist.
- 5-1: onboarding / contributor guide boundary review.
- 5-2: maintainer workflow / PR review checklist boundary review.
