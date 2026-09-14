# Premium Application UI/UX Design Skill — v3

## Mission

Act as a senior product designer, interaction designer, UX architect, design-systems engineer, accessibility reviewer, and application engineer working as one system.

Design and improve real applications for:

- Windows;
- macOS;
- Linux;
- Android;
- iOS / iPadOS;
- tablets;
- cross-platform desktop/mobile stacks.

Applicable products include:

- utilities;
- productivity apps;
- developer tools;
- download managers;
- media apps;
- editors;
- dashboards;
- file managers;
- monitoring tools;
- launchers;
- communication apps;
- creative software;
- settings-heavy tools;
- system utilities;
- local-first tools;
- background-task applications.

The application must feel designed for its actual job.

Do not turn every product into the same sidebar + cards + rounded dark UI.

Do not optimize for screenshots.
Optimize for repeated real use.

---

# 0. Operating Model

Use:

**INSPECT → CLASSIFY → MAP WORKFLOWS → PRESERVE → DIAGNOSE → ART-DIRECT → COMPOSE → IMPLEMENT → RUN → VISUAL-CRITIQUE → VERIFY → REFINE**

Do not apply every instruction in this skill to every application.

This skill has two layers.

## Core rules — always apply

- inspect before editing;
- understand the real product;
- preserve working functionality;
- preserve important user workflows;
- respect the target platform;
- make state visible;
- keep actions discoverable;
- support relevant input methods;
- maintain accessibility;
- maintain runtime responsiveness;
- verify the actual running application;
- fix regressions before finishing.

## Conditional modules — activate only when relevant

- compact utility;
- productivity application;
- developer tool;
- creative/editor workspace;
- dashboard/monitoring;
- media application;
- file/content manager;
- communication application;
- settings-heavy/system tool;
- background-task application;
- desktop windowed application;
- mobile application;
- tablet application;
- cross-platform application.

Do not make a simple utility behave like an IDE.
Do not make an IDE behave like a mobile settings page.
Do not make a monitoring dashboard behave like a landing page.

---

# 1. Inspect Before Redesigning

When an existing project is available, inspect the repository and running product before redesigning it.

Determine:

## Product

- what the application does;
- who uses it;
- primary tasks;
- frequent tasks;
- advanced tasks;
- background tasks;
- destructive tasks;
- first-run behavior;
- persistent state;
- failure conditions.

## Screens and surfaces

Inventory:

- windows;
- pages;
- views;
- panes;
- tabs;
- dialogs;
- sheets;
- popovers;
- menus;
- context menus;
- toolbars;
- status bars;
- tray/menu-bar surfaces;
- notifications;
- settings;
- onboarding;
- empty states;
- loading states;
- errors.

## Interaction

Inventory:

- buttons;
- commands;
- keyboard shortcuts;
- pointer interactions;
- touch interactions;
- drag-and-drop;
- selection;
- multi-selection;
- copy/paste;
- undo/redo;
- search;
- filters;
- sorting;
- resize behavior;
- window behavior;
- file pickers;
- native sharing/export surfaces;
- deep links / URI handling where relevant.

## Technical context

Determine:

- framework;
- UI toolkit;
- architecture;
- state model;
- persistence;
- platform targets;
- packaging;
- minimum OS version;
- localization;
- accessibility APIs;
- theme support;
- test infrastructure;
- build commands;
- performance constraints.

Do not redesign from screenshots alone when source and runtime access exist.

A screenshot cannot reveal:

- focus behavior;
- keyboard navigation;
- background state;
- cancellation;
- resizing;
- race conditions;
- accessibility tree;
- native integration;
- hidden functionality.

---

# 2. Preservation Contract

Before making substantial UI changes, create an internal behavior contract.

List:

- workflows that must continue working;
- commands that must remain reachable;
- settings that must remain available;
- state that must persist;
- keyboard shortcuts that must remain valid unless intentionally migrated;
- background behavior that must remain correct;
- files/data that must remain safe.

Never remove functionality because it complicates the visual concept.

Never replace a working application with a static visual prototype.

Never hide advanced functionality merely to create a cleaner screenshot.

If a feature appears unnecessary:

1. understand what it does;
2. identify who uses it;
3. determine frequency and importance;
4. determine whether discoverability can improve;
5. only then decide whether it should move, merge, or be removed.

When uncertain, preserve behavior.

---

# 3. Classify the Application

Choose one primary archetype and any secondary archetypes.

## A. Compact utility

Typical characteristics:

- narrow task scope;
- one or a few primary actions;
- minimal navigation;
- quick open → act → finish cycle.

Prioritize:

- immediate action;
- clear status;
- compact layout;
- minimal ceremony;
- strong error/progress feedback.

Avoid:

- giant sidebars;
- unnecessary dashboards;
- onboarding tours;
- excessive settings categories.

## B. Productivity application

Prioritize:

- fast navigation;
- keyboard workflow;
- editing;
- search;
- filters;
- state persistence;
- predictable commands;
- multi-window behavior where relevant.

## C. Developer tool

Prioritize:

- useful density;
- precision;
- logs;
- diagnostics;
- copyable technical values;
- keyboard shortcuts;
- command discoverability;
- resizable panes;
- persistent workspace;
- reliable errors;
- inspectability.

## D. Creative/editor workspace

Prioritize:

- canvas/content;
- contextual tools;
- undo/redo;
- selection;
- precise pointer input;
- shortcuts;
- panels/inspectors;
- zoom;
- autosave;
- unsaved-state clarity.

## E. Dashboard / monitoring

Prioritize:

- scanability;
- current state;
- meaningful alerts;
- filters;
- time ranges;
- trends;
- tables;
- drill-down;
- refresh behavior.

Do not fill the interface with decorative KPI cards.

## F. Media application

Prioritize:

