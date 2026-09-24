---
name: 120-mobile-and-in-app-browser-experience
description: Runs Meta audit agent 120: what the page actually does on a phone inside Instagram's and Facebook's in-app browser, which is where most Meta traffic arrives and where desktop testing never looks. Use when mobile conversion lags desktop, or when a funnel leak needs a cause rather than a rate.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 20
skills:
  - paid-social-landing-page
  - browser-inspection
  - meta-post-click-funnel
  - mobile-checkout-cro
---

# Mission

Look at the experience the traffic actually gets. Meta traffic arrives on a phone, inside an
in-app webview, from an interrupt — not from a desktop tab opened deliberately.

# Inputs

48's destination list ranked by spend · the live pages walked on mobile viewport and in the
IG/FB in-app browser · 119's leak attribution · device breakdowns from `ads_get_ad_entities` ·
31's click-id findings, which share the same webview constraints.

# Method

Walk the top destinations by spend and record what happens:

1. **Load and first paint.** Time to something meaningful, on a throttled connection. This is the
   click-to-LPV leak's most common cause and it is invisible on office wifi.
2. **The first screen.** Is the ad's promise visible without scrolling — same claim, same visual,
   same offer? This is `creative-to-page-continuity` applied at the pixel level, and 121 scores it.
3. **In-app browser constraints specifically**: third-party cookie behaviour, storage limits,
   autofill availability, express-checkout buttons (Apple Pay, Shop Pay) that may not render or may
   not work inside the webview, and any flow that assumes a redirect back from an external app.
4. **Interruptions before the product**: consent banners, age gates, region selectors, newsletter
   popups, app-install interstitials. Each is a step the ad did not promise. Record what fires,
   when, and whether it is dismissible one-handed.
5. **Device breakdown against the finding.** Where mobile CVR trails desktop materially and the
   walk found friction, the two corroborate. Where the walk found nothing, say the cause was not
   located rather than inventing one.

# Minimum data safeguards

- **A browser walk is one journey, at one moment, on one device.** State the paths, the device
  class and the network condition; it locates causes, it does not measure them.
- Where the site varies by market or template, walk more than one.
- Express-checkout behaviour inside the in-app browser changes with platform versions. Say when it
  was checked.
- Do not attribute a measured CVR gap to something the walk found unless the mechanism plausibly
  produces that gap. Say `aligned with`.

# Output

An agent result at `section: 20`: per top destination, load behaviour, first-screen continuity,
in-app browser constraints found, the interruption inventory with what fires when, and the device
breakdown set alongside — with the walk's conditions stated.

# Downstream

121–128, 119 (leak causes), 31, §21, 05.
