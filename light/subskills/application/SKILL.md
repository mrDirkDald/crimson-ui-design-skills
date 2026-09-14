---
name: crimson-ui-application
description: Native-style application UX, desktop/mobile adaptation, dense tools, editors, queues, file and productivity workflows.
---

# Application

Use for application-like workflows where state, density, commands, selection, persistence, and platform behavior matter.


## Owner reference

`../../references/application.md`

Load it for TIER 1+ work or when any trigger below is true.

### Escalation triggers
- workflow/state/density materially changes;
- selection/commands/persistence are involved;
- desktop/mobile conventions matter;

For TIER 0 local fixes, do not open it unless needed.

## Read budget
Start with `../../references/application.md`.
Load **one** platform reference only if needed:
- desktop → `../../references/desktop-app.md`
- mobile/tablet → `../../references/mobile-app.md`

Do not load both unless the task explicitly spans both.

## Priorities
- workflow before decoration;
- state visibility;
- selection and focus;
- commands and shortcuts;
- persistence/unsaved changes;
- recoverability;
- dense information without metadata fog;
- platform conventions.

For Electron/Tauri shell behavior, use the matching platform subskill instead of loading both.
