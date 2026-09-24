# Canonical data model

Every agent in the library reads and writes the same entities with the same keys. This file
says what those are, so two agents analysing the same account cannot quietly disagree about
what an "ad" or a "purchase" is.

The rule underneath all of it: **normalise, but never destroy the raw value.** A normalised
column sits beside the source column, not on top of it. When section 3 finds a gap between
Meta and Shopify, the first question is always "what did each side actually report", and an
audit that overwrote the source values cannot answer it.

## Keys

| Entity | Key | Notes |
|---|---|---|
| Account | `account_id` | `act_` prefix stripped in the normalised column, preserved raw. Confirm which account is live — most brands have legacy and test accounts, and the one you were pointed at is not always the one spending. |
| Campaign | `campaign_id` | Names change; ids do not. Never key on name. |
| Ad set | `adset_id` | |
| Ad | `ad_id` | The grain of `creative-record.yaml`. |
| Creative | `creative_id` | Many ads can share one creative — deduplicate before counting "how many creatives are we running". |
| Product | `product_id` | Meta catalog id. Joins to `sku` via the catalog, not by string-matching titles. |
| SKU | `sku` | The commerce platform's identifier. Authoritative for margin. |
| Order | `order_id` | From the commerce platform. Authoritative for revenue. |
| Customer | `customer_id` | From the commerce platform. The only place new-vs-returning can be established. |
| Audience | `audience_id` | Custom and lookalike audiences. |
| Dataset / pixel | `dataset_id` | Meta's current name for what people still call the pixel. |
| Date | `date` | Account timezone, ISO. |

## Normalisation rules

**Currency.** One reporting currency per run, stated in `scope.md`. Meta returns formatted
strings (`"$58,758.12 USD"`, `"1,694,974"`, `"1.55%"`, `"Not available"`) — parse them, keep
the raw string. `"Not available"` parses to null, never to zero.

**Timezone.** The ad account's timezone, which is frequently not the store's. A day-level
comparison across the two without aligning this produces a gap that looks like a measurement
defect and is not one.

**Dates.** Meta reports on the **conversion** date by default; commerce platforms report on the
**order** date, and Meta's attribution window means a purchase can be credited to a click days
earlier. Section 3 aligns this explicitly before comparing anything.

**Ratios are never averaged.** CTR, ROAS, frequency, hook rate, CVR — recompute from the
component sums at the level you want. Averaging an ad-level ratio to get an ad-set ratio
weights a 12-impression ad the same as a 1.2-million-impression one, and the answer is wrong in
a direction nobody can predict. This is the single most common way a Meta report becomes
fiction.

**Breakdowns do not compose.** Meta rejects some breakdown combinations and silently changes
totals across others. Pull one breakdown dimension per call, reconcile each breakdown against
its parent total, and if the rows do not sum, rows are missing — say so rather than presenting
the subset as the whole.

**Attribution window is part of the number.** A 7-day-click figure and a 7-day-click-1-day-view
figure are different measurements of different things. One window per run, stated in the file
header of every dataset. A row on a different window is dropped, not silently included.

## Source of truth

```text
orders / revenue / customers : commerce platform (Shopify) > analytics > Meta
margin / COGS                : commerce platform or finance > anything derived from ROAS
media delivery               : Meta > third-party estimates
creative content             : Meta (ads_get_creatives) > inference from the ad name
relevance / auction / EMQ    : Meta, but classified PLATFORM_STATED, never OBSERVED
catalog / feed state         : Meta catalog diagnostics > inference from ad performance
web behaviour                : GA4 > assumption
rendered post-click UX       : browser > screenshots > assumption
competitor creative          : Meta Ad Library — what is running, never what is working
```

## The three derived datasets

Everything downstream reads these rather than re-querying, so the dashboard, the findings and
the executive page cannot disagree.

| Dataset | Written by | Schema | Grain |
|---|---|---|---|
| `creative-database.csv` | 59 | `creative-record.yaml` | one row per ad |
| `reconciliations/` | 37–42 | `reconciliation-schema.yaml` | one row per compared metric |
| `scale-matrix.md` | 158 | `scale-matrix.yaml` | one row per angle × product × offer × audience |

## Canonical economics

Computed once in section 1, consumed everywhere. An agent that recomputes contribution margin
from its own assumptions will disagree with the executive page, and the reader has no way to
tell which is right.

| Value | Owner | Definition |
|---|---|---|
| Gross margin % | §1 | (revenue − COGS) ÷ revenue, from the commerce platform |
| Contribution margin | §1 | gross margin − variable costs (shipping, payment fees, fulfilment, returns) |
| Break-even ROAS | §1 | 1 ÷ contribution margin % |
| CAC ceiling | §1 | contribution margin per first order, adjusted for repeat value |
| Break-even new-customer CAC | §1 | the first-order-only version, before LTV |
| Blended MER | §3 | store revenue ÷ **total** ad spend, every paid channel |

Where margin is assumed rather than derived, the assumption is labelled in `assumptions.md` and
every dependent figure is published as a range across the plausible band, with a statement of
whether the recommendation changes across it. Usually it does not — and saying so is more
useful than withholding the number.
