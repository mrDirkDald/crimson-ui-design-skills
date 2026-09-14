---
name: crimson-ui-application
description: Native-style application UX, desktop/mobile adaptation, dense tools, editors, queues, file and productivity workflows.
---

# Application

Use for application-like workflows where state, density, commands, selection, persistence, and platform behavior matter.


## Deep aspect subskills

This parent skill owns the broad domain. For MAX-depth work, load one or more aspect subskills below whenever they materially affect the decision.

MAX mode does **not** impose a one-aspect limit. It is acceptable to load several aspect subskills for a genuinely cross-cutting task, but each loaded aspect must have a clear reason.

| Aspect | Load | Purpose |
|---|---|---|
| Workflow Architecture | `aspects/workflow-architecture/SKILL.md` | Shape application UI around the sequence of user decisions and state transitions. |
| Commands and Shortcuts | `aspects/commands-shortcuts/SKILL.md` | Design discoverable command surfaces for keyboard, mouse, touch, pen, and context actions. |
| Selection and Focus | `aspects/selection-focus/SKILL.md` | Keep current selection, keyboard focus, multi-selection, and inspector ownership unambiguous. |
| Persistence and Recovery | `aspects/persistence-recovery/SKILL.md` | Protect application state, unsaved work, undo, failure recovery, and destructive actions. |
| Density, Panels, and Inspectors | `aspects/density-inspectors/SKILL.md` | Manage dense professional interfaces without burying the primary task in chrome. |
| Desktop / Mobile Adaptation | `aspects/desktop-mobile-adaptation/SKILL.md` | Translate the same product model across pointer/keyboard and touch-constrained environments. |

### Aspect loading rule

Use the parent skill first, then load:
- one aspect for a focused deep problem;
- several aspects when root causes cross boundaries;
- the owner reference(s) when implementation or verification requires more complete detail.

Do not replace an aspect subskill with generic advice if the task clearly belongs to that aspect.

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
