# Backlog: Legacy SCC Access And Source Acquisition Variance

Status: deferred
Created: 2026-09-04
Updated: 2026-09-04

## Summary

A bounded SCC HTML acquisition sample succeeded on newer decisions, but a second older sample returned 403 Forbidden responses on the same source-link pattern. This means the problem is not a generic SCC parser failure; it is a source-access variance issue for older SCC decisions that must be tracked as a separate backlog item.

## Why this matters

The pipeline is intended to preserve source HTML and structure for decision content. The evidence shows that:

- newer SCC cases can be accessed through the source URL pattern and produce valid HTML snapshots;
- older SCC decisions may reject the same access pattern with 403 responses;
- this must be treated separately from chunking and parsing quality at the product level.

## Current evidence

- 10-case fresh SCC sample: 10/10 acquired with `status=applied reason=valid-html`
- older sample attempted on cases in the 1935/1936 SCR range: all returned `403 Forbidden` and `decision-content-not-found`
- this is a source availability/access problem, not a chunking or mapping failure

## Decision boundary

Do not treat this as a blocker to the core pipeline. Continue on the working decisions and keep the legacy access issue in the backlog for a dedicated follow-up.

## Recommended follow-up

- add a small, bounded SCC legacy-access probe script;
- record which SCC timestamp ranges or item variants return 403;
- decide whether those cases need alternate source families, a different endpoint, or an explicit source exemption.
- keep activity history, submissions, and other SCC add-ons out of scope until decision-source acquisition is stable.
