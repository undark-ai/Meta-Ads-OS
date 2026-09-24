---
name: audit-preflight
description: Runs the two checks that must happen before any Meta audit, task or skill starts — whether the business-context document exists and is current, and whether the connectors that particular job needs are actually connected — then offers the user the chance to fix either before work begins rather than discovering the gap in the findings. Use at the start of every full audit, and in reduced form before any single task or skill. Offers and records; never blocks.
---
# Audit preflight

Two questions, asked **before** work starts, never after:

1. **Do we know the business?** Does `.agents/product-marketing.md` exist, and is it current?
2. **Can we see the data?** Are the connectors *this particular job* needs actually connected?

Both have the same failure mode. Discovered mid-run they become a caveat in the report; asked up
front they become a decision the user gets to make. A caveat costs the user a re-run.

**Preflight offers, it never blocks.** Every question below has "proceed as-is" as a valid answer,
and choosing it is recorded rather than argued with. The one thing preflight must never do is skip
the question and quietly produce a degraded audit.

## Check 1 — business context

```
.agents/product-marketing.md
```

| State | What to do |
|---|---|
| **Missing** | Say it does not exist and what that costs — §1 names the primary goal from account behaviour alone, §9's angle analysis has no persona library to resolve against, §21's offer audit has no margin intent to compare realised discounting against. Ask: create it now, or run without it? |
| **Present, ≤90 days old** | Use it. Say when it was last updated. No question needed. |
| **Present, >90 days old** | Say how old it is and ask: refresh it now, or run against it as-is? |
| **Present but contradicted** | If a prior run found declared context disagreeing with measured data, put that specific disagreement in the question — it is the strongest argument for a refresh. |

Read the file's modification time from the filesystem, and prefer an explicit `last_updated` field
inside the document where one exists — a file touched by a git checkout is not a file whose
contents were reviewed.

**Age is not the only trigger.** Any of these invalidates the document regardless of date, and is
worth naming in the question when it is visible in the data: a new product line, a price change, a
repositioning, a new market or country, a change of primary customer, or a creative library that
has moved to angles the document never mentions. A six-month-old document that still matches the
measured data is fine; a three-week-old one that does not is not.

### If the user chooses to create or refresh

1. **Run `feel-brand-strategy`** to establish the brand and positioning foundations — Foundation,
   Environment, Expression, Launch. It is **not vendored into this repository**; it ships as a
   plugin skill. If it is not available in the session, say so and fall back to `product-marketing`
   alone rather than silently skipping the step.
2. **Research before interrogating.** Read the live site — homepage, product pages, about, pricing,
   shipping and returns — and whatever public presence exists: search results, Instagram and
   TikTok profiles, review sites, competitor comparisons. Pull the Meta Ad Library
   (`ad-library-extraction`) for what the brand and its category actually run. Then read whatever
   measured data is already reachable: revenue by product, AOV, new-vs-returning split, the
   account's own top-spending angles.
3. **Ask only what research could not answer.** Arrive with a draft and a short list of genuine
   gaps, not a blank questionnaire. Asking a client what they sell, when the site says so plainly,
   spends their patience on something you could have read. Good remaining questions are usually
   margin intent, the promotional calendar, which products are strategic rather than merely
   profitable, and who they think the customer is — the last of which §12 will then test.
4. **Write it up**, then hand off to `product-marketing` for the canonical shape.

### The evidence rule carries through

Everything in that document is **client-declared, not measured**. A marketing-layer skill's output
is never evidence for a quantified finding. Refreshing the document raises its quality; it never
promotes it to evidence, and §12 still reconciles who the client says buys against who measurably
does.

## Check 2 — connectors

Run discovery first (`mcp-discovery`) so the question is grounded in what is actually connected
rather than in what you assume. **Enumerate the gateway's connected-app list explicitly, and never
carry a previous run's `UNAVAILABLE` into this one** — connectors get authorised between runs, and
preflight is exactly where that should be found. Asking a user to connect something they connected
last week is a worse failure than not asking.

### For a full e-commerce Meta audit

