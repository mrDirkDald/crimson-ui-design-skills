---
name: crimson-ui-web
description: Browser sites, web apps, SaaS, PWA, responsive web behavior, forms, navigation, and web-specific UX.
---

# Web

Use for browser-rendered products.


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
Load `../../references/web-reference-corpus.md` only for meaningful redesign, beautiful/premium/studio-quality briefs, or reference-led direction.

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
