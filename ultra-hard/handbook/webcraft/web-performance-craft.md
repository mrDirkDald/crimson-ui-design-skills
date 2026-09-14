# Performance as part of craft

## Purpose

This HARD handbook chapter is a deep operational guide for **performance as part of craft**. Use it together with `references/web-craft-analysis.md` and the platform/stack guide that actually governs the implementation.

## Detailed rules

1. Treat responsiveness and load stability as visual quality; a premium page that jitters, blocks input, or shifts layout is not premium.
2. Budget font files, video, 3D, images, third-party scripts, hydration, and animation work before adding them.
3. Prefer transform/opacity animation where appropriate, lazy-load below-fold media, and size assets intentionally.
4. Progressively enhance expensive experiences; preserve useful content when WebGL, JS, or media fails.
5. Measure representative devices and network conditions instead of validating only on a powerful development machine.

## HARD workflow

1. Inspect the real product, content, references, and runtime before styling.
2. Record evidence and must-preserve behavior.
3. Define the local design thesis and success criteria.
4. Compare at least one credible alternative when the structure is genuinely ambiguous.
5. Implement using the real stack and existing conventions where sound.
6. Verify desktop and mobile composition, keyboard/focus behavior, reduced motion, loading/error state, and performance impact where applicable.
7. Report PASS/FAIL/BLOCKED rather than claiming unobserved success.

## Anti-patterns

- copying a reference site's surface treatment without understanding its product logic;
- using visual novelty to hide weak hierarchy or weak proof;
- applying one universal card/radius/glow system to every page;
- treating desktop screenshots as the complete responsive design;
- sacrificing semantics or input accessibility for animation;
- inventing marketing proof or product capabilities.

## Verification checklist

- [ ] The page has one explainable visual/experience thesis.
- [ ] Primary action and primary proof are obvious without relying only on accent color.
- [ ] The structure is product-specific after hiding the logo and accent.
- [ ] Media and typography feel intentionally related to the subject.
- [ ] Mobile is recomposed rather than merely stacked.
- [ ] Motion has a reduced-motion equivalent.
- [ ] Semantic controls and keyboard order remain correct.
- [ ] Performance-sensitive media/effects have a fallback or budget.
- [ ] No fabricated proof, metric, logo, review, or success state is present.

## Evidence to collect

```text
TARGET SURFACE:
PRODUCT SUBJECT:
PRIMARY USER DECISION:
CURRENT VISUAL ANCHOR:
CURRENT PROOF:
CURRENT STRUCTURE:
REFERENCE SIGNALS:
ANTI-REFERENCE SIGNALS:
MOBILE DIFFERENCES:
RUNTIME LIMITATIONS:
```

## Deliverable

Record the selected direction, why it fits the subject, the strongest alternative considered, implementation implications, must-preserve behavior, and the concrete runtime evidence used to validate the result.


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
