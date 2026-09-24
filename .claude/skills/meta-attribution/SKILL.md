---
name: meta-attribution
description: "When the user wants to reconcile Meta's reported numbers against reality for an e-commerce or D2C brand — why Ads Manager doesn't match Shopify or GA4, which attribution window to run, and how to prove Meta is actually driving incremental revenue. Also use when the user mentions 'Meta doesn't match Shopify,' 'attribution window,' '7-day click,' 'view-through conversions,' 'modeled conversions,' 'GA4 shows fewer conversions,' 'is Meta taking credit,' 'incrementality,' 'holdout test,' 'geo lift,' or 'conversion lift.' For building the report or dashboard itself, see meta-reporting. For fixing the underlying event and dedup wiring, see meta-capi-and-events. For general cross-channel tracking setup, see analytics."
metadata:
 version: 1.0.1
---

<!-- execution-boundary: documents-writes -->
<!-- Names write tools without calling them: names the lift-test creation call when explaining incrementality options.
     Calling them is the execution lane's, under EXECUTION-PROTOCOL.md. -->

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Meta Attribution & Incrementality — D2C E-commerce

Ads Manager will never match Shopify, and chasing the last dollar of that gap is the most common way D2C teams waste a week. This skill explains exactly why the two numbers differ, which attribution window to actually run, and how to measure whether Meta is driving incremental revenue rather than claiming credit for revenue you'd have earned anyway.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- **AOV and typical consideration length** — the window choice is a function of how long people take to buy, not a preference.
- **Store-side revenue and order count for the same period**, from Shopify or the equivalent. Without it there is nothing to reconcile against.
- **Whether a post-purchase survey is running**, and whether Pixel and CAPI both fire Purchase with a shared `event_id`.

## Requires the Meta Ads MCP for Live Work

Reading the account's current windows and comparing reported conversions across them goes through the MCP: `ads_get_ad_entities` and `ads_get_ad_entities` for reported purchases and values, `ads_get_dataset_quality` for event match quality and dedup health, and `ads_experiment_lift_create_test` / `ads_experiment_abtest_get_test` / `ads_experiment_lift_get_test` / `ads_experiment_list_tests` for conversion-lift studies. If the MCP isn't connected, say so and stop rather than fabricating numbers — the frameworks below need no connection.

## Attribution Windows

| Window | What it counts | Typical D2C use |
|---|---|---|
| **1-day click** | Purchases within 24h of a click | Impulse purchases, flash offers, low AOV. The most conservative view. |
| **7-day click** | Purchases within 7 days of a click | The default for most D2C. Matches browse-then-buy behavior. |
| **1-day view** | Purchases within 24h of an impression with no click | Upper-funnel contribution. Always report separately. |
| **7-day click + 1-day view** | Both, combined | Meta's default and the most generous. Inflates apparent performance if you don't know it's on. |

The window is a **reporting** choice, not a delivery choice — changing it changes the numbers, not the ads. That cuts both ways: switching from 7-day click to 1-day click can halve reported conversions with zero change in real performance. Whenever a "drop" appears, check whether someone changed the window before diagnosing anything else.

### Choosing a Window

- **Impulse, under ~$50 AOV**: 1-day click. If people don't buy the same day, they mostly don't buy.
- **Standard browse-then-buy D2C**: 7-day click. This is the right default.
- **High-ticket or long consideration ($300+, furniture, mattresses, jewelry)**: 7-day click, plus a store-side cross-check, because a real share of purchases land outside any Meta window. Do not solve this by widening the window — solve it with MER and post-purchase survey data.
- **Upper-funnel or brand campaigns**: report 1-day view as its own line. Never blend view-through into the same ROAS figure you judge prospecting on.

Pick one window, write it down, and use it consistently. Comparing this month at 7-day click against last month at 7-day-click-plus-1-day-view is not a comparison.

## Why Meta and Shopify Never Match

Five causes, compounding. All five are usually present at once, which is why the gap is never explained by one fix.

