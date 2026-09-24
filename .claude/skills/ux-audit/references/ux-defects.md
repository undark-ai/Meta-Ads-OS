# UX Defect Catalog

Defects by category, each with the conversion cost that justifies fixing it. Use this as the sweep list during the seven-phase review — but only report what you observed.

---

## Responsive and layout

| Defect | Why it costs conversions | Severity |
|---|---|---|
| Horizontal page scroll at 375px | Content is cut off and the page feels broken; a strong bounce signal | Blocker |
| Content clipped or overlapping at any tier | Copy and CTAs become unreadable | Blocker |
| CTA not reachable above the fold on mobile | Visitors leave before finding the action | High |
| Untested 768px breakpoint | A visibly broken layout on tablets and landscape phones | High |
| No `max-width` on text at 1920px | Line lengths past ~75 characters measurably slow reading | Medium |
| Sticky nav overlapping the first section | Hides the headline — the most important content on the page | High |
| Fixed pixel widths on containers | Overflow at small viewports | High |
| Tables overflowing without a scroll container | Data is unreachable; the page scrolls sideways | High |
| Hero image shrinking rather than reflowing/cropping | Faces and product detail become unreadable at mobile size | Medium |
| Inconsistent spacing rhythm | Reads as unfinished; erodes trust in higher-consideration purchases | Medium |
| Misalignment against the grid | Same | Nit to Medium |

**Check first:** `documentElement.scrollWidth > clientWidth` at 375px. Fastest high-value check in the whole audit.

---

## Touch and pointer

| Defect | Cost | Severity |
|---|---|---|
| Tap targets under 44×44px | Mis-taps on the primary action; directly lost conversions | Blocker on a CTA, High elsewhere |
| Adjacent targets with no spacing | Wrong-element taps, especially on plan selectors and quantity steppers | High |
| Hover-only affordances | Do not exist on touch — the feature is simply invisible | Blocker if it gates conversion |
| Drag/swipe with no button or keyboard alternative | Excludes touch-limited and keyboard users; carousels and comparison sliders are the usual culprits | High |
| Interactive elements within 8px of the screen edge | Triggers browser back-swipe instead | Medium |
| CTA under the browser chrome or safe-area inset | The button exists but can't be tapped | Blocker |

---

## Forms

| Defect | Cost | Severity |
|---|---|---|
| Missing or placeholder-only labels | Fields become ambiguous once typing starts; abandonment rises | Blocker |
| Wrong `inputmode` / missing `autocomplete` | Every field costs more typing on mobile; one of the largest mobile conversion factors | High |
| `type="number"` on postal code, phone, or card fields | Breaks leading zeros and international formats, adds spinner arrows | High |
| Validation on every keystroke | Reads as being scolded mid-thought | Medium |
| Errors only on submit, at the top of the page | The user must hunt for what failed | High |
| Error messages hidden behind the mobile keyboard | The user cannot see why the form failed — an invisible dead end | Blocker |
| Field contents cleared on error | The most reliable form-abandonment cause there is | Blocker |
| No feedback on submit | Double submissions, or a user who assumes it failed and leaves | High |
| Unguarded double-submit | Duplicate orders or signups; support cost | High |
| Custom inputs that defeat browser autofill | Silently multiplies typing cost on mobile | High |
| Required fields marked by colour alone | Invisible to colour-blind users | High |
| No visible progress indicator on multi-step forms | Perceived length rises; drop-off with it | Medium |

For checkout-specific form guidance see `../../checkout-cro/references/form-fields.md`.

---

## Feedback and state

| Defect | Cost | Severity |
|---|---|---|
| No loading state on async actions | The user assumes the click failed and clicks again, or leaves | High |
| Blank panel instead of an empty state | Reads as broken | High |
| Unhandled error state | Dead end with no recovery path | Blocker |
| No confirmation after a successful action | Uncertainty; repeat submissions; support tickets | High |
| Optimistic UI that silently reverts | Destroys trust in whether anything saved | High |
| Destructive actions with no confirmation | Data loss | High |
| No visible active/current state in navigation | Users lose their place in longer flows | Medium |

---

## Interaction and navigation

