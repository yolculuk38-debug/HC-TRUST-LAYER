# Summary Failure Test Status

Status: completed test-hardening slice

Completed reference:

- #855 added failure-state coverage for `hc-trust verify-package --summary`.

Current locked behavior:

- invalid package summary returns exit code `1`;
- summary prints `status: INVALID`;
- summary prints `verified: false`;
- summary prints `human_review_required: true`;
- summary includes conflicting evidence;
- advisory boundaries remain visible.

Do-not-repeat:

- do not repeat #855 unless new repository evidence appears.

Next safe action:

- add issuer-proof-present coverage for summary output, then choose the next small local trust slice.
