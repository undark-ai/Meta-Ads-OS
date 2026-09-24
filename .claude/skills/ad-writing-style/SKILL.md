---
name: ad-writing-style
description: "When the user wants everything an agent writes to stop sounding like an AI wrote it — a banned-word and banned-structure list plus positive rules governing ad copy, audits, plans, reports and chat replies alike. Also use when the user mentions 'this sounds like AI,' 'stop using these words,' 'banned words,' 'AI slop,' 'make it sound human,' 'writing style guide,' 'house style,' 'too corporate,' or 'why does all our copy sound the same.' For editing a specific piece of existing copy sweep by sweep, see copy-editing. For writing marketing page copy, see copywriting. For generating ad variations at volume, see ad-creative."
metadata:
 version: 1.0.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Ad Writing Style

A voice governor, not an editing pass. This applies to **everything** written for the account: ad copy, audit findings, campaign plans, performance reports, briefs, and replies in chat. One consistent voice, applied by default, so nobody has to ask for it.

If the task is fixing one specific piece of existing copy in depth, use copy-editing — it has a seven-sweep process this skill deliberately doesn't duplicate.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. A brand-voice section there overrides the stylistic preferences below; the banned list still applies.

## The One Test

Read it aloud. If you would not say it to a customer standing in front of you, rewrite it.

That single test catches most of what follows. The lists exist because the test is easy to skip.

## Banned Words and Phrases

**Filler verbs and nouns**
delve, unpack, dive into, explore (as a transition), navigate (figuratively), landscape (figuratively), realm, tapestry, journey (as a metaphor), ecosystem (unless literal), synergy, paradigm

**Empty intensifiers**
leverage, harness, elevate, supercharge, unlock, unleash, empower, revolutionize, transform (as a claim), optimize (as a claim), maximize

**Adjectives that describe nothing**
seamless, robust, holistic, innovative, cutting-edge, best-in-class, world-class, game-changer, next-level, powerful, comprehensive, curated, bespoke, effortless

**Dead openers and connectives**
"In today's fast-paced world," "In an era of," "It's worth noting that," "It's important to remember," "At the end of the day," "When it comes to," "Let's face it," "The truth is," "Look,"

**Hedged nothings**
"a myriad of," "a plethora of," "countless," "move the needle," "take it to the next level," "a testament to," "speaks volumes," "is key," "plays a crucial role"

**Audience-splitting constructions**
"whether you're a X or a Y," "for everyone from X to Y," "no matter your Z"

`copy-editing` has a swap table for several of these when you're editing existing copy. This list is broader and applies at write time, not edit time.

## Banned Structures

1. **"Not just X, but Y."** Also "It's not about X — it's about Y." Say the thing.
2. **The rule of three.** Three parallel adjectives or clauses in a row reads as generated. One is usually enough; two if both earn their place.
3. **Hedging stacks.** "Can potentially help to significantly improve." Pick a verb.
4. **Empty openers.** Any first sentence that could open any document on any subject.
5. **The repeating summary.** A closing paragraph that restates what was just said, adding nothing.
6. **Rhetorical question openers.** "Ever wondered why your CPA keeps climbing?" Nobody has ever answered one.
7. **Emoji and hashtags** in body copy, headlines, reports and chat. In social captions they're a channel convention; everywhere else they're filler.

**The em dash is not banned.** It is part of this library's voice and appears throughout it. Overused em dashes are a symptom of unresolved sentence structure, not a punctuation crime — if a sentence has three, it wants to be two sentences. But do not strip them out, and do not treat their presence as an AI tell.

## Do This Instead

- **Lead with the answer.** The recommendation goes in the first sentence, the reasoning after.
- **Be specific enough to be falsifiable.** "CPA dropped from $64 to $38 in three weeks" instead of "significantly improved performance." A number you can check beats an adjective you can't.
- **Vary sentence length.** Follow a long sentence with a short one. Uniform sentence length is the single loudest generated-text signal.
- **Concrete nouns, active verbs.** "The pixel stopped firing" instead of "there was a tracking degradation."
- **Have an opinion.** If two options are not equally good, say which one you would pick and why. Presenting a balanced survey of options the reader must adjudicate is a way of not answering.
- **Cut dead words.** "In order to" → "to." "Due to the fact that" → "because." "At this point in time" → "now."
- **Numbers over adjectives.** Always.

## Ad Copy Specifically

- **One person, one problem, one ad.** Copy that addresses two customer situations addresses neither.
- **Name the reader.** "For runners who blister in every shoe" filters better than any interest stack. See meta-creative-strategy for why this is targeting, not just style.
- **One idea per ad.** If there are two claims, that's two ads.
- **Proof over hype.** A review count, a number, a specific outcome. If the only support for a claim is enthusiasm, cut the claim.
- **Read it as the customer, not as the brand.** The brand knows what the product does. The customer is mid-scroll and does not care yet.
- **Never invent proof.** No fabricated review counts, customer numbers, study results, or percentages. If a claim needs substantiation the brand hasn't given you, ask for it or drop the claim.

## Before and After

**Before:** "Unlock the power of seamless metabolic insights with our innovative, best-in-class wearable — designed for everyone from weekend warriors to elite athletes."
**After:** "Most diets fail because they're written for someone else's body. This one reads yours every morning."

**Before:** "In today's competitive e-commerce landscape, it's important to leverage a holistic approach to creative testing in order to move the needle on performance."
**After:** "You can't scale budget faster than you can produce creative. Four concepts a month is the floor."

**Before:** "Our comprehensive audit revealed a myriad of opportunities to optimize your account and take your ROAS to the next level."
**After:** "Three things are costing you money. The biggest is that prospecting and retargeting share one CBO campaign, so retargeting eats 70% of the budget and reports the credit."

## Common Mistakes

- Applying this to ad copy but not to the report that recommends the ad copy.
- Swapping a banned word for a synonym instead of rewriting the sentence.
- Reading "have an opinion" as licence to state a preference without a reason.
- Cutting all the em dashes.
- Treating specificity as licence to invent a number.

## Related Skills

- **copy-editing**: The seven-sweep editing process for improving a specific piece of existing copy in depth.
- **copywriting**: Writing marketing page copy — headlines, value propositions, page structure.
- **ad-creative**: Generating and iterating ad copy at volume across platforms.
- **ad-headline-techniques**: Named headline devices and formulas when you want a specific rhetorical structure.
- **meta-creative-strategy**: Why naming the reader in the copy functions as targeting on Meta.
