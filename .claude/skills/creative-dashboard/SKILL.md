---
name: creative-dashboard
description: When rendering a Meta account's creative performance as a Top Creatives dashboard — ad cards ranked by spend, purchases, ROAS, hook rate or hold rate, with Performance/Attention/Funnel tabs, a creative patterns table, and a per-ad drill-down showing the funnel path against account medians and the promise-handoff score. Use when the user asks for a "creative analysis dashboard," "top creatives report," "what creatives is Meta scaling," "hook rate analysis," or a "Motion-style creative dashboard." Required output of the creative inventory section. For the underlying dataset, see creative-data-model.
---
# Creative dashboard

The creative sections end in a shipped dashboard, not a chapter of prose. Nobody reads a
creative analysis as a table of 140 ad names; they look at cards, sort them, and click into the
two that surprise them.

`assets/artifact-template.html` is a complete working artifact. `assets/chrome-snapshot-template.html`
is the standalone variant with real thumbnails and ad previews. Most of the work is rewiring
config, not writing code.

## The one rule that matters

**Read `audits/<run-id>/creative-database.csv`. Do not re-query Meta.**

The upstream version of this template pulled its own data. In this repository it does not,
because a dashboard and a findings list that disagree are worse than either alone — and they
disagree the moment two components pull with slightly different windows, attribution settings or
row limits.

**Verification:** the dashboard's header figures (spend, purchases, blended CPA, blended ROAS)
must equal §5's campaign totals. If they diverge, something re-queried. Fix that before shipping
it; do not reconcile the two by hand.

## What it shows

| Element | Detail |
|---|---|
| **Rank by** | Spend · Purchases · ROAS · Hook rate · Hold rate |
| **Filter** | All · Video · Static |
| **Performance tab** | Spend, purchases, CPA, ROAS per card |
| **Attention tab** | Hook rate, hold rate, video quartile retention (p25/50/75/100) |
| **Funnel tab** | Impression → 3-sec → click → LPV → ATC → checkout → purchase |
| **Header strip** | THE READ, spend, purchases, blended CPA, blended ROAS, top-ad share |
| **Creative tags** | Rule-based from the naming convention; AI-assisted where names don't parse |
| **Patterns table** | Tag → ads, spend, purchases, CPA, ROAS. This is §9's input |
| **Drill-down drawer** | AI read (verdict / what worked / where it broke / next move), funnel path vs **account medians**, full ad copy, 12-metric grid, placement/device/age/gender breakdowns, promise-handoff score |

**Top-ad share** is worth more attention than it looks. One ad carrying 70% of spend is a
portfolio-depth finding, and the header surfaces it before anyone opens a card.

The drill-down compares each ad against **account medians**, not against a benchmark. "This ad's
ATC rate is 40% below the account median" is actionable; "this ad's ATC rate is 2.1%" is not.

## Configuring it — six edits

Agent 60 rewrites these from the audit's own findings. None should be hand-typed per client.

1. **`MCP`** — the Meta connector's server id. It differs per account: discover it at runtime
 (ToolSearch `ads_get_ad_entities`, read the value between `mcp__` and `__ads_`). Never
 hardcode one from another account.
2. **`ACCOUNTS`** — from `ads_get_ad_accounts`; first entry is the default. Set
 `mcpEnabled: false` on any account Meta has not enabled for MCP, so it renders disabled
 rather than being silently omitted from a list its owner expects to see.
3. **`BRAND` / `BRAND_DESC`** — the card tag and the AI-tagging prompt. `BRAND_DESC` is what
 tells the classifier what the product actually is; a vague one produces vague tags.
4. **`state.since` / `state.until`** — the window that has spend, from step 2 of
 `creative-data-model`. Never ship a range the account was dormant in: the dashboard renders
 empty and reads as broken rather than as accurate.
5. **`LP_GENOMES`** — one entry per destination, captured in §20 by actually fetching the pages.
 Hero claim, trust elements, section order, offer, CTAs. These ground the promise-handoff
 score, so a stale summary produces a confidently wrong score. Re-capture every run. Adjust
 `destFor()`'s routing keywords to the account's naming.
