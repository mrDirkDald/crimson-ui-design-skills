# Anti-Neuroslop UI — Surface Economy and Product-Specific Layout

## Purpose

Use this reference when an interface starts to look like a generic AI-generated dashboard:
- sidebar + cards as the default;
- every group enclosed in a rounded rectangle;
- excessive borders and nested panels;
- equal visual weight across unrelated sections;
- large padding around very little content;
- generic SaaS structure applied to a product that should feel like a tool/workspace.

This is not anti-card. Cards are valid when they communicate a real state, interaction, selection, scroll, elevation, safety, or object boundary.

## Contents

- Core principle
- Container Necessity Test
- Rectangular Enclosure Budget
- Surface Economy
- Chrome-to-Content Ratio
- Anti-Cardification Gate
- Sidebar + Dashboard Guard
- Continuous Workspace
- Product-Specific Layout Archetypes
- Shape / Border / Rounded Rectangle Discipline
- Density and Visual Weight
- Edge-to-Edge Work Areas
- Inspector / Split-Pane / Command-Bar Patterns
- Navigation and Dashboard Necessity
- Product-Specific Identity
- Anti-Template Test
- Redesign Procedure
- Whole-Screen Silhouette
- QA Checklist

## 1. Content structure before containers

Group information in this order:

1. alignment;
2. proximity;
3. typography;
4. whitespace;
5. scale/value;
6. divider;
7. container only when semantically useful.

Do not begin by asking “what cards do I need?”

Ask:
- what is the main work object;
- what changes together;
- what must remain visible;
- what has an independent interaction/state lifecycle.

## 2. Container Necessity Test

Before adding a visible card/panel/border, answer:

```text
WHAT DOES THIS CONTAINER MEAN?
```

Good reasons:
- independently selectable object;
- separate scroll region;
- draggable/reorderable item;
- distinct state boundary;
- transient elevated surface;
- modal/popover/dialog;
- contextual inspector;
- collapsible group;
- destructive/safety boundary;
- comparison unit.

Weak reasons:
- “it looks cleaner”;
- “dashboards use cards”;
- “each section needs a box”;
- “otherwise the screen feels empty”.

If whitespace, alignment, and typography already group the content, do not add another box.

## 3. Rectangular Enclosure Budget

Every visible rectangle adds visual weight.

Count:
- cards;
- bordered sections;
- inset wells;
- nested panels;
- boxed rows;
- mini-stat cards;
- toolbar shells.

Do not use a fixed numeric limit. Instead ask whether the number of enclosures is greater than the number of real semantic boundaries.

If the UI feels “assembled from components” instead of designed as one composition, reduce enclosures.

## 4. Surface Economy

Prefer a small surface stack:

```text
CANVAS
PRIMARY WORKSPACE
OPTIONAL SECONDARY PANE / INSPECTOR
TRANSIENT OVERLAY
```

Avoid:

```text
canvas
→ card
→ nested card
→ inset card
→ chip
→ bordered value
```

Nested surfaces must earn their existence.

## 5. Chrome-to-Content Ratio

Chrome is framing around the actual task:
- borders;
- padding;
- headers;
- card shells;
- status wrappers;
- repeated metadata containers;
- oversized navigation/branding.

A repeated-use tool should maximize meaningful work content.

If a controller diagram, queue, editor, timeline, data table, or mapping canvas is visually smaller than its framing, the hierarchy is wrong.

## 6. Anti-Cardification Gate

FAIL when:
- every section is a rounded rectangle;
- settings are split into cards merely to manufacture hierarchy;
- one card contains another card without independent state;
- support/status cards compete with the primary work;
- borders are doing the job of hierarchy;
- all cards have nearly identical importance.

Refactor using:
- section heading + whitespace;
- aligned rows;
- one continuous work surface;
- local divider;
- inspector;
- split pane;
- list/table;
- direct manipulation.

## 7. Sidebar + Card Dashboard Default Guard

Do not automatically choose:

```text
left sidebar
+ page title
+ card grid
+ quick stats
```

This is only one archetype.

Alternatives:
- top tabs;
- compact command bar;
- workspace + inspector;
- list + details;
- canvas + properties;
- queue + detail panel;
- device visualizer + contextual controls;
- split pane;
- single-surface progressive disclosure.

Use sidebar only when durable top-level destinations actually justify it.

## 8. Continuous Workspace Principle

Tools centered around one primary object should often feel like one continuous workspace.

Examples:
- controller mapping;
- image editor;
- graph editor;
- server console;
- timeline;
- device configurator.

Prefer:

```text
primary object/workspace
+ contextual controls
+ inspector
```

over:

```text
object card
+ settings card
+ status card
+ action card
```

The user should feel they are operating the object, not browsing a dashboard describing it.

## 9. Product-Specific Layout Archetype

Identify the product archetype before composing the page.

### Device/controller configurator
Good:
- device visualization + live state + contextual inspector;
- mapping canvas + action inspector;
- profile strip + device workspace;
- calibration workspace.

### Editor
Good:
- document/canvas + inspector;
- command bar + tree + editor;
- timeline + properties.

### Downloader/queue
Good:
- compact input/action area + queue workspace + contextual details.

### Monitoring tool
Good:
- live data + event list + alert/status region.

Do not force every archetype into generic dashboard cards.

## 10. Shape Language

Identity can come from product-specific shape language:
- cut corners;
- line terminals;
- axis rings;
- mapping nodes;
- trigger/stick arcs;
- tab geometry;
- controller silhouette;
- selected-state marker.

Choose one or two recurring shape ideas.

Do not combine every fashionable geometry at once.

## 11. Rounded Rectangle Discipline

Rounded rectangles are appropriate for:
- buttons;
- fields;
- selectable tiles;
- floating tools;
- dialogs;
- independent objects;
- chips/badges.