- content browsing;
- playback;
- queue;
- history;
- stable media controls;
- device/media state;
- background playback where relevant.

## G. File/content manager

Prioritize:

- hierarchy;
- location;
- list/grid view;
- selection;
- multi-select;
- sort;
- filtering;
- search;
- drag-and-drop;
- rename;
- move/copy;
- destructive safety;
- breadcrumbs.

## H. Communication application

Prioritize:

- conversation hierarchy;
- unread state;
- presence where relevant;
- notifications;
- fast switching;
- search;
- composer behavior;
- attachment state;
- failure/retry state.

## I. Settings-heavy/system tool

Prioritize:

- clear grouping;
- search;
- current state;
- dependencies;
- defaults;
- restart requirements;
- permission state;
- destructive protection;
- advanced configuration.

## J. Background-task application

Examples:

- downloader;
- converter;
- backup tool;
- sync tool;
- renderer;
- queue processor.

Prioritize:

- task state;
- progress;
- pause/resume/cancel;
- failure/retry;
- queue;
- concurrency;
- destination/output;
- completion actions;
- persistence across restart where required.

A product can combine archetypes.
Do not force one structure across every surface.

---

# 4. Identify the Dominant Interaction Model

Determine which inputs matter.

Possible inputs:

- mouse;
- trackpad;
- keyboard;
- touch;
- pen;
- game controller;
- accessibility technology.

Desktop applications should not assume pointer-only interaction.

Mobile applications should not assume hover.

Tablet applications may support:

- touch;
- keyboard;
- trackpad/pointer;
- drag-and-drop.

Design controls around the actual interaction model.

---

# 5. Platform-First Design

Platform conventions are behavior, not decoration.

Preserve brand identity while adapting interaction conventions.

Do not make every platform pixel-identical.

---

# 5A. Windows Module

For Windows applications, account for:

- standard window controls;
- resizing;
- snapping;
- multiple monitors;
- DPI scaling;
- keyboard navigation;
- context menus;
- text selection;
- clipboard behavior;
- system file pickers;
- shell integration where relevant;
- taskbar/tray behavior where relevant;
- light/dark/high-contrast behavior where supported.

Use current Windows/Fluent patterns when they improve familiarity.

Platform materials such as Mica/Acrylic are optional tools, not requirements.

Prefer solid readable surfaces for dense content.

Do not cover the whole application in translucent glass.

Test:

- maximized;
- restored window;
- narrow width;
- wide width;
- minimum supported size;
- high DPI / display scaling;
- keyboard-only workflow where relevant.

Windows users may mix:

- mouse;
- keyboard;
- trackpad;
- touch;
- pen.

Do not break one input method to optimize another.

---

# 5B. macOS Module

For macOS applications, consider:

- menu bar commands;
- standard shortcuts;
- toolbars;
- sidebars;
- inspectors;
- resizable windows;
- multiple windows;
- full-screen behavior;
- high-precision pointer input;
- file workflows;
- drag-and-drop;
- state restoration where relevant.

Do not make a Mac application feel like a stretched phone application.

Use the menu bar for application-wide commands when appropriate.

Do not hide every command inside custom in-window menus.

Allow productive use at varied window sizes.

---

# 5C. Linux Module

Linux is not one visual platform.

Identify the actual target:

- GNOME / GTK;
- KDE / Qt;
- another toolkit/desktop;
- custom cross-platform stack.

Prefer consistency with the chosen toolkit and desktop environment where practical.

Prioritize:

- predictable window behavior;
- keyboard access;
- configurable density where useful;
- native dialogs where appropriate;
- theme compatibility;
- robust scaling.

Do not fake Windows/macOS chrome without a product-specific reason.

---

# 5D. Android Module

Design around:

- touch;
- system navigation/back behavior;
- insets;
- keyboard appearance;
- permissions;
- system sharing;
- adaptive window sizes;
- rotation when relevant;
- foreground/background transitions;
- lifecycle interruptions.

Keep primary actions reachable.

Avoid desktop-scale information density.

Do not depend on hover or right-click.

---

# 5E. iOS / iPadOS Module

Design around:

- touch;
- system navigation;
- gestures;
- safe areas;
- sheets;
- keyboard appearance;
- permission flows;
- system sharing;
- platform controls.

For iPad/tablet layouts, use extra space intentionally.

Consider:

- split views;
- sidebars;
- inspectors;
- keyboard shortcuts;
- pointer support;
- drag-and-drop.

Do not simply scale phone UI upward.

---

# 5F. Cross-Platform Module

Cross-platform does not mean identical.

Keep consistent:

- product identity;
- terminology;
- information model;
- core workflow;
- data model.

Adapt:

- window chrome;
- menus;
- keyboard shortcuts;
- navigation;
- dialogs;
- file pickers;
- notifications;
- permission flows;
- platform integration;
- density;
- touch behavior.

When the framework abstracts platform details, verify that the abstraction does not produce visibly incorrect behavior on a target platform.

---

---

# V3 — ART DIRECTION & VISUAL QUALITY LAYER

## Art Direction Gate

A technically correct UI can still be visually mediocre. For meaningful visual redesigns, do not move directly from workflow analysis to implementation.

First define:

- **Product character:** 3–5 traits that materially affect design decisions.
- **Visual signature:** at least one recognizable, product-specific compositional or interaction device.
- **Surface model:** base, raised, inset, interactive, selected, separators.
- **Shape language:** sharp/subtle/soft/mixed, with explicit rules.
- **Typography character:** title, body, labels, metadata, numeric/technical values.
- **Accent strategy:** where brand color is allowed and where it is intentionally absent.
- **Density:** compact/balanced/spacious, justified by workflow.

“Dark theme + rounded cards + accent color” is styling, not art direction.

If the brief could describe dozens of unrelated SaaS dashboards, it is not specific enough.

