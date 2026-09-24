---
name: capi-and-emq
description: When auditing the Meta pixel, Conversions API, event deduplication and Event Match Quality on an e-commerce account — whether purchase signal actually reaches Meta, at the right value, matched to the right person, counted once. Use when the user asks "audit my pixel," "is my CAPI working," "event match quality," "duplicate conversions," "why is my EMQ low," "deduplication," or "am I sending the right events." This is the measurement gate's core. For what Meta does with the gaps, see modeled-conversions.
---

<!-- execution-boundary: documents-writes -->
<!-- Names write tools without calling them: names pixel-event writes to explain why changing them is not reversible.
     Calling them is the execution lane's, under EXECUTION-PROTOCOL.md. -->
# CAPI and Event Match Quality

Five layers, audited in this order. Each depends on the one above it, and a fault high up makes
everything below it unreadable — which is why finding a broken purchase event in layer 2 changes
what layer 5's numbers mean rather than sitting beside them as a separate issue.

## Layer 1 — Is signal arriving at all

`ads_get_datasets`, `ads_get_dataset_details`, `ads_get_dataset_stats`.

- Which dataset (pixel) is the account actually optimising against? Multiple datasets with one
 active is normal; multiple **receiving** events is a finding.
- Event volume over time. A step change in the trend maps to a site deploy, a consent-banner
 change or a tag-manager edit — check §5's change map before diagnosing.
- Freshness. Events arriving hours late are a server-side implementation problem.
- Browser vs server split per event. **Browser-only Purchase in 2026 is a serious finding**:
 ATT and browser restrictions mean a material share of purchases never reach Meta at all.

## Layer 2 — Are the right events firing, with the right payload

The e-commerce funnel: `ViewContent`, `AddToCart`, `InitiateCheckout`, `Purchase`. Registration
and lead events where the account runs them.

For `Purchase` specifically, every one of these is a common, high-impact defect:

| Check | Why it matters |
|---|---|
| `value` present and non-zero | Value-optimised bidding degrades silently without it |
| `value` is order value, not line-item or subscription lifetime | Drives implied AOV in §3 straight off |
| `currency` correct and consistent | A multi-currency store sending mixed currencies untagged corrupts every value figure |
| `content_ids` present and matching the catalog | Without it, dynamic ads and catalog attribution cannot work |
| `content_type` correct (`product` vs `product_group`) | Variant-level mismatch breaks catalog matching |
| Fires **once** per order | Confirmation-page refreshes double-count; check against store orders |
| Does not fire on cart or thank-you views that aren't orders | The most common source of a claim ratio above 1 |

`ads_pixel_event_read` and `ads_pixel_parameter_read` show the configured events and parameters.
Compare them against what the store actually sends — configuration and reality diverge.

## Layer 3 — Deduplication

Browser and server both sending Purchase, without dedup, doubles the count.

- Every event needs a shared `event_id` **and** `event_name` across browser and server.
- `ads_get_dataset_quality` reports the dedup rate. A low rate with both channels active means
 events are being counted twice.
- The symptom in §3 is a claim ratio above 1 that survives window alignment.
- Check timing: server events arriving outside Meta's dedup window are not deduplicated even
 with a matching `event_id`.

## Layer 4 — Event Match Quality

EMQ is how well Meta can match an event to a person. Low EMQ means more modelling, worse
optimisation and weaker audiences — it is upstream of nearly every other measurement problem.

Match keys, in rough order of value:

| Key | Notes |
|---|---|
| `email` | Highest value. Hashed |
| `phone` | High value, frequently missing on e-commerce |
| `fbc` / `fbp` cookies | Click and browser id. Requires the click id to be captured and persisted through checkout |
| `external_id` | The store's customer id. Cheap to add, materially improves matching |
| First/last name, city, state, zip, country | Available at checkout; often not sent |
| IP and user agent | Server-side only |

**Thresholds — reasonable defaults; tune to the account's own traffic mix once a baseline
exists.** Meta's EMQ runs 0–10; target **8.0+**. Below 7.0 is a real attribution problem quietly
costing efficiency. Below 6.0, Meta cannot reliably attribute at all.

| Match key | Healthy | Warning | Broken |
|---|---|---|---|
| Email | >40% | 20–40% | <20% |
| Phone | >20% | 10–20% | <10% |
| `fbp` (browser cookie) | >85% | 70–85% | <70% |
| `fbc` (click id) | >50% on click-through events | 30–50% | <30% |
| IP | >95% | 85–95% | <85% |
| `external_id` | >30% where passed | 10–30% | <10% |

Common causes of low EMQ: advanced matching disabled; CAPI not sending email or phone for
logged-in users; hashing done wrong (Meta needs SHA-256, lowercased, trimmed); heavy iOS traffic
degrading `fbp`/`fbc`; identifiers captured at checkout but never passed server-side.

Report **coverage per key**, not just the aggregate score. An EMQ of 6.2 built on email alone is
a different account from a 6.2 built on six partial keys, and the fixes are different.

The most common finding: `fbc` not persisted through a multi-step or third-party checkout, so
server events arrive without the click id and cannot be matched to the ad that drove them.

EMQ is Meta's score of Meta's own matching — classify it `PLATFORM_STATED` and corroborate
against first-party order data before drawing a conclusion from it.

## Layer 5 — Aggregated Event Measurement and domain verification

- **Domain verified?** Without it, no event configuration exists at all, and everything above is
 moot for iOS web traffic.
- **Event priority order.** `Purchase` must be priority 1. An account with `AddToCart` above
 `Purchase` is optimising toward the wrong event for iOS users — common, high impact, and a
 five-minute fix.
- Only 8 events can be configured; only the highest-priority event in a session counts for
 affected users. Lower-priority events are under-reported **by design**, not broken.
- Value sets configured, if value optimisation is used.
- Where checkout is on a third party's domain, verification and AEM behave differently — see
 `meta-third-party-conversion-tracking`.

## The verdict

§2 closes with one, and it orders the rest of the audit:

| Verdict | Meaning |
|---|---|
| **GREEN** | Purchase measurement is trustworthy enough to optimise on |
| **YELLOW** | Usable with explicit caveats, which are named |
| **RED** | Optimisation economics cannot be trusted |

`RED` **orders** the audit; it does not end it. Every other section still runs, findings are
marked `DEGRADED`, and no scale or kill recommendation is issued that depends on conversion
values just shown to be unreliable.

## Reporting a fix

This audit does not apply fixes. Where an event configuration change is warranted, write it as a
recommendation with the exact parameter and value, and note that
`ads_pixel_event_create|update|delete` mutations **rewrite how the account measures itself from
that moment on**. Historical data keeps the old definition, so the discontinuity is permanent
and belongs in the change register — otherwise the next audit reads the step in the trend as a
performance event.
