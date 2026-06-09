# HC Control Bot Check Status Guide

This guide explains the HC Control Bot related checks that may appear on a pull request.

## Expected checks

A normal pull request may show two HC Control Bot related checks:

- HC Control Bot Report
- HC Control Bot Advisory Comment

## HC Control Bot Report

This check runs the deterministic scanner and produces report output.

Expected trigger:

- pull_request

## HC Control Bot Advisory Comment

This check displays advisory scanner metadata in one pull request comment when comment writing is available.

Expected trigger:

- pull_request_target

## Why they are separate

The report check and the comment check are separate because they serve different roles and have different permission needs.

The report check is read/report oriented.

The comment check is advisory comment oriented.

## Duplicate check note

There should normally be one HC Control Bot Report check for a pull request event.

If duplicate report checks appear, review workflow triggers first.

## Authority boundary

HC Control Bot checks support review.

Human final authority remains unchanged.
