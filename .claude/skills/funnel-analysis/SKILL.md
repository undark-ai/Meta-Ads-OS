---
name: funnel-analysis
description: When mapping and sizing the Meta post-click funnel — impression to 3-second view to click to landing-page view to product view to add-to-cart to checkout to purchase — and finding which stage is actually losing the money. Use when the user asks "where am I losing people," "funnel drop-off," "why do I get clicks but no sales," "add to cart rate is low," or "which stage should I fix first." Rank leaks by absolute lost orders, never by rate.
---
# Funnel analysis

Meta's funnel starts earlier than a search funnel does. The first two stages — did the scroll
stop, did they stay — have no Google equivalent, and they are where a Meta account most often
loses people before any page is involved.

```
impression → 3-sec view → click → landing-page view → product view → add-to-cart → checkout → purchase
 │ │ │ │ │ │ │
 delivery the hook the promise the page the product the offer the checkout
```

## Rank by absolute lost orders

A stage with a 12% conversion rate against a 20% benchmark looks worse than one at 68% against
72%. But if the second stage carries ten times the traffic, fixing it is worth several times
more.

```
lost_orders = entrants × (benchmark_rate − actual_rate) × downstream_conversion
```

Always rank on that, never on the rate gap. Ranking on rate sends teams to fix the worst-looking
stage rather than the most expensive one, and the worst-looking stage is usually the one with
the least traffic.

## What each drop actually means

| Drop | Cause | Owns it |
|---|---|---|
| Impression → 3-sec | The hook, thumbnail or first frame. Nothing after it matters yet | §9 creative |
| 3-sec → click | The ad earns attention but does not create desire, or the CTA is unclear | §9 creative |
| Click → landing-page view | **Not a creative problem.** Page speed, redirects, broken links, app-browser failures. A gap above ~20% is a technical finding | §20 |
| LPV → product view | Message match. The page is not obviously about what the ad promised | §20, `creative-to-page-continuity` |
| Product view → add-to-cart | Product page: price, photography, reviews, variants, shipping, trust | §20 `pdp-for-paid-social` |
| ATC → checkout | Cart friction, unexpected shipping cost, no express checkout | §20 `mobile-checkout-cro` |
| Checkout → purchase | Payment options, form friction, forced account creation, final cost shock | §20 `mobile-checkout-cro` |

The click-to-LPV gap deserves specific attention because it is invisible in Ads Manager's default
view and is frequently large. People who clicked, paid for, and never arrived are pure waste, and
the fix is technical rather than creative.

## Starting ranges, where the account has no history yet

Use the account's **own medians** as the primary comparison — these are a starting point for a new
account, not targets, and an account's own 90-day history replaces them the moment it exists.

| Stage | Formula | Starting range |
|---|---|---|
| Impression → click | clicks / impressions | 1–3% Feed · 0.5–1.5% Stories and Reels |
| Click → landing-page view | LPV / outbound clicks | 40–70% — below this is technical, not creative |
| LPV → product view | ViewContent / LPV | |
| Product view → add to cart | ATC / ViewContent | 8–20% |
| ATC → checkout | InitiateCheckout / ATC | 40–60% |
| Checkout → purchase | Purchase / InitiateCheckout | 30–60% |
| Click → purchase overall | Purchase / clicks | 1–5% |

Quoting one of these as a target against an account whose own median is materially different is
worse than quoting nothing: it manufactures a finding out of a category difference.

## Segment before concluding

An account-level funnel hides everything useful. The same funnel is a different shape by:

- **Creative** — the whole point. A high-hook, low-ATC ad attracts the wrong people
- **Product** — hero product versus long tail
- **Device** — mobile checkout completion is routinely far below desktop, and mobile is most of
 the traffic
- **Placement** — Reels traffic converts differently from Feed traffic
- **Audience** — retargeting funnels are compressed and should be

Segment by at least creative and device before drawing a conclusion. An account-level ATC rate
is a number, not a finding.

## Benchmarks

Use the account's **own medians** as the primary comparison. "This ad's ATC rate is 40% below
the account median" is actionable; "this ad's ATC rate is 2.1%" is not.

External benchmarks are context only, and vertical-specific. §11's industry benchmark call gives
CPM, CTR and CPA context; nothing gives a reliable external add-to-cart benchmark, and quoting
one from memory is worse than using the account's own distribution.

## Data sources

- **Meta**: impression, 3-sec, click, LPV, ViewContent, ATC, InitiateCheckout, Purchase —
 subject to the pixel's own quality (§2). A funnel built on broken events measures the events
 rather than the funnel.
- **GA4**: the mid-funnel, independently. Where GA4 and Meta disagree on the same step, that is a
 §3 reconciliation item, not something to average.
- **Commerce platform**: banked orders. The denominator that makes the rest real.
- **Browser**: what the stage actually looks like. A rate is a symptom; the page is the cause.

## Run the funnel for every paid channel, not just Meta

A single-channel funnel cannot tell **"our checkout is broken"** from **"Meta traffic is worse
qualified than search traffic."** Those have opposite fixes — one is a §20 site job, the other is a
§13 targeting and creative job — and the only way to separate them is to put the channels side by
side on the same stages, over the same window, from the same source.

GA4 is that source, because it measures every channel the same way. Meta's own numbers cannot be
compared to Google's own numbers; each platform counts its own conversions on its own window.

| Stage | GA4 field | Read across channels |
|---|---|---|
| Sessions | `sessions` | traffic volume by channel |
| Add to cart | `addToCarts` | first real intent signal |
| Checkout | `checkouts` | commitment |
| Purchase | `transactions` | the outcome |
| Revenue | `purchaseRevenue` | value per session, which is the honest comparison |

