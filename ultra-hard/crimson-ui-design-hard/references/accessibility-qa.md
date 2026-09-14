# Accessibility QA

## Contents
- Evidence rules
- WCAG 2.2 AA measurable baseline
- Keyboard/focus
- Screen readers
- Async announcements
- Forms/tables/charts/drag-drop
- Zoom/reflow/localization
- Themes/forced colors
- Native accessibility
- Target/input considerations

## Evidence rule

PASS requires observed evidence.
Record tool/platform, viewport or text scale, state and input method when relevant.
Do not infer runtime accessibility from source structure alone.

## Web baseline — WCAG 2.2 AA

Use WCAG 2.2 Level AA as default measurable baseline when web conformance is in scope unless product requirements specify another standard.

### Text contrast
- normal text: at least `4.5:1`;
- large-scale text: at least `3:1`.

Do not round a failing computed ratio upward.

### Non-text contrast / focus
Verify applicable controls, component boundaries, focus indicators and state distinctions meet relevant WCAG contrast requirements.
Do not communicate required state using color alone.

### Target size
For WCAG 2.2 SC 2.5.8, target is at least `24 × 24 CSS px` **or** a legitimate criterion exception/spacing alternative applies.
This is a minimum, not a universal ideal touch target.

### Resize / reflow
Where applicable, verify text resize to `200%` without loss of content/functionality and required reflow without avoidable two-dimensional scrolling.

## Keyboard / focus

Check:
- logical focus order;
- visible focus;
- Enter/Space activation;
- Escape behavior;
- menu/list navigation;
- no accidental focus traps;
- modal trap only when appropriate;
- focus restoration after dialogs/routes/async replacement.

## Screen reader

When relevant and tooling exists, test with platform screen reader such as Narrator/NVDA/JAWS, VoiceOver, TalkBack or supported equivalent.

Check:
- name/role/state/value;
- landmarks/navigation;
- labels/errors;
- dialog announcements;
- selected/expanded/toggled states;
- async status announcements/live regions;
- focus after async insertion;
- table headers/relationships;
- chart summary/data alternative;
- decorative content hidden appropriately.

If required screen-reader runtime is unavailable, mark BLOCKED.

## Async announcements

Meaningful completion/failure/validation/content replacement/background-task state should be available non-visually when needed.
Avoid announcement spam and unexpected focus movement.

## Forms

Verify labels, instructions, required/optional state, error association, invalid-state semantics, submit/pending feedback and preserved input after error.

## Tables

Verify headers, sort/selection state and keyboard behavior where implemented.

## Charts

Provide accessible name/summary, non-hover alternative, non-color-only encoding and a data alternative when critical information cannot otherwise be understood.

## Drag/drop

If drag/drop is essential, provide an accessible alternate action where feasible and communicate valid target/result.

## Zoom / text scaling

Test relevant browser zoom, OS scaling, Dynamic Type/font scaling.
Look for clipping, overlap, hidden actions, broken navigation or non-reflowing content.

## Localization / RTL

Test longer strings, dates/numbers/plurals and long values.
If RTL is supported, verify mirroring, directional icons, alignment, navigation and mixed LTR technical content.

## Themes / forced colors / high contrast

When supported verify light/dark/system, forced-colors/high-contrast, focus, borders/icons, active vs disabled and semantic states not conveyed only by color.

## Native accessibility

Do not reduce native accessibility to web semantics.
Use platform APIs/tools and the platform module in `references/application.md` plus `desktop-app.md` or `mobile-app.md`.

Verify relevant:
- accessible tree semantics;
- keyboard/touch traversal;
- custom control actions;
- text scaling;
- async task state;
- assistive-tech focus/order.

## Pointer / touch / stylus

Essential actions should not rely solely on hover.
Check touch target usability beyond bare WCAG minimum when the product is touch-first.
Stylus precision may enable denser interactions, but essential alternatives should remain available to the product's supported inputs.
