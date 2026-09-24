# Viewport Protocol and Capture Discipline

How to drive the page so every finding is anchored to something you actually saw.

---

## Browser setup

**Preferred:** Playwright MCP or Chrome DevTools MCP, driving the real page.

**Acceptable:** a short local Playwright or Puppeteer script that navigates, resizes, screenshots, and dumps console output.

```js
// Minimal capture script — adapt the URL and output path
import { chromium } from 'playwright';

const TIERS = [375, 768, 1024, 1440, 1920];
const URL = process.argv[2];

const browser = await chromium.launch();
const page = await browser.newPage();

page.on('console', m => console.log(`[${m.type()}] ${m.text()}`));
page.on('requestfailed', r => console.log(`[failed] ${r.url()}`));

await page.goto(URL, { waitUntil: 'networkidle' });

for (const width of TIERS) {
  await page.setViewportSize({ width, height: width < 500 ? 812 : 900 });
  await page.screenshot({ path: `audit-${width}.png`, fullPage: true });
  // Horizontal overflow check — a Blocker on mobile
  const overflow = await page.evaluate(() =>
    document.documentElement.scrollWidth > document.documentElement.clientWidth
  );
  console.log(`${width}px — horizontal overflow: ${overflow}`);
}

await browser.close();
```

In this environment Chromium is pre-installed at `/opt/pw-browsers/chromium` with `PLAYWRIGHT_BROWSERS_PATH` already set — do not run `playwright install`.

---

## Viewport tiers

| Width | Represents | What breaks here most often |
|---|---|---|
| **375** | Small phone (iPhone SE / mini) | Horizontal overflow, tap targets, text over hero images, CTA below the reachable zone, keyboard-obscured errors |
| **768** | Tablet portrait / large phone landscape | The gap between the mobile and desktop breakpoint — often untested and visibly broken |
| **1024** | Small laptop | Nav collapsing too early or too late, cramped multi-column layouts |
| **1440** | Standard desktop | The design's intended state; your baseline |
| **1920** | Wide desktop | Unconstrained max-width, hero images stretching, text lines exceeding readable measure |

375 and 768 find the most real defects. 1920 finds the ones nobody has ever looked at.

Test a **taller-but-narrow** state too (375×667) — content that fits at 812px height frequently pushes the CTA out of reach at 667px.

---

## What to capture at each tier

1. **Full-page screenshot**
2. **Above-the-fold screenshot** — what a visitor sees before scrolling is the conversion-critical frame
3. **Horizontal overflow boolean** — `scrollWidth > clientWidth` on `documentElement`. Any `true` on mobile is a Blocker
4. **Console output** — errors, warnings, failed requests
5. **The primary CTA's position and size** — is it above the fold? Is it at least 44×44px?

---

## Interaction states to exercise

Static screenshots miss most real defects. Drive the page:

| State | How to trigger | What to check |
|---|---|---|
| Hover | `page.hover()` on every interactive element | Feedback exists and is not the *only* affordance |
| Focus | `page.keyboard.press('Tab')` repeatedly | Visible ring, logical order, no trap, no invisible focused element |
| Active | Click and hold | Distinct from hover |
| Disabled | Find disabled controls | Visually distinct, and contrast still legible |
| Loading | Throttle to Slow 4G, then act | Skeleton or spinner, not a frozen UI |
| Empty | Clear inputs, filter to nothing | An empty state exists, not a blank panel |
| Error | Submit an invalid form | Inline, adjacent, actionable; field contents preserved |
| Double-submit | Click submit twice fast | Guarded, not two orders or two signups |

---

## Network and motion conditions

- **Slow 4G throttle** for the whole Phase 5 pass. Most performance defects are invisible on a fast connection
- **`prefers-reduced-motion: reduce`** — set it and reload. Animations should stop and content should render in its final readable state, not disappear. A scroll-triggered reveal that never fires under reduced motion is a Blocker: the content is simply gone
- **Cache-disabled first load** — this is what a new visitor gets, and it's the one that matters for LCP
- **In-app browser emulation** where paid social is a significant traffic source. Instagram, Facebook, and TikTok webviews break wallets, autofill, and some JS APIs. Emulate the user agent if you can't test the real thing, and flag it as partial coverage

---

## Auditing without a browser

State the limitation at the top of the report, then extract what you legitimately can.

**From static markup you can verify:**
- Missing `alt` attributes
- Form inputs with no associated `<label>`
- Heading order and whether there's exactly one `h1`
- Missing landmarks (`main`, `nav`, `header`, `footer`)
- `type="number"` on postal code or card fields
- Missing `autocomplete` and `inputmode` attributes
- Missing `lang` on `<html>`
- Viewport meta tag absent, or `user-scalable=no` (an accessibility failure)
- Fixed pixel widths and absolute positioning likely to overflow
- Hero images served at full resolution with no `srcset`
- Render-blocking scripts in `<head>`
- Colour token values you can compute contrast ratios from

**What you cannot verify without rendering** — mark all of these **not tested**:
- Actual computed contrast (CSS cascade, opacity, and background images all change it)
- Focus visibility and tab order
- Layout at any specific viewport
- Real LCP, CLS, INP
- Whether interactions work
- Anything about states

Do not convert "the markup suggests this might be a problem" into a finding. Write it as a check the user should run, and say what would confirm it.
