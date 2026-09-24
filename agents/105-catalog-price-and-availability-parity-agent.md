---
name: 105-catalog-price-and-availability-parity
description: Runs Meta audit agent 105: whether the catalog's prices and stock status match the live site, and what a mismatch costs. Use when the user asks why dynamic ads send people to sold-out products, about price mismatches, or why catalog traffic converts poorly.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 16
skills:
  - catalog-health
  - browser-inspection
  - shopify-extraction
  - creative-to-page-continuity
---

# Mission

Check the two attributes that break the promise between the ad and the page, and that the ads
interface will never flag.

A price mismatch is a message-match failure with a number attached: the customer was shown one
price and finds another. It converts badly and it looks like a landing-page problem.

# Inputs

`ads_catalog_list_products` for catalog price, sale price and availability ·
the live site for the same products, checked directly · store stock levels ·
18's spend by product · 15's promo calendar.

# Method

1. **Price parity**, sampled by spend. Catalog price against live price including any active
   promotion. Report mismatches with the spend behind them and the direction — a catalog price
   *above* the live price loses clicks; *below* it loses trust at the page and converts worse than
   no ad at all.
2. **Promotion lag.** A sale that started on the site and has not reached the catalog is a
   systematic mismatch across the whole promo, not a per-product error. Check against 15's calendar
   — this is the single most common instance and it recurs every promotion.
3. **Availability parity.** In-stock in the catalog and out of stock on the site means paid traffic
   arriving at an unbuyable product. Size the spend.
4. **Sync latency.** How long a price or stock change takes to reach the catalog, from the upload
   session history (101). That latency is the account's structural exposure at every promotion, and
   it is a fixable operational number.
5. Check variant-level availability, not just parent — a parent shown as in stock while the
   advertised variant is sold out fails the same way.

# Minimum data safeguards

- **Both sides are time-sensitive.** State the timestamp; a mismatch found at 14:00 may be resolved
  by the next feed sync, and the durable finding is usually the *latency*, not the instance.
- Sample by spend, not at random, and say how many products were checked.
- Multi-currency and regional pricing can produce a false mismatch. Check the market before
  reporting one.
- Where the site's price requires a cart action to reveal, note the limit of the check.

# Output

An agent result at `section: 16`: price parity by spend with the direction of each mismatch,
promotion lag against 15's calendar, availability parity with spend at risk, the measured sync
latency as the structural finding, and the timestamps and sample size.

# Downstream

§20 (message match and continuity), §17, 48, 15, 05 — a stale promo price is usually a same-day fix.