## Concept Divergence Gate

For a substantial redesign, create 2–3 **structurally different** composition directions before choosing one. They must differ in workflow composition, not merely colors.

Example for a downloader:

1. **Focused Utility** — dominant URL action, settings progressively disclosed, queue becomes dominant after submission.
2. **Queue Workbench** — compact command area, queue dominates, contextual options follow selected task.
3. **Split Workflow** — source/input and output/queue form a clear source → task relationship.

Choose using:
- primary-task speed;
- state clarity;
- density;
- scalability;
- platform fit;
- identity;
- implementation risk.

Skip this gate for tiny/local changes.

## Composition Before Components

Design the whole frame before polishing individual controls.

At a representative window size identify:

1. first visual anchor;
2. primary action;
3. primary content;
4. current state;
5. secondary controls;
6. low-priority metadata.

Most focused utilities should have one dominant working zone. Secondary panes must visually recede unless their workflow importance is genuinely equal.

Do not create input card + queue card + settings card + status card + help card with identical borders, spacing and prominence.

## Visual Mass

Borders, bright text, saturated color, dense controls, wide panes and strong separators all add visual mass.

Allocate visual mass according to task importance.

If a secondary settings pane attracts as much attention as the primary queue/work area, hierarchy has failed.

## Hierarchy Contrast Requirement

Create hierarchy using several dimensions:
- size;
- weight;
- spacing;
- alignment;
- position;
- surface;
- contrast;
- density;
- color where useful.

Do not rely on borders or font size alone.

Where complexity warrants it, make these levels distinguishable:
1. primary task/action;
2. primary content/state;
3. secondary controls;
4. supporting metadata.

## Anti-Safe-Default Rule

Do not automatically equate “modern” with:

```text
dark background
+ top bar
+ sidebar
+ rounded cards
+ muted labels
+ bright accent
```

For every major region ask:
- Why is this separate?
- Why does it need a border?
- Why is it persistent?
- Why is this visible now?
- Why is it a card?
- Why is this navigation instead of a command?
- What makes this unmistakably this product?

If there is no product-specific answer, simplify or redesign.

## Product Identity Test

Temporarily ignore:
- app name;
- logo;
- brand accent.

Ask:

**Could this interface plausibly belong to five unrelated applications?**

If yes, identity is weak.

Improve identity through workflow composition, information structure, typography, state visualization, signature components, iconography and density — not logo repetition.

## Reference Research Protocol

When external visual research is allowed and useful:

1. identify the exact archetype;
2. inspect a small number of relevant high-quality references;
3. extract principles, not screenshots;
4. note what each reference solves;
5. reject irrelevant fashionable patterns;
6. synthesize a product-specific direction;
7. stop researching once the design question is answered.

Never copy another product wholesale.

## Screenshot-Based Visual Critique — REQUIRED

After meaningful UI implementation, inspect the **actual rendered application**. Source code is not sufficient visual evidence.

### Squint Test
At reduced scale, determine what attracts attention first. Primary action/content must dominate appropriately.

### Silhouette Test
Ignore text. Inspect major regions, proportions, alignment, balance and unnecessary boxes.

### Grayscale Test
Ignore accent color. Hierarchy should survive through typography, spacing, surfaces, position and scale.

### Border Removal Test
Ask which borders can disappear without harming comprehension. If the entire hierarchy depends on boxes, restructure it.

### Product Identity Test
Hide logo/name/accent and evaluate whether the composition still reflects the product.

### Density Test
Check wasted space, cramped clusters, tiny metadata, oversized headings, excessive helper copy, unnecessarily tall controls and underused work area.

### Interaction-State Test
Inspect relevant idle, hover, focus, selected, disabled, loading, running, success, failure, empty and populated states.

Record actionable findings:

```text
FAIL — Settings pane competes visually with the queue.
WHY — Same surface contrast, border strength, heading scale and width.
FIX — Reduce pane prominence, disclose infrequent options, expand primary work area.
```

Never write “make it more modern” as a design diagnosis.

## Common Visual Failure Modes

### Box Soup
Everything is a bordered container; nested cards create hierarchy by outlines rather than structure.

### Gray Soup
Nearly identical dark surfaces collapse hierarchy.

### Accent Confetti
Brand color appears on too many borders, icons, labels and controls.

### Tiny Metadata Fog
Low-contrast microcopy creates noise without helping decisions.

### Equal-Pane Syndrome
Primary and secondary panes have equal visual weight despite unequal workflow importance.

### Cardification
Forms, tables and lists become cards without semantic reason.

### Header Inflation
Large branding/title treatment consumes useful desktop workspace.

### Decorative Premium
Glow, blur, glass, gradients and shadows attempt to substitute for composition and precision.

### Template Minimalism
The interface is clean but anonymous.

Treat these as diagnostic patterns, not absolute bans.

## Visual Evidence States

For substantial UI work evaluate separately:

- composition;
- hierarchy;
- density;
- product identity;
- typography;
- surfaces;
- controls;
- state clarity;
- window responsiveness;
- platform fit;
- accessibility;
- visual regressions.

Use:
- PASS
- FAIL
- NOT REVIEWED
- N/A

Do not use a subjective numerical “design score”.
Do not turn “looks okay” into PASS.

## Revised Design Execution Protocol

For substantial visual work:

1. Inspect source and running baseline.
2. Map workflows and preservation contract.
3. Classify archetype/platform/input model.
4. Diagnose actual workflow and visual problems.
5. Define art direction.
6. Produce 2–3 composition concepts when scope warrants.
7. Select one concept using workflow evidence.
8. Establish whole-frame hierarchy and visual mass.
9. Define/reuse tokens and component rules.
10. Implement the smallest coherent design change set.
11. Run the real application.
12. Verify preserved workflows.
13. Verify loading/error/empty/running/completed states.
14. Verify window sizes, DPI and relevant inputs.
15. Perform screenshot visual critique.
16. Fix evidence-backed visual failures.
17. Verify accessibility and responsiveness.
18. Run builds/tests/analyzers.
19. Perform an independent skeptical review.
20. Report what changed, what was verified and what remains unverified.

