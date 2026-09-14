# Desktop Application UI

## Contents
- Window model
- Menus/shortcuts/command palette
- Context menus
- Editors/file managers
- Save/undo/workspaces
- Input methods
- Windows/macOS/Linux differences
- Tray/notifications/startup
- File associations/single instance/updater
- Desktop accessibility

## Window model

Verify relevant:
- restored/maximized;
- minimum practical size;
- common/wide size;
- DPI/scaling;
- multi-monitor;
- saved position/size;
- close/minimize behavior.

Do not design a fixed screenshot.

## Menus / shortcuts / command palette

For command-heavy apps:
- define command ownership;
- avoid shortcut collisions;
- expose discoverability;
- reflect enabled/disabled context;
- keep shortcuts stable.

Use a command palette when the command set is genuinely large or keyboard-first. It supplements, not replaces, discoverable core navigation/actions.

## Context menus

Use for object/context-specific actions.
Actions should match current selection.
Do not hide the only path to critical actions in a context menu.
Provide keyboard alternatives where relevant.

## Editors / creative tools

Define relevant:
- selection model;
- tool mode;
- contextual inspector;
- undo/redo;
- autosave/save;
- history;
- multi-document/workspace;
- keyboard shortcuts;
- canvas zoom/pan;
- dirty state;
- session restoration.

Tool panels should not compete with the active document/canvas without workflow reason.

## File/content managers

Support relevant:
- rename/create/move/copy;
- drag-and-drop;
- search/filter/sort;
- multi-select/bulk/context actions;
- replace/skip/keep-both conflicts;
- operation progress/failure.

Drag/drop needs valid-target feedback, invalid-drop handling, conflict handling and an alternate essential-action path.

## Save / undo / history

Choose explicit save model: explicit Save, autosave, or hybrid.
Communicate saving/saved/failed/conflict/pending where relevant.
Define undo command boundaries and non-undoable destructive operations.
Do not fake undo by restoring only visual state.

For multi-document/workspace apps define tabs/documents/windows, dirty indicators, close behavior, reopen/recovery, split views and session restoration.

## Pointer / mouse / touch / stylus

When multiple inputs are plausible verify:
- hover-only affordances have another path;
- right-click/context menu behavior;
- pointer target size;
- drag threshold/feedback;
- touch target size;
- stylus precision vs touch;
- long-press conflicts;
- hover capability is not assumed on touch devices.

## Platform differences

### Windows
Consider snap/maximize expectations, menu/keyboard access, taskbar/tray, high contrast/forced colors, file associations and updater/installer expectations.

### macOS
Consider global app menu, standard close/minimize/zoom, Command shortcuts, sheets, lifecycle when windows close, Dock/menu-bar behavior.

### Linux
Consider desktop-environment/window-manager variance, portal/file-picker behavior, tray availability, theme/font differences.

Platform consistency outranks decorative uniformity.

## Notifications / tray / background

Notify only for meaningful out-of-focus events.
Define click action, deduplication, privacy-sensitive content and quiet behavior.

If app continues in background:
- close vs minimize-to-tray must be explicit;
- tray actions reflect real state;
- users have a clear quit path;
- avoid surprise persistence.

## Startup / file associations / single instance

Autostart should be explicit and avoid stealing focus.
File associations/Open With must handle unsupported/multiple files, running vs fresh launch, unsaved state and correct workspace routing.

For single-instance apps route second-launch payload safely to the existing instance and preserve current work.
For multi-instance apps define shared-state safety.

## Updater / restart-required

Model available/downloading/ready/failed.
Preserve user work before restart.
Never force restart during unsafe state.
Communicate restart requirement and retry/recovery.

## Desktop accessibility

Accessibility is part of design, not only QA.

### Windows
Expose correct UI Automation semantics through the chosen stack, preserve keyboard navigation/focus and verify Narrator for critical custom controls.

### macOS
Preserve native accessibility roles/actions through AppKit/SwiftUI/framework equivalents, verify VoiceOver for critical custom controls and full-keyboard access where relevant.

### Linux
Use the framework/platform accessibility bridge available to the target stack and test critical keyboard/screen-reader paths on supported environments when feasible.

Custom controls must expose equivalent name/role/state/action semantics.


## Desktop chrome-to-content ratio

Desktop utilities should not spend most of the window on navigation shells, branding blocks, bordered cards, and oversized padding.

Let the actual workspace dominate.

Keep compact:
- title/command bars;
- navigation;
- status;
- repeated controls.

Give space to:
- mapping diagrams;
- editor/canvas;
- queue;
- data;
- preview.

A desktop app should not look like a marketing dashboard squeezed into a window.
