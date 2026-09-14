# Accessibility

## Design responsibility

Accessibility affects hierarchy, interaction, content, code, and QA.

## Keyboard

Every interactive control that must be keyboard-operable needs a predictable focus order, visible focus, logical grouping, and escape/recovery behavior for temporary layers.

## Screen readers

Use semantic elements/native controls where possible. Provide accessible names, roles, values, and state. Decorative icons should not duplicate nearby labels.

## Contrast

Check actual foreground/background pairs including hover, disabled, selected, focus, error, and text over imagery. Do not assume a palette-level contrast check covers every component.

## Target size

Visible glyph size can be small while hit target remains comfortably usable. This is especially important for toolbar and table-row actions.

## Cognitive accessibility

Use clear language, predictable placement, reversible actions, stable navigation, and meaningful error recovery.

## Motion

Respect reduced motion and avoid flashes or unavoidable disorienting transformations.
