# Unknown Language / Toolkit Fallback — HARD

No UI stack is exempt from design quality because it is unfamiliar.

## Classification first

Before inventing toolkit-specific advice, determine:

```text
LANGUAGE:
TOOLKIT / FRAMEWORK:
RENDERING MODEL:
EVENT LOOP:
STATE MODEL:
LAYOUT MODEL:
STYLE / THEME MODEL:
INPUT MODEL:
FOCUS MODEL:
ACCESSIBILITY MODEL:
PACKAGING MODEL:
TEST / PREVIEW MODEL:
```

Then classify the UI as DOM/document, retained native widgets, declarative retained widgets, immediate mode, scene graph/canvas, terminal/TUI, embedded, game-engine, or custom GPU renderer.

Apply universal rules from the closest architecture family. Search project documentation/source for actual APIs before coding. Do not guess function names, events, or accessibility support.

## Minimum quality gates

Regardless of stack, preserve behavior, model states explicitly, avoid blocking the event loop, provide understandable focus/input behavior, support resize/scaling/content expansion as applicable, use coherent type/color/icon systems, verify loading/error/recovery states, and inspect the real runtime when available.


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
