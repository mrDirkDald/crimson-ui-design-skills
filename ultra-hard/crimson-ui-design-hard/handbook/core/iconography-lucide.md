# Iconography and Lucide

## Baseline

Preserve a coherent existing icon system. If none exists, use Lucide Icons as the baseline visual vocabulary where technically practical.

## Why Lucide

Lucide is broadly available, SVG/vector-based, consistent, readable at UI sizes, and covers common product actions. The value is consistency, not the brand name itself.

## Geometry

Keep standard geometry unless the product deliberately defines a variation. Normalize visible size across icons rather than trusting raw path bounds. A `Play` triangle and a `Settings` gear may need optical adjustment even at the same nominal box.

## Stroke

Avoid random strokeWidth overrides. If the design system chooses a non-default stroke, centralize the decision through one wrapper.

## Color

Use `currentColor`/semantic foreground tokens for monochrome controls. Avoid baking hover/danger/disabled colors into the SVG asset itself.

## Icon + text

Do not decorate every text label with an icon. Icons are valuable for repeated actions, compact controls, toolbars, object types, navigation anchors, and spatial affordances.

## Icon-only buttons

They require accessible names and enough target size. Provide tooltip where useful but never make tooltip the only accessible name.

## Custom icons

Create custom SVG when the product needs a domain object that Lucide represents inaccurately, or when a unique brand glyph is central. Match Lucide stroke character if custom icons live beside Lucide.

## Emoji rule

Emoji are not UI icons. Do not use 📁 ⚙️ 🔍 ✅ ❌ ⬇️ 🚀 ✨ as control graphics. They vary by platform and break icon-system coherence.


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
