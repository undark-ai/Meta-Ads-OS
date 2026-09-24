---
name: 28-consent-and-signal-loss
description: Runs Meta audit agent 28: how much event signal never fires at all — consent banners, tracking prevention, blockers and platform restrictions. Sizes the traffic Meta cannot see, which is directional and large rather than random. Use when the user asks about consent mode, GDPR impact, ad blockers, iOS, or why the pixel undercounts.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 2
skills:
  - capi-and-emq
  - ecommerce-measurement
  - browser-inspection
  - ga4-extraction
---

# Mission

Size the events that never happen, so §3's shortfall is not mistaken for absent demand and §2's
verdict accounts for a ceiling nobody can fix by configuration.

# Inputs

The live site in a browser: consent banner behaviour before and after choice, which tags fire in
each state · `ads_get_dataset_stats` browser-versus-server volumes from 21 ·
store sessions and orders as the denominator of truth · GA4's own consent-affected volumes where
present · the account's markets from 16, because consent regimes differ by market.

# Method

1. **Inspect the banner.** Does the pixel fire before consent, after consent only, or regardless?
   Each is a different legal and measurement position, and the audit reports what it observes
   rather than advising on the law.
2. **Consent rate.** Where the platform reports it, take it; otherwise bound it by comparing
   browser event volume against store sessions.
3. **Browser-side loss.** Compare browser `Purchase` volume against store orders. The shortfall
   is consent plus tracking prevention plus blockers combined — a single figure, not separable
   without instrumentation the audit does not have. Report it as combined, and say so.
4. **What server-side recovers.** The whole point of CAPI is that a server event fires regardless
   of the browser. Where browser loss is large and the server share is also low, the account is
   losing signal it has already paid to be able to recover, and that is 23's fix with this
   agent's number attached.
5. Split by market where consent regimes differ materially. An EU-heavy account and a US-heavy
   one have structurally different ceilings, and one account-level figure describes neither.

# Minimum data safeguards

- **This is a bound, not a measurement.** Signal that never fired leaves no record; the shortfall
  against store orders is the best available estimate and it bundles several causes. Say so
  wherever the figure appears.
- Store sessions and browser events count different things. Use the ratio's *movement* and the
  purchase-level comparison rather than treating a session-to-event ratio as a consent rate.
- Do not attribute the whole shortfall to consent. Direct, organic and email traffic is in store
  orders and was never Meta's to see.
- Browser inspection is a point-in-time read of one journey. State that, and check more than one
  market where the site varies.

# Output

An agent result at `section: 2`: observed banner behaviour, the consent rate or its bound, the
combined browser-side loss against store orders, what server-side currently recovers, and the
split by market.

# Downstream

41 (the "Meta below store orders" diagnosis row), 23 (the recovery case), 36 — this is a ceiling
on the verdict, not a defect to be fixed to zero — and 42.
