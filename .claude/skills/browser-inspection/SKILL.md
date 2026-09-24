---
name: browser-inspection
description: When inspecting the rendered post-click experience that Meta traffic actually lands on — landing pages, product pages, cart and checkout, on mobile and in the in-app browser. Use when a funnel leak needs a cause rather than a rate, when auditing message match, or when the user asks "what's wrong with my landing page." A conversion rate is a symptom; the page is where the cause is.
---
# Browser inspection

A conversion rate tells you a stage is losing people. Only the page tells you why.

## Inspect the real arrival path

Meta traffic does not arrive the way an audit usually looks at a site.

- **Mobile first, and mostly.** Inspect at a phone viewport before a desktop one. Most Meta
 traffic is mobile, and most audits are written on desktop.
- **The in-app browser.** Traffic arrives in the Facebook or Instagram in-app browser, which
 handles cookies, storage, autofill and some scripts differently. Things that work in Safari
 fail there, silently, and it is where "it works on my machine" costs the most.
- **Through the real link.** Follow the ad's actual `link_url`, including its redirect chain and
 its UTM parameters, not the clean homepage URL. The redirect chain is itself a finding
 (`link-tracking`).
- **Cold.** Clear state. A returning visitor with a cart and a dismissed popup sees a different
 page from the one the ad is buying.

## What to inspect, and for what

| Page | Looking for |
|---|---|
| Landing page | Does it repeat the ad's promise — the claim, the visual, the offer — above the fold? |
| Product page | Price clarity, photography, reviews placement, variant selection, shipping and returns visibility, trust signals |
| Cart | Unexpected costs, express checkout availability, edit friction |
| Checkout | Form length, forced account creation, payment options, final cost shock |

Inspect the **highest-spend** destinations, not the homepage. An audit of a page that receives
2% of paid traffic is a well-evidenced irrelevance.

## Message match is the first check

The ad made a promise. Open the page and ask whether a stranger would recognise it as the same
thing:

- Is the ad's core claim repeated in the first screen, in similar words?
- Is the ad's hero visual recognisable on the page?
- Is the offer the ad named present, at the price the ad named?
- Does the page answer the objection the ad raised?

Score it (`creative-to-page-continuity`). A break here explains a large LPV-to-ATC gap better
than anything on the page's own merits, and it is fixable without redesigning anything.

## Performance

Measure what a phone on a mediocre connection experiences, not what a lab score reports. Time to
first meaningful paint, and time until the page is interactive. A large click-to-landing-page-view
gap in §19 is usually here or in the redirect chain, and it is pure waste — clicks paid for and
never delivered.

## What to record

Evidence, not impressions. Screenshots at the viewport inspected, the URL and its redirect
chain, the device and browser context, and the specific element at fault. "The page is cluttered"
is not a finding; "the ad's €20-off claim does not appear anywhere above the fold on mobile;
first mention is at 1,400px scroll depth" is.

## Where a browser is unavailable

Fall back to Meta's own Conversion Rate Ranking as a partial signal (`delivery-diagnostics`) —
it is Meta saying that people who click do not convert relative to competitors, which locates
the problem post-click without describing it. Mark §20 `DEGRADED`, and say what a browser pass
would have added.
