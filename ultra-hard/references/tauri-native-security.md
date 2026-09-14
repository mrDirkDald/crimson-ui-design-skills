# Tauri Native & Security

## Contents
- Least privilege
- Filesystem/process
- CSP/remote content
- Updater/restart
- Tray/notifications
- Deep links/single instance
- Autostart/file associations
- Packaged-vs-dev
- Logging and verification

## Least privilege

Capabilities are a security boundary.

Grant windows/webviews only what they need.

Review:
- capability files;
- window labels;
- plugin permissions;
- resource scopes;
- platform differences.

Do not fix permission errors by granting broad access first.

## Filesystem

Distinguish:
- user-selected files;
- app-owned config/data/cache/logs;
- arbitrary filesystem access.

Scope narrowly.

Handle:
- cancellation;
- unavailable path;
- permission failure;
- path persistence;
- restart.

## Process / shell

Do not add shell privileges for convenience.

When external process execution is real product behavior:
- structured arguments;
- avoid unsafe command-string construction;
- capture exit status;
- capture useful stderr/stdout;
- map process lifecycle to task lifecycle;
- preserve cancellation.

Started is not completed.

## CSP / remote content

Remote content is a separate trust decision.

Do not expose native capabilities broadly to remote origins.

Review:
- CSP;
- origin/API configuration;
- plugin access;
- window capability scope.

Do not introduce remote content for visual convenience.

## Updater

When updater exists:
- model available/downloading/ready/failed;
- preserve unsaved work;
- avoid unsafe forced restart;
- support retry/recovery;
- distinguish restart from normal close.

## Restart-required flow

Communicate restart requirement.
Preserve pending work.
Avoid restart during destructive state.
Restore session when appropriate.

## System tray

Define:
- icon/menu state;
- show/open action;
- quit action;
- background behavior;
- task/progress reflection when useful.

Do not surprise users by continuing after close without clear product semantics.

## Notifications

Use for meaningful out-of-focus events.

Handle:
- permission;
- deduplication;
- click action;
- privacy-sensitive content;
- quiet behavior.

## Deep links / protocol handlers

Validate:
- URL/scheme parsing;
- unsupported payload;
- app-not-running vs running;
- correct route/window;
- unsaved state;
- untrusted parameters.

## Single instance

If single-instance:
- route second-launch args/file/deep-link to existing instance;
- focus/show correct window;
- preserve current work.

If multi-instance:
- define shared-state safety.

## Autostart

When supported:
- explicit setting;
- predictable startup;
- avoid stealing focus;
- recover from integration failure.

## File associations / Open With

Handle:
- unsupported file;
- multiple files;
- running vs fresh launch;
- correct workspace;
- unsaved state;
- error recovery.

## Packaged vs dev

Be suspicious of differences in:
- dev-server origin;
- asset paths;
- filesystem paths;
- CSP;
- capabilities;
- updater;
- protocol registration;
- notifications/tray;
- environment variables.

Dev PASS is not packaged PASS.

## Logging / privacy

Avoid logging secrets, tokens, or unnecessary sensitive paths.

Keep enough context for diagnostics.

## Production verification

When relevant verify:
- packaged assets;
- intended capability access;
- safe denied-access behavior;
- updater/tray/notification/deep-link behavior;
- file/protocol registration;
- restart flow.

If packaging/native environment is unavailable, mark BLOCKED.


## IPC trust-boundary checklist

For privileged commands review:
```text
INPUT SOURCE:
VALIDATION:
AUTHORIZATION / CAPABILITY:
RESOURCE SCOPE:
PATH / URL NORMALIZATION:
SIDE EFFECT:
ERROR EXPOSURE:
LOGGING:
```

Treat frontend-provided IPC data as untrusted for privileged operations.

## Command input validation

Validate privileged command inputs in Rust/native code even when TypeScript types exist.

Check:
- enum/range constraints;
- identifiers;
- path/URL format;
- resource ownership;
- allowed operation;
- payload size where relevant.

Frontend validation improves UX; backend validation protects trust boundaries.

## Path traversal / symlink / canonicalization

For filesystem-sensitive operations:
- reject or constrain `..` traversal where applicable;
- understand canonicalization timing;
- consider symlink escape from an allowed root;
- avoid insecure prefix-string checks;
- re-check path assumptions around create/rename when TOCTOU matters.

Do not assume a displayed path is the actual resolved target.

## Secrets / credential storage

Do not store secrets in:
- frontend source;
- localStorage/plain preferences;
- logs;
- bundled config.

Use platform secure storage/keychain/credential mechanisms when secrets must persist.

Separate:
- non-secret preferences;
- tokens/credentials;
- encryption keys.

## Updater integrity

When updater exists:
- preserve signature/integrity verification required by the updater design;
- do not bypass verification to make updates work;
- validate update source/config;
- fail closed on invalid integrity state;
- expose recoverable user state without leaking sensitive diagnostics.

## Remote URL allowlisting

For external URLs/navigation:
- allowlist trusted schemes/origins when appropriate;
- validate deep-link/remote parameters;
- avoid sending privileged data to arbitrary destinations;
- use system browser intentionally for external content when safer.



## TOCTOU-sensitive filesystem patterns

When security depends on filesystem identity, recognize time-of-check/time-of-use risk.

Avoid assuming that:
`validate path → later open path`
always refers to the same object.

Where consequence warrants it:
- minimize time between validation and use;
- operate on handles/descriptors where the platform/API makes that safer;
- re-check security-sensitive metadata at use time;
- avoid following attacker-controlled symlink changes;
- perform create/replace operations atomically where possible.

Do not add complex TOCTOU machinery to low-risk ordinary file picking without a concrete threat model.

## Capability audit

For releases or privilege-expanding changes, produce a compact audit:

```text
WINDOW / WEBVIEW:
CAPABILITY:
COMMAND / PLUGIN:
RESOURCE SCOPE:
WHY REQUIRED:
USER-VISIBLE FEATURE:
CAN IT BE NARROWER:
```

Flag:
- wildcard grants;
- unused grants;
- secondary windows inheriting main-window privilege;
- write/process access where read-only would suffice.

## Security regression tests

For privileged flows, add targeted negative tests where feasible:
- malformed IPC;
- unauthorized resource;
- out-of-scope path;
- traversal attempt;
- symlink escape case;
- disallowed remote URL/scheme;
- invalid updater integrity/signature;
- denied permission;
- external-process argument edge cases.

A security fix without a regression test is more likely to regress.


## Capability diff review

Treat capability changes as security-sensitive diffs.
For each release-changing capability record added/removed permissions and scopes, affected windows/webviews, justification and whether a narrower alternative exists.

A visual/UI change should not silently broaden native capability scope.

## Symlink-safe output policy

For user-selected output roots, decide whether symlinks are allowed, followed, rejected, or resolved according to product semantics.
The policy should be explicit for security-sensitive writes.
Avoid path-prefix string checks as an authorization boundary.
