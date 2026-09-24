---
name: paid-social-landing-page
description: When auditing or designing the landing page that Meta traffic actually arrives on — cold, interrupted, mobile, in an in-app browser. Use when the user asks "why doesn't my landing page convert," "landing page for Facebook ads," "paid social landing page," or when a funnel leak sits between landing-page view and product view. For whether the page keeps the ad's promise, see creative-to-page-continuity. For product pages specifically, see pdp-for-paid-social.
---
# Paid-social landing pages

The page a Meta visitor lands on is not the page a search visitor lands on, even when it is the
same URL.

| | Search arrival | Paid social arrival |
|---|---|---|
| Intent | Typed a query. Already looking | Was scrolling. Was interrupted |
| Knowledge | Knows what they want | Knows only what the ad just told them |
| Device | Mixed | Overwhelmingly mobile |
| Browser | Safari, Chrome | The Facebook or Instagram **in-app browser** |
| Patience | Will scroll and compare | Will leave |

Designing for the first and buying traffic for the second is the most common structural mistake
in D2C paid social, and it shows up as a conversion-rate problem that no amount of creative
testing fixes.

## The in-app browser

Meta traffic largely arrives in the Facebook or Instagram in-app browser, which is not the
device's default browser and does not behave like it.

- Cookie and storage behaviour differs, which breaks click-id persistence (`link-tracking`) and
  therefore EMQ.
- Autofill is weaker or absent, so every form field costs more than it does elsewhere.
- Some payment sheets and third-party scripts behave differently or fail silently.
- The viewport is shorter than the phone's — the in-app chrome takes real estate — so "above the
  fold" is less than a designer's mobile mock assumes.

**Test in the real in-app browser.** This is where "it works on my machine" costs the most, and
a desktop audit will never find it.

## The first screen

At a phone viewport, inside the in-app chrome, cold. What must be there:

1. **The ad's claim**, in similar words (`creative-to-page-continuity`).
2. **What the product is**, unambiguously. A visitor who saw one 6-second video does not know.
3. **The offer**, if the ad named one, at the price the ad named.
4. **One primary action.** Two competing CTAs halve the signal.
5. **A reason to believe** — one, not a wall. A review count, a guarantee, a recognisable name.

Everything else is below the fold and that is fine. The first screen exists to confirm the
visitor is in the right place, not to sell.

## Speed is a conversion feature here

A large click-to-landing-page-view gap in §19 is people who paid to arrive and never did.
That is pure waste, and it usually traces to the redirect chain or to a page that takes too long
on a mid-tier phone over mobile data.

Measure what a phone on a mediocre connection experiences, not a lab score. And check the
redirect chain — every hop is a delay and a chance to lose UTM parameters.

## Objection handling in order

Paid-social visitors carry objections search visitors have already resolved. The page answers
them in roughly the order they arise:

1. *What is this?* — first screen
2. *Is it for me?* — the situation the ad named, restated
3. *Does it work?* — proof, ideally the proof type the ad used
4. *Why should I believe you?* — reviews, press, guarantee
5. *What does it cost, really?* — price, shipping, returns. **Before** checkout, not at it
6. *What if I'm wrong?* — returns policy, guarantee

Shipping cost discovered at checkout is the single most common cart-abandonment cause, and it is
a landing-page failure as much as a checkout one.

## What to check on an audit

- Rendered at a phone viewport, in the in-app browser, cold, through the ad's real link
- The first screen against the highest-spend ads' promises
- Time to interactive on mobile data; the redirect chain
- Whether one page is serving ads making materially different promises
- Whether awareness level and destination match
- Popup timing — an interstitial firing before the visitor has read the claim converts an
  interruption into an exit (`popups`)

## What not to recommend

A landing page per ad. Most accounts cannot maintain them, and a stale bespoke page is worse
than a good shared one. The useful finding is usually **which promise the shared page should
keep** — the one the highest-spend ads make — and which ads should be pointed somewhere else.
