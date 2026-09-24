---
name: 31-click-id-persistence
description: Runs Meta audit agent 31: whether fbclid, fbc and fbp survive the journey from ad click to server-side purchase event. The most common single cause of low EMQ on e-commerce accounts. Use when fbc coverage is low, checkout is multi-step or on another domain, or the user asks why server events cannot be matched to ads.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 2
skills:
  - capi-and-emq
  - meta-third-party-conversion-tracking
  - browser-inspection
  - link-tracking
---

# Mission

Follow the click id from the ad to the purchase event and find where it is dropped.

This is the most common finding in the whole match-quality layer: `fbc` is not persisted through a
multi-step or third-party checkout, so server events arrive without the click id and cannot be
matched to the ad that drove them. The ads still work; the account just cannot see that they did.

# Inputs

29's `fbc` and `fbp` coverage · the live journey, walked in a browser: ad link → landing page →
cart → checkout → confirmation, on mobile and in the in-app browser · `link_url` and its
parameters from `creative-database.csv` · 23's implementation route · 33 where checkout is
off-domain.

# Method

Trace the chain, and name the step where it breaks:

| Step | What must survive |
|---|---|
| Ad link | `fbclid` appended by Meta — and preserved by any redirect or link shortener in the path |
| Landing | `fbclid` read and written to the `_fbc` cookie; `_fbp` set |
| Navigation | Both cookies surviving domain changes, subdomains and app-to-web transitions |
| Checkout | Cookies readable at the point the order is created |
| Server event | `fbc` and `fbp` read from the cookie and included in the payload |

Common breaks, in rough order of frequency: a redirect or shortener stripping `fbclid` before the
landing page ever sees it; checkout on a different domain where the cookie is not readable; a
server integration that never reads the cookies at all; and a single-page app that sets the cookie
after the first navigation, missing users who bounce straight to a product page.

**Walk it in the in-app browser.** Instagram and Facebook open links in their own webview, and
cookie and storage behaviour there differs from Safari or Chrome — a chain that works in a desktop
test can break for the traffic that actually matters.

# Minimum data safeguards

- A browser walk is one journey at one moment. State the paths tested and the devices, and where
  the site varies by market or template, test more than one.
- `fbc` is expected to be low on view-through and organic-assisted events by construction. Judge
  coverage on **click-through** events, per the band in `capi-and-emq`, or the figure will look
  broken on a working account.
- Where a third party owns checkout, the fix may be theirs and not the account's. Say who owns it
  — a recommendation addressed to the wrong party does not get done.

# Output

An agent result at `section: 2`: the traced chain with the breaking step named, the paths and
devices tested, the in-app browser result, `fbc` coverage on click-through events, and the owner
of each fix.

# Downstream

29 (the largest single EMQ cause), 23, 33, 35 (link parameters and redirects), 36, §25.
