# Collaboration / Comments Pattern — HARD

## Primary job

Identify the user's decision, object, and irreversible consequences before choosing layout. The main object/workflow should dominate support chrome.

## Structure

Design the information architecture around the real task rather than a generic dashboard. Keep frequent actions close to the object/state they affect. Use progressive disclosure for advanced settings and destructive/rare operations.

## Required states

Model initial/empty, populated, loading, partial/stale, validation/error, success, disabled/read-only, permission/availability failure, and recovery when they apply.

## Interaction

Provide predictable focus order, keyboard behavior, pointer/touch/controller equivalents where relevant, and explicit feedback for asynchronous or destructive operations.

## Visual direction

Use product-specific objects, content, diagrams, timelines, maps, previews, device silhouettes, canvases, tables, or media instead of translating every concept into equal cards.

## Accessibility and resilience

Preserve semantic controls, labels, non-color state cues, scaling, localization, reduced motion, and useful behavior under degraded network/data/runtime conditions.

## Verification

Test the full high-frequency path, at least one failure/recovery path, dense-content/overflow behavior, keyboard/focus, and representative responsive/window sizes.


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
