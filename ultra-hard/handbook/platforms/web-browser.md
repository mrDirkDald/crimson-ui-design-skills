# Web Browser UI

## Platform lens

DOM/CSS layout, browser history, keyboard focus, responsive reflow, URL/deep link semantics, web accessibility APIs, network/loading behavior.

## Design rule

Respect platform expectations unless the product has a concrete reason to diverge. “Cross-platform consistency” does not require making every platform identical. Preserve product identity while adapting interaction, navigation, typography, density, windowing, system surfaces, and accessibility to the environment.

## Verification

Test the real platform behavior whenever possible. Emulator/browser screenshots cannot prove every native convention, input behavior, system dialog, DPI issue, safe-area issue, or accessibility API mapping.

## Iconography

Preserve a coherent existing icon set. Otherwise use Lucide/vector assets where appropriate. When the platform has a strong semantic native symbol system, use it when it materially improves platform correctness, but do not mix styles randomly. Emoji are not UI icons.

## Page-level craft for beautiful websites

Browser correctness and art direction are separate gates. A beautiful site must satisfy both.

When page-level identity matters:
- compose the whole document, not isolated components;
- use real browser semantics and URLs while preserving visual experimentation;
- define a media system rather than collecting individually attractive assets;
- art-direct line breaks, type scale, crop, and section rhythm;
- use motion for continuity, hierarchy, causality, or atmosphere rather than blanket reveal animation;
- treat mobile as a separate composition problem when necessary.

### Responsive art direction

Do not reduce responsive behavior to:

```text
desktop: [text | media]\nmobile: [text]\n        [media]
```

For expressive work inspect:
- alternate crop/focal point;
- headline line-break strategy;
- section reordering;
- reduced/simplified motion;
- navigation transformation;
- overlap removal/replacement;
- media count reduction;
- interaction substitution for hover/scroll effects;
- mobile-specific signature device.


## HARD expansion — evidence and implementation protocol

Before changing this area, record the actual product behavior, governing components/styles, user frequency, platform conventions, and failure/recovery states. Distinguish a visual preference from an observable usability or coherence problem.

### Decision procedure

1. Identify the user job and current state.
2. Identify what information/action must be recognized first.
3. Trace the code/style/state owner that actually governs the surface.
4. Separate structural, visual, interaction, accessibility, and content issues.
5. Choose the smallest coherent change unless several governing layers are failing together.
6. Implement with the real toolkit rather than screenshot-specific hacks.
7. Verify normal, edge, loading, error, disabled, keyboard/focus, scaling/responsive, and recovery states where relevant.
8. Report observed evidence and remaining unknowns.

### Cross-cutting constraints

- Preserve working behavior and useful platform conventions.
- Do not hide critical state behind color, hover, animation, or decorative media alone.
- Do not introduce generic cards/containers unless they represent a real semantic/interaction boundary.
- Keep product-specific objects and workflow visually stronger than support chrome.
- Respect localization expansion, high-DPI/text scaling, reduced motion, and assistive technology where applicable.
- Avoid unrelated refactors and dependency churn.
- Do not claim PASS for behavior that was not run or observed.

### Runtime checklist

- [ ] Primary job remains discoverable.
- [ ] Primary and destructive actions are distinguishable.
- [ ] Empty/loading/error/disabled/recovery behavior is intentional.
- [ ] Focus/keyboard/input behavior is preserved.
- [ ] Overflow and scaling are handled.
- [ ] Theme and semantic color behavior remain coherent.
- [ ] No fake content, proof, metric, control, or success state was introduced.
- [ ] The rendered result was inspected when the environment permits it.


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