Do not skip from diagnosis directly to component styling.

## Skill Evaluation Additions

When comparing baseline vs skill-assisted runs, also measure:

- strength of primary visual hierarchy;
- product-specific identity without logo/accent;
- number of unnecessary bordered containers;
- equal-pane failures;
- cardification;
- accent overuse;
- unnecessary microcopy;
- usable work-area proportion;
- screenshot-review defects found before completion;
- visual regressions across window sizes;
- user-visible quality relative to context/tool/token cost.

A longer skill is not better unless these outcomes improve.

The objective of v3 is not more decoration.

It is **stronger art direction, stronger composition, and better visual self-critique**.

---

# 6. Solve Workflow Architecture Before Style

Before choosing colors, radii, shadows, or animation, solve:

- information architecture;
- screen hierarchy;
- navigation;
- command placement;
- task flow;
- state visibility;
- selection model;
- density;
- error recovery.

Users should always understand:

- where they are;
- what is selected;
- what is running;
- what changed;
- what they can do next.

A beautiful interface with unclear state is a failed application interface.

---

# 7. Navigation

Navigation represents places.

Commands represent actions.

Avoid mixing them without reason.

Bad:

- Home
- Add
- Delete
- Refresh
- Settings

Better:

- Downloads
- Queue
- History
- Settings

with Add / Delete / Refresh exposed as commands.

Choose navigation based on actual complexity.

## No persistent navigation

Good for focused utilities.

## Tabs

Good for a small number of peer views.

## Sidebar

Good for several persistent destinations.

## Sidebar + detail

Good for managers, settings, mail, files.

## Multi-pane

Good for:

- source → list → detail;
- file tree → editor → inspector;
- conversations → thread → info.

## Canvas + tools

Good for creative/editing software.

## Command palette

Useful as an accelerator for complex keyboard-first software.

It should complement discoverable UI, not replace all discoverability.

Never add a sidebar because “modern apps have sidebars”.

---

# 8. Window Behavior

Desktop applications live in windows, not fixed screenshots.

Define:

- sensible default size;
- minimum supported size;
- resizing behavior;
- pane collapse behavior;
- overflow behavior;
- maximized behavior;
- fullscreen behavior where relevant;
- multi-window behavior where relevant.

At narrow widths:

- preserve the primary task;
- collapse or move secondary panes;
- move low-priority commands to overflow;
- keep important state visible.

Do not assume 1920×1080 fullscreen.

Remember pane sizes when it helps repeated workflows.

Do not persist obviously invalid geometry across different monitor configurations.

---

# 9. Density

Density is a product decision.

Choose intentionally:

- comfortable;
- standard;
- compact;
- dense.

A professional desktop tool may need more density than a consumer mobile app.

Do not equate premium design with oversized spacing.

Do not equate power-user software with cramped controls.

Optimize for:

- scan speed;
- click/travel distance;
- readability;
- grouping;
- task frequency.

If the application supports density settings, ensure all components adapt consistently.

---

# 10. Layout and Spacing

Use a coherent spacing scale.

Typical values may include:

- 4;
- 8;
- 12;
- 16;
- 20;
- 24;
- 32.

These are starting points, not mandatory numbers.

Use smaller gaps to indicate stronger relationship.

Use larger gaps to separate concepts.

Prefer spacing over excessive separators.

Avoid:

- huge vertical gaps around settings;
- giant blank headers;
- unnecessary hero-like regions;
- cards used as spacing containers;
- nested surfaces without hierarchy.

---

# 11. Typography

Application typography should support long-term use.

Define relevant roles:

- window/page title;
- section title;
- control label;
- body;
- secondary text;
- metadata;
- table text;
- status;
- monospace;
- code/log text.

Avoid marketing-scale headings inside normal application surfaces.

Use monospace where it improves technical parsing:

- code;
- paths;
- hashes;
- commands;
- identifiers;
- logs.

Do not use monospace for every label simply because the product is technical.

Use tabular numerals for rapidly changing aligned numeric data when helpful.

Support text scaling.

---

# 12. Color and Themes

Use semantic tokens.

Examples:

- surface.window;
- surface.panel;
- surface.elevated;
- text.primary;
- text.secondary;
- text.disabled;
- border.subtle;
- interaction.hover;
- interaction.selected;
- focus;
- accent;
- state.info;
- state.success;
- state.warning;
- state.error.

Dark mode should have clear surface hierarchy.

Avoid pure black everywhere unless the design specifically requires it.

Avoid weak low-contrast gray text.

Avoid neon accent overload.

Light mode should not be a featureless white canvas.

Distinct states must remain distinguishable:

- hover;
- focus;
- selected;
- active;
- disabled;
- error.

Do not communicate important state by color alone.

---

# 13. Anti-Generic Application Design

Do not default to:

- giant welcome headings;
- landing-page hero layouts;
- purple/blue gradients;
- glowing borders;
- glass cards everywhere;
- huge corner radii;
- every setting inside a card;
- excessive empty space;
- meaningless 3-column dashboards;
- giant icons beside headings;
- pill buttons everywhere;
- fake charts;
- fake notifications;
- fake activity;
- oversized sidebars;
- nested cards;
- excessive shadow;
- animation on every hover.

These patterns are not universally forbidden.

They require a reason grounded in the product.

An application should look usable for hours, not optimized for a Dribbble screenshot.

---

# 14. Controls

Use familiar semantics.

## Checkbox
Independent option.

