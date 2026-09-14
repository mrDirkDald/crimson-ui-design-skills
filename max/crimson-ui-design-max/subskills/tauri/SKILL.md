---
name: crimson-ui-tauri
description: Tauri-specific IPC/state/window UX plus native privilege, filesystem, process, updater, tray, deep-link and security behavior.
---

# Tauri

Use only for Tauri-specific concerns.


## Deep aspect subskills

This parent skill owns the broad domain. For MAX-depth work, load one or more aspect subskills below whenever they materially affect the decision.

MAX mode does **not** impose a one-aspect limit. It is acceptable to load several aspect subskills for a genuinely cross-cutting task, but each loaded aspect must have a clear reason.

| Aspect | Load | Purpose |
|---|---|---|
| Tauri Commands and IPC | `aspects/commands-ipc/SKILL.md` | Design typed command invocation and asynchronous UI state around Tauri's frontend/native boundary. |
| Capabilities and Security | `aspects/capabilities-security/SKILL.md` | Keep Tauri permissions/capabilities aligned to the minimum real product need. |
| Windows and Application State | `aspects/windows-state/SKILL.md` | Coordinate Tauri windows, dialogs, state synchronization, and background tasks. |
| Filesystem, Process, and Shell UX | `aspects/filesystem-process-shell/SKILL.md` | Design safe native file/process interactions without exposing dangerous generic controls. |
| Updater, Tray, and Deep Links | `aspects/updater-tray-deeplink/SKILL.md` | Handle lifecycle integrations in a way that matches desktop expectations. |
| Renderer Integration | `aspects/renderer-integration/SKILL.md` | Apply web/TS UI implementation cleanly inside a Tauri shell without importing unnecessary web-only patterns. |

### Aspect loading rule

Use the parent skill first, then load:
- one aspect for a focused deep problem;
- several aspects when root causes cross boundaries;
- the owner reference(s) when implementation or verification requires more complete detail.

Do not replace an aspect subskill with generic advice if the task clearly belongs to that aspect.

## Owner reference

`../../references/tauri-ui.md`

Load it for TIER 1+ work or when any trigger below is true.

### Escalation triggers
- Tauri IPC/state/window behavior changes;
- background/native interaction is material;
- shell behavior affects UX;

For TIER 0 local fixes, do not open it unless needed.

## Read budget
Choose what applies:
- UI IPC/state/background tasks/windows → `../../references/tauri-ui.md`
- native privilege/filesystem/process/updater/tray/deep links/security → `../../references/tauri-native-security.md`
- renderer TypeScript/Tailwind only when needed → `../../references/typescript-tailwind.md`

Do not load Web merely because Tauri renders HTML/CSS.
Do not load Electron references.
