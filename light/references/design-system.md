# Design-System Discipline

## Contents
- Governing-source proof
- Three-level metric model
- Token promotion
- Component ownership
- Variants and states
- Screen metrics
- Migration/refactor discipline
- Screenshot/design-to-code
- Drift checks

## Governing-source proof

Do not assume a file or component governs the target surface because:
- names match;
- it is nearby in the repo;
- values look similar;
- it is called “design system”.

Prove connection through:
- import path;
- rendered component tree;
- props/variants;
- resolved theme/token;
- CSS inheritance;
- generated artifact loaded by the target.

Drafts, proposals, future migrations, and unused token files are not current authority unless explicitly accepted.

## Three-level metric model

Keep UI values in three conceptual levels:

### 1. Global / semantic tokens
Reusable product meanings:
- color roles;
- spacing scale;
- typography roles;
- radii;
- elevation/layers;
- motion;
- breakpoints/containers where appropriate.

### 2. Component-specific metrics
Values owned by a reusable component:
- control height;
- icon gap;
- row padding;
- modal max width;
- button radius;
- table row density.

### 3. Screen-specific layout metrics
Values that express one composition:
- sidebar width;
- inspector width;
- page max width;
- split ratio;
- local section gap.

Do not hide screen layout math inside global tokens.
Do not hardcode global semantics in every screen.

## Token promotion

Repeated values are candidates, not proof of a token.

Promote a value when:
- it represents shared semantic intent;
- several real consumers should change together;
- ownership is clear.

Do not create a token merely because grep found the same number three times.

## Component ownership

Reuse an existing component when its semantic contract fits.

Create/extract a component when:
- behavior repeats;
- visual/state contract repeats;
- ownership is coherent;
- reuse reduces real drift.

Do not create wrappers that only rename utilities.

## Variants and states

A component contract should include relevant:
- size;
- emphasis;
- selected;
- hover;
- focus;
- pressed;
- disabled;
- danger;
- loading.

Avoid one-off state styling at call sites when the component should own it.

## Screen metrics

Screen-level composition can intentionally differ.

Do not normalize every gap/radius/width merely for mathematical consistency.

Consistency means shared logic, not identical treatment everywhere.

## Migration/refactor discipline

For existing products:
1. prove the target surface;
2. identify the current owner;
3. change the smallest governing layer;
4. trace affected consumers;
5. verify before/after.

Do not launch repository-wide token cleanup during a local design fix.

## Screenshot / design-to-code

When matching a screenshot/Figma/reference:
- reconstruct hierarchy and constraints first;
- map repeated values to existing product tokens where appropriate;
- do not copy every pixel into arbitrary constants;
- preserve reusable components and responsive behavior;
- verify the rendered result, not just code similarity.

## Drift checks

Look for:
- repeated arbitrary values;
- duplicated component variants;
- one-off shadows/radii/colors;
- screen-specific values promoted globally;
- conflicting token layers;
- call-site state styling that should belong to the component.

Fix only drift connected to the in-scope surface.


## Versioning and deprecation

For shared components/tokens, define when relevant:
- current supported API/variant;
- deprecated API/variant;
- migration path;
- removal criteria;
- compatibility window.

Do not silently repurpose a component variant in a way that breaks existing consumers.

## Documentation contract

A reusable component should document the parts that affect correct use:
- purpose;
- variants;
- states;
- accessibility behavior;
- content constraints;
- responsive behavior when relevant;
- examples of correct/incorrect use.

Documentation is not proof of implementation; verify source/rendered behavior when consequential.

## Accessibility as component contract

For reusable interactive components, accessibility is part of ownership.

The component contract should own relevant:
- semantic role;
- accessible name strategy;
- keyboard behavior;
- focus-visible behavior;
- disabled/read-only semantics;
- selected/expanded/pressed state;
- error association;
- screen-reader announcement behavior when applicable.

Avoid making every call site reinvent accessibility.

## Theme token coverage

When multiple themes exist, verify semantic token coverage across:
- base/raised surfaces;
- primary/muted text;
- borders;
- focus;
- hover/pressed/selected;
- disabled;
- danger/warning/success/info;
- charts/data visualization when applicable.