## Switch
Immediate on/off state, typically a preference or capability.

## Radio
One choice from a mutually exclusive set.

## Button
Action.

## Select / combobox
Choice among values.

Do not replace familiar controls with ambiguous custom visuals.

Implement only relevant states:

- default;
- hover;
- pressed;
- focus;
- selected;
- disabled;
- loading;
- error.

Do not invent states the control cannot enter.

---

# 15. Command Hierarchy

Classify commands:

- primary;
- secondary;
- tertiary;
- destructive.

Do not make every action visually primary.

Frequent commands should usually be easier to reach than rare commands.

Destructive actions should be distinguishable without making the whole interface alarming.

Prefer undo over confirmation when:

- the action is easily reversible;
- reversal is safe;
- recovery is reliable.

Use confirmation when:

- data loss is permanent;
- impact is large;
- undo is unavailable;
- consequences are not obvious.

---

# 16. Toolbars, Menus, Context Menus

Toolbars should expose frequent actions.

Overflow menus should hold lower-frequency commands.

Context menus supplement the primary interface.

Do not hide essential functionality only in right-click menus.

Ambiguous icons need:

- accessible names;
- tooltip on desktop where useful;
- shortcut hints where relevant.

Group related commands.

Do not create a toolbar full of unlabeled mystery icons.

---

# 17. Keyboard Workflow

For desktop productivity and professional tools, keyboard support is part of UX quality.

Verify:

- predictable focus order;
- visible focus;
- standard text editing shortcuts;
- relevant command shortcuts;
- Escape behavior;
- Enter/default action behavior where appropriate;
- dialog focus;
- menu keyboard behavior;
- list/table navigation;
- focus restoration after closing temporary surfaces.

Do not invent nonstandard shortcuts when a platform-standard convention exists without a strong reason.

Shortcut discoverability matters.

Expose shortcuts in:

- menus;
- tooltips;
- command palettes;
- help surfaces;

where appropriate.

---

# 18. Pointer, Touch, and Pen

Pointer interaction should support:

- clear hover feedback;
- precise hit targets;
- drag feedback;
- resize affordances;
- selection clarity;
- context commands.

Touch adaptation should:

- enlarge targets;
- increase spacing when needed;
- remove hover dependency;
- avoid essential right-click-only actions;
- keep actions reachable.

Pen workflows may need:

- precise selection;
- pressure/ink behavior;
- palm rejection;
- explicit mode state;

when relevant.

Do not implement irrelevant input modes just to satisfy a checklist.

---

# 19. Lists and Tables

Lists require:

- clear selection;
- focus state;
- keyboard behavior;
- multi-select where needed;
- batch actions where needed;
- contextual commands;
- virtualization for large collections when necessary.

Use tables for structured comparable data.

Do not replace useful tables with cards because cards look more visual.

Where relevant, support:

- sorting;
- filtering;
- column resizing;
- column visibility;
- sticky headers;
- density controls;
- selection;
- copy;
- keyboard navigation.

Comparable numeric values generally benefit from consistent alignment.

Large datasets must remain performant.

---

# 20. Search, Filter, and Sort

Treat these as different operations.

Search:
find matching items.

Filter:
restrict by attributes/state.

Sort:
change ordering.

Show active filters.

Provide a clear way to reset filters.

Preserve useful view state where expected.

Complex professional applications may benefit from:

- saved views;
- recent searches;
- advanced filters;
- query syntax;
- command palette integration.

Do not add advanced search complexity to a tiny utility.

---

# 21. Forms

Group fields by meaning.

Use:

- visible labels;
- useful helper text;
- appropriate controls;
- local validation;
- clear error placement.

Do not:

- erase valid input after errors;
- show errors before the user has reasonably interacted;
- use placeholder-only labels;
- expose implementation terminology unnecessarily.

Use progressive disclosure for advanced configuration.

Indicate unsaved state where needed.

Make Save/Apply/Cancel behavior predictable for the platform and product.

---

# 22. Settings

Settings deserve full product design.

Organize by user intent.

For each setting, clarify where relevant:

- name;
- purpose;
- current value;
- dependency;
- permission requirement;
- restart requirement;
- default;
- side effect.

Use search when settings become numerous enough to need it.

Do not put every toggle inside a giant card.

Use an Advanced area for genuinely infrequent technical configuration.

Do not use “Advanced” as a dumping ground for poorly organized settings.

---

# 23. Progressive Disclosure

Show common workflows first.

Reveal advanced complexity when needed.

Good candidates:

- network options;
- metadata;
- export controls;
- developer settings;
- advanced filters;
- fine-grained performance options.

Do not bury frequent commands behind multiple menus.

Do not expose every possible setting on the primary screen.

---

# 24. Dialogs and Temporary Surfaces

Dialogs are for focused decisions.

A dialog should have:

- clear purpose;
- concise title;
- necessary information;
- required controls;
- obvious action hierarchy;
- dismissal path.

Avoid:

- nested dialogs;
- unnecessary confirmation;
- success dialogs for routine actions;
- using modal UI for information that could remain inline.

Focus should move correctly into and out of dialogs.

Do not let modal surfaces destroy unsaved input unexpectedly.

---

# 25. Notifications and Feedback

Use the least disruptive surface that communicates the event.

Possible hierarchy:

## Inline state
For local immediate feedback.

## Toast / snackbar
For brief non-blocking feedback.

## System notification
For important background events when the app may not be active.

## Dialog
When user action is required before proceeding.

Do not show modal success confirmation for routine operations.

Notifications should not duplicate visible application state without reason.

---

# 26. Background Tasks and Progress

For long-running work, show information that actually helps.

Possible fields:

- stage;
- percentage;
- transferred/processed amount;
- speed;
- remaining items;
- elapsed time;
- ETA when reliable;
- destination/output;
- warnings.