Split by `sessionDefaultChannelGroup` for the channel view, and by `sessionSourceMedium` when you
need placement-level detail — Meta's placements arrive as distinct source/medium pairs
(`Instagram_Reels / paid`, `Facebook_Mobile_Feed / paid`), which makes GA4 an **independent check
on §18's placement economics** rather than a repeat of it.

**Pair it with each platform's spend** so the comparison ends in cost per outcome rather than rate:
Meta from `ads_get_ad_entities`, Google Ads from `metrics.cost_micros` via
`GOOGLEADS_SEARCH_STREAM_GAQL`. A channel converting at half the rate for a third of the cost per
session is not the problem it looks like.

### What the cross-channel read tells you

| Pattern | Reading |
|---|---|
| One channel's session→ATC far below the others | Traffic quality or message match, not the site. Owned by that channel |
| **All** channels drop at the same stage | The site. §20, and no amount of creative work fixes it |
| Paid social ATC healthy but checkout worse than search | Colder, less decided traffic arriving with the same friction. Both a §20 and a §14 finding |
| Paid social trailing "search" on any measure | **Check the split first.** Against blended search this is almost always brand contamination rather than a real gap |
| A channel with sessions and near-zero transactions | Check it is real traffic before treating it as a funnel problem |

Search traffic arrives with intent and paid-social traffic arrives interrupted, so paid social
converting below search is normal, not a defect. **Say what the expected gap is before calling one
a problem** — the finding is a channel that falls outside its own history, not one that trails
search.

### Always separate brand from generic before comparing search to paid social

**This is not optional and there is no window in which the blended figure is the right one.**

Brand search harvests people who already typed the company's name. Much of that demand was created
by paid social, so a blended search figure is partly Meta's own work, priced as if it were Google's
and then used as the stick to beat Meta with. Comparing blended search to paid social does not
overstate search slightly; it **inverts the ranking**, because brand carries most of the
transactions on a fraction of the spend.

Split at least three ways and never fewer:

| Segment | What it is | Compare to paid social? |
|---|---|---|
| **Brand** | Queries containing the brand name or a close variant | **No.** Report separately as demand harvesting |
| **Generic / non-brand** | Category and problem queries | **Yes — this is the only valid comparison** |
| **Shopping / PMax / cross-network** | Mixed intent, and it is not search | No. Its own row |
| Competitor / conquest | Rival brand terms | Its own row |

How to split, in order of preference: the account's own campaign naming where it encodes brand
versus non-brand; a search-term-level brand-regex where term data is reachable; GA4
`sessionCampaignName` joined to the platform's per-campaign spend. **Never split by
`sessionDefaultChannelGroup` alone** — GA4's "Paid Search" is brand and generic mixed together, and
`Cross-network` quietly holds PMax, so a channel-group comparison is the blended error wearing a
different label.

Two traps that follow from it:

- **Attribute spend to the same segment as the sessions.** PMax spend belongs in cross-network, not
  in search. Putting it in search understates search CAC and flatters the comparison twice over.
- **Use one source's transactions for both sides.** Each platform counts its own conversions on its
  own window and both over-claim — on one live account Meta claimed 2.09× GA4's transactions and
  Google search 2.21×. Take both numerators from GA4 or the comparison is measuring the platforms'
  reporting habits rather than their performance.

A brand line converting at three or four times the site average with a CAC in the low tens is
normal and is **not** evidence that search outperforms social. It is evidence that people who
already know the brand buy readily, which is a §26 incrementality observation, not a §29 budget
one.

## Show it, don't only tabulate it

A funnel is a shape. A table of eight percentages hides the shape; a chart makes the cliff obvious
to someone who will not read the table.

**§19's output must include rendered charts, not only figures:**

- **A funnel chart per channel** — absolute counts, bar width proportional to volume, so a stage
  carrying ten times the traffic looks ten times as wide. This is the same argument as ranking by
  absolute lost orders, made visually.
- **A stage-by-stage drop-off comparison across channels** — one grouped bar or small-multiple per
  stage, channels side by side, so the stage where they diverge is visible at a glance.
- **Lost orders per stage**, ranked, in the same currency as everything else in the run.

Build them with `dataviz` and render inline in the audit artifact — SVG or Canvas, no external
libraries, working in both light and dark themes. Label every axis with its unit and state the
window and source under each chart, exactly as the tables do. A chart carrying no window is the
same defect as a dataset carrying no attribution setting.

**Never chart a rate without its denominator beside it.** A 68% stage on 40 sessions and a 68%
stage on 40,000 draw identically and mean nothing alike.

**The brand/generic split applies to every chart, not only to the tables.** A blended "Paid Search"
bar is not a channel — it is two behaviours averaged into a number that describes neither, and it
is the more dangerous half of the output because a reader takes the shape from the chart and never
reaches the table. Splitting the table and captioning the chart with a warning is **not** a fix:
it leaves the wrong bar on the page and asks the reader to correct for it.

This happened on a live run. The table was split and the chart was not; the caption said the bar
was "mostly brand", and the bar still showed paid search converting at 38.8% against paid social's
14.5% when the comparable segment converted at 10.2%. If a segment is not fit to appear in the
table, it is not fit to appear as a bar.

The same rule covers PMax. It is not search, it does not belong in a search bar, and GA4 files it
under `Cross-network` where a channel-group chart will silently hide it.

## Output

For §19: the funnel by creative and by device, **the same funnel by channel from GA4**, each
stage's absolute lost orders, the single largest leak with its currency value, the charts above,
and the section that owns the fix. Where the leak is post-click, the finding belongs to §20 even
though it was found here — and say so, rather than recommending new creative for a checkout
problem. Where the leak appears in **every** channel, say that too: it is the strongest available
evidence that the site rather than the traffic is the constraint.