| Connector | Standing | What is lost without it |
|---|---|---|
| **Meta Ads** | Required | There is no audit |
| **Commerce platform** — Shopify, WooCommerce | Required | Revenue truth. Every ROAS stays a platform claim; §3 reconciliation and all margin collapse |
| **Composio** or equivalent gateway | **Strongly recommended** | Rung 2 of the ladder, and the usual route to everything below when no native server exists |
| **GA4** or another first-party analytics tool | Strongly recommended | §19's funnel mid-stages, and the only neutral arbiter in §3 between two platforms that both over-claim |
| **Google Ads** — and any other paid channel | **Strongly recommended in practice** | Blended MER needs *total* ad spend, so a Meta-only figure is wrong rather than partial. Two platforms routinely claim the same order, which is invisible with one connected |
| **Google Search Console** | Recommended | §26 incrementality — brand impressions and clicks are how you separate demand created from demand harvested, and a Meta campaign that lifts brand search is doing something reported ROAS cannot see |
| **Google Merchant Center** | Required *if* Shopping or PMax runs alongside | §22 SKU economics across channels, and the feed problems that also break Meta's catalog |
| **Meta catalog** | Required *if* catalog, DPA or Advantage+ Shopping runs | §16 feed quality, disapprovals, product diagnostics |
| **Semrush** or equivalent | Optional | §27 competitive context. Third-party estimates only — never revenue truth |
| **Email / CRM** — Klaviyo, Attentive, Flashy | Recommended | §24's LTV loop: whether first-party value flows *back* into Meta as value-based audiences and suppression |

### Also worth asking for, and usually forgotten

| Connector | Why it earns its place |
|---|---|
| **Google Tag Manager** | §2 reads the actual tag and CAPI configuration instead of inferring it from the rendered page |
| **Payment or finance data** — Stripe, the store's payments, bank | Reconciles platform revenue against *settled* money, the only fully independent check |
| **BigQuery**, where a GA4 raw export exists | User-level joins — the only route to a true paid-traffic funnel rather than a modelled one |
| **The customer-list sources behind value-based audiences** | §24 cannot tell a stale list from an absent one without them |

Adjust the list to the account. No catalog campaigns means Meta catalog is not required; a
subscription business substitutes its billing system for parts of the commerce platform.

### How to ask

**One batched question, not a sequence of prompts.** For each gap give the connector, what it
costs, and how much work connecting is. Then offer the three real options: connect some now,
proceed without them, or proceed and accept the affected sections closing `BLOCKED`.

Never present a missing connector as fatal while the ladder has rungs left — check the gateway and
the commerce-platform-as-proxy routes **before** asking the user for anything.

## Scaling preflight to a single task

A full audit needs both checks in full. A single task or skill needs **only the parts that bear on
it**, and asking for more is friction the user did not agree to.

| Task or skill | Context check | Connectors to ask about |
|---|---|---|
| Creative fatigue, angle analysis | **Yes — this is what it is for** | Meta Ads |
| Ad copy review or generation | **Yes — positioning and voice are the input** | Meta Ads |
| Landing page / CRO | Yes — positioning drives message match | Meta Ads, GA4, browser |
| Catalog / feed health | Skip | Meta Ads, Meta catalog, commerce platform |
| Budget reallocation | Yes — margin and priorities | Meta Ads, commerce platform |
| Reconciliation / attribution | Skip | Meta Ads, commerce platform, GA4, every other paid channel |
| Incrementality | Yes | Meta Ads, commerce platform, GSC, other paid channels |
| Audience strategy | Yes — who the client thinks buys is the hypothesis | Meta Ads, CRM |
| Competitive analysis | Yes — positioning is the comparison basis | Semrush, Ad Library, browser |
| Cross-channel funnel | Skip | GA4, Meta Ads, Google Ads, commerce platform |

Two rules for the reduced form. If the task needs **no** connector the session lacks and the
context document is current, **ask nothing and start** — a preflight that interrupts a two-minute
task has cost more than it saved. And where one missing input would change the answer rather than
merely narrow it, ask about that one thing specifically rather than presenting the whole matrix.

## Confirming the account

Two checks that save a wasted run:

1. **`is_ads_mcp_enabled: false` beats `is_queryable: true`.** An account can report queryable and
   still be un-queryable, and the failure otherwise surfaces deep into the sweep.
2. **Confirm there is spend in the intended window.** Pull account-level monthly increments over a
   wide range. A dormant account is a preflight answer, not a §5 mystery.

If the user explicitly wants a legacy account audited, do it — and flag that current decisions
should rest on the active one.

## Record it

Write `audits/<run-id>/preflight.md`: the context document's state and the user's decision, the
connector matrix with each one's status and ladder rung, what the user chose to connect, and what
they chose to proceed without. When a section later closes `BLOCKED` or `DEGRADED`, this is the
file that shows it was a known, accepted trade rather than an oversight.
