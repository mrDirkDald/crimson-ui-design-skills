---
name: crimson-ui-electron
description: Electron-specific window, preload, IPC, native integration, security-aware desktop UX.
---

# Electron

Use only for Electron-specific concerns.


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
