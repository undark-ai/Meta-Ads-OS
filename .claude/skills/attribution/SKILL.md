---
name: attribution
description: When deciding which attribution window and model a Meta account should run on, and reconciling Meta's view against GA4, the commerce platform and the CRM. Use when the user asks "which attribution window," "7-day click or 1-day," "Meta vs GA4," "should I use view-through," "data-driven attribution," or "who gets credit for this sale." For whether Meta caused the sale at all, see incrementality. For the modelling inside Meta's number, see modeled-conversions.
---
# Attribution

Attribution answers *who gets credit*. It does not answer *what caused the sale* — that is
`incrementality`, and conflating the two is the most expensive confusion in paid media.

An account can have flawless attribution and be wasting half its budget on demand it would have
captured anyway.

## Choosing the window

Meta's default is 7-day click, 1-day view. Match the window to the actual purchase cycle rather
than accepting the default:

| Purchase cycle | Window | Reasoning |
|---|---|---|
| Impulse, under ~€50 | 1-day click, or 7-day click | Most purchases happen same-session; a long window credits coincidence |
| Considered, €50–€300 | 7-day click | The default earns its place here |
| High-consideration, €300+ | 7-day click, and acknowledge under-crediting | Meta's maximum is shorter than the real cycle; the account is systematically under-credited and should know it |

Three rules regardless:

1. **One window per run.** A 7-day-click figure and a 7-day-click-1-day-view figure measure
 different things.
2. **A window change invalidates period comparisons.** Check
 `ads_account_get_activity_logs` before comparing across one.
3. **A longer window raises ROAS without anything improving.** When someone reports an
 improvement, check the window first.

## View-through, separately

Always reported separately from click-through. A blended figure that silently includes
view-through is not comparable to anything, and it is the number most often used to justify
retargeting spend.

On prospecting, view-through may capture real influence. On retargeting it is largely people who
were going to buy anyway. Either way it is an incrementality question, and until §26 answers it,
view-through-inclusive claims are `INFERRED` at best.

## Why Meta and GA4 disagree

They will never match, and the audit's job is to say *why* rather than to pick one.

| Difference | Meta | GA4 |
|---|---|---|
| Model | Last-touch within Meta's own window | Data-driven across all channels by default |
| View-through | Included by default | Not counted |
| Modelling | Fills ATT gaps statistically | Models its own gaps differently |
| Scope | Only Meta-attributed | All channels, so Meta gets a smaller share |
| Identity | Meta's graph, cross-device | Client id / user id, weaker cross-device |

Meta claiming more than GA4 attributes to it is **expected**, not a defect. The finding is when
the size of the gap changes, or when the gap cannot be explained by these differences at all.

## The hierarchy

```
Did money arrive? → the commerce platform. Authoritative.
How many orders? → the commerce platform. Authoritative.
Which channel influenced? → GA4 (or the analytics layer). Directional.
Did Meta cause it? → incrementality testing. Nothing else answers this.
What did Meta claim? → Meta. A claim, never banked revenue.
```

Never present Meta-claimed value as banked revenue. Where both appear in one table, label them.

## Untagged traffic breaks all of it

If §2 finds paid clicks reaching the store without UTMs, first-party data cannot separate paid
from organic at all. Meta's claim share then becomes an **upper bound, not a measurement**, and
that qualifier travels everywhere it appears.

This is common, and the honest statement is narrow: the claim cannot be checked, here is what it
would take. Not "your ROAS is overstated" — which is a claim the audit cannot support either.

## Output

For §25: the current window and model, whether they fit the purchase cycle, the view-through
share, the modelled share, the Meta/GA4/store comparison from §3 with its explanation, and one
recommendation on the window.

Where the recommendation is to change the window, state that it will change reported ROAS
without changing performance, and that period comparisons across the change are invalid.
