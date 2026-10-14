# Verification viewer text boundary correction

## Investigation before implementation

The maintainer supplied two open CodeQL findings on the main branch: #13
(`js/xss-through-dom`, high) and #14 (`js/xss-through-exception`, medium), both in
`docs/verification-viewer.html`. Source baseline is #1250 merge
`dd27203180bf6c3ff95732e20efa3d0b4eb236f5`.

The existing `safe` helper supplies missing-value defaults; it is not HTML output
encoding. Dynamic package/source labels and exception details reach HTML template
rendering. The fix must preserve those values as visible text while retaining
the existing layout, plain-text exports and original JSON copy/download content.

## Bounded implementation and validation plan

Encode dynamic text at HTML template boundaries, including the trust-result
label and raw JSON view. Render exception details through DOM text properties.
Add executable regressions for package fields, local filenames, bundled load
errors and local parse errors, using inert markup markers without executable
payloads. Verify ordinary bundled examples and unchanged raw JSON/text exports.

Touch the existing validation workflow only to run these regressions when the
viewer changes; preserve its permissions and review gates. Current-head Codex
review, CI and main-branch CodeQL analysis are required. A successful analysis
job alone does not prove the private alert count; do not dismiss alerts manually
or claim closure without a scan result or alert-state observation.

No uploaded private data, exploit payload, schema change or trust-authority
expansion belongs in this patch. Remaining viewer trust-claim semantics are a
separate A4 inventory item.

## Local validation

The executable regression suite failed on five rendering paths before the fix
and passes all eight cases afterward. It executes the actual inline JavaScript
with a DOM recorder and independently parses generated HTML; it does not claim
browser-engine execution or alert-state access. All five bundled examples retain
their report sections, original JSON copies and plain-text values remain intact,
and failed loads disable package actions.

CPython 3.14.7 / Node 24.19.0: 1396 full-suite tests passed, including the eight
focused cases (counts overlap), with one upstream TestClient warning. Canonical,
terminology, docs and whitespace guards passed with two existing README wording
warnings. Current-head CI and matching review remain required before merge.

CodeQL follow-up: make the test harness's script-tag extraction case insensitive
to handle HTML tag spelling consistently (review comment 4268609031). This is a
test-source extractor, not an HTML sanitizer. The production text encoder and
DOM-only exception rendering remain unchanged. Re-run all eight focused cases.
