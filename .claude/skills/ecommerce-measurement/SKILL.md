---
name: ecommerce-measurement
description: When judging whether a D2C store's purchase measurement is good enough to optimise on — the GREEN/YELLOW/RED verdict that orders the rest of a Meta audit, and what each verdict permits. Use when the user asks "can I trust these numbers," "is my tracking good enough," "should I fix tracking before scaling," or when section 2 needs to close. For the pixel and CAPI mechanics, see capi-and-emq.
---
# E-commerce measurement verdict

§2 closes with one verdict, and it orders everything after it.

| Verdict | Meaning | What it permits |
|---|---|---|
| **GREEN** | Purchase measurement is trustworthy enough to optimise on | Everything |
| **YELLOW** | Usable with explicit, named caveats | Everything, with the caveat carried on each dependent figure |
| **RED** | Optimisation economics cannot be trusted | Everything except scale and kill calls that depend on conversion value |

**`RED` orders the audit; it does not end it.** Continue every section. Mark affected findings
`DEGRADED`. Waste, structure, creative, catalog, audiences, hygiene and CRO findings are all
still delivered in full — most of them never needed conversion value to begin with.

Ending an audit at a `RED` verdict delivers nothing and is the more common failure. So is
continuing as if the verdict were `GREEN`, which delivers something worse than nothing.

## What drives each verdict

| Signal | GREEN | YELLOW | RED |
|---|---|---|---|
| Purchase event fires once per order | Yes | Minor duplication, quantified | Systematic duplication |
| CAPI active with dedup | Yes, dedup rate high | Active, dedup imperfect | Browser-only, or dedup broken |
| Purchase value correct and consistent | Yes | Minor currency or bundling issues | Wrong value, or missing |
| EMQ | Strong across several keys | Moderate | Weak, email only or worse |
| Domain verified, Purchase priority 1 | Yes | Verified, priority order wrong | Not verified |
| §3 claim ratio after alignment | Explained | Explained with residual | Unexplained and material |
| Paid traffic identifiable at the store | Yes | Partial UTM coverage | Untagged |
| Modelled share | Low and known | Moderate and known | High, or unknown |

Any single `RED` column drives the verdict. These are not weighted and averaged — a correct
value on a duplicated event is still a wrong number.

## The untagged case

If paid clicks reach the store without UTMs, first-party data cannot separate paid from organic
at all. The verdict is `RED`, and Meta's claim share becomes an **upper bound, not a
measurement** — a qualifier that travels everywhere the number appears.

This is the most common `RED` and the most fixable. It is also the one where the audit must be
careful about what it claims: it cannot say the ROAS is overstated, only that the ROAS cannot be
checked, and here is what checking would take.

## Reporting it

State the verdict, the two or three signals that drove it, what it costs in decisions the audit
cannot make, and the shortest path to the next verdict up. "Fix tracking" is not a
recommendation; "add `external_id` and persist `fbc` through the third-party checkout — this
moves EMQ from weak to moderate and should close most of the 1.4 claim ratio" is.
