---
name: modeled-conversions
description: When separating what Meta observed from what Meta modelled or estimated — modelled conversions, view-through attribution, Aggregated Event Measurement, ATT signal loss, and the attribution-window default. Use when the user asks "why doesn't Meta match Shopify," "what are modeled conversions," "should I use view-through," "7-day click or 1-day," "AEM," "iOS 14 impact," or whenever a Meta-reported figure is about to be used in an economic conclusion. This is the skill that decides whether a number may carry the OBSERVED evidence class.
---
# Modelled conversions

Meta reports one number where there are three: what it saw, what it inferred, and what it
estimated statistically. Ads Manager does not separate them by default, so every economic
conclusion built on the headline figure inherits an unknown amount of modelling.

The rule this exists to enforce: **a modelled or estimated value never carries the `OBSERVED`
evidence class.** It is `PLATFORM_STATED` or `INFERRED`, and the modelled share travels with it
wherever it appears.

## What is actually in the number

| Component | What it is | Trustworthy for |
|---|---|---|
| **Observed, deduplicated** | A pixel or CAPI event matched to a click | Everything |
| **Observed, view-through** | A purchase after an impression, no click | Nothing on its own — see below |
| **Modelled** | Meta's statistical estimate of conversions it could not observe, mostly from ATT-restricted iOS traffic | Direction, not level |
| **AEM-restricted** | iOS web events, limited to 8 prioritised events, aggregated and delayed | Directional; not user-level |

The proportions are account-specific and move. **Find them for this account**; never assume an
industry figure.

## Establishing the modelled share

Not directly exposed as one field. Triangulate:

1. `ads_get_dataset_quality` — event match quality, match-key coverage and event freshness. Low
 EMQ means more modelling, because fewer events could be matched.
2. Compare **1-day-click** against the account's default window. The gap is where the
 attribution assumptions live.
3. Compare Meta-claimed purchases against banked orders (§3). Meta above store orders is
 double-counting or over-modelling; Meta far below with healthy first-party tracking is
 under-attribution.
4. Segment by platform where available. iOS-heavy delivery carries more modelling than
 Android-heavy or desktop.

If the share genuinely cannot be established, write `UNKNOWN`. **Never write 0.** A zero is a
claim that the number is fully observed, and that claim is almost never true.

## View-through

A view-through conversion is a purchase by someone who saw the ad and did not click. On
prospecting it may be real influence. On retargeting it is frequently a person who was going to
buy anyway and happened to be served an impression on the way.

Rules:

- Report click-through and view-through **separately**, always. A blended ROAS that silently
 includes view-through is not comparable to anything.
- Retargeting ROAS with view-through included is the least reliable number in the account, and
 it is the one most often used to justify retargeting budget.
- View-through is an **incrementality** question, and §26 is where it gets answered. Until a
 holdout or lift test exists, view-through-inclusive claims are `INFERRED` at best.

## The attribution window

Meta's default is **7-day click, 1-day view**. That default is a choice, and it is not neutral:

- A longer window claims more purchases, so ROAS rises without anything improving.
- Comparing periods across a window change is invalid. Check `ads_account_get_activity_logs`
 for when the setting changed before comparing anything across it.
- A 7-day-click figure and a 7-day-click-1-day-view figure are different measurements of
 different things. **One window per run**, stated in `scope.md` and in every dataset header.
- Match the window to the actual purchase cycle. A €40 impulse product does not need 7 days; a
 €900 considered purchase needs more than 7 and will be systematically under-credited.

## Aggregated Event Measurement

For iOS web traffic, AEM limits the account to **8 prioritised conversion events**, aggregates
them, and delays reporting. Consequences the audit must check:

- **Event priority order matters.** Purchase must be priority 1. An account with `Purchase`
 ranked below `AddToCart` is optimising toward the wrong event for a meaningful share of
 traffic. This is a common, high-impact, entirely fixable finding.
- Only the highest-priority event in a session is counted for those users, so lower-priority
 events are under-reported by design — not broken.
- Domain verification is a prerequisite. Unverified domain means no event configuration at all.
- Value optimisation on iOS needs value sets configured; without them, value-based bidding
 degrades quietly.

## ATT

Since iOS 14.5, opted-out users are not individually trackable. The share of an account's
traffic affected depends on its audience, so **measure it, do not assume it**.

Practical effects: smaller and slower-building custom audiences; retargeting pools that
under-represent iOS users; longer feedback loops so learning phase takes longer; and modelled
purchases filling the gap in reporting.

CAPI with strong match keys is the mitigation — it restores server-side signal for events the
browser cannot report. `capi-and-emq` covers implementation; the audit's job here is to
establish how much signal is actually reaching Meta and what that does to the confidence on
everything downstream.

## How this changes the audit

1. **Every economic finding states its measurement basis** — window, modelled share,
 view-through included or not, reconciled against first-party or not. This is a required
 property of the agent contract, not a footnote.
2. **§3 publishes the modelled share** as one of its five headline measures.
3. **A creative ranking where modelled share varies materially across ads is not a ranking of
 creative.** Say so before presenting it.
4. **A `RED` measurement verdict** follows from a high modelled share plus an unreconciled gap.
 It orders the audit — no scale or kill calls on those numbers — but never stops it.

## What to tell the user

Not "Meta's numbers are wrong". They are a measurement with a known method and known limits, and
the method is defensible for what Meta uses it for.

The correct statement is narrower and more useful: *this figure includes an estimated X% modelled
purchases and Y% view-through; the store banked Z orders in the same window; here is what that
means for the decision you are about to make.*
