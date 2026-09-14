# JUCE — HARD Stack Guide

## Inspect first

Confirm framework/toolkit version, project entry points, state ownership, layout/styling system, icon system, accessibility primitives, build commands, packaging target, and existing test/preview harness. Do not invent APIs.

## Architecture mapping

Classify retained/declarative/immediate/DOM/canvas architecture. Identify what owns state, render scheduling, navigation, asynchronous work, and lifecycle. Keep UI-specific changes inside the correct layer.

## Design-system implementation

Map semantic color, typography, spacing, radius, motion, focus, icon and component-state roles into the stack's native styling/resource mechanism. Avoid local raw-value drift.

## Interaction and accessibility

Use native semantic controls where possible. Verify keyboard/focus, pointer/touch as relevant, accessible names/roles/state, scaling, localization, reduced motion, and custom-control semantics.

## Runtime concerns

Watch event-loop blocking, repeated rendering/layout, asset paths, fonts, platform packaging, window/lifecycle behavior, and production-vs-development differences.

## Verification

Build/run the real target when possible. Inspect empty/loading/error/disabled states, resize/responsive behavior, high-DPI/text scaling, keyboard/focus, theme, and packaged asset correctness.


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
