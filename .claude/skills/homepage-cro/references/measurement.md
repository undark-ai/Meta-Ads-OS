# Homepage Measurement

The homepage is the hardest page in e-commerce to measure honestly, because its contribution is almost entirely **assisted**. It rarely closes a sale itself; it routes.

---

## The core problem: assisted revenue

A homepage session that ends in a purchase three pages later is a homepage success, and every last-click view of the data will credit the PDP instead. Conversely a homepage with wonderful engagement metrics and no downstream revenue looks healthy in every report a brand normally runs.

So compute these two before anything else:

**Homepage-assisted conversion rate** — of sessions that *touched* the homepage at any point, what share converted anywhere on the site?

**Revenue per homepage session** — total revenue from sessions that touched the homepage ÷ those sessions.

Then compare both against sessions that never touched the homepage, and against your other major landing pages. That comparison is the honest answer to "is the homepage working," and most brands have never run it.

Two ways to get it:

- **GA4** — Explore → Path exploration from the homepage, plus a segment of "sessions including page = /" compared against sessions excluding it. Crude but available to everyone
- **PostHog / Mixpanel / Amplitude** — a session-scoped property flagging homepage-touched, then funnel and revenue analysis on that segment. Much cleaner, and worth the setup

**Beware the confound:** homepage-touched sessions skew toward brand search, direct, and returning visitors — people who were more likely to buy anyway. A raw comparison overstates the homepage's contribution. Segment by source and by new/returning before drawing a conclusion, and say so in the report rather than presenting the headline number as causal.

---

## Event spec

