# Electron Integration & Security

## Contents
- Architecture
- Main/preload/renderer boundary
- contextBridge API design
- IPC validation
- BrowserWindow security
- Navigation/window-open
- Session permissions
- CSP/remote content
- Filesystem/process boundaries
- Deep links/single instance
- Updater/restart
- Packaging/fuses
- Security regression checklist
- Runtime verification

## Architecture

Electron is a desktop application with web rendering.

Application UX rules remain primary.

Renderer owns presentation/local interaction.
Main process owns privileged native operations and application lifecycle.
Preload exposes a minimal deliberate bridge.

Do not load Web merely because renderer code uses HTML/CSS/React.

## Main / preload / renderer boundary

Renderer must not receive broad Node/Electron authority for convenience.

Prefer:
- renderer: unprivileged UI;
- preload: narrow translation/bridge;
- main: privileged execution and validation.

Keep privileged state out of ordinary renderer globals.

## contextBridge API surface

Expose capability-shaped methods, not transport primitives.

Good conceptual API:
```text
window.files.pickFolder()
window.downloads.start(request)
window.downloads.cancel(taskId)
```

Bad conceptual API:
```text
window.ipc.send(channel, anything)
window.require(...)
window.electron.ipcRenderer
```

Do not expose the entire `ipcRenderer`, generic `invoke`, generic `send`, or event objects to renderer code.

Wrap event callbacks so renderer receives only intended data, not privileged Electron event objects.

## IPC contract and sender trust

Treat renderer IPC input as untrusted.

For every privileged handler define:
- allowed sender/window/origin;
- channel/command;
- request schema;
- authorization/permission;
- side effect;
- response/error;
- cancellation.

Validate IPC sender identity when multiple/untrusted webContents can exist.

Do not use generic “execute arbitrary command” IPC.

## BrowserWindow security baseline

For windows that can process untrusted or remotely influenced content, prefer secure Electron defaults/practices:
- `contextIsolation` enabled;
- renderer sandboxing enabled where compatible;
- Node integration disabled unless there is a concrete trusted-local reason;
- `webSecurity` not disabled;
- no `allowRunningInsecureContent`;
- no unnecessary experimental/Blink features.

A local trusted renderer is still not a reason to expose unlimited privilege.

## Session permission handlers

For sessions that can load remote/untrusted content, explicitly control permissions.

Use permission request/check handlers appropriate to the Electron version.

Decide based on:
- requesting origin;
- permission type;
- current feature/context.

Default-deny unexpected permission classes.

Do not automatically approve camera/mic/notification/etc. merely because Chromium requested them.

## Navigation interception

Limit unexpected navigation.

For renderer-created navigation:
- allow only intended app routes/origins;
- send external links to a validated external-open flow where appropriate;
- deny dangerous/unexpected schemes.

Do not let untrusted content navigate a privileged window to arbitrary content.

## Window-open policy

Use main-process window-open handling for new windows/popups.

Default-deny unexpected creation.

If allowing:
- validate URL;
- define safe BrowserWindow options in main;
- do not let renderer choose privileged webPreferences.

Avoid `<webview allowpopups>` style broad behavior.

## External URL policy

Never pass untrusted URLs directly to `shell.openExternal`.

Validate:
- scheme;
- origin/host when appropriate;
- product intent.

Prefer explicit allowlists for security-sensitive flows.

## CSP / secure content

Use a restrictive Content Security Policy appropriate to the app.

Load remote resources only over secure protocols when required.

Do not disable CSP/web security to fix frontend integration.

If remote content is necessary, isolate it from privileged APIs.

## Filesystem / path safety

Privileged file operations must validate:
- path;
- allowed root/scope;
- traversal;
- symlink/canonicalization implications;
- operation type;
- overwrite behavior.

Renderer-side TypeScript validation is UX, not a security boundary.

## Process / shell safety

Use structured executable + argument APIs.

Avoid renderer-controlled shell command strings.

Validate:
- executable/operation;
- args;
- working directory;
- environment exposure.

Map process exit/cancel to truthful task state.

## Deep links / protocol handlers

Treat deep-link/protocol payloads as untrusted.

Validate:
- scheme;
- route;
- identifiers;
- URL/path payload;
- current auth/workspace state.

Route to the correct existing/new window safely.

## Single instance

If using single-instance behavior:
- handle second-instance payload in main;
- validate file/deep-link args;
- focus/show appropriate window;
- preserve unsaved work.

## Updater / restart

Model:
- update available;
- downloading;
- ready;
- failed;
- restart required.

Preserve unsaved work.
Do not bypass update integrity/signature mechanisms.
Do not force restart during unsafe work.

## Packaging / custom protocols / file://

Dev success is not packaged-app proof.

Verify relevant:
- packaged assets;
- preload path;
- native modules;
- custom protocol behavior;
- updater;
- file associations;
- tray/notifications.

Prefer a safe custom protocol over broad `file://` assumptions when architecture/security benefits.

## Electron fuses

For production hardening, review relevant Electron fuses.

Change only with clear understanding of runtime/build consequences.

Do not treat fuses as a substitute for correct renderer/preload/main boundaries.

## Security regression checklist

For privilege-affecting changes, test relevant:

```text
[ ] contextIsolation remains enabled where expected
[ ] sandbox remains enabled where expected
[ ] webSecurity remains enabled
[ ] preload exposes only narrow APIs
[ ] ipcRenderer / generic invoke/send is not directly exposed
[ ] privileged IPC validates sender + input
[ ] unexpected navigation is denied
[ ] unexpected window creation is denied
[ ] external URL schemes/origins are validated
[ ] session permissions are explicitly handled when relevant
[ ] CSP remains restrictive
[ ] traversal/symlink edge cases are covered for scoped filesystem work
[ ] updater integrity is preserved
[ ] packaged runtime verified or BLOCKED
```

## TypeScript / Tailwind

If renderer uses TypeScript/Tailwind, also read:
`references/typescript-tailwind.md`

## Runtime verification

When relevant verify:
- Electron launches;
- preload bridge works;
- IPC works;
- permission/navigation/window policies behave;
- native integrations work;
- packaged build works.

If required runtime/platform is unavailable, mark BLOCKED.


## Session partition / storage isolation

When multiple trust domains/accounts/windows exist, decide whether they should share one Electron session/partition.
Do not let unrelated remote content inherit cookies/storage/permissions merely because it opens in another window.

Review:
- persistent vs in-memory partition;
- cookie/storage scope;
- permission handlers per session;
- cache/auth implications;
- cleanup on sign-out when product semantics require it.

## Preload API versioning

Treat the preload bridge as a product-internal API.
For material evolution:
- keep method names/DTOs explicit;
- prefer additive changes;
- fail clearly on incompatible renderer/main versions;
- avoid broad generic escape hatches added for compatibility.

## Security regression tests

Automate relevant assertions where feasible:
- BrowserWindow `webPreferences` secure values;
- preload exports do not include raw `ipcRenderer` or generic transport;
- unexpected navigation/window-open denied;
- permission requests default-denied unless allowlisted;
- external URL schemes restricted;
- privileged IPC rejects malformed/untrusted input;
- packaged CSP remains present.
