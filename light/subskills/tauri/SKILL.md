---
name: crimson-ui-tauri
description: Tauri-specific IPC/state/window UX plus native privilege, filesystem, process, updater, tray, deep-link and security behavior.
---

# Tauri

Use only for Tauri-specific concerns.


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