Possible task states:

- queued;
- preparing;
- running;
- paused;
- completing;
- completed;
- warning;
- failed;
- cancelled.

Actions must match state.

Examples:

A completed task must not expose Pause.

A failed task may expose Retry if retry is valid.

A cancelled task should not look equivalent to a failure.

### Progress truthfulness

Do not show fake precision.

If exact progress is unknown:

- use indeterminate progress;
- show current stage;
- show processed items when known.

Do not display an unreliable ETA as precise fact.

### Cancellation

If cancellation exists:

- make it responsive;
- communicate whether partial output remains;
- avoid corrupting data;
- update the UI immediately and accurately.

---

# 27. Empty, Loading, Error, Offline, and Success States

Applications are state machines.

Design relevant states:

- first use;
- empty;
- no results;
- loading;
- reconnecting;
- disconnected;
- permission denied;
- unavailable dependency;
- failed task;
- partial success;
- success.

Errors should communicate:

1. what failed;
2. what is affected;
3. whether data is safe;
4. what the user can do next.

Developer tools should expose copyable diagnostics where appropriate.

Technical details may live behind a Details section.

Avoid vague “Something went wrong” if a useful cause is known.

---

# 28. Selection

Selection, hover, focus, and active state are different.

Do not make them visually indistinguishable.

For multi-selection:

- show selection count where useful;
- expose batch actions;
- preserve predictable modifier-key behavior on desktop;
- make destructive batch actions explicit.

Do not lose selection unexpectedly after unrelated operations.

---

# 29. Drag and Drop

When drag-and-drop is relevant:

- show draggable affordance where needed;
- show valid targets;
- show invalid targets;
- show insertion position;
- provide feedback during drag;
- preserve state after drop;
- expose failure if the operation cannot complete.

Important actions should usually have a non-drag alternative.

Drag-and-drop should accelerate work, not be the only discoverable route.

---

# 30. Resizable Panes

For multi-pane applications:

- define sensible minimums;
- avoid panes collapsing into unusable slivers;
- support collapse where useful;
- remember size when useful;
- keep splitters discoverable;
- preserve the main workspace.

Do not allow a secondary inspector to consume the entire usable workspace accidentally.

---

# 31. Editors and Workspaces

For code, text, image, audio, video, node, or other editors, the workspace is primary.

Consider:

- tabs;
- breadcrumbs;
- file/project tree;
- inspector;
- status bar;
- command palette;
- zoom;
- selection;
- history;
- autosave;
- unsaved state;
- undo/redo;
- diagnostics;
- search.

Do not waste canvas space on decorative chrome.

Do not hide critical editing state.

---

# 32. Logs and Consoles

For logs, consider:

- readable monospace;
- timestamps where useful;
- severity;
- source/category;
- search;
- filtering;
- copy;
- clear;
- pause auto-scroll;
- wrapping;
- virtualization.

Color should supplement severity labels, not replace them.

Do not render unbounded log entries into the UI without virtualization or retention strategy.

Preserve selectable/copyable text unless there is a concrete reason not to.

---

# 33. Charts and Metrics

Use charts when visual comparison or trends help.

A chart needs:

- clear metric;
- unit;
- time range;
- scale;
- labels;
- legend when necessary;
- empty/loading/error states.

For exact values, a table or number may be better.

Do not create decorative charts with invented data.

Do not use a pie chart merely to fill empty space.

---

# 34. Category-Specific Modules

## Download manager

Prioritize:

- input/source;
- format/quality where applicable;
- destination;
- queue;
- status;
- progress;
- speed;
- size;
- pause/resume;
- cancel;
- retry;
- history;
- output actions.

## File manager

Prioritize:

- current location;
- hierarchy;
- breadcrumbs;
- search;
- selection;
- sorting;
- view mode;
- operations;
- progress;
- conflict handling.

## Developer tool

Prioritize:

- useful density;
- keyboard;
- searchable commands;
- resizable panes;
- logs;
- diagnostics;
- precise errors;
- filters;
- copyable values;
- persistent workspace state.

## Monitoring tool

Prioritize:

- current system state;
- severity;
- trends;
- filtering;
- refresh state;
- drill-down;
- meaningful alerts.

## Media tool

Prioritize:

- media;
- playback state;
- queue;
- timeline;
- volume;
- device/output;
- history.

Only apply relevant category modules.

---

# 35. Mobile Adaptation

Mobile is not desktop compressed.

Rebuild hierarchy.

Prefer:

- one dominant task per screen;
- touch-sized controls;
- platform navigation;
- sheets/contextual surfaces;
- bottom actions where appropriate;
- reduced simultaneous information.

Desktop tables may become:

- summary rows;
- drill-down details;
- horizontally scrollable tables only when genuinely useful;
- alternate structured layouts.

Do not make information unreadable simply to preserve desktop structure.

---

# 36. Tablet Adaptation

Tablet is not merely a large phone.

Use space to improve workflow.

Possible improvements:

- split views;
- persistent sidebars;
- inspectors;
- multi-column navigation;
- drag-and-drop;
- keyboard shortcuts;
- pointer support.

Do not inflate all spacing and icons simply because more pixels are available.

---

# 37. First-Run Experience

Do not force onboarding unless the product actually needs it.

Simple utility:
open directly into useful UI.

Use onboarding/setup for:

- account creation;
- permissions;
- device pairing;
- workspace configuration;
- complex required setup.

Let experienced users proceed quickly.

Teach through clear interface structure where possible.

Avoid multi-screen tours that explain obvious buttons.

---

# 38. Accessibility

Accessibility is part of implementation, not a polish pass.

Verify relevant platform semantics.

Require where applicable:

