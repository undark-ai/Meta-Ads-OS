# Discovery, Navigation, and Merchandising

Getting the visitor from "I'm interested" to the right product page. On a brand-search-heavy homepage this is most of the job.

---

## Navigation

| Check | The failure to look for |
|---|---|
| **Information scent** | "Shop," "Collections," "The Range" — labels that don't say what's behind them |
| **Depth** | More than two levels before reaching products. Every level loses people |
| **Breadth** | More than about 7 top-level items. Hick's Law applies to navigation before anywhere else |
| **Category clarity** | Internal business structure exposed as customer-facing labels |
| **Overlap** | "Best Sellers," "Popular," and "Featured" as three separate destinations with the same products |
| **Sale placement** | A prominent "Sale" item trains every visitor to shop only on discount. On a premium brand this is a pricing-power leak |
| **Mobile menu** | Not reachable in one tap, or three levels deep, or search absent from inside it |
| **Mega-menu on mobile** | A desktop mega-menu reflowed into an unusable accordion tower |
| **Account and cart** | Not obvious, or cart count not updating |

### Search

Search deserves its own attention on a homepage audit, and most audits skip it. On brand-search and returning-visitor traffic, site search is a **primary** path — these visitors arrive knowing what they want.

- Is the search input **visible**, or hidden behind an icon? Visible input raises usage materially
- Does it tolerate typos and synonyms?
- Does it suggest products, or only return a results page?
- **What does the zero-results state do?** A dead end here loses a visitor at the highest intent on the site. It should offer suggestions, popular products, and a working route onward
- Is search usage and zero-result rate even tracked? Search queries are the cheapest customer-research data a store owns, and the queries with no results are a product and a taxonomy roadmap

---

## Category architecture

The question is whether the catalogue is organized **the way customers shop** or **the way the business is organized internally**. Internal structure leaking into navigation is one of the most common and most costly homepage problems.

| Taxonomy | Example | Fits when |
|---|---|---|
| **Product-based** | Shirts / Shoes / Bags | Customers arrive knowing the product type. Default for familiar categories |
| **Need-based** | Travel / Work / Everyday | The same product serves different situations, and the situation drives the choice |
| **Outcome-based** | Stay organized / Sleep better / Perform harder | The product is a means to an end the customer cares about more than the object |
| **Customer-based** | For Men / For Women / For Professionals | Fit or suitability genuinely differs by segment |
| **Collection-based** | New / Best Sellers / Essentials | Returning visitors and browse-led shopping. Works best *alongside* another taxonomy, not instead of one |

**Most D2C homepages should offer two routes, not one:** a primary taxonomy for people who know what they want, plus a secondary need- or outcome-based route for people who don't. Offering five parallel taxonomies is the same failure as offering none — the visitor can't tell which one to use.

How to choose: use search query data and the actual language in reviews and support tickets. If customers search "waterproof jacket for commuting," a need-based route matching that phrasing will beat a product grid.

---

## Discovery modules

Rank these by what they actually do, and cut the ones doing nothing.

| Module | Job | When it earns its place |
|---|---|---|
| **Category tiles** | Route to the right section | Almost always, on any catalogue above a handful of SKUs. The workhorse |
| **Best sellers** | Discovery plus social proof in one | Almost always. Real bestsellers, not manually curated favourites |
| **New arrivals** | The reason returning visitors came back | High repeat-purchase or seasonal brands. **Must actually be new** |
| **Shop by need / use case** | A second route for undecided visitors | Where the same product serves multiple situations |
| **Bundles / sets** | Raise AOV and simplify choice | Where the products genuinely go together |
| **Featured collection** | Merchandise a campaign or season | When there's a real campaign. Not as permanent furniture |
| **Personalized recommendations** | Relevance for returning visitors | Only with enough data to beat bestsellers. Otherwise it's a worse bestsellers module |
| **Quiz / product finder** | Configuration or fit complexity | Where choice is genuinely hard. A quiz for three SKUs is friction dressed as helpfulness |
| **Reorder / subscribe** | Returning-customer speed | Consumables, subscriptions, high repeat rate. **The most commonly missing module** |

**Answer this directly: can a visitor tell "where do I start?"** If the homepage offers a hero, four parallel taxonomies, two grids, and a quiz, the answer is no — and the fix is subtraction.

### Horizontal carousels in discovery modules

Same problem as hero carousels, smaller stakes. Items off-screen get very little engagement. On mobile, a 2-up grid usually outperforms a horizontal strip. If a carousel stays: show a partial next item so scrollability is discoverable, provide previous/next buttons and keyboard access as an alternative to swiping, and never auto-rotate.

---

## Product cards

Cards on the homepage are doing PDP-preview work. Audit them as a unit.

| Element | What good looks like |
|---|---|
| **Image** | Consistent treatment across the grid. One inconsistent card makes the whole grid look unmanaged |
| **Second image on hover/tap** | Useful — but must not be the only way to see an important angle |
| **Product name** | Comprehensible without category context. Internal style names alone fail |
| **Price** | Always visible. Sale price with the original only where the reference-price claim is substantiated — see the compliance note in `trust-and-promotions.md` |
| **Rating + review count** | Present on cards where volume supports it. One of the cheapest conversion additions to a grid |
| **Colour / variant swatches** | Shown where variants matter, and reflecting real availability |
| **Badges** | Sparingly. "Best seller" on eight of nine cards means nothing |
| **Quick add** | Good for repeat and low-consideration purchases. Poor where a variant must be chosen — a quick add that silently picks a size causes returns |
| **Quick view** | Useful on larger catalogues. Must be dismissible and keyboard-accessible |
| **Out of stock** | Marked clearly, not hidden and not silently linking to a dead PDP |
| **Tap target** | The whole card, not just the title |

Consistency matters more than any individual element. A grid where three cards have ratings and six don't reads as broken rather than selective.

---

## Merchandising freshness and decay

The most commonly missed finding in homepage audits, because reviewers look at design and not at operations. Every one of these is a live revenue leak:

| Decay | Cost |
|---|---|
| Hero product out of stock or discontinued | Paid and brand traffic routed to a dead end |
| Expired promo bar | Broken promise; support tickets; trust damage |
| "New Arrivals" months old | Returning visitors — the module's whole audience — see nothing new and stop checking |
| Wrong-season creative | Reads as abandoned, undermining every trust signal on the page |
| Sold-out featured collection | Same as the hero problem, one click deeper |
| Dead or redirecting nav links | Direct loss at high intent |
| Stale press or awards ("As seen in… 2019") | Ageing proof reads as declining relevance |
| Unverified counts ("Join 50,000 customers") | Undated numbers age badly and become misleading |

Do not report these as one-off fixes. **Recommend a maintenance cadence with a named owner** — a weekly stock-and-promo check on homepage-featured items, and a monthly creative and proof review. This recurs because nobody owns it, and a fix without an owner is a fix that decays again in six weeks.

Where the platform supports it, recommend automating the highest-risk case: hide or swap homepage modules automatically when featured products go out of stock.
