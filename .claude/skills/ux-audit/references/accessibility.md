# Accessibility Checklist (WCAG 2.1 AA)

Scoped to what actually appears on marketing pages, signup flows, and checkouts. Every item here is also a conversion item — this is not a compliance appendix.

Rank these inside the main severity list, not in a separate section. A missing form label is a Blocker whether or not the user asked about accessibility.

---

## The keyboard pass

Do this first. It takes two minutes and finds the most Blockers.

Press Tab from the top of the page to the bottom.

| Check | Failure severity |
|---|---|
| Focus indicator is visible on every focusable element | **Blocker** — `outline: none` with no replacement is the single most common serious failure |
| Tab order follows visual reading order | **High** |
| No keyboard trap — you can always Tab out, and Esc closes modals | **Blocker** |
| Modals move focus in on open and return it on close | **High** |
| Focus is never on an invisible or off-screen element | **High** |
| Every interactive element is reachable — no click-only `<div>`s | **Blocker** |
| Skip-to-content link exists on pages with long navigation | **Medium** |
| Custom dropdowns, carousels, and accordions are operable by keyboard | **Blocker** if they gate conversion |

`tabindex` values above 0 are almost always a bug. Fix DOM order instead.

---

## Contrast

Measure it; don't eyeball it. Opacity, gradients, and background images all change the real ratio.

| Content | AA minimum |
|---|---|
| Body text | **4.5:1** |
| Large text (18pt+ / 14pt+ bold) | **3:1** |
| UI component boundaries and graphical objects | **3:1** |
| Focus indicators | **3:1** against adjacent colours |
| Disabled controls | Exempt, but still legible in practice |

The recurring offenders on marketing pages:

- Grey body text on white — `#999` on `#fff` is 2.85:1 and fails
- White or light text over a hero photo, where contrast varies across the image and fails somewhere
- Placeholder text used as the field label, typically 2–3:1
- CTA label text against the button fill — check this specifically; it's the most consequential single ratio on the page
- Light-grey borders on form inputs, failing the 3:1 component requirement
- Brand colours that pass in the design file and fail after an opacity value is applied

Do not inflate the bar. AA is 4.5:1 for body text. Require 7:1 only when the user has an explicit AAA target — over-specifying costs credibility on the findings that matter.

---

## Semantic structure

| Check | Notes |
|---|---|
| Exactly one `<h1>` | The page's actual subject, not a logo or a nav item |
| Heading levels don't skip | h2 → h4 with no h3 breaks screen-reader navigation |
| Headings describe content, not styling | Never use a heading tag for visual size alone |
| Landmarks present | `<header>`, `<nav>`, `<main>`, `<footer>` |
| Lists are real lists | `<ul>`/`<ol>`, not `<div>`s with bullet characters |
| Buttons are `<button>`, links are `<a>` | A `<div onClick>` is unreachable by keyboard and invisible to assistive tech |
| `lang` set on `<html>` | Affects screen-reader pronunciation |
| Page has a unique, descriptive `<title>` | |

---

## Forms

The highest-conversion-impact accessibility category.

| Check | Failure severity |
|---|---|
| Every input has a programmatically associated `<label>` | **Blocker** |
| Labels remain visible when the field has content | **High** — placeholder-only labels vanish on typing |
| Required fields are marked in text, not by colour alone | **High** |
| Errors are announced (`aria-live` or `role="alert"`) and linked to the field | **High** |
| Error text describes the fix, not just the failure | **High** |
| Field contents survive a validation error | **Blocker** |
| Autocomplete attributes present on identity, address, and payment fields | **High** — a WCAG 2.1 requirement and a large mobile conversion factor |
| Fieldsets and legends group related radios and checkboxes | **Medium** |
| No timeout that can silently discard entered data | **High** |

---

## Images and media

- Meaningful images have descriptive `alt`
- Decorative images have `alt=""` — not a missing attribute, and not a filename
- Text is not baked into images (it can't be zoomed, translated, or read)
- Video has captions; nothing autoplays with sound
- Media has visible, keyboard-operable pause controls
- Icon-only buttons have an accessible name (`aria-label` or visually hidden text)

---

## Motion

- `prefers-reduced-motion: reduce` is respected
- Under reduced motion, scroll-triggered content still renders in its **final readable state**. Content that only appears via animation is content that disappears for these users — a Blocker
- Nothing autoplays motion for more than 5 seconds without a pause control
- No parallax or scroll-jacking that can't be turned off
- No flashing above 3Hz

---

## Touch and zoom

- Tap targets at least **44×44px** with adequate spacing
- Page zooms to 200% without content loss or horizontal scroll
- Viewport meta does **not** contain `user-scalable=no` or `maximum-scale=1` — a Blocker
- Orientation is not locked
- Nothing requires a multi-point or path-based gesture without a single-pointer alternative (drag sliders, before/after comparisons, and swipe carousels all need buttons or keyboard steps)

---

## Content and status

- Link text is meaningful out of context — "Read the 2026 pricing guide," not "Click here"
- Information is never conveyed by colour alone (add an icon, text, or pattern)
- Status changes — cart updates, form success, filter results — are announced via a live region
- Anything opening in a new tab says so

---

## What to report and how

For each failure give: the WCAG criterion, what you observed, the viewport, and the fix.

> **Blocker — Focus indicator removed (2.4.7 Focus Visible).** Tabbing through the pricing page at 1440px shows no visible focus state on any of the three plan CTAs; `outline: none` is applied with no replacement. Keyboard and switch users cannot tell which plan they're about to select. Fix: add a `:focus-visible` ring at 3:1 against the card background.

Don't cite criterion numbers at people who didn't ask for compliance work — lead with the user consequence and put the reference at the end.
