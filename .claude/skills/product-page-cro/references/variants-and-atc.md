# Variants and the Add-to-Cart Module

The conversion module. Everything above it persuades; this is where the shopper acts — and where confusion converts into either abandonment or a return.

---

## Variant selection

### Control type

| Option | Use | Avoid |
|---|---|---|
| **Swatches** | Colour, material, finish — anything visual | A dropdown listing colour names. Shoppers buy the colour they can see |
| **Chips / buttons** | Size, capacity, model, quantity tiers — up to ~8 options | Dropdowns for small option sets; they hide the choice and add a tap |
| **Dropdown** | Genuinely long lists (30+ sizes, model years) | Anything under 8 options |
| **Guided finder** | Compatibility, fit, or configuration with real complexity | Making the shopper cross-reference a spec table themselves |

Dropdowns for colour and size are one of the most common PDP defects, and the cost is highest on mobile where each one adds a native picker round-trip.

### What to check for every option

| Check | The failure |
|---|---|
| Label clarity | "Style A / Style B" — meaningless. Name what differs |
| Sensible default | Nothing preselected, forcing an extra decision; or the least popular variant defaulted |
| Visible consequence | Shopper can't tell what changes when they pick |
| Price updates | Price doesn't move when a more expensive variant is selected — a trust break at checkout |
| Availability per option | Out-of-stock variants look identical to available ones until the shopper commits |
| Gallery updates | Selecting "Navy" leaves a green product on screen |
| URL updates | No deep-linkable variant URL, so the shopper can't share or return to their selection, and paid traffic can't land on the right variant |
| Back-navigation | Selection lost on browser back |
| Jargon explained | Technical option names with no inline help |
| Error prevention | Nothing stops an impossible or incompatible combination |

### Sizing, fit, and compatibility

These are conversion **and** margin levers — a sizing failure converts today and returns next week.

- Size guide accessible inline, without leaving the page or opening a PDF
- Measurements in the shopper's units, with a way to switch
- Model height and worn size stated on apparel imagery
- Review-sourced fit signal where volume allows ("runs small" is the single most useful sentence on an apparel PDP)
- Compatibility checkers for technical products, not a spec table the shopper must interpret
- Fit or sizing recommendations based on a couple of inputs, where the catalogue justifies building it

**Check return reasons before recommending here.** If "wrong size" or "didn't fit" dominates, the sizing experience is the highest-value item in the whole audit, ahead of anything cosmetic.

---

## Stock and availability states

Most PDPs handle "in stock" and fail everything else. Each state needs a deliberate design.

| State | What the page should do |
|---|---|
| **In stock** | Say so plainly, or say nothing. A green "In stock" badge is fine; it doesn't need emphasis |
| **Low stock** | Show a count **only if it's real and live**. An invented "Only 3 left!" is a fabricated scarcity claim — a trust liability and a regulatory risk in several jurisdictions |
| **Out of stock (this variant)** | Keep the variant visible but clearly marked. Offer back-in-stock notification capture. Suggest the nearest available variant |
| **Out of stock (all variants)** | Never a dead end. Capture an email for restock, show genuinely similar products, state an expected date if known |
| **Backorder / preorder** | State the ship date explicitly, before add-to-cart, not in the confirmation email |
| **Discontinued** | Redirect or replace with the successor product, and say so. Do not leave an orphan PDP |

Out-of-stock handling is one of the most commonly neglected and highest-ROI areas on a PDP. Every out-of-stock visit that ends without a captured email or a redirected shopper is fully paid-for traffic thrown away.

---

## The add-to-cart module

### Checklist

| Element | What good looks like |
|---|---|
| **Primary CTA** | One unmistakable action. High contrast, full width on mobile, ≥44px tall |
| **CTA copy** | "Add to cart" is a safe default. "Add to bag" if the brand uses it consistently. Avoid vague ("Select") and avoid over-commitment framing where the purchase is considered |
| **Buy Now** | Only when it genuinely shortens the path (express wallet straight to payment). Two competing buttons split attention — if both exist, one must be visually secondary |
| **Quantity** | Stepper, not a free text field. Sensible min/max tied to real stock. Hide it entirely where quantity is almost always one |
| **Price** | Adjacent to the CTA and reflecting the selected variant, including any subscription or bundle discount |
| **Stock status** | Visible before the click, per selected variant |
| **Delivery estimate** | A date, not "3–5 business days." "Order in the next 4 hours for Tuesday delivery" beats a countdown badge, and it's honest |
| **Shipping cost** | Cost or free-shipping threshold visible here. Shipping first discovered at checkout is a PDP failure that gets recorded as checkout abandonment |
| **Returns** | Window and whether returns are free — one line, adjacent |
| **Payment options** | Wallet and BNPL availability indicated, so affordability is resolved before checkout |

### What happens after the click

The shopper must always know **what happens when I click this**. Audit the confirmation specifically:

| Pattern | Assessment |
|---|---|
| **Cart drawer** | Usually best. Confirms the add, shows the cart, offers a clear path to checkout, keeps browsing possible |
| **Toast / inline confirmation** | Fine for multi-item shopping, but must be unmissable and must not vanish before it's read |
| **Redirect to cart page** | Acceptable, but ends the browsing session — worse for basket-building catalogues |
| **Silent add** | A defect. The shopper cannot tell whether it worked, and re-clicks or leaves |
| **Page jump to top** | A defect, especially on mobile — the shopper loses their place |

Also check: does the drawer cross-sell without obstructing checkout? Is the cart count updated everywhere? Is a double-click guarded against, or does it add two? Does a failed add (stock gone mid-session) surface a clear message, or fail silently?

---

## Sticky CTA

Right on long PDPs, especially mobile. It must:

- Show the **selected variant** and the **current price**, not a generic button
- Appear only after the primary CTA scrolls out of view
- Sit above the safe-area inset on mobile
- Not obscure content — check it against reviews and the footer at 375×667
- Not collide with chat, cookie, or accessibility widgets

A sticky bar that shows "Add to cart" without saying which variant, or that covers the last line of every review, costs more than it earns.

---

## Distractions around the module

Audit everything competing with the CTA at the moment of decision, and decide **keep / reduce / move / remove / test** for each:

| Element | Usual verdict |
|---|---|
| Cross-sell or "complete the look" adjacent to the CTA | **Move** below the decision |
| Promo banner stack above the fold | **Reduce** to one line, or remove |
| Newsletter popup on a PDP | **Remove** or delay past the decision. A discount popup that interrupts an in-progress purchase converts a buyer into a code-hunter |
| Chat bubble overlapping the CTA on mobile | **Move** |
| Multiple secondary CTAs (wishlist, compare, share) | **Reduce** and make visually subordinate |
| Accessibility overlay widget | Keep the button, check it doesn't cover the CTA — and note that overlays are not a substitute for actual accessibility work (see `ux-audit`) |
| Video autoplaying near the CTA | **Test** — it competes for attention at the worst moment |

---

## Subscription and bundle options

Where offered, check:

- The default is honest. Pre-selecting subscribe-and-save without making one-time purchase equally visible is a dark pattern, and it generates cancellations and chargebacks
- The saving is stated in both percentage and absolute terms
- Cancellation terms are visible **before** add-to-cart, not buried in terms
- Bundle pricing shows the component prices so the saving is verifiable
- Bundle and quantity discounts don't create a decision so complex it slows the purchase (Hick's Law)

Where the default state, framing, or cancellation terms are in question, write **Legal review required** alongside the UX recommendation — subscription auto-renewal disclosure is regulated in the US, UK, and EU.
