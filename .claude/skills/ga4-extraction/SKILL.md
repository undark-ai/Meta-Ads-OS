---
name: ga4-extraction
description: When pulling behavioural and mid-funnel data from GA4 for a Meta audit — session and funnel events, landing pages, source/medium, device and geography — and using it as the neutral third source in reconciliation. Use whenever the funnel's mid-stages, page-level behaviour, or an independent view of paid traffic is needed. Directional for attribution, never authoritative for revenue.
---
# GA4 extraction

GA4's value in a Meta audit is being **neither party to the dispute**. When Meta claims 400
purchases and the store banked 250, GA4 is the third reading that helps explain the gap.

It is directional for attribution and authoritative for nothing about money.

## What to pull

| Data | Used by |
|---|---|
| Sessions, users by source/medium/campaign | §3, §2 link tracking |
| The e-commerce funnel: `view_item`, `add_to_cart`, `begin_checkout`, `purchase` | §19 funnel |
| Landing pages with sessions and conversion rate | §20 CRO |
| Device and browser | §19, §23 |
| Geography | §23 |
| Purchases and revenue by channel | §3 reconciliation |

## What it is good for

**The mid-funnel, independently.** Meta's own ViewContent/ATC/InitiateCheckout depend on the same
pixel whose health §2 is questioning. GA4 measures the same steps through a different pipe, and
where the two disagree that disagreement is informative rather than something to average.

**Page-level behaviour.** Meta knows an ad drove a click. GA4 knows what happened on the page,
which is where §20's findings live.

**Detecting untagged traffic.** Inflated `(direct)` or `(none)` volume is the signature of lost
attribution, and it quantifies what §2's link-tracking finding costs.

## What it is not good for

- **Revenue truth.** The commerce platform is authoritative. GA4 misses purchases for the same
 consent and blocking reasons Meta does.
- **Comparing like for like with Meta.** GA4's default is data-driven attribution across all
 channels; Meta's is last-touch inside its own window with view-through. Meta claiming more than
 GA4 attributes to it is **expected**, not a defect.
- **New vs returning.** GA4's returning-user definition is device- and cookie-based, not
 customer-based. It is not the same question the commerce platform answers, and substituting it
 produces a confidently wrong new-customer CAC.

## Handling the differences

Do not reconcile GA4 to Meta by adjusting either. Report all three — Meta claim, GA4 attribution,
store banked — with the definitional differences named. §3's job is to explain the shape of the
gap, not to close it.

## Where GA4 is unavailable

Common, and survivable. §19's mid-funnel then rests on Meta's own events alone, which means the
funnel is only as good as §2's verdict — say so, and mark the section `DEGRADED` rather than
presenting a single-source funnel as corroborated.
