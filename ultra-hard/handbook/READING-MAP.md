# Reading Map — HARD

HARD is not token-constrained, but indiscriminate loading can still reduce reasoning quality. Load broadly when the problem is broad; keep routing relevant.

## Review-only
`subskills/review/` → visual/color/application/web as evidence requires → QA.

## Beautiful website
`references/web-craft-analysis.md` + `references/skills-sh-patterns.md` + `references/web.md` + `references/visual-direction.md` + `handbook/webcraft/` + real stack/language + `references/visual-qa.md`.

## Expressive website
Add `references/expressive-web.md` + `subskills/expressive-web/` + performance/accessibility webcraft chapters.

## Operational SaaS / data-heavy web
Use `references/web.md`, `subskills/web/`, design system, data-dense patterns, state/error QA, real framework/language guides. Do not force expressive-web treatment.

## Desktop/native application
Use application + desktop/mobile references, application subskills, platform guide, stack guide, language guide, QA.

## Electron / Tauri
Use application + desktop rules as UX baseline, then Electron/Tauri domain + security/runtime references. Renderer web rules apply only to renderer implementation, not as a reason to make the app behave like a website.

## Color / visual identity
Use visual + color subskills, visual-direction, palette references, accessibility, product-specificity, and runtime screenshots.

## Design system
Use design-system domain + color/visual/implementation + component API audit + visual regression + accessibility.

## Unknown stack
Read `handbook/languages/unknown-language-toolkit.md` and classify architecture before giving APIs.

## Completion
Always finish with the QA material that can verify the claims you intend to make.

## ULTRA-HARD deep layer

- `ultra/ULTRA-INDEX.md` — full index of deep playbooks.
- `ultra/OPERATING-MANUAL.md` — no-token-economy operating model and deep-read routing.
- `ultra/engineering-deep/` — full high-depth engineering skill references carried into the frozen snapshot.



## ULTRA-HARD deep appendix

When this topic is materially relevant, do not evaluate only the default state. Expand the review across these dimensions:

### State coverage

```text
default
hover / pointer-over (if applicable)
focus-visible
pressed / active
selected / current
disabled / unavailable
loading / pending
empty / zero-data
partial / stale
success / completion
warning / risk
error / failure
offline / disconnected
permission denied / limited
read-only / locked
long content / localization
narrow / constrained
wide / high-density
reduced motion
high contrast / forced colors
```

### Input coverage

Check each relevant input independently: mouse/pointer, keyboard, touch, stylus, controller/remote, assistive technology, and automation/API-driven state. Never assume that a path reachable by hover or precise pointer is reachable by every other input.

### Responsive / adaptive coverage

Record what changes at narrow, standard, wide, ultrawide, high-text-scale, and long-content conditions. Reordering, collapsing, cropping, scroll ownership, navigation model, inspector behavior, command availability, and motion complexity may change independently.

### Evidence standard

Runtime observation outranks inference. A static code path can show intent but not prove visible focus, hit target behavior, animation timing, scroll containment, package/runtime assets, or assistive technology behavior. Report `BLOCKED` when the target environment cannot be exercised.

### Root-cause test

Before adding another local override, ask whether the issue belongs to a governing token, component contract, layout primitive, state model, navigation model, or content structure. Fix the highest stable layer that explains the failure without rewriting unrelated logic.

### Stop condition

Stop when acceptance criteria are met, must-preserve behavior remains correct, high-impact in-scope failures are resolved, and further change would add more churn or decorative novelty than user value.