| Event | Fires when | Key properties |
|---|---|---|
| `homepage_view` | Homepage renders | `is_returning`, `traffic_source`, `device`, `logged_in` |
| `promo_bar_click` | Announcement bar clicked | `message`, `position` |
| `promo_bar_dismissed` | Bar dismissed | `message` |
| `hero_cta_click` | Hero CTA clicked | `cta_label`, `destination`, `slide_index` (if a carousel) |
| `hero_slide_viewed` | Each carousel slide displayed | `slide_index`, `dwell_ms` — **this is the data that settles the carousel argument** |
| `nav_interaction` | Nav item or menu opened | `label`, `level`, `device` |
| `search_opened` | Search focused or opened | — |
| `search_submitted` | Query submitted | `query`, `result_count` |
| `search_zero_results` | Query returns nothing | `query` — a free product and taxonomy roadmap |
| `category_tile_click` | Category/collection tile clicked | `label`, `position`, `module` |
| `module_viewed` | Any homepage module scrolls into view | `module_name`, `position` |
| `module_click` | Any module engaged | `module_name`, `position`, `target` |
| `product_card_click` | Product card clicked from homepage | `item_id`, `module_name`, `position` |
| `quick_add` | Quick add used from homepage | `item_id`, `module_name` |
| `popup_shown` | Email/SMS modal displayed | `trigger_type`, `seconds_on_page`, `is_subscriber` |
| `popup_dismissed` | Modal closed | `trigger_type`, `seconds_shown` |
| `email_signup` | Capture completed | `placement` (popup / inline / footer) |
| `ugc_interaction` | UGC or review module engaged | `module_name` |
| `view_item` | PDP reached | (hands off to `product-page-cro`'s spec) |

Four that most stores lack and that change decisions:

- **`module_viewed` paired with `module_click`** — gives you a per-module engagement rate, which is the only defensible basis for cutting sections. Without it, "remove this section" is an opinion
- **`hero_slide_viewed` with the slide index** — per-slide engagement is what ends carousel debates, and it almost always ends them the same way
- **`search_zero_results`** with the query — the cheapest customer research in the business
- **`popup_shown` with `is_subscriber`** — quantifies how much of the popup's cost falls on people already on the list

---

## Segmentation

Never report a blended homepage number. Segment by:

- **New vs. returning** — the single most important split on a homepage. These are different products
- **Traffic source** — brand search, direct, paid social, email, organic, referral. Their needs diverge sharply
- **Logged-in vs. anonymous** — logged-in visitors should arguably see a different homepage
- **Device** — desktop vs. mobile vs. tablet
- **Geography** — surfaces shipping and currency problems
- **Customer status and purchase history** — first-timer, one-time buyer, repeat, VIP
- **Browser and OS** — including in-app webviews (Instagram, TikTok, Facebook), where carousels and sticky elements commonly break
- **Landing page vs. mid-session** — a visitor who *landed* on the homepage and one who *navigated back* to it want different things, and lumping them together hides both

---

## The five metrics to watch

| Metric | Definition | Why it's here |
|---|---|---|
| **Revenue per homepage session** | Revenue from homepage-touched sessions ÷ those sessions | The scoreboard. Everything else is diagnostic |
| **Homepage-assisted conversion rate** | Converting homepage-touched sessions ÷ homepage-touched sessions | Whether the hub routes people to purchase |
| **Product-view rate from homepage** | Sessions reaching a PDP ÷ homepage sessions | The homepage's actual job, measured directly. The best intermediate KPI for tests |
| **Homepage exit rate** | Exits ÷ homepage sessions, split by source | A high exit on brand-search traffic is a routing failure, not a persuasion failure |
| **Per-module engagement rate** | `module_click` ÷ `module_viewed`, by module | Tells you what to cut. The most actionable homepage metric almost nobody has |

Guardrails alongside: full-price sell-through (for promotional changes), email capture rate (for popup changes), AOV, LCP and CLS, and search zero-result rate.

---

## Qualitative instrumentation

- **Scroll depth** — where the page dies. If 70% never reach a module, its content isn't the problem; its position is
- **Click maps** — reveals dead modules and, importantly, non-clickable elements people *try* to click, which is a labelling failure
- **Rage clicks** — cluster on carousels that don't respond and on product cards where only the title is a link
- **Session recordings** filtered to homepage-landing sessions that exited without a product view. Watch fifteen, mobile first
- **On-site poll** — "What are you looking for today?" on the homepage. The answers are your category taxonomy, in customers' own words
- **Search query log** — what people search for, and what returns nothing
- **Support tickets** — "I couldn't find X on your site" is a navigation finding with a name attached

---

## Diagnosing before recommending

1. **Homepage share of sessions.** If it's small, say so — it caps how much this audit can be worth, and that's honest advice
2. **Source and new/returning split of homepage sessions.** This sets the entire audit's priorities. See Rule 0 in `SKILL.md`
3. **Revenue per homepage session vs. other landing pages**, controlling for source
4. **Product-view rate from homepage**, split by device
5. **Next-page distribution.** Which module is actually carrying discovery? It's often not the one the team thinks
6. **Per-module engagement.** Rank modules. The bottom of that list is your removal candidate list
7. **Per-slide hero engagement**, if a carousel exists
8. **Search usage and zero-result rate**
9. **Popup impressions vs. signups vs. subscriber-suppression rate**
10. **LCP and CLS on the homepage template**, throttled, cache-disabled — the hero is usually the culprit

Then write the audit against what you found, and label which findings came from data and which from the structural walk.

---

## Setup notes

- **GA4** gives landing-page reports and path exploration out of the box; everything diagnostic above (module views, slide views, search zero-results, popup impressions) needs adding
- **Shopify** confirms stock status on homepage-featured products — this is how you catch merchandising decay programmatically rather than by eye
- **Hotjar** for scroll maps, click maps, and filtered recordings. The single fastest way to find dead modules
- **Site search analytics** may live in the search app (Searchanise, Algolia, Klevu) rather than in GA4 — pull it deliberately
- Homepage tests usually need to run at the **template level** with segment analysis after, not as a single blended test

See `tools/integrations/` for per-tool setup, `../../analytics/SKILL.md` for the broader plan, `../../product-page-cro/references/measurement.md` for the PDP events downstream, and `../../checkout-cro/references/measurement.md` for the checkout events after that.
