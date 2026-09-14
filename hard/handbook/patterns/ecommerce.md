# E-commerce Pattern

## Purpose

Use this guide when the target surface primarily behaves like e-commerce. Preserve domain-specific behavior rather than copying a generic template.

## Core structure

- **discovery**: define the user goal, state, hierarchy, interaction, failure/recovery behavior, responsive treatment, and accessibility semantics.
- **product detail**: define the user goal, state, hierarchy, interaction, failure/recovery behavior, responsive treatment, and accessibility semantics.
- **variant selection**: define the user goal, state, hierarchy, interaction, failure/recovery behavior, responsive treatment, and accessibility semantics.
- **cart**: define the user goal, state, hierarchy, interaction, failure/recovery behavior, responsive treatment, and accessibility semantics.
- **checkout**: define the user goal, state, hierarchy, interaction, failure/recovery behavior, responsive treatment, and accessibility semantics.
- **order state**: define the user goal, state, hierarchy, interaction, failure/recovery behavior, responsive treatment, and accessibility semantics.

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
