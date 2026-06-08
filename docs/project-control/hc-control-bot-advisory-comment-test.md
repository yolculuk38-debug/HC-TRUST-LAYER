# HC Control Bot Advisory Comment Test

Mode: documentation only.

This file is a small test surface for the HC Control Bot advisory comment pilot.

## Purpose

This PR should trigger the advisory comment workflow after the pilot workflow has been merged.

Expected behavior:

- one advisory comment is created or updated;
- the comment uses changed file path metadata only;
- no labels are applied by the advisory comment workflow;
- no assignments are applied;
- no review decision is submitted;
- no merge action is performed;
- no autonomous authority is introduced.

## Boundary

Human final authority remains unchanged.
