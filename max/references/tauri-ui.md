# Tauri UI Integration

## Contents
- Version inspection
- Responsibility boundary
- IPC contract
- Commands/events/channels
- State ownership
- Background tasks/cancellation
- Errors/serialization
- Managed Rust state
- Window behavior
- Runtime verification

## Version inspection

Inspect actual project files before assuming syntax/version:
- `src-tauri/Cargo.toml`;
- `package.json`;
- lockfile;
- Tauri config;
- capabilities;
- frontend framework/config.

Do not migrate versions unless requested or required.

## Responsibility boundary

Frontend/TypeScript usually owns:
- rendering;
- presentation state;
- input;
- local interaction;
- formatting.

Rust usually owns:
- privileged native operations;
- trusted invariants;
- CPU-heavy/native work;
- filesystem/process integration;
- durable backend state when appropriate.

Do not move presentation logic into Rust merely because commands exist.
Do not move privileged logic into frontend for convenience.

## IPC contract

Treat IPC as a real API.

For each command define:
- name;
- request DTO;
- response DTO;
- error contract;
- cancellation semantics when relevant.

Prefer meaningful operations over chatty IPC.

## Commands / events / channels

Commands:
- request → response;
- clear success/error.

Events:
- small notifications;
- low-volume pub/sub.

Channels:
- ordered progress/output;
- frequent streaming;
- higher-volume continuous data.

Avoid global events for high-frequency streams.

## Typed wrapper layer

Avoid raw `invoke(...)` throughout UI components.

Prefer small domain wrappers that centralize:
- command names;
- request/response types;
- error mapping.

Do not build a giant abstraction for a tiny API.

## State ownership

Choose one authoritative owner:
- frontend;
- Rust;
- persisted storage;
- external process/service.

UI progress is often a projection of Rust-owned task state.

Avoid duplicated authoritative state.

## Background tasks

Prefer:
`start → operation ID → typed progress → completed/failed/cancelled`

Use stable IDs, not array indices.
Throttle/coalesce visual updates when needed.

## Cancellation

Define:
- cancel owner/token;
- request;
- backend acknowledgement;
- cleanup;
- final state.

A Cancel button must not only hide UI while work continues unexpectedly.

## Errors

Separate:
- internal diagnostic context;
- stable error category/code;
- user-facing recovery.

Do not dump raw debug strings/secrets into normal UI.

## Serialization

Use explicit DTOs with stable field names, predictable optionality, enums/unions for finite states, and documented units.

Do not couple frontend to Rust debug formatting.

## Managed Rust state

When used:
- define synchronization;
- keep locks short;
- distinguish memory-only from persisted;
- avoid global mutable state by default.

## Async / blocking

Identify whether work is:
- async I/O;
- blocking I/O;
- CPU-heavy;
- external-process waiting.

Do not block async executor threads with heavy synchronous work.

## Window behavior

Multiple windows need a product reason.

For each define:
- role/label;
- capability needs;
- state ownership;
- close/minimize;
- restore behavior.

Custom title bars must account for drag regions, maximize behavior, system menu, snap, DPI/scaling, and accessibility.

Native title bar is valid.

## Window persistence

When useful:
- restore size/position/state;
- validate off-screen positions;
- adapt after monitor/DPI changes;
- preserve safe minimum size.

## Runtime verification

Browser preview cannot prove Tauri integration.

When relevant verify:
- Tauri app launches;
- IPC works;
- progress/cancellation works;
- windows behave;
- native dialogs/events work.

If unavailable, mark native verification BLOCKED.


## Versioned DTO evolution

When IPC payloads persist across frontend/backend version boundaries or long-lived state:
- version contracts explicitly when compatibility risk is real;
- prefer additive changes;
- define defaults for newly optional fields;
- reject unsupported incompatible versions clearly;
- migrate persisted DTOs separately from transient UI state.

Do not depend on field ordering or debug serialization.

## Restart / reconnect recovery

If the frontend webview reloads/restarts while Rust/native work continues:
- define whether operations survive;
- query authoritative backend state after reconnect;
- resubscribe to progress;
- avoid creating duplicate operations;
- reconcile terminal tasks that completed while UI was absent.

Do not assume event history is replayed automatically.

## Worker / child-process crash recovery

When native tasks use child processes/workers:
- detect unexpected exit;
- map it to a truthful task state;
- retain useful diagnostics;
- define retry safety;
- clean orphan resources;
- avoid presenting stale progress as running.

If a task can resume, define resume semantics explicitly.

## IPC compatibility regression tests

For important command contracts, test:
- valid request;
- malformed request;
- backend error;
- cancellation;
- reconnect/query-state;
- old/new DTO compatibility where supported.

The frontend type system alone is not sufficient evidence.


## Task journal / reconciliation pattern

For long-running operations that may outlive a webview/reload, prefer an authoritative task registry/journal containing stable ID, current state, progress snapshot, terminal result/error and cancellation capability where relevant.

On reconnect:
1. query current authoritative tasks;
2. reconcile local projections;
3. resubscribe to streaming updates;
4. avoid duplicate starts;
5. surface tasks that completed while UI was absent.

Do not rely on transient events as the only source of task truth.