1. **They use different attribution models entirely.** Meta claims a purchase it can tie to an impression or click in its window. Shopify credits by last non-direct referral. GA4 uses data-driven or last-click across channels. All three can legitimately claim the same order. This is not a bug and there is no reconciliation that resolves it.
2. **View-through counting.** Meta counts purchases from people who saw the ad and never clicked. No store-side analytics tool will ever agree with that, because nothing happened on the site to record.
3. **Pixel/CAPI deduplication gaps.** If browser and server events for the same purchase don't share an `event_id`, Meta counts the order twice. Doubling that appears overnight is nearly always this — see meta-capi-and-events.
4. **Aggregated Event Measurement modeling.** For users who opted out of tracking, Meta reports modeled rather than observed conversions. Modeled numbers are directionally useful and individually unverifiable.
5. **Cross-device stitching.** Meta knows the person who saw the ad on their phone is the person who bought on a laptop, because both sessions are logged into the same account. Your analytics sees two visitors.

**Never reconcile to the dollar.** Pick one source of truth and hold it. For this library that source is **MER** — total revenue from the store divided by total ad spend — because it is immune to attribution games. Use Meta's in-platform numbers to compare ads against each other, and MER to judge whether the account is working.

The practical read: if in-platform ROAS rises while MER stays flat, Meta is taking credit, not creating revenue. That divergence is the most valuable signal in this whole skill.

## Reporting Discipline

- Report Meta-reported purchases **and** store orders for the same period, side by side, with the gap stated as a number. Do not silently pick whichever is flattering.
- Split prospecting from retargeting before averaging anything. Retargeting inflates in-platform ROAS by design — it converts people who were already coming back.
- State the window on every report. A ROAS figure without its attribution window is not a figure.
- Where the numbers disagree, say which one you trust for which decision and why.

## Incrementality: Proving Meta Actually Caused the Revenue

Attribution assigns credit. Incrementality asks a different question: what would have happened if the ads hadn't run? Only a designed test answers it.

**Conversion lift (holdout).** Meta's own lift test holds back a randomized share of the audience and compares purchase rates. Run it through `ads_experiment_lift_create_test` and read it with `ads_experiment_abtest_get_test` / `ads_experiment_lift_get_test`. This is the cleanest available answer for a single campaign. Constraints: it needs real volume, and it needs to run long enough to cover your purchase cycle — a two-week test on a 30-day consideration product measures the wrong thing.

**Geo holdout.** Split comparable regions, run ads in one set and not the other, compare total store revenue per region rather than platform-reported conversions. Slower and noisier than a platform lift test, but it measures total business impact and it works when you distrust the platform entirely. Match regions on baseline revenue, not population. Confounds to control for: regional promotions, weather, shipping-time differences, and any retail presence.

**Where to use each.** Platform lift tests answer "did this campaign work." Geo holdouts answer "does Meta work for us at all." Run the second one rarely and take it seriously.

**Post-purchase survey triangulation.** Ask "how did you hear about us?" and "is this your first purchase?" at checkout. Self-reported attribution is biased but it is *differently* biased from platform attribution, and where the two disagree you have found something worth investigating. This is also the only practical read on new-vs-returning mix that Ads Manager cannot give you honestly.

**Sequence.** Get the event wiring clean first (meta-capi-and-events), then settle on one window and one source of truth, then measure incrementality. Running a lift test on top of broken dedup measures your instrumentation.

## Common Mistakes

- Widening the attribution window to make a campaign look profitable. That is a reporting change dressed as a result.
- Blending view-through into prospecting ROAS.
- Treating a Meta-vs-Shopify gap as an error to be closed rather than a structural property to be understood.
- Comparing periods measured on different windows.
- Judging retargeting on in-platform ROAS.
- Calling a platform lift test "incrementality" when it ran for less than one purchase cycle.
- Diagnosing a conversion drop before checking whether the attribution setting changed.

## Related Skills

- **meta-reporting**: Building the actual weekly or monthly report and dashboard once you have settled the window and the source of truth.
- **meta-capi-and-events**: Fixing the dedup, event match quality and AEM issues behind two of the five divergence causes.
- **meta-high-value-audiences**: Value-based audiences and the customer-tier context most incrementality questions arise from.
- **paid-measurement-readiness**: Whether the account can be measured at all yet, and the maturity level at which incrementality testing becomes worth running.
- **google-ads-measurement**: The same platform-vs-store reconciliation on the Google side, plus Google-specific conversion-action and Consent Mode auditing.
- **analytics**: GA4 channel grouping, UTM strategy and cross-channel tracking setup.
- **ab-testing**: Experiment design, sample sizing and how to read a result that isn't significant.