| Defect | Cost | Severity |
|---|---|---|
| Click-only `<div>`s instead of buttons/links | Unreachable by keyboard, invisible to assistive tech, unopenable in a new tab | Blocker |
| Browser back button broken by client routing | A top-three cause of session abandonment in SPAs | Blocker |
| No deep-linkable URL for a shareable state | Kills sharing and paid-traffic landing precision | Medium |
| Navigation not collapsing on mobile | Consumes the entire above-the-fold area | High |
| Competing primary CTAs | Split attention lowers action rate | High |
| Full site navigation inside a conversion flow | A leak out of the funnel at the worst moment | High |
| Modal that can't be dismissed by Esc or overlay click | Feels like a trap; drives exits | High |
| Interstitial appearing before the page is read | Bounce | High |

---

## Typography and content

| Defect | Cost | Severity |
|---|---|---|
| Body text under 16px on mobile | Triggers iOS zoom-on-focus and hurts readability | High |
| Line length beyond ~75 characters | Measurably slower reading, higher abandonment on long pages | Medium |
| Line height below ~1.4 for body copy | Dense, tiring blocks people skip | Medium |
| Inconsistent type scale | Breaks the hierarchy that guides scanning | Medium |
| Text baked into images | Not zoomable, translatable, selectable, or readable by assistive tech | High |
| Light-grey body text | Fails contrast and gets skipped | High |
| All-caps for more than a few words | Slows reading noticeably | Nit |
| Justified text on the web | Creates rivers of whitespace, harder for dyslexic readers | Nit |

---

## Animation and motion

| Defect | Cost | Severity |
|---|---|---|
| Content that only appears via scroll animation | Invisible under reduced motion, and to anyone whose script fails — the content is gone | Blocker |
| `prefers-reduced-motion` ignored | Accessibility failure; physical discomfort for some users | High |
| More than 1–2 animated elements per viewport | Splits attention away from the CTA | Medium |
| Scroll-jacking | Removes user control of their own scroll; strong exit driver | High |
| Motion that doesn't pause when off-screen or hidden | Battery and CPU cost, especially on mobile | Medium |
| Auto-rotating carousel with no pause control | Content vanishes mid-read | High |
| Transitions long enough to feel laggy | Perceived slowness on every interaction | Medium |

---

## Performance

Performance is a conversion lever, not an engineering concern. Measure it, don't estimate it.

| Metric | Good | Needs work | Poor |
|---|---|---|---|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | 2.5–4.0s | > 4.0s |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | 0.1–0.25 | > 0.25 |
| **INP** (Interaction to Next Paint) | ≤ 200ms | 200–500ms | > 500ms |

Measure on a **throttled connection with cache disabled** — that's the new visitor from a paid ad, who is the visitor that matters.

Common causes, in the order they usually turn out to be responsible:

1. **Unoptimized hero image.** A 3MB PNG where a 120KB WebP would do. Usually the single biggest LCP contributor on marketing pages. Check for `srcset`, modern formats, correct intrinsic dimensions, and `loading="eager"`/`fetchpriority="high"` on the LCP image specifically
2. **Render-blocking scripts in `<head>`.** Tag managers, chat widgets, A/B testing snippets, and font loaders
3. **Layout shift from late-loading content.** Images and iframes without width/height, injected banners and cookie bars, web fonts swapping without `font-display: optional`/`swap` plus a matched fallback metric, and A/B test flicker
4. **Third-party scripts.** Chat, analytics, heatmaps, ad pixels — count them. Ten tags is common and rarely justified. Each one is main-thread time
5. **Fonts.** Multiple families and weights, no preload, no subsetting
6. **Unused JavaScript.** A full framework bundle for a static landing page
7. **No caching or CDN** on static assets

**An A/B testing tool causing a visible flicker of the original content is a Blocker** — it undermines both conversion and the validity of the tests it's running.

---

## Search and discovery

| Defect | Cost | Severity |
|---|---|---|
| No zero-results state with a recovery path | Dead end at high purchase intent | High |
| No suggestions or autocomplete on a large catalogue | Users can't find what they'd have bought | Medium |
| Search that doesn't tolerate typos or synonyms | Same | Medium |
| Filters that reset on back-navigation | Forces the whole task to be repeated | High |

---

## Reporting scale

Right-size the report to the ask:

- **"Review this page"** → the seven phases, all viewports, full report
- **"Check this on mobile"** → 375 and 768, plus the touch, forms, and performance categories
- **"Is this accessible?"** → the keyboard pass, contrast, semantics, and forms, reported against WCAG criteria
- **"Review my PR / this change"** → scope to what the change touched, plus a responsive and keyboard pass on the affected components
- **"Why is this page slow?"** → the performance section only, measured, with the cause ranked

In every case, lead with the fixes most likely to move the primary conversion action.
