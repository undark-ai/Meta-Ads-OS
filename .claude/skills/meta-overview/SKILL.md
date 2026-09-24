---
name: meta-overview
description: "When the user wants the ground truth on Meta ads for an e-commerce or D2C brand — why it's the core paid channel for most brands, how the algorithm actually works (Andromeda + Gem), unit economics (break-even ROAS, new-customer CAC, LTV, MER), and the operating model behind the whole system. Also use when the user mentions 'how does Meta's algorithm work,' 'is Meta worth it for my store,' 'break-even ROAS,' 'MER,' 'Andromeda,' 'why is my ROAS misleading,' or 'Meta vs Google for ecommerce.' This is the ground-truth companion to meta-ads, the e-commerce Meta hub — use meta-ads for hands-on strategy and execution. This repository is Meta-only; for the e-commerce Meta hub, see meta-ads."
metadata:
 version: 1.0.1
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Meta Ads for D2C Ecommerce - Overview

Why Meta is the backbone channel for most D2C brands, how the algorithm works (Andromeda + Gem), and the operating model for running Meta ads against real unit economics. This is the ground-truth layer behind the meta-ads hub — the mental model everything else in the suite builds on.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context when the question needs numbers:

- AOV and contribution margin per order (required for break-even ROAS)
- Whether the product is mass-market (broad appeal, sub-$150 AOV) or niche/high-AOV

---

## Why Meta for D2C

Meta remains the highest-leverage paid channel for most ecommerce brands:

- **Demand generation, not demand capture.** Google and Amazon harvest people already searching; Meta creates buyers who didn't know your product existed. That makes it the growth engine - and it means creative does the selling.
- **The purchase loop closes fast and on-platform-measurable.** Unlike long consideration cycles, most ecom orders land within days of the click, so the algorithm gets dense purchase signal to learn from.
- **Scale.** Once a product's creative and unit economics work, Meta can take budget from hundreds to hundreds of thousands per month faster than any other channel.

**The catch:** you're on a discovery platform - people are scrolling, not shopping. Creative quality is the targeting. And in-platform ROAS flatters itself; you must judge it against **break-even ROAS (AOV ÷ contribution margin per order)** and blended **MER**, or you'll scale losses confidently.

---

## How the Algorithm Works: Andromeda + Gem

Two systems decide who sees your ads. Understanding them drives strategy.

### Andromeda (Ad Processing Layer)

ML model that processes your ads - copy, images, video transcripts, carousels, targeting hints - and filters to the creative concepts it thinks will perform.

**Critical point:** Andromeda needs volume of *distinct concepts*, not micro-variations (blue vs green button). Think: UGC testimonial vs problem/solution vs unboxing vs founder story vs offer-led vs meme. Post-2024, Andromeda is dramatically better at finding converters - creative quality now matters more than targeting, and broad targeting + great creative routinely beats hyper-segmented setups.

### Gem (User Matching Layer)

Analyzes each user's behavior - organic interactions, ad engagement, browsing and purchase patterns - and matches them to the concepts Andromeda selected. Picks the best user for each ad.

### What This Means for D2C

- **Mass-market products (broad appeal, sub-$150 AOV):** lean fully into the algorithm. Broad targeting, high creative volume, let Andromeda and Gem work.
- **Niche or high-AOV products:** the algorithm still needs help finding your buyer. Seed it with purchaser lookalikes and strong creative that self-selects the audience ("for people who..."), and expect longer learning.
- **Either way:** the pixel + CAPI purchase signal is the fuel. Weak or double-counted purchase events starve the algorithm; fix tracking before touching structure.

**Bottom line:** validate unit economics and tracking FIRST, then scale creative volume. The algorithm optimizes delivery; your margin math decides whether delivery is worth buying.

---

## The Operating Model

### Three Campaign Types

1. **Retargeting** - People who already know you: product viewers, cart abandoners, engagers. Highest ROAS, lowest risk, small share of spend. Start here to prove tracking and creative.
2. **Prospecting** - Reach strangers: broad, purchaser lookalikes, or Advantage+ shopping. This is where 70-90% of budget eventually goes, judged on **new-customer CAC**, with purchasers excluded.
3. **Retention / repeat** - Ads to existing customers for replenishment, cross-sell, and launches. Only worth a dedicated line when the catalog and repurchase cycle justify it (email/SMS usually carries this cheaper - use ads to grow the list, then let the list work).

### Three Phases of Campaign Structure

1. **ABO (Validation)** - Test audiences/angles with equal budgets. Find what produces profitable purchases, not just cheap clicks.
2. **CBO (Creative Scaling)** - Consolidate winners, scale with more creative concepts.
3. **Advantage+ Shopping (Automated Scaling)** - Full automation once you have ~50+ purchases/week; feed it your best creative and customer lists, control only budget and the new/existing customer split.

See meta-campaign-structure for the full architecture and settings.

### The Roadmap

1. **Month 1:** Tracking (pixel + CAPI + catalog) and retargeting - prove the loop works.
2. **Months 2-3:** Prospecting - validate angles and audiences, establish real new-customer CAC vs first-order margin.
3. **Month 4+:** Consolidate into Advantage+ / broad, scale creative production as the growth constraint.
4. **Ongoing:** post-purchase surveys and MER to keep in-platform numbers honest; grow email/SMS so paid traffic compounds.

---

## D2C Meta Benchmarks (reference ranges - the account's own history beats these)

| Metric | Typical | Strong | Red Flag |
|--------|---------|--------|----------|
| CTR (prospecting) | 1.0-2.0% | 2.5%+ | < 0.8% |
| CPM | $15-35 | < $15 | > $50 (non-Q4) |
| Prospecting ROAS | near break-even | 1.5x break-even | < 60% of break-even |
| Blended MER | 3-5 | 5+ | < 2.5 |
| Frequency (prospecting, 7d) | 1.5-2.5 | < 2 | > 4 |
| New-customer share of purchases | 60-80% | 80%+ | < 50% on "prospecting" |

Break-even ROAS = AOV ÷ contribution margin per order. Compute it before judging anything. (For live account numbers to judge these ranges against, see meta-ads-mcp and creative-data-model — and remember these ranges are advisory, never evidence for a quantified finding.)

---

## How This Differs From Other Channels

- **vs Google Search/Shopping:** Meta creates demand, Google captures it. Meta ROAS looks worse in-platform but drives the branded-search lift Google then claims. Read both through MER.
- **vs TikTok:** similar discovery mechanics, faster creative burn, weaker purchase signal density; Meta is usually the base layer, TikTok the amplifier.
- **vs email/SMS:** ads acquire, owned channels retain. The list you build from purchasers and lead offers is the margin engine that makes paid CAC affordable.

## Related Skills

- **meta-ads**: The e-commerce Meta hub — hands-on strategy, audiences, creative testing, and optimization built on this ground truth.
- **meta-campaign-structure**: The account architecture and three-phase roadmap this overview summarizes.
- **google-ads-overview**: The same ground-truth layer for Google — read both before reallocating budget between the two channels, since Google's in-platform ROAS overstates its contribution and Meta's understates it.
- **ads**: Platform-agnostic paid-ads strategy when the question spans Google, LinkedIn, TikTok, and other channels.
- **full-audit**: The evidence-graded audit lane — 30 sections against live account data, where these benchmarks get tested rather than assumed.
