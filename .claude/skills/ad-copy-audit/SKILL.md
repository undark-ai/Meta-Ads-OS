---
name: ad-copy-audit
description: When auditing the ad copy a Meta account is actually running — reading primary text, headline, description and CTA from the creative database, scoring each on the craft dimensions that move purchases, joining every score to what that ad measurably earned, and producing concrete rewrites for the ads worth rewriting. Use when the user asks "review my ad copy," "is our copy any good," "why do these ads get clicks but no sales," "rewrite these ads," or "what should the copy say instead." For generating new copy at volume see ad-creative; for page copy see copywriting; for the voice rules every rewrite obeys see ad-writing-style.
---
# Ad copy audit

The creative database already carries what every ad **says** — `primary_text`, `headline`,
`description`, `cta_type` — beside what it **earned**. This skill is the join between them.

That join is the whole point. Copy scored on craft alone is an opinion; copy scored on craft and
then set against measured purchases is an argument. Neither half is worth much without the other:
a beautifully written ad below the purchase floor has proved nothing, and a winning ad whose copy
you cannot describe teaches you nothing you can reuse.

## Read from the creative database, never re-query

§7 wrote `audits/<run-id>/creative-database.csv` once. Read the copy columns from it, exactly as
§§8–11 read the performance columns. An ad whose copy came from a fresh pull and whose ROAS came
from the file is comparing two different moments.

Where `primary_text` is null but the ad has spend, that is a §7 extraction gap — record it, do not
quietly drop the row. Rows that genuinely have no copy (a pure catalog/DPA ad drawing text from the
feed) are `N/A` for this skill, not zero-scored.

## Score the copy on what moves purchases

Six dimensions. Score each 0–3 with the evidence quoted from the ad itself, never as a bare number.

| Dimension | 0 | 3 | Why it earns a place |
|---|---|---|---|
| **Specificity** | "Premium quality, great fit" | "Stays put through a 12-hour shift" | Vague claims are unfalsifiable, so nobody believes them |
| **Named problem** | Product described, no problem | The reader recognises their own complaint in the first line | Meta traffic is interrupted, not searching. It has no problem in mind yet |
| **Proof** | Assertion only | A number, a review, a demonstration, a named source | The claim and the reason to believe it are different jobs |
| **Objection handled** | None | The thing that stops this buyer, answered in the ad | The objection gets raised on the page anyway; better to answer it before the click |
| **Single clear ask** | Three competing CTAs, or none | One action, matching `cta_type` and the landing page | Two asks is one too many |
| **Offer clarity** | Offer implied or absent | The offer is stated and matches what the page shows | A promise the page does not keep is the most expensive kind |

Score against **this account's own top performers first**, not against a generic ideal. An account
whose winners are all plain product shots with two-line copy has told you something, and grading it
against a UGC-testimonial rubric would produce a page of fixes that make it worse.

## The volume rule applies to copy exactly as it does to creative

Most ads sit below the purchase floor for their whole life. `learning-phase-and-significance`
governs here without exception:

- Above the floor → the join is a **verdict**. Copy patterns can be ranked on purchases.
- Below the floor → `INSUFFICIENT_DATA`. You may still score the craft, but say plainly that the
  score is unvalidated on this account, and never present a below-floor ad's ROAS as evidence its
  copy works.
- Where the account has validated that a faster signal predicts purchases *here*,
  `leading-and-lagging-signals` allows CTR or hold rate to **triage** copy. It never allows them to
  carry a verdict, and the correlation and n get quoted at the point of use.

A copy recommendation built on four purchases is a coin flip with a rationale attached.

## Find the pattern, not the winner

The output is not "these five ads are well written". It is which **copy decision** wins purchases:

- Opening line type — problem, question, claim, social proof, pattern interrupt
- Length band — does this account's audience read 40 words or 200
- Person — first, second, third
- Whether the offer appears in the primary text, the headline, both or neither
- Price mentioned or withheld
- CTA type against its measured conversion, not against convention
- Language and register — for a non-English account, whether the winners are formal or colloquial

Recompute each from component sums across the ads carrying that trait. **Never average ad-level
rates.** Two ads at 3% CTR do not make a 3% trait when one had 900 impressions and the other
900,000.

Report every pattern with its spend and purchase count beside it, so a reader can see which
conclusions the volume actually supports.

## Rewrite only what is worth rewriting

Three tests before a rewrite earns its place. All three, not any:

1. **The ad carries enough spend to matter** — a rewrite of a ₪40 ad is a hobby.
2. **The copy is the plausible constraint** — not the placement, the audience, the offer or the
   landing page. Check §18 and §19 first: an ad with a strong hook rate and a collapsing add-to-cart
   rate has a page problem, and rewriting its headline changes nothing.
3. **There is a specific, quotable weakness** — "could be stronger" is not a finding. Name the line.

For each rewrite, give the original and the replacement side by side, the single dimension it
changes, and what you expect to move. Change **one** dimension at a time: a rewrite that alters the
hook, the proof and the CTA at once teaches nothing when it wins.

`ad-writing-style` governs every line produced here — it is not optional, and it is what stops a
rewrite reading as though a machine wrote it. Where `.agents/product-marketing.md` exists, the
rewrite uses its positioning and voice; where it does not, say that the rewrite rests on inferred
positioning and carries lower confidence.

## The boundary

**This skill never edits an ad.** It produces a recommendation with the original preserved beside
it. Applying copy to a live account is agent 206 under `EXECUTION-PROTOCOL.md` — change plan,
approval, preview before publish, create paused.

A copy score is a **marketing-layer judgement**, not evidence. It never carries `OBSERVED`. The
performance it is joined to does, and the two must stay distinguishable in the output — a finding
that reads "this copy is weak and its ROAS is 1.1" is mixing an opinion and a measurement without
saying which is which.

## Output

`audits/<run-id>/findings/copy-audit.md`:

- The six-dimension scorecard per ad above the spend threshold, with the weak line quoted
- Copy patterns ranked by purchases, each with spend and n, and each marked verdict or
  `INSUFFICIENT_DATA`
- Rewrites for the ads that pass all three tests, original beside replacement, one dimension each
- What could not be assessed: null copy fields, catalog ads with no static text, and any ad below
  the floor whose craft score is therefore unvalidated

Feeds §9's angle analysis and §10's testing system. Where the audit concludes the constraint is
post-click rather than copy, say so here rather than shipping rewrites that cannot help.
