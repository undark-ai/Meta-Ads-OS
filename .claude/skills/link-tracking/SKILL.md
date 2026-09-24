---
name: link-tracking
description: When auditing whether a store can attribute its own paid traffic — UTM parameters on Meta destination URLs, click id capture and persistence, redirect chains, and app-browser behaviour. Use when the user asks "why doesn't GA4 show my Meta traffic," "UTM," "utm_source not set," "my paid traffic shows as direct," or when section 2 needs to establish whether paid can be separated from organic at all.
---
# Link tracking

This decides whether the store can see paid traffic at all. If it cannot, first-party data
cannot arbitrate anything, Meta's claim share becomes an upper bound rather than a measurement,
and that qualifier travels through §3, §25, §26 and the executive page.

It is cheap to fix and frequently broken, which makes it one of the highest-return findings in a
Meta audit.

## What to check

**UTM presence and consistency.** Every ad's `link_url` (or its URL parameters field) carries
source, medium, campaign, content and term. Report coverage as a share of **spend**: 90% of ads
tagged while the three biggest spenders are not is a failing account, and a count-based metric
hides it.

**Naming consistency.** `facebook` / `Facebook` / `fb` / `meta` as `utm_source` fragments the
same traffic across four rows in GA4, and every channel report built on it is wrong. Case
included — most analytics tools treat these as distinct.

**Dynamic parameters.** Meta's `{{campaign.name}}`, `{{adset.name}}`, `{{ad.name}}` and
`{{placement}}` macros populate automatically and keep tagging correct as campaigns change.
Hand-typed UTMs go stale the first time someone duplicates an ad set.

**Click id (`fbclid`) capture and persistence.** The click id must survive to the purchase event
for server-side matching to work. It commonly does not survive:

- A redirect chain that strips query parameters
- A third-party or hosted checkout on another domain
- An app that opens a new context
- A consent banner that blocks the script that would have stored it

This is the most frequent cause of low EMQ on otherwise well-implemented accounts, and it looks
like a CAPI problem rather than a link problem.

**Redirect chains.** Every hop is a chance to lose parameters and a delay before the landing-page
view fires. A large click-to-LPV gap (§19) frequently traces to here rather than to page speed.

**In-app browsers.** Meta traffic largely arrives in the Facebook or Instagram in-app browser,
which handles cookies, storage and some scripts differently from Safari or Chrome. Test the
actual arrival path in the in-app browser, not in a desktop tab — this is where "it works on my
machine" costs the most.

## How to check it

1. Pull `link_url` for every ad from `ads_get_creatives`; parse and tabulate the parameters.
2. Follow the redirect chain for the highest-spend destinations and see what survives.
3. Check GA4's paid-social channel volume against Meta's reported clicks. A large shortfall with
 healthy tagging points at the redirect or the consent layer.
4. Check the share of GA4 traffic landing in `(direct)` or `(none)` — inflated direct traffic is
 the signature of lost attribution.
5. Inspect the arrival in a real in-app browser context.

## Output

For §2 and §28: spend-weighted UTM coverage, naming inconsistencies with the traffic they
fragment, click-id persistence through to purchase, redirect-chain findings, and whether the
store can separate paid from organic — the answer §3 depends on.

Where it cannot, say so before any claim-share number is presented, not after.
