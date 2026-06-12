# Issuer Proof Sample Status

Status: completed sample and quickstart slice

Completed reference:

- #849 updated the sample verification package with issuer proof evidence.

Current sample path:

```text
examples/verification-package/valid/
```

Current sample includes:

- `manifest.json`
- `metadata/source-info.txt`
- `issuer-proof.json`

Current command:

```bash
hc-trust verify-package examples/verification-package/valid
```

Expected local result:

- package status: `VERIFIED`
- issuer proof status: `PRESENT`
- `advisory_only=true`
- `public_safe=true`
- `truth_guarantee=false`

Do-not-repeat:

- do not repeat #838, #839, #841, #843, #845, #846, #847, #848, or #849 unless new repository evidence appears.

Next safe action:

- choose the next small local trust slice before changing protected paths.
