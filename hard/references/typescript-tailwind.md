# TypeScript + Tailwind UI

## Contents
- Existing stack
- Type safety
- Component boundaries
- Token discipline
- Arbitrary values
- Dynamic classes
- Responsive/layout
- State styling
- Motion/z-index/icons
- Verification

## Existing stack

Inspect:
- `tsconfig`;
- Tailwind version/config/theme;
- framework;
- component library;
- existing tokens;
- class/variant helpers.

Do not migrate architecture because newer syntax exists.

## Type safety

Prefer strong TypeScript guarantees where practical:
- `strict`;
- `unknown` at trust boundaries;
- narrowing before use;
- finite-state unions/enums;
- typed domain wrappers.

Do not enable flags that create a giant unrelated migration.

Runtime data may still need validation at:
- network boundaries;
- imported files;
- external process output;
- persisted versioned data;
- untyped events.

## Component boundaries

Extract a component when:
- behavior repeats;
- visual/state contract repeats;
- ownership is coherent;
- reuse reduces drift.

Avoid:
- one giant component;
- dozens of meaningless wrappers.

## Token discipline

Prefer semantic tokens for repeated product meaning:
- surface;
- text;
- border;
- accent;
- status;
- spacing;
- typography;
- radius;
- motion.

Use the existing token system if sound.

Do not create a second competing layer.

For deeper guidance read `references/design-system.md`.

## Arbitrary values

Arbitrary values are valid for true one-offs.

Challenge repeated patterns such as:
- `mt-[13px]`;
- `rounded-[11px]`;
- `w-[437px]`;
- `z-[9999]`.

Repeated arbitrary values often indicate missing token, layout issue, or component drift.

Do not ban arbitrary values.

## Dynamic class detection

Do not construct utility class names in ways Tailwind cannot detect statically.

Prefer mapping to complete class strings.

## Class sprawl

Extract variants/components when repetition causes:
- inconsistent hover/focus/disabled;
- duplicated visual contract;
- repeated arbitrary values;
- hard-to-review state combinations.

Do not hide every few utilities behind custom CSS.

## Layout

Prefer:
- flex;
- grid;
- intrinsic sizing;
- min/max;
- overflow rules;
- container queries when appropriate.

Avoid absolute-positioning ordinary UI with piles of magic numbers.

For resizable desktop webviews, pane/container constraints may matter more than device labels.

## Scroll ownership

Define which region scrolls.

Avoid:
- nested scroll traps;
- `100vh` + fixed regions causing double scroll;
- focused content hidden under sticky UI.

## Themes

If multiple themes exist:
- use semantic tokens;
- verify hover/focus/disabled;
- verify borders/icons/status.

Do not invent light mode when product is intentionally dark-only.

## State styling

Keep coherent:
- hover;
- focus-visible;
- pressed;
- selected;
- disabled;
- danger.

Do not mute active secondary actions until they look disabled.

## Motion

Avoid `transition-all` as a mindless default.

Animate intentional properties.

Expressive products may legitimately use richer motion when justified.

## Z-index

Use a small intentional layer model:
- base;
- sticky;
- popover;
- modal;
- toast.

Avoid arbitrary escalation.

## Icons

Prefer one coherent icon style.

Check:
- stroke/fill;
- optical size;
- baseline;
- icon-only accessible name;
- semantics.

Do not put icons on every button automatically.

## Tailwind color harmony discipline

When Tailwind is used, keep color relationships semantic.

Prefer semantic surface/text/border/accent/status tokens over unrelated component-local palette choices.

Challenge:
- `rose-*`, `red-*` and custom hex values all representing the same danger meaning;
- hover states that jump to another hue family without intent;
- dark mode using an unrelated accent family;
- arbitrary hex values accumulating across components.

Do not replace a coherent existing product palette merely to match Tailwind's default named colors.

## Tailwind neuroslop