6. **`ANGLES` / `FORMATS` / `THEMES`** in `ruleTags()` — the account's own angle vocabulary and
 naming convention, from §7. The shipped regexes are illustrative; an account whose ads are
 about something else gets nothing from them.

## Creative tagging

Rule-based first, from the naming convention. AI only for ads whose names do not parse, and the
prompt instructs it to **return an empty array rather than guess** — a fabricated tag pollutes
the patterns table, which is the one output §9 depends on.

Tag source is recorded per `creative-taxonomy`. An account where most tags are model-inferred
gets a lower-confidence patterns table, and the report says so.

AI tags cache in `localStorage` (`cd_aitag_*`); bump the key after changing the prompt or the
old tags persist against new logic.

## Known platform limits — state these up front

Not caveats to bury. Someone will ask about each one, and discovering them live costs a session.

- **No inline thumbnails in the artifact.** The sandbox blocks Meta's CDN and strips inline
 images from `ads_get_ad_preview`. Cards use styled placeholders plus **Preview ↗** (Meta's
 rendered preview, opens in browser) and **Ads Manager ↗** (deep link with `selected_ad_ids`).
- **`file://` links and `prompt()` are blocked** in the artifact. The Open-in-Chrome button
 copies the path to the clipboard rather than opening it.
- **Thumbnails expire.** `thumbnail_url` is 64px and dies in weeks. Signed URLs cannot be
 upscaled — editing `stp=` returns a signature mismatch.
- **Preview iframes need a Facebook login** and are short-lived. They render the full ad and
 videos play, which is why they are worth using — but the snapshot is a point-in-time artifact,
 and the handover should say so.
- **Not available from the connector at all:** per-second retention curves, video storyboards,
 transcripts, comment data. Quartiles are the retention proxy.
- **`is_ads_mcp_enabled: false` beats `is_queryable: true`.**

## The Chrome snapshot

For a version with visible creative imagery, bake the data into
`chrome-snapshot-template.html` and write it to `audits/<run-id>/top-creatives-chrome.html`:

1. Bake `RAW_ADS` from `creative-database.csv` — **parsed numbers, not Meta's formatted
 strings**. A snapshot that re-parses is a snapshot that can re-parse wrong.
2. Bake `THUMBS` from `ads_get_creatives` (`id`, `object_type`, `thumbnail_url`, `image_url`).
3. For the top creatives, bake `PREVIEWS` from `ads_get_ad_preview` — iframes at 335×450,
 transform-scaled to card width.

Regenerate rather than promising permanence.

## Publishing

Published as an Artifact, and written to the run directory. Load `artifact-design` before
publishing, per the artifact workflow.

Two things to tell the user when handing it over: artifact updates require their approval before
the new version renders, and image-load errors from `scontent-*.fbcdn.net` in the debug log are
**expected**, not a fault.

## What it must not do

- **Not re-query.** Covered above, and it is the first thing to check when the numbers look off.
- **Not render a metric the account cannot supply — and say which kind of "cannot".** No video
 ads in the account means no Attention tab: hide it, and let §7 close `N/A` for that part. A
 connector that **withholds the field from an account full of video** is a different case with the
 same symptom: do not hide it silently, because the reader will conclude the account runs no video.
 Show the tab with the metric marked unavailable and the reason stated (`video_plays_3s_source:
 UNAVAILABLE`), and let §7 close `DEGRADED`, not `N/A`.
- **Not rank on hook rate by default.** Hook rate ranks ads by their ability to stop a scroll,
 which is a diagnostic, not the goal. Default to spend; offer the rest — and **withdraw the
 hook-rate sort entirely when the column is null**, rather than offering a control that does
 nothing.
- **Not present a modelled figure as observed.** Where modelled share varies materially across
 ads, the header says so — otherwise the ranking is partly a ranking of measurement artefacts.