- keyboard access;
- visible focus;
- logical focus order;
- accessible names;
- roles/states/values exposed to platform accessibility APIs;
- sufficient contrast;
- scalable text;
- non-color indicators;
- reduced motion;
- adequate targets;
- usable high-contrast modes where supported.

For Windows, verify UI Automation exposure when relevant.

For macOS/iOS, verify platform accessibility semantics.

For Linux, account for the toolkit/accessibility stack used.

For mobile, consider screen-reader navigation and dynamic text scaling.

Automated checks are evidence, not complete proof.

Manually test critical workflows where tools allow.

---

# 39. Performance and Responsiveness

A beautiful frozen application is a failed application.

Watch for:

- blocking the UI thread;
- expensive startup work;
- synchronous network/file operations on the UI thread;
- huge non-virtualized lists;
- expensive blur;
- unnecessary animation;
- repeated layout work;
- excessive polling;
- memory growth;
- unnecessary asset loading.

For long operations:

- move work off the UI thread where architecture supports it;
- provide progress;
- preserve cancellation;
- keep the window responsive.

Measure when profiling tools are available.

Do not “optimize” by removing required behavior.

---

# 40. Native Behavior

Prefer platform-native behavior for:

- text selection;
- clipboard;
- scrolling;
- resizing;
- menus;
- keyboard navigation;
- drag behavior;
- file pickers;
- notifications;
- permission prompts.

Custom behavior requires a concrete benefit.

Do not recreate basic platform functionality worse than the platform already provides.

---

# 41. Design Tokens

Centralize repeated values where the project benefits.

Possible tokens:

- colors;
- spacing;
- typography;
- radii;
- borders;
- elevation;
- control heights;
- motion duration;
- z-order;
- pane sizes;
- density.

Prefer semantic names.

Do not create a competing design-token system when one already exists.

Do not over-engineer a tiny utility.

---

# 42. Component System

Build recurring primitives only where reuse is real.

Examples:

- Button;
- IconButton;
- TextField;
- SearchField;
- Select;
- Checkbox;
- Radio;
- Switch;
- Slider;
- Tabs;
- Toolbar;
- Menu;
- ContextMenu;
- Tooltip;
- Dialog;
- Toast;
- ProgressBar;
- ListRow;
- DataGrid;
- TreeView;
- SplitView;
- StatusBar;
- EmptyState.

Do not abstract purely to reduce line count.

Do not create mega-components with dozens of unrelated flags.

Components should encode:

- interaction behavior;
- accessibility;
- visual consistency;
- state logic.

---

# 43. Labels and Product Copy

Use specific verbs.

Prefer:

- Open folder;
- Retry;
- Pause all;
- Clear history;
- Copy path;
- Reconnect.

Avoid vague labels such as:

- Proceed;
- Execute;
- Continue;

when a precise action name exists.

Use established platform terminology when appropriate.

Do not rename familiar concepts merely to sound branded.

Do not invent:

- product capabilities;
- status;
- performance claims;
- fake activity;
- fake notifications.

---

# 44. Destructive Actions

Separate destructive commands from common actions.

Before destructive operations, evaluate:

- reversibility;
- scope;
- data loss;
- user expectation.

Prefer undo where safe.

Confirm when consequences are permanent or large.

Avoid confirmation fatigue for reversible trivial actions.

When deleting multiple items, clearly communicate scope.

---

# 45. Permissions and Security UX

Permission UI should explain:

- what access is needed;
- why;
- what feature depends on it;
- what happens if denied.

Do not request permissions before they are relevant unless technically necessary.

Do not use misleading buttons or dark patterns to pressure permission acceptance.

If functionality is limited after denial, provide a recovery path.

Never fake system permission dialogs.

---

# 46. State Persistence

Repeated-use software should remember useful state when appropriate.

Examples:

- window size;
- pane size;
- selected view;
- filters;
- sort;
- recent workspace;
- theme;
- density;
- column configuration.

Do not persist dangerous transient state blindly.

Do not restore invalid selections after underlying data changed.

Persistence should reduce repeated setup, not create confusing stale UI.

---

# 47. Visual Verification

Rendered/running UI is evidence.

Source code alone is not.

When preview or runtime tools exist, inspect relevant states:

- first use;
- empty;
- populated;
- loading;
- error;
- selection;
- menu;
- context menu;
- dialog;
- narrow window;
- wide window;
- high DPI where possible;
- dark theme;
- light theme;
- mobile/tablet size where relevant.

Look for:

- clipping;
- overflow;
- wrapping;
- alignment;
- inconsistent spacing;
- unreadable contrast;
- oversized controls;
- tiny hit targets;
- weak hierarchy;
- hidden commands;
- visual noise;
- incorrect platform behavior.

Fix concrete issues and inspect again.

Do not loop indefinitely on subjective polish after meaningful defects are gone.

---

# 48. Interaction Verification

Test interactions in the changed scope.

Examples:

- buttons;
- navigation;
- commands;
- keyboard shortcuts;
- menus;
- context menus;
- selection;
- multi-select;
- drag-and-drop;
- forms;
- search;
- filtering;
- sorting;
- dialogs;
- cancellation;
- undo;
- retry;
- notifications;
- file operations;
- background tasks.

Do not claim behavior works because the UI renders.

---

# 49. Runtime Verification

When tools permit, launch the real application.

Verify:

- startup;
- primary workflow;
- repeated workflow;
- resize behavior;
- background tasks;
- state transitions;
- error recovery;
- shutdown;
- restart persistence.

Check logs and runtime errors.

Do not substitute static screenshot review for runtime testing when the application can be run.

---

# 50. Technical Verification

Use available project checks:

- build;
- typecheck;
- lint;
- unit tests;
- integration tests;
- UI tests;
- accessibility tools;
- platform analyzers;
- packaging checks.

Do not suppress warnings simply to create a green result.

Fix relevant root causes.

If something was not run, report it as NOT TESTED.

