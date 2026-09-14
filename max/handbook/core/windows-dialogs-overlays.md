# Dialogs, Sheets, Popovers, Drawers, Menus and Overlays

Choose overlay type by interaction model. A modal dialog blocks the parent task. A nonmodal panel or inspector supports the task. A popover is contextual and transient. A menu is a command list. A drawer/sheet often adapts secondary content for constrained width.

## Focus and dismissal
Move focus intentionally into modal content, trap it only when modal semantics require it, and restore focus to the invoking control on close. Escape/back should dismiss when safe. Clicking outside may dismiss lightweight popovers, but should not cause accidental data loss.

## Stacking
Avoid modal-on-modal chains. If a second complex layer is required, reconsider information architecture. Keep z-index/elevation hierarchy centralized.

## Mobile sheets
Bottom sheets should account for safe area, keyboard, drag handle if draggable, content scroll, and clear dismissal. Do not use a bottom sheet for every action simply because it is fashionable.

## Menus
Menus need clear grouping, keyboard navigation, disabled state, check/radio semantics where applicable, destructive separation, and stable icon alignment. Do not combine navigation, toggles, and dangerous actions without grouping.
