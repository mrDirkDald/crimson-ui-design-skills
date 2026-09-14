---
name: crimson-ui-electron
description: Electron-specific window, preload, IPC, native integration, security-aware desktop UX.
---

# Electron

Use only for Electron-specific concerns.


## Deep aspect subskills

This parent skill owns the broad domain. For MAX-depth work, load one or more aspect subskills below whenever they materially affect the decision.

MAX mode does **not** impose a one-aspect limit. It is acceptable to load several aspect subskills for a genuinely cross-cutting task, but each loaded aspect must have a clear reason.

| Aspect | Load | Purpose |
|---|---|---|
| Window and Shell UX | `aspects/window-shell/SKILL.md` | Design Electron window behavior, chrome, multi-window flows, and platform integration coherently. |
| Preload and IPC | `aspects/preload-ipc/SKILL.md` | Keep renderer UX responsive while respecting Electron process boundaries. |
| Native Dialogs, Menus, and OS Integration | `aspects/native-dialogs-menus/SKILL.md` | Choose between native Electron/OS surfaces and custom UI intentionally. |
| Updater, Tray, and Deep Links | `aspects/updater-tray-deeplink/SKILL.md` | Design lifecycle surfaces that often sit outside the main window. |
| Electron Security and UX Boundaries | `aspects/electron-security/SKILL.md` | Prevent design/implementation choices from weakening Electron's security model. |
| Electron Renderer UX | `aspects/renderer-ux/SKILL.md` | Apply application design principles inside the renderer without treating Electron as merely a website wrapper. |

### Aspect loading rule

Use the parent skill first, then load:
- one aspect for a focused deep problem;
- several aspects when root causes cross boundaries;
- the owner reference(s) when implementation or verification requires more complete detail.

Do not replace an aspect subskill with generic advice if the task clearly belongs to that aspect.

## Owner reference

`../../references/electron.md`

Load it for TIER 1+ work or when any trigger below is true.

### Escalation triggers
- IPC/preload/window/native integration changes;
- security boundaries are involved;
- desktop shell behavior is material;

For TIER 0 local fixes, do not open it unless needed.

## Read budget
Read `../../references/electron.md`.
Add `../../references/typescript-tailwind.md` only if renderer implementation needs it.

Do not load Tauri references.

## Preserve
- preload boundaries;
- IPC contracts;
- window behavior;
- native dialogs/menus where appropriate;
- security assumptions;
- updater/deep-link/tray behavior if present.

Application UX rules remain primary; Electron rules govern shell/platform integration.