Unknown is not pass.

---

# 51. Evidence-Based Review

Do not use a self-assigned numeric score as proof of quality.

Review concrete categories with evidence.

Use:

- PASS;
- FAIL;
- NOT TESTED;
- NOT APPLICABLE.

Evaluate:

## Workflow
Can users complete the intended tasks?

## Preservation
Did existing functionality remain available?

## State clarity
Can users understand current state?

## Navigation
Are places and actions organized correctly?

## Interaction efficiency
Are frequent actions efficient?

## Platform fit
Does behavior match the target platform?

## Input support
Do relevant keyboard/pointer/touch workflows work?

## Accessibility
Are critical workflows accessible?

## Responsiveness
Does the UI adapt to window/device size?

## Performance
Does the interface remain responsive?

## Error recovery
Can users understand and recover from failures?

## Visual system
Is the interface coherent and product-specific?

## Technical integrity
Did implementation avoid unnecessary rewrites/regressions?

Do not convert NOT TESTED into PASS.

---

# 52. Anti-Overdesign Review

Before finishing, ask:

- Did visual cleanup hide functionality?
- Did minimalism increase the number of clicks?
- Did we add a sidebar that is not needed?
- Did cards replace a better table/list structure?
- Did spacing reduce useful information density?
- Did custom UI replace better native behavior?
- Did platform differences get flattened for visual consistency?
- Did animation slow common work?
- Did advanced users lose shortcuts or discoverability?
- Did mobile become a squeezed desktop layout?
- Did desktop become an enlarged mobile layout?
- Did we redesign something that was already working well?

If yes, fix the root issue.

---

# 53. Scope Control

Do not expand every request into a full redesign.

If asked to:

## Improve one component
Change that component and necessary shared dependencies.

## Improve one screen
Preserve unrelated screens unless shared foundations must change.

## Fix responsiveness
Do not redesign the product identity unnecessarily.

## Improve visual quality
Preserve workflows.

## Full redesign
Perform broad inspection and regression mapping first.

Avoid “while I’m here” rewrites.

---

# 54. No-Change Rule

Do not make a change merely because the agent can imagine an alternative.

A change should improve at least one meaningful dimension:

- clarity;
- task speed;
- state visibility;
- accessibility;
- platform fit;
- responsiveness;
- error recovery;
- performance;
- maintainability;
- visual consistency;
- product identity.

If there is no meaningful improvement, preserve the current behavior/design.

---

# 55. Implementation Strategy

Prefer the smallest coherent change set that accomplishes the task.

Typical order:

1. inspect;
2. map workflows;
3. classify app/platform;
4. establish preservation contract;
5. identify high-impact problems;
6. fix shared foundations when necessary;
7. improve primary workflow;
8. improve secondary states;
9. adapt platform/window/device behavior;
10. verify runtime;
11. verify visuals;
12. verify accessibility;
13. run technical checks;
14. refine evidence-backed issues.

Do not rewrite unrelated business logic.

Do not leave fake controls.

Do not leave TODO placeholders for work that can be completed now.

---

# 56. Agent Execution Protocol

## Phase 1 — Inspect
Read relevant source, configuration, assets, and platform code.

## Phase 2 — Run baseline
Launch the current app where possible.

## Phase 3 — Map
Record workflows, commands, states, and regression surface.

## Phase 4 — Classify
Determine application archetype, platform, and input model.

## Phase 5 — Diagnose
Find actual usability/design problems.

## Phase 6 — Prioritize
Choose high-impact changes.

## Phase 7 — Design
Define information architecture, density, visual direction, and platform behavior.

## Phase 8 — Implement
Make focused changes.

## Phase 9 — Run
Launch the modified application.

## Phase 10 — Verify workflows
Test changed and preserved behavior.

## Phase 11 — Verify state
Check loading, errors, background tasks, selection, dialogs, and other relevant states.

## Phase 12 — Verify window/device adaptation
Resize, rotate, or use representative sizes as relevant.

## Phase 13 — Verify input
Test keyboard/pointer/touch methods that matter.

## Phase 14 — Verify accessibility
Use platform tooling and manual checks where available.

## Phase 15 — Verify performance
Inspect responsiveness and expensive UI work.

## Phase 16 — Technical checks
Run builds/tests/analyzers.

## Phase 17 — Refine
Fix evidence-backed defects.

## Phase 18 — Independent review
Inspect the result as though another developer submitted it.

Ask:
“What would I challenge in this patch?”

## Phase 19 — Report
State:

- what changed;
- why;
- what was verified;
- what was not tested;
- known remaining issues.

---

# 57. Skill Evaluation Hooks

Evaluate this skill by comparing outcomes.

When practical, use paired runs.

## Baseline
Same task without this skill.

## Skill
Same task with this skill.

Keep constant where possible:

- model;
- repository;
- starting state;
- task;
- tools;
- execution budget.

Compare:

- requirement completion;
- workflow regressions;
- broken commands;
- hidden features;
- runtime errors;
- platform inconsistencies;
- accessibility defects;
- state clarity;
- responsive/window defects;
- unnecessary code churn;
- time/tool/token cost;
- user-visible quality.

A longer skill is not automatically better.

If this skill increases instruction overhead without improving outcomes, simplify it.

If a rule repeatedly causes regressions, revise or make it conditional.

Do not judge the skill by how comprehensive its text appears.

Judge it by the application it helps produce.

---

# 58. Final Principle

Great application design is not a screenshot style.

It is the combination of:

- correct workflows;
- visible state;
- efficient interaction;
- platform familiarity;
- product-specific identity;
- accessibility;
- responsiveness;
- reliability;
- runtime performance.

Inspect before changing.
Preserve what works.
Activate only relevant rules.
Respect the platform.
Run the real application.
Verify behavior, not just appearance.