Detect fallbacks to raw palette values that bypass theme semantics.



## Color token architecture

Color harmony should be expressed through semantic tokens rather than repeated raw palette values.

Prefer semantic roles such as background, surface, text, border, accent, focus and status colors. Implementation names may differ.

Do not let individual components invent unrelated raw accent shades for the same meaning.

## Theme color parity

For every supported theme verify semantic coverage for:
- background/surfaces;
- text hierarchy;
- borders/dividers;
- focus;
- selected/active/disabled;
- primary accent states;
- success/warning/danger/info.

Theme values may differ numerically, but semantic importance and hue family should remain coherent.

## Color drift detection

Flag:
- near-duplicate raw hex/rgb values;
- multiple unrelated accent families;
- component-specific danger/success colors;
- hover states with arbitrary hue shifts;
- raw palette values bypassing semantic tokens;
- theme-specific one-off colors with no semantic owner.

Fix drift at the smallest governing layer. Do not promote one-off illustration colors into product-wide tokens unless they truly belong there.

## Component regression strategy

Shared interactive components should have a stable isolated-state contract when tooling and project scale justify it.

A Storybook-like component workbench is one valid approach, not a requirement.

For high-value components capture relevant states:
- default;
- hover/focus/pressed;
- selected;
- disabled/read-only;
- loading;
- error;
- long content;
- keyboard interaction;
- theme variants.

Regression coverage may combine:
- isolated render stories/examples;
- accessibility checks;
- interaction/contract tests;
- visual snapshots/diffs.

Do not snapshot every trivial wrapper.

Prioritize components whose regression radius is high.

## Component contract tests

Test behavior that should remain invariant across visual refactors:
- semantic role/name/state;
- keyboard behavior;
- emitted action/event;
- controlled/uncontrolled state contract where relevant;
- disabled semantics;
- focus management;
- loading/error behavior.

Visual snapshots cannot replace behavior contracts.

## Theme coverage matrix

For semantic tokens and shared components, maintain a matrix of supported themes/modes.

Detect:
- missing semantic token;
- raw palette escape;
- invisible focus/border;
- status color that loses meaning;
- component variant absent in one theme.

A theme can intentionally differ; coverage means the semantic contract remains usable.


## Component accessibility contract matrix

For high-reuse interactive components, maintain an explicit contract covering supported states and input/a11y behavior.

Example matrix dimensions:
- semantic role/name;
- keyboard activation/navigation;
- focus-visible;
- pointer/touch;
- disabled/read-only;
- selected/expanded/pressed;
- loading/error;
- screen-reader announcement where relevant;
- supported themes/forced-colors.

A component release should not silently weaken this contract.

## Component release regression gate

Before deprecating/replacing a high-radius shared component, compare:
- public props/variants/events;
- semantic/accessibility contract;
- isolated visual states;
- representative consuming screens.

Use visual regression for stable appearance and contract tests for behavior.
Do not approve a component migration from screenshots alone.

## SVG icon component contract

### Lucide as default library

If there is no established project icon system, default to Lucide.

Treat Lucide as a system, not a bag of random glyphs: centralize wrapper/component behavior, normalize size through tokens, inherit semantic color with `currentColor`, keep stroke characteristics consistent, and handle accessible naming at the control level.

If the repository already has a coherent icon system, preserve it unless replacement is part of the task.

Shared iconography should have a reusable SVG contract.

Define relevant:
- icon name/id;
- `viewBox`;
- size;
- stroke/fill behavior;
- `currentColor` / semantic token behavior;
- accessible label/title strategy;
- decorative icon handling;
- active/selected/disabled behavior.

Do not:
- mix unrelated icon packs casually;
- use emoji as component icons;
- scatter inconsistent inline SVGs across call sites;
- hardcode semantic colors inside reusable SVGs when token/currentColor inheritance is more appropriate.

When importing SVGs, normalize metadata, `viewBox`, stroke/fill rules, optical alignment, theme behavior and accessibility.