Detect:
- arbitrary-value soup;
- rounded everything;
- shadow on every surface;
- border on every container;
- random near-identical grays;
- copied giant class strings with slight drift;
- uncontrolled z-index;
- excessive `!important`;
- fixture-only fixed widths.

Fix the system cause.

## Verification

Run project-defined:
- typecheck;
- lint;
- build;
- tests when relevant.

Do not invent commands without inspecting scripts.

Dev-server appearance is not proof of packaged/native correctness.


## Framework-level UI state ownership

Inspect the actual framework before applying patterns.

### React
When applicable:
- distinguish server/client state from local presentation state;
- avoid duplicating derived state;
- avoid effects for calculations that can be derived during render;
- keep async loading/error/success states explicit;
- preserve controlled/uncontrolled component contracts.

### Vue
When applicable:
- keep source-of-truth state explicit;
- avoid unnecessary watchers when computed state fits;
- keep composables/domain state ownership coherent;
- preserve reactive state boundaries through refactors.

### Svelte
When applicable:
- keep reactive derivation separate from imperative side effects;
- avoid duplicating state between stores and component locals;
- model async/error states explicitly.

These are architecture heuristics, not reasons to rewrite an existing sound state layer.

## Server / client / hydration boundaries

For SSR/hydrated frameworks:
- do not rely on browser-only APIs during server render;
- keep server/client ownership explicit;
- prevent hydration mismatch from nondeterministic content;
- avoid layout/state flashes caused by late client-only decisions;
- preserve accessibility during loading/hydration.

Do not move the whole UI client-side merely to avoid one hydration problem.

## Async UI state model

For remote/native async operations prefer explicit finite states over scattered booleans.

Conceptually:
```text
idle
loading
success(data)
empty
error(recoverable?)
```

For mutations also consider:
- optimistic;
- pending;
- confirmed;
- rolled back.

Do not let `isLoading`, `hasError`, `isEmpty`, and stale data produce impossible combinations.


## Error boundary / async failure ownership

For frameworks with error boundaries/router error surfaces, decide which layer owns:
- render failure;
- route/data-load failure;
- mutation failure;
- native IPC failure.

Do not catch every error at the leaf component and replace it with generic toast text.
Preserve enough context for local recovery and diagnostics.

## State-machine pressure test

When several booleans can produce impossible combinations, model the UI as a finite union/state machine instead.
Use this especially for async, auth, background-task, upload/download and multi-step form states.

## SVG icon implementation

### Lucide default for web UI

When no project icon library exists, prefer Lucide. For React/TypeScript, prefer `lucide-react` when dependency changes are allowed and appropriate.

```tsx
import { Download } from "lucide-react";

<button type="button">
  <Download aria-hidden="true" className="size-4" />
  Download
</button>
```

Import only used icons, keep size consistent, use `aria-hidden="true"` when adjacent text labels the action, and give icon-only buttons an accessible name. Keep default stroke behavior unless the product system intentionally standardizes another value.

If dependency installation is not allowed, use Lucide-compatible SVG assets or the existing project icon system rather than emoji.

For TypeScript/Tailwind frontends:
- prefer the project's existing SVG/icon component system;
- use SVG-rendering icon libraries or reusable SVG components;
- keep sizing consistent through shared tokens/utilities;
- prefer `currentColor` when icon color should follow semantic state;
- avoid duplicated raw SVG markup when a reusable icon component exists;
- never use emoji characters inside buttons, menus, tabs, inputs, status rows, toolbars or navigation as icon substitutes.

Bad:
```tsx
<button>⚙️ Settings</button>
<button>📁 Open</button>
<button>⬇️ Download</button>
```

Preferred:
```tsx
<button><SettingsIcon aria-hidden="true" />Settings</button>
<button><FolderOpenIcon aria-hidden="true" />Open</button>
<button><DownloadIcon aria-hidden="true" />Download</button>
```

For icon-only buttons, put the accessible name on the control.
