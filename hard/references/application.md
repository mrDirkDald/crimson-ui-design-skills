# Application UI Core

## Contents
- Product patterns
- Navigation and command model
- Selection/repeated content
- Forms/dialogs/settings
- Auth/account/session
- Sync/offline
- Shared background task model
- Platform routing
- Completion contract

## Product patterns

### Focused utility
`compact command/input → primary work/result area → contextual options → persistent critical state/action`

### Editor / creative workspace
`document/canvas → selection → contextual inspector → command surface → undo/history`

### File/content manager
`location/navigation → content plane → explicit selection → search/filter/sort → bulk/context actions → details/preview`

### Background-task app
`task creation → queue/list → progress/state → pause/cancel/retry → output/destination`

### Communication app
`conversation/navigation → content plane → compose/reply → unread/attention → search`

### Native data tool
`scope/filter → dense data surface → selection → inspect/edit → bulk/export`

## Navigation and commands

Navigation represents places; commands represent actions.
Choose structure from real IA: tabs, sidebar, sidebar+detail, multi-pane, canvas+tools, menus/command surfaces, or none.

Verify:
- selected destination;
- return/back path;
- depth;
- state restoration;
- breadcrumbs only when hierarchy warrants them;
- command enabled/disabled state.

Do not add a sidebar because desktop apps often have one.

## Selection / repeated content

Define:
- single vs multi-select;
- range/modifier selection;
- selection persistence;
- actions applying to selection;
- behavior after move/delete/rename.

Use lists for scan/action sequences, tables for comparable data, grouped rows for task/state collections, cards only when grouping adds meaning.

For task rows prefer:
1. useful title;
2. type/format/quality;
3. state/progress;
4. source/technical metadata;
5. secondary actions.

Test 0, 1–2, 10–20+ items, long content, missing metadata, mixed states.

## Native form additions

Core `SKILL.md` owns shared form behavior.
Native additions:
- predictable tab/focus order;
- platform text controls where appropriate;
- native file/folder pickers;
- Apply/OK/Cancel conventions when platform/product uses them;
- IME/text-service compatibility;
- platform-native validation affordances where useful.

## Dialogs

Use modal surfaces for focused decisions, not general navigation.
Require:
- clear purpose;
- action hierarchy;
- safe dismissal;
- initial focus/focus restoration;
- Escape/cancel behavior where conventional;
- destructive action not accidentally default.

Avoid nested dialogs and routine-success dialogs.

## Settings

Organize by user intent.
Expose relevant current value, dependency, restart requirement, permission requirement, default/reset and side effect.
Use progressive disclosure for advanced options.
Avoid card walls.

## Native auth / account / session

For account-based apps model relevant:
- signed out;
- authenticating;
- signed in;
- session expired;
- reauthentication required;
- forbidden/role changed;
- account/workspace switch;
- sign-out with unsaved work.

Preserve intended destination after reauth when appropriate.
Do not collapse distinct failures into one generic auth error.

## Sync / offline

Distinguish:
- online/synced;
- local changes pending;
- syncing;
- conflict;
- offline with local access;
- offline unavailable;
- reconnecting;
- failed sync.

Never claim saved/synced before product semantics confirm it.
Preserve edits through temporary connectivity loss when architecture supports it.
Make conflict ownership/recovery explicit and prevent duplicate mutation replay.
Show when data may be stale.

## Shared background task model

For download/sync/render/convert/backup show only useful:
- stable task identity;
- state;
- progress;
- amount/time/speed when useful;
- pause/resume/cancel/retry when supported;
- destination/output.

Routine success should usually be state change, inline feedback, or transient notification—not a giant banner.

## Platform routing

Desktop-specific command/window/integration behavior:
`references/desktop-app.md`

Mobile/tablet behavior:
`references/mobile-app.md`

Load only the platform module that applies.

## Completion additions

```text
[ ] Navigation/command model is coherent
[ ] Selection/bulk behavior is explicit
[ ] Forms/dialogs recover safely
[ ] Account/sync states are truthful when relevant
[ ] Background-task states are truthful
[ ] Many-item/long-content states work
[ ] Platform-specific reference was loaded only if relevant
```

# MAX Edition Application Addendum

For complex applications, map command ownership, selection, focus, undo/redo, persistence, background activity, error recovery, multi-window state, shortcuts, and platform shell behavior before reorganizing visual hierarchy. Dense software should become clearer, not merely larger and more spacious.
