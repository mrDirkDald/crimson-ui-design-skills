---
name: crimson-ui-web
description: Browser sites, web apps, SaaS, PWA, responsive web behavior, forms, navigation, and web-specific UX.
---

# Web

Use for browser-rendered products.


## Deep aspect subskills

This parent skill owns the broad domain. For MAX-depth work, load one or more aspect subskills below whenever they materially affect the decision.

MAX mode does **not** impose a one-aspect limit. It is acceptable to load several aspect subskills for a genuinely cross-cutting task, but each loaded aspect must have a clear reason.

| Aspect | Load | Purpose |
|---|---|---|
| Responsive Layout | `aspects/responsive-layout/SKILL.md` | Recompose web interfaces across widths rather than shrinking or vertically stacking desktop blindly. |
| Navigation and Routing | `aspects/navigation-routing/SKILL.md` | Make location, history, back behavior, deep links, and route transitions predictable. |
| Forms and Validation | `aspects/forms-validation/SKILL.md` | Design web forms that preserve user input, explain errors, and prevent duplicate or ambiguous submission. |
| Data-Dense Web Interfaces | `aspects/data-dense-web/SKILL.md` | Design tables, dashboards, filters, charts, and dense web workspaces without turning everything into cards. |
| Web State and Feedback | `aspects/web-state-feedback/SKILL.md` | Make async actions, optimistic updates, loading, retry, offline, and stale states understandable. |
| Web Performance as Design | `aspects/web-performance-design/SKILL.md` | Keep motion, media, fonts, hydration, and layout complexity from degrading the user experience. |

### Aspect loading rule

Use the parent skill first, then load:
- one aspect for a focused deep problem;
- several aspects when root causes cross boundaries;
- the owner reference(s) when implementation or verification requires more complete detail.

Do not replace an aspect subskill with generic advice if the task clearly belongs to that aspect.

## Owner reference

`../../references/web.md`

Load it for TIER 1+ work or when any trigger below is true.

### Escalation triggers
- responsive behavior is material;
- forms/navigation/data visualization need detailed treatment;
- browser conventions affect the result;

For TIER 0 local fixes, do not open it unless needed.

## Read budget
Primary reference: `../../references/web.md`.
Load `../../references/typescript-tailwind.md` only if implementation architecture/Tailwind/TypeScript details matter.
Load expressive-web only when the brief explicitly calls for expressive/award-like behavior.

## Focus
- responsive reflow/reprioritization;
- navigation/history behavior;
- forms and validation;
- loading/error/empty states;
- keyboard/focus behavior;
- data tables/charts;
- browser conventions;
- performance-sensitive visual decisions.

Do not read native-app references merely because the UI resembles desktop software.

## Responsive
Do not treat mobile as desktop stacked vertically.
Reprioritize and preserve task order.

## Data color
Use categorical, sequential, and diverging palettes according to data semantics.
Do not use color alone for critical category distinction.

## Implementation
If TypeScript/Tailwind matters, route to `../implementation/SKILL.md`.
