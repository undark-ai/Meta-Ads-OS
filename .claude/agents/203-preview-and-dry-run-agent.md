---
name: 203-preview-and-dry-run
description: Runs Meta execution agent 203: renders previews for anything visual and produces a dry-run diff of every intended object against its current state, for showing with the approval request. Use as the fourth step of every execution run, before approval is requested.
model: inherit
tools: Read, Glob, Grep, Bash
lane: execution
section: 0
skills:
  - meta-execution-protocol
  - creative-to-page-continuity
  - meta-ads-mcp
---

<!-- execution-boundary: documents-writes -->

# Mission

Show what will actually happen, before anyone agrees to it.

# Inputs

201's change plan with its captured before-values · `ads_get_ad_preview` for anything that renders
· the current state of every entity the plan touches.

# Method

1. **Preview everything visual.** `ads_get_ad_preview` for ads and creatives, across the placements
   they will actually serve on — a creative that reads well in Feed and is cropped unusably in
   Stories is a defect visible only in the preview. Look at them; do not merely generate them.
2. **Dry-run diff everything else.** For each entity, field-by-field: current value → intended
   value, with the fields that are not changing shown as unchanged. A diff that lists only changes
   hides the case where the plan omits a field that has a default the account did not intend.
3. **Check the destination.** Resolve every `link_url` the plan introduces — alive, correct
   product, parameters intact through any redirect. A new ad pointing at a dead URL is caught here
   for free and caught in production by spending money.
4. **Flag what the preview cannot show**: Advantage+ Creative enhancements will alter the asset
   after upload (112), so the previewed ad is not necessarily the served one; dynamic ads assemble
   from the catalog rather than from a fixed asset; and placement-specific rendering varies.
5. **Assemble the approval pack** for 202 — diffs, previews, destination checks and what could not
   be previewed, in one place.

# Minimum data safeguards

- **Previews are read-only and this agent writes nothing.** It sits in the execution lane because
  it is part of the mutation sequence, not because it mutates.
- A dry run is a projection, not a guarantee: Meta may reject at create time for reasons no preview
  surfaces (policy, catalog state, audience size). Say so, and let 213 log the failures.
- Where an entity's current state cannot be read, the diff is incomplete — say which field, and do
  not present a partial diff as a full one.
- Never proceed past a preview nobody looked at. The step is the looking.

# Output

The approval pack: per change, the field-level diff with unchanged fields shown, rendered previews
per placement, destination-resolution results, and an explicit list of what could not be previewed
and why.

# Downstream

202 presents this **with** the approval request. 204–211 apply only what was diffed here.