They are not a default wrapper for:
- every text group;
- every status row;
- every navigation section;
- every informational block.

A rounded rectangle is not a hierarchy system.

## 12. Border Discipline

Borders should communicate:
- boundary;
- selection;
- focus;
- separation;
- interaction;
- elevation.

Do not outline everything.

If removing half the borders makes the UI cleaner without reducing clarity, those borders were decorative noise.

## 13. Density Hierarchy

Use density based on task frequency:
- compact for repeated controls;
- moderate for settings;
- more spacious for onboarding/explanation;
- highly explicit around destructive/safety actions.

Do not apply the same padding/radius/spacing to every section.

## 14. Visual Weight Hierarchy

Assign visual weight:

```text
PRIMARY WORK
PRIMARY ACTION / CURRENT SELECTION
CURRENT STATE
SECONDARY CONTROLS
SUPPORT
METADATA
```

Support blocks should not be as visually large as the main work object.

## 15. Edge-to-Edge Work Areas

For mapping canvases, controller diagrams, editors, timelines, previews, and dense lists, let the work area use the available space.

Do not inset everything inside a large padded card inside another card.

## 16. Inspector Pattern

When selection changes properties/actions, prefer a contextual inspector.

Example:

```text
[ controller/mapping workspace ] [ selected control inspector ]
```

Inspector may show:
- selected input;
- current mapping;
- action picker;
- sensitivity/deadzone;
- test/reset.

This is often stronger than many settings cards.

## 17. Split-Pane Pattern

Use split pane when two contexts need to remain visible:
- process list + rule editor;
- profiles + selected profile;
- bindings + action details;
- device list + diagnostics.

Do not force drill-down when side-by-side is more efficient.

## 18. Command-Bar Pattern

For desktop tools, a compact command bar may outperform large CTA cards.

Use for:
- save;
- reset;
- test;
- profile;
- enable/disable;
- import/export;
- diagnostics.

Do not turn every command into a large colored rectangle.

## 19. Navigation Weight

Navigation should not dominate the application unless navigation itself is the main task.

For small utilities:
- compact navigation;
- restrained brand block;
- minimal empty nav space;
- let workspace dominate.

## 20. Dashboard Necessity Test

Ask:

```text
Does the user need a summary before acting?
Or do they primarily need to operate/configure something?
```

If direct configuration is the job, the home screen may simply be the active device/profile workspace.

Do not add a dashboard just because desktop apps “need a dashboard”.

## 21. Status Presentation

Do not create a card for each status.

Prefer inline status when possible:

```text
● Connected
Xbox 360 Controller
Battery 100%
```

Use a larger surface only when failure/setup/system state requires explanation.

## 22. Product-Specific Identity

For controller software, identity can come from:
- controller silhouette;
- stick arcs;
- trigger geometry;
- button cluster;
- axis paths;
- mapping lines;
- calibration rings;
- live input pulse;
- profile slots.

These are stronger than:
- generic gradient card;
- glowing border;
- abstract blob;
- universal SaaS tile.

## 23. Controller Utility Layout Example

A strong RZTK-like layout could use:

```text
TOP COMMAND / PROFILE STRIP
profile + controller + engine state

MAIN WORKSPACE
large live controller

CONTEXTUAL INSPECTOR
selected stick/button/trigger

SECONDARY LIVE STRIP
axes + active window + precision + connection

MODE NAVIGATION
Mouse / Bindings / Keyboard / Auto Pause / Profiles
```

This is more product-specific than:

```text
sidebar
+ dashboard title
+ controller card
+ setup card
+ quick-settings cards
+ profile card
```

## 24. Anti-Template Test

Hide:
- logo;
- product name;
- accent color;
- hero/device artwork.

Ask:

> Could this exact structure become a VPN, notes app, AI assistant, server dashboard, finance app, and controller utility with only text changes?

If yes, the structure is too generic.

Strengthen workflow, object model, controls, state, terminology, and information structure.

## 25. AI-Neuroslop Warning Bundle

Treat this bundle as a warning:
- near-black canvas;
- 12–16px rounded cards;
- subtle one-pixel borders;
- gray mini-labels;
- one bright accent;
- Lucide;
- sidebar;
- equal card grid;
- pills;
- soft glow;
- large heading + tiny subtitle.

Every item can be good.

The failure is using the entire bundle without product-specific reasoning.

## 26. Redesign Procedure

When UI is over-cardified:

1. identify primary work object;
2. remove purely decorative outer cards in a branch/copy;
3. rebuild grouping with alignment, spacing and type;
4. restore only semantic containers;
5. choose one primary surface;
6. choose at most one persistent secondary pane when useful;
7. turn repeated cards into rows/lists/inspector;
8. reduce borders;
9. reduce radius repetition;
10. enlarge/directly expose the product object;
11. verify states;
12. compare whole-screen silhouette.

Do not just lower border opacity.

## 27. Whole-Screen Silhouette Test

At a glance, can you identify:
- dominant work area;
- secondary support area;
- navigation;
- state?

Or does the screen read as many equal rectangles?

Strong tools usually have a recognizable silhouette.

## 28. QA Checklist

FAIL if:
- every major section is carded without semantic reason;
- cards dominate primary work;
- hierarchy depends mostly on rectangles/borders;
- generic sidebar + card grid is used despite a more specific work model;
- nested surfaces have no independent state/interaction;
- chrome gets more attention than task content;
- all zones use identical density;
- support blocks equal primary work in visual weight;
- the design remains generic after hiding logo/name/accent.

PASS when:
- containers have clear reasons;
- workspace dominates;
- grouping survives with fewer borders;
- layout matches product archetype;
- density follows task frequency;
- product identity is structural;
- whole-screen silhouette is clear.
