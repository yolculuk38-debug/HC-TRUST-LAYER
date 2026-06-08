# HC Control Bot Advisory Comment Validation

Mode: documentation only.

This file validates the best-effort advisory comment workflow after the workflow update.

## Expected behavior

- The advisory workflow runs on this pull request.
- If comment writing is allowed, one advisory comment is created or updated.
- If comment writing is not allowed, the workflow records a warning and exits successfully.
- No labels are applied by the advisory comment workflow.
- No assignments are applied.
- No review decision is submitted.
- No merge action is performed.

## Boundary

Human final authority remains unchanged.
