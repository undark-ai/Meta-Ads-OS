---
name: meta-post-click-funnel
description: When sizing the post-click leaks in a Meta funnel against ad-level data — landing-page view to product view to add-to-cart to checkout to purchase, per creative and per device, with each leak valued in lost orders. Use when the user asks "where am I losing people after the click," "which stage should I fix," or when a funnel finding needs a currency value rather than a rate. Bridges the creative sections to the CRO sections.
---
# Meta post-click funnel

§19 maps the whole funnel. This is the half after the click, sized per creative — which is what
makes a CRO finding attributable to the ads that are paying for it.

```
landing-page view → product view → add-to-cart → checkout → purchase
```

## Size in lost orders, not rate gaps

```
lost_orders = entrants × (account_median_rate − actual_rate) × downstream_conversion
lost_value  = lost_orders × contribution_per_order
```

Ranking on the rate gap sends a team to the worst-looking stage. Ranking on lost orders sends
them to the most expensive one, and those are rarely the same stage — the worst rate usually
sits on the lowest-traffic step.

Use `contribution_per_order` from §1, not revenue. A checkout fix worth "€40k of revenue" is
worth €24k at 60% margin, and the effort decision is made against the second number.

## Per creative, not per account

An account-level funnel is a number. A per-creative funnel is a diagnosis.

Join the funnel to the creative database and the pattern usually resolves immediately:

| Pattern | Reading |
|---|---|
| High hook rate, high CTR, **low LPV rate** | Technical. Redirect chain, page speed, in-app browser failure. Not creative |
| Good LPV, **low product-view rate** | Message match. The page is not obviously about what the ad promised |
| Good product view, **low ATC** | The product page, or the ad attracted the wrong person. Check which by looking at the angle |
| Good ATC, **low checkout** | Cart friction, or a shipping cost discovered too late |
| Good checkout, **low purchase** | Payment options, form friction, final cost shock |
| One creative leaks everywhere | The ad is attracting the wrong audience entirely. That is a §9 finding, not a CRO one |

The last row matters: a creative whose whole funnel underperforms is not a page problem. It
attracted people who were never going to buy, and the page is being blamed for the ad's
targeting.

## Device is the second cut

Mobile checkout completion is routinely far below desktop, and mobile is most Meta traffic. An
account-level checkout rate averages a mobile problem with a desktop non-problem and hides both.

Always segment by device before concluding, and report the mobile figure as the headline —
that is the one carrying the spend.

## The click-to-LPV gap

Worth calling out separately because it is invisible in Ads Manager's default view and is
frequently large.

These are people who clicked, whom the account paid for, and who never arrived. Not a
conversion problem — pure waste. Above roughly 20%, it is a technical finding, and the causes
are the redirect chain, page speed on mobile data, and in-app browser failures.

## Where the numbers come from

- **Meta**: LPV, ViewContent, AddToCart, InitiateCheckout, Purchase — subject to §2's verdict. A
  funnel built on broken events measures the events.
- **GA4**: the same steps through a different pipe. Where they disagree, that is a §3
  reconciliation item, not something to average.
- **Commerce platform**: banked orders, the denominator that makes it real.

Where §2 is `RED`, the funnel is still worth building — the *shape* survives measurement
problems better than the levels do — but mark it `DEGRADED` and do not attach currency values
to the stages with confidence.

## Output

For §19: the funnel per creative and per device, each stage's lost orders and lost contribution,
the single largest leak, and the section that owns the fix. Hand each leak to its owner —
`pdp-for-paid-social`, `mobile-checkout-cro`, `creative-to-page-continuity` — rather than
recommending "improve the landing page".
