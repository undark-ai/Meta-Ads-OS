---
name: lead-capture-optimization
description: "When the user wants to run Meta lead ads or lead-capture campaigns for e-commerce or D2C list growth — email/SMS capture, quiz funnels, giveaways and waitlists, friction tuning for subscriber quality, and welcome-flow handoff. Also use when the user mentions 'lead ads,' 'instant forms,' 'grow our email list with ads,' 'quiz funnel,' 'giveaway campaign,' 'waitlist signups,' or 'cost per lead.' This covers Meta lead ads and paid list-growth. For on-site capture popups, see popups;"
metadata:
 version: 1.1.1
---

<!-- execution-boundary: documents-writes -->
<!-- Names write tools without calling them: describes the audience build a lead flow hands off to.
     Calling them is the execution lane's, under EXECUTION-PROTOCOL.md. -->

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Lead Capture Optimization for D2C Meta Ads

How to use Meta lead campaigns for e-commerce list growth — email/SMS capture, quiz funnels, giveaways, and waitlists — balancing subscriber volume with subscriber quality, and converting captures into first purchases through the welcome flow.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):
- Purchase-campaign CAC vs. break-even, and AOV/margin for the products the welcome flow will sell
- Email/SMS platform in use and whether real-time lead sync is available

## Why D2C Brands Run Lead Capture on Meta

Purchases aren't the only valuable conversion. Lead capture works when: CAC on direct purchase campaigns is above break-even for a considered product; you're pre-launch (waitlist); you want owned-audience insurance against rising CPMs; or your product benefits from personalization (quiz). A subscriber who converts through a welcome flow often costs a fraction of a cold-purchase CAC — judge lead campaigns on **cost per first purchase within 30-60 days**, not cost per lead.

## Instant Forms vs Landing Pages

| Method | Conversion Rate | Subscriber Quality | When to Use |
|---|---|---|---|
| Meta Instant Forms | Higher | Lower without friction tuning | Fast list growth, giveaways, waitlists |
| On-site capture (quiz, LP) | Lower | Higher — they visited your site, pixel fires, session data accrues | Quiz funnels, offer-gated discounts |

Start with instant forms for speed; invest in on-site funnels in parallel — on-site captures retarget better and convert to purchase at higher rates.

## The Amnesia Problem

The #1 quality issue with instant forms: auto-fill makes signup so frictionless that people don't register what they signed up for. They ignore your welcome email, never redeem the discount, and drag down deliverability. **The fix is intentional friction** — enough that the subscriber remembers you.

## Capture Campaign Types

| Type | Mechanics | Quality Profile |
|---|---|---|
| **Discount capture** | "Get 15% off your first order" → email/SMS → code delivered in welcome flow | Medium-high intent; closest to purchase |
| **Quiz funnel** | "Find your perfect [product] in 60 seconds" → results gated by email | High — zero-party data personalizes the welcome flow and future creative |
| **Giveaway** | "Win a $200 bundle" | High volume, lowest intent — expect heavy churn; segment these subscribers separately and sunset non-engagers fast |
| **Waitlist / early access** | Pre-launch or restock signup | High intent, time-boxed — convert fast at launch or lose them |
| **Content/guide** | Lookbooks, routines, sizing guides | Niche; works for considered purchases |

## Form Setup for Subscriber Quality

1. **Form type:** Meta offers "More Volume" (aggressive auto-fill) and "Higher Intent" (adds a review step). Use **Higher Intent** by default; reserve More Volume for giveaways where raw reach is the goal.
2. **Fields:** email always; **phone for SMS only if you'll actually text them** (SMS consent language required). Every extra field cuts completion but raises quality.
3. **Add 1-2 qualifying questions** (multiple choice beats open text): "What are you shopping for?" / "What's your biggest frustration with [category]?" — these qualify the subscriber, add useful friction, AND feed segmentation in your email platform.
4. **Confirmation screen:** tell them exactly what happens next — "Your 15% code is on its way to your inbox (check promotions tab). It expires in 7 days." Generic "Thanks!" feeds the amnesia problem. Link straight to the bestsellers collection with the code pre-applied if possible.

### Instant Form Type: More Volume vs Higher Intent

Meta offers two instant-form types and the difference is one screen. **More Volume** submits as soon as the fields are filled. **Higher Intent** adds a review step the person must confirm before submitting.

**Default to Higher Intent.** The review step costs a small share of submissions and removes most of the accidental ones — the taps that happen because a pre-filled form was one thumb-press away. On a channel where the whole problem is subscribers who don't remember subscribing, a confirmation screen is the cheapest quality filter available.

### Instant Form or Landing Page? The Numeric Test

Stop arguing about it and read your own conversion rate:

| Your landing page converts at | Use |
|---|---|
| 5%+ | The landing page. It is already doing better than the friction trade-off is worth |
| 2–5% | Test both. The answer depends on your welcome flow's strength |
| Under 2% | The instant form. The page is the bottleneck, not the offer |

**Question count is the other hard number: abandonment spikes above 3 questions.** One to three qualifying questions, multiple choice rather than open text, easiest first. Never re-ask something Meta already auto-fills.

## The Friction Framework

| Goal | Friction | Setup |
|---|---|---|
| Max volume (giveaway, waitlist) | Low | More Volume form, email only |
| Balanced (discount capture) | Medium | Higher Intent form, email + 1 question |
| Max quality (quiz, SMS list) | High | On-site quiz/LP, email + phone + 2-3 questions |

Every friction element cuts completion rate but raises downstream purchase rate. Increase friction if welcome-flow conversion is weak; decrease it if volume can't feed the algorithm.

## The Welcome-Flow Handoff (where the money is)

Lead capture only pays off if the handoff to email/SMS is instant and aggressive:

1. **Sync in real time** — Meta leads must hit your email/SMS platform within minutes (native integration or Zapier), not via daily CSV export. Speed-to-first-email is the top conversion variable.
2. **Welcome flow:** email 1 immediately (deliver the code/quiz results/entry confirmation), then 3-5 emails over 7-14 days: social proof, bestsellers, founder story, objection handling, code-expiry reminder. Mirror on SMS if captured.
3. **Deadline the incentive** — a 7-day expiring code outperforms an evergreen one.
4. **Close the loop with retargeting** — build a custom audience of leads who haven't purchased (via the Meta Ads MCP: `ads_create_custom_audience`, `ads_update_custom_audience_users`); run proof-heavy ads alongside the flow.

### Feed Purchase Quality Back to Meta

The core problem with optimizing for leads is that Meta has no idea which subscribers ever bought. It will happily find you thousands of people who fill in forms and never spend a cent, and the CPL will look excellent the whole time.

Close the loop by sending downstream events back via CAPI or offline conversions, mapped to the D2C chain rather than a sales pipeline:

| Send back | When | What it teaches Meta |
|---|---|---|
| `CompleteRegistration` / `Subscribe` | On capture | Baseline — what you're currently optimizing on |
| `Purchase` with value | On the subscriber's **first order** | Which capture ads produce buyers, not just emails |
| A custom repeat-purchase event | On the **second order** | Which capture ads produce customers worth acquiring |

Once first-order volume supports it, **optimize the capture campaign toward the purchase event, not the lead event.** Expect imperfect match rates; the signal still improves targeting materially, and delayed data is still useful data — the algorithm learns from the pattern, not from any single order.

This is the highest-leverage fix available to a lead-capture campaign and almost nobody running one has done it.

## Measurement

Track by campaign and question answers: cost per subscriber, welcome-flow conversion rate, **cost per first purchase (30/60-day)**, and revenue per subscriber at 60 days. A $1 giveaway lead that never buys is worse than a $6 quiz lead with a 20% purchase rate.

### Form Completion Diagnostics

Three symptoms, three different causes. The metric pair tells you which:

| Pattern | Cause | Fix |
|---|---|---|
| High CTR, low form-open rate | Ad-to-form message mismatch. The ad promised one thing, the form asks for something else | Rewrite the form greeting to continue the ad's sentence, not to restart the conversation |
| High form-open, low submit rate | Too many fields, an unclear value exchange, or poor mobile rendering | Cut to 1–3 questions, state plainly what they get, and open the form on a phone yourself. If it's the landing-page variant failing, the defect is usually mechanical — see **ux-audit** |
| High submit rate, high junk rate | No qualifying questions, or an over-incentivized offer pulling freebie-seekers | Add a qualifying question; reduce or reframe the incentive toward the product rather than a generic prize |

**Segment form data by ad set, not just by campaign.** Junk rate is rarely uniform — it usually traces to one audience or one offer, and account-level averages hide it completely.

## Common Mistakes

1. Judging on CPL instead of cost per first purchase
2. Slow lead sync — welcome email arriving hours later kills conversion
3. Zero friction on discount captures → coupon-scrapers and dead weight on your list
4. Collecting phone numbers with no SMS program (friction with zero payoff)
5. No expiry on the incentive
6. Mixing giveaway subscribers into your main sends and tanking deliverability

## Related Skills

- **popups**: On-site capture popups and embedded forms — the owned-site side of list growth.
- **lead-magnets**: Designing the lead-magnet asset itself (guides, quizzes, content offers).
- **emails**: The welcome flows and nurture sequences that turn captured leads into first purchases.
- **meta-ads**: The e-commerce Meta hub — where lead campaigns fit in the broader account strategy.
- **sms**: SMS program strategy if you're capturing phone numbers.
