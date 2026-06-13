# Code Volume Risk Status

Status: advisory checkpoint.

This note records the repository status for the external report section named "Kod miktarı sorunu".

## What is accepted

The repository has a broad source tree. Code volume and unclear implementation status are real maintainability risks.

The current safe response is inventory-first review, not cleanup by assumption.

## What is not accepted without evidence

The following claims must not be treated as repository truth without a full inventory:

- that there are exactly `150+` Python files;
- that most source files are stubs;
- that any named source file is unused from its filename alone;
- that the repository has exactly `85` branches;
- that branches can be safely deleted from a count estimate alone.

## Current repository evidence

Existing project-control records already show that some reported source areas have search-visible source, test, or documentation anchors. Existing records also require a non-mutating source inventory before any cleanup.

The current connector branch searches do not provide a reliable full branch count. They must not be used as the basis for branch deletion.

## Required next evidence

Before moving, archiving, deleting, or rewriting source files, collect:

- full non-mutating source inventory output;
- import or reference evidence;
- direct test evidence;
- documentation or quickstart references;
- protected-path relationship status;
- human-reviewed reason for any cleanup action.

## Decision

Keep all source cleanup and branch cleanup blocked until the inventory and review gates are satisfied.
