# Admin / Data Table Pattern

## Purpose

Use this guide when the target surface primarily behaves like admin / data table. Preserve domain-specific behavior rather than copying a generic template.

## Core structure

- **columns**: define the user goal, state, hierarchy, interaction, failure/recovery behavior, responsive treatment, and accessibility semantics.
- **density**: define the user goal, state, hierarchy, interaction, failure/recovery behavior, responsive treatment, and accessibility semantics.
- **filter/sort**: define the user goal, state, hierarchy, interaction, failure/recovery behavior, responsive treatment, and accessibility semantics.
- **selection**: define the user goal, state, hierarchy, interaction, failure/recovery behavior, responsive treatment, and accessibility semantics.
- **bulk action**: define the user goal, state, hierarchy, interaction, failure/recovery behavior, responsive treatment, and accessibility semantics.
- **pagination/virtualization**: define the user goal, state, hierarchy, interaction, failure/recovery behavior, responsive treatment, and accessibility semantics.

## Hierarchy

Make the primary job visible before secondary analytics, explanatory copy, or decorative media. Repeated actions should remain stable across state changes.

## State coverage

Design default, loading, empty, partial, error, success, permission-limited, and long-content states where they are plausible. Do not validate only a perfect demo state.

## Responsive/adaptive behavior

Reprioritize controls by task frequency. Avoid shrinking dense desktop patterns until they become unusable. For mobile, convert secondary panels to sheets/routes/accordions when appropriate.

## Accessibility

Preserve semantic naming, focus order, visible focus, readable status, non-color-only differences, and usable targets.

## Product-specificity

Use the real domain entities and workflow. If the layout could be copied unchanged into an unrelated product, the design is not finished.

## Common failures

- duplicate primary actions;
- fake data or invented metrics;
- too many equal-priority cards;
- helper content competing with the core task;
- hidden recovery path;
- color-only status;
- responsive stacking without reprioritization.


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
