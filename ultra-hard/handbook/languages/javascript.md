# JavaScript UI Implementation Guide — HARD

## Purpose

Use this guide when UI code is materially implemented in **JavaScript**. Typical ecosystems include **browser DOM, Electron, React/Vue/Svelte ecosystems, Node-powered tooling**. The language alone does not determine the UI architecture; inspect the actual toolkit and version before applying APIs.

## Primary engineering concern

Pay special attention to **event loop, DOM semantics, state, hydration, async failure, bundle cost**.

## Step 1 — classify the UI architecture

Determine whether the target is retained-mode widgets, declarative/reactive widgets, immediate-mode, DOM/web, scene graph/canvas, terminal UI, game-engine UI, embedded UI, or a custom renderer. This classification determines state, layout, focus, accessibility, and rendering rules more reliably than the language name.

## Step 2 — inspect real project conventions

Collect:

```text
LANGUAGE VERSION:
TOOLCHAIN / BUILD SYSTEM:
UI TOOLKIT + VERSION:
ENTRY POINT:
STATE OWNER:
RENDER / EVENT LOOP OWNER:
THREADING / ASYNC MODEL:
THEME / STYLE SYSTEM:
NAVIGATION MODEL:
ACCESSIBILITY API:
TEST / PREVIEW HARNESS:
PACKAGING TARGET:
```

Do not invent APIs or upgrade frameworks solely to make a design implementation easier.

## State and event ownership

- identify the single source of truth for each meaningful state;
- avoid duplicated mutable state across view and model layers;
- model loading/success/error/empty/disabled states explicitly;
- keep background work away from the UI/render thread unless the toolkit explicitly permits it;
- marshal results back through the toolkit's supported mechanism;
- preserve cancellation, lifecycle, and disposal behavior;
- do not create animation timers or polling loops that outlive the surface.

## Layout and responsive/adaptive behavior

- use the toolkit's real layout primitives before hard-coded absolute positioning;
- define minimum/maximum sizes and overflow intentionally;
- support DPI/text scaling and localization expansion where the platform does;
- separate content constraints from decorative dimensions;
- test narrow, wide, dense-content, and high-scaling states;
- for canvas/immediate-mode UI, implement your own reliable hit testing, focus, and scaling rather than assuming widget behavior exists.

## Styling / design-system mapping

Map semantic roles rather than scattering raw values:

```text
canvas / surface / elevated surface
primary / secondary / muted text
border / divider
accent / selection / focus
success / warning / danger / info
spacing scale
radius scale
typography roles
motion durations/easing
icon sizes/strokes
```

Preserve a coherent existing system when it is sound. Replace systemic visual drift deliberately rather than layering endless local overrides.

## Input and focus

Verify pointer/mouse, keyboard, touch, controller/remote, stylus, or other relevant inputs independently. Hover is never the only path to critical information or action. Keep logical focus order and visible focus. Respect platform shortcuts and text-input/IME behavior.

## Accessibility

Prefer native semantic controls where possible. When using custom drawing, bridge name/role/state/value and keyboard/focus behavior through the platform/toolkit accessibility system. Do not rely on color alone. Respect text scaling and reduced motion where supported.

## Performance

Measure before optimizing. Watch layout thrash/repeated measurement, excess allocations, huge scene/widget trees, unnecessary re-renders/recompositions, synchronous I/O, image decoding on the UI thread, unbounded animation, and expensive transparency/effects.

## Packaging / runtime verification

Development preview is not final proof. Build the actual target configuration when possible. Verify fonts/assets/icons, theme selection, scaling, window lifecycle, permissions, file paths, and native packaging behavior.

## Common failure modes

- implementing a screenshot while bypassing the project's actual state model;
- hard-coded pixel coordinates that fail under resize or DPI;
- background work freezing the event loop;
- inaccessible custom controls;
- mixing multiple visual systems or icon packs;
- fake disabled/loading/success states;
- assuming desktop behavior on touch/mobile or vice versa;
- claiming runtime PASS after only static source inspection.

## Verification checklist

- [ ] The real toolkit/version was identified.
- [ ] State ownership is explicit and impossible combinations are prevented.
- [ ] UI-thread/event-loop rules are respected.
- [ ] Layout survives resize/scaling/content expansion.
- [ ] Keyboard/focus and other relevant input paths work.
- [ ] Accessibility semantics are present for custom controls.
- [ ] Theme/icon/type systems are coherent.
- [ ] Loading/error/empty/disabled/recovery states are verified.
- [ ] The packaged/runtime target was inspected when available.

## Deliverable format

```text
LANGUAGE / TOOLKIT:
ARCHITECTURE CLASS:
STATE MODEL:
LAYOUT MODEL:
INPUT MODEL:
ACCESSIBILITY MODEL:
IMPLEMENTATION CHANGES:
BUILD / TEST EVIDENCE:
RUNTIME EVIDENCE:
BLOCKED / UNKNOWN:
```


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
