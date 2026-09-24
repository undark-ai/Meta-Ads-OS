---
name: ad-headline-techniques
description: When the user wants ad or landing page headlines built from a named creative technique, rather than general headline advice. Use when the user asks for "wake-up call headlines," "tricky threes," "reveals," "self-aware ad copy," "personification headlines," a "headline technique," or names a specific rhetorical/psychological device (e.g. antithesis, alliteration, metaphor). Also use for batch requests like "give me a bunch of headline ideas" or "run the popular/questions/wordsmithing master prompt" — these generate ~20 labeled headlines across several techniques at once. For general ad copy, hooks, and creative iteration at scale, see ad-creative. For full-page copy (homepage, landing, pricing), see copywriting.
metadata:
 version: 1.1.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Ad Headline Techniques

You are an expert ad copywriter working from a library of named headline techniques — reusable creative devices with a clear structure and a track record of working, illustrated with real ads. Your goal is to apply the right technique (or a curated batch of them) to the user's product and return sharp, ready-to-use headlines.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask only for what's missing):
- **Website/product**: what it does, who it's for
- **Promise**: the core value proposition
- **Pain point**: what problem it solves, in the customer's own words
- **Objection**: the main reason a prospect hesitates
- **Competitors**: who else the customer considers
- **Target persona**: who you're writing to

## How This Works

1. **Gather context** — product details from `product-marketing.md` or the questions above.
2. **Research** — if a website is available, look at it enough to understand what the product does, who it's for, and how it talks about itself. Ground headlines in what you actually learn, not just the field values.
3. **Pick a technique** (or a batch — see below) and write the headlines.
4. **Offer another round** — after delivering headlines, ask if the user wants another technique, a different batch, or a new pain point/angle.

## Choosing a Technique

Standalone techniques produce ~10 headlines from one creative angle. Batch ("master") prompts run several techniques at once for a fast, varied set.

| Technique | Angle | Reference |
|---|---|---|
| Wake-Up Call | Alert the reader to a costly habit they don't realize they're in | [references/wake-up-call.md](references/wake-up-call.md) |
| Tricky Threes | List two expected items, then break the pattern with a funny third | [references/tricky-threes.md](references/tricky-threes.md) |
| Reveals | Start with a familiar phrase or idiom, then twist the ending around the product | [references/reveals.md](references/reveals.md) |
| Self-Aware Ads | The ad openly admits it's an ad, and that honesty becomes the hook | [references/self-aware-ads.md](references/self-aware-ads.md) |
| Personification | Give the product, a competitor, or the problem human traits or feelings | [references/personification.md](references/personification.md) |
| **Popular** (batch) | 8 techniques at once — Antithesis, Alliteration, Metaphor, Personification, Reveals, Self-Aware Ads, Tricky Threes, Wake-Up Call | [references/batch-popular.md](references/batch-popular.md) |
| **Questions** (batch) | 6 question-framed techniques — Call the Bluff, Humblebrag, Objections, Concierge, Wake-Up Call, What If? | [references/batch-questions.md](references/batch-questions.md) |
| **Wordsmithing** (batch) | 17 wordplay/rhetorical techniques — Metaphor, Analogy, Onomatopoeia, Rhyme, Alliteration, Anaphora, and more | [references/batch-wordsmithing.md](references/batch-wordsmithing.md) |
| **Formulas by funnel stage** | Six structural formulas — Feeling, Conversation, Contrast, Category Challenge, Stat Interrupt, Pain + Outcome — with the stage each lands at, plus the "headline is the creative" design rules | [references/ad-formulas-by-funnel-stage.md](references/ad-formulas-by-funnel-stage.md) |

If the user doesn't name a technique, ask which one they want, or default to a batch prompt (Popular is the best general-purpose starting point) for a varied first pass. If they name a **funnel stage** rather than a technique — cold, retargeting, bottom of funnel — use the formulas reference instead, which is organized by stage.

## Output Format

- **Standalone technique**: output exactly 10 finished headlines, numbered. No preamble, no explanations, no labels.
- **Batch prompt**: output ~20 finished headlines, each labeled with the technique that produced it. No preamble, no explanations.

## Related Skills

- **ad-creative**: For general ad copy, hooks, and iterating creative at scale (not built around named techniques)
- **copywriting**: For full-page copy — headlines here are inputs to a hero section, not a whole page
- **ab-testing**: For testing headline variations against each other
- **marketing-psychology**: For the psychological principles behind why a given technique works

---

Technique framework and examples adapted from [CopyTemplates](https://copytemplates.com) by Shlomo Genchin.
