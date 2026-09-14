# Component Anatomy and State Contracts

A component is not just a rectangle with styles. Define its semantic role, content model, interactive state, focus behavior, density variants, responsive behavior, accessibility name/description, icon relationship, error/loading handling, and theme behavior.

## Buttons
Primary buttons represent the highest-value action in the local context. Secondary and tertiary actions should not visually compete. Destructive actions require semantic distinction and consequence-aware labels. Icon-only buttons need accessible names and stable hit targets. Loading buttons should preserve width where possible to avoid layout jumps.

## Inputs
Inputs need persistent identity, value state, placeholder/helper distinction, focus, validation, disabled/read-only difference, autofill behavior where relevant, and clear error recovery. Prefix/suffix icons must not crowd the value or reduce touch targets.

## Selectors and toggles
Checkbox, radio, switch, segmented controls, and select/dropdown serve different decision models. Do not replace a boolean checkbox with a switch unless immediate effect or platform convention supports it. Segmented controls are for a small set of peer modes, not arbitrary navigation.

## Cards
Cards are containers, not a default grouping mechanism. Use them when an item needs an independent surface, boundary, action set, or media object. Do not wrap every section in a rounded card simply to look polished.

## Tables and lists
Rows need selection, hover/focus if interactive, empty/loading/error states, predictable action placement, and density suited to task frequency. Use sticky headers and virtualization only when they improve real use and do not break accessibility.

## Dialogs
Dialogs interrupt. Use them for focused decisions, short forms, confirmation with meaningful consequence, or information that cannot safely coexist with the underlying state. Large multi-step workflows often belong in a page/panel instead. Escape/cancel and focus restoration must work.

## Tooltips
Tooltips explain unfamiliar icons or concise secondary detail. Do not hide essential instructions in hover-only tooltips. Tooltips should not become mini-modals.

## Badges/chips
Use badges for compact state/category/count when the meaning is stable. Avoid badge spam that converts every metadata item into a pill and destroys hierarchy.
