---
name: crimson-ui-design-max
description: Exhaustive, token-unconstrained UI/UX design and implementation skill for web, desktop, mobile, native, cross-platform, game, embedded, terminal, Electron, Tauri and unfamiliar UI stacks. Use when maximum design depth is preferred over context efficiency.
---

# Crimson UI Design MAX

This is the exhaustive edition. Do not optimize primarily for token count. Optimize for design correctness, coherence, product fit, implementation safety, accessibility, and verified runtime quality.

## 0. Operating principle

For meaningful UI work, understand the product before touching visual details.

Use this sequence:

```text
UNDERSTAND PRODUCT
→ TRACE REAL SURFACE
→ DEFINE CONTRACT
→ PRESERVE BEHAVIOR
→ DIAGNOSE SYSTEM
→ CHOOSE PHASE
→ DEFINE VISUAL / UX THESIS
→ DESIGN STRUCTURE
→ MAP TO REAL TOOLKIT
→ IMPLEMENT
→ RUN
→ INSPECT
→ VERIFY STATES
→ FIX ROOT CAUSES
→ STOP
```

A beautiful screenshot that breaks workflow is a failure. A technically correct implementation that looks generic, incoherent, or inaccessible is also a failure.

## Nested subskill architecture

Every major domain skill contains **multiple deep aspect subskills**.

Architecture:

```text
ROOT MAX SKILL
→ DOMAIN SUBSKILL
  → ASPECT SUBSKILL(S)
    → DEEP REFERENCE / HANDBOOK
```

Examples:

```text
color
→ harmony-theory
→ semantic-color-tokens
→ theme-adaptation
→ color-accessibility
→ data-color
→ palette-generation
```

```text
application
→ workflow-architecture
→ commands-shortcuts
→ selection-focus
→ persistence-recovery
→ density-inspectors
→ desktop-mobile-adaptation
```

```text
qa
→ visual-hierarchy-audit
→ interaction-state-audit
→ accessibility-audit
→ responsive-cross-platform
→ visual-regression
→ evidence-reporting
```

MAX mode is intentionally expansive. If several aspect subskills materially affect correctness, load all of them.

The purpose of nested subskills is **depth and specialization**, not token reduction.

## 1. Task contract

Before meaningful work establish a contract. Expand it when the task is broad.

```text
REQUESTED OUTCOME:
PRIMARY USERS:
PRIMARY JOB:
ACCEPTANCE CRITERIA:
MUST PRESERVE:
ALLOWED TO CHANGE:
NOT IN SCOPE:
KNOWN CONSTRAINTS:
PLATFORM / DEVICE:
INPUT METHODS:
THEME REQUIREMENTS:
ACCESSIBILITY REQUIREMENTS:
PERFORMANCE REQUIREMENTS:
LOCALIZATION REQUIREMENTS:
UNKNOWN:
BLOCKED:
```

Do not silently convert “improve this screen” into “rewrite the application”. Do not silently preserve a broken visual system either.

## 2. Evidence hierarchy

Prefer evidence in this order:

1. rendered runtime behavior;
2. code paths proven to govern the target surface;
3. resolved tokens/themes/styles actually applied;
4. component props/variants/state logic;
5. product requirements and content;
6. design documentation that is demonstrably current;
7. screenshots/reference images;
8. repository comments/README only when consistent with runtime;
9. inference.

Names and nearby files are not proof that a style or component controls the target UI.

## 3. Phase selection

Use one or move between them deliberately:

- `REVIEW`: inspect and report only.
- `REFINE`: keep accepted structure; correct local weaknesses.
- `REDESIGN`: change the governing visual/interaction structure because local fixes would create patches.
- `IMPLEMENT`: build the selected direction.
- `VERIFY`: run and inspect the result.

Do not redesign just because redesign is more interesting.

## 4. Systemic redesign gate

Escalate toward REDESIGN when several of these fail together under one root cause:

- palette/accent hierarchy;
- typography roles;
- spacing rhythm;
- surface/border/elevation language;
- action hierarchy;
- layout proportions;
- navigation model;
- information architecture;
- state clarity;
- imagery integration;
- product specificity;
- responsive behavior;
- interaction feedback;
- icon language.

Record:

```text
SYSTEMIC CONFLICT:
EVIDENCE:
AFFECTED LAYERS:
WHY LOCAL PATCHES ARE INSUFFICIENT:
MUST PRESERVE:
NEW VISUAL / UX THESIS:
```

When systemic disharmony is confirmed, changing the entire visual layer is allowed. Do not rewrite unrelated business logic.

## 5. Product-specificity test

Temporarily ignore logo, product name, hero image, and branded copy.

Ask:

> Could this exact structure and styling be relabeled for several unrelated products with almost no change?

If yes, strengthen identity through workflow, content model, interaction, domain controls, typography, information structure, media treatment, and real state. Do not solve genericity with random decoration.

## 6. Composition hierarchy

For every important surface identify:

1. first visual anchor;
2. primary job;
3. primary action;
4. primary content/workspace;
5. current state;
6. secondary controls;
7. tertiary metadata;
8. recovery path.

Visual mass should follow task importance. Helper cards, onboarding panels, metadata, and decorative media must not accidentally become co-primary.

## 7. Color

Use semantic palette architecture. Color is not a decoration layer added after layout.

Define relevant roles:

```text
CANVAS
SURFACE
SURFACE-ELEVATED
TEXT-PRIMARY
TEXT-SECONDARY
TEXT-MUTED
BORDER
DIVIDER
ACCENT-PRIMARY
ACCENT-SECONDARY (optional)
SELECTION
FOCUS
SUCCESS
WARNING
DANGER
INFO
```

Use the dedicated color references for exhaustive palette recipes. Harmony and accessibility are separate gates. A palette can be harmonious but unreadable; a high-contrast palette can be ugly and incoherent.

## 8. Typography

Typography must establish role, hierarchy, rhythm, density, and brand tone.

Define:

```text
DISPLAY / BRAND
PAGE TITLE
SECTION TITLE
SUBSECTION TITLE
BODY
CONTROL LABEL
METADATA
CODE / TECHNICAL
NUMERIC / TABULAR
CAPTION
```

Avoid “tiny metadata fog”, giant headings without product reason, random font-weight jumps, and multiple display fonts competing for identity.

## 9. Spacing

Use a coherent scale and optical judgment together. Common scales such as 4/8/12/16/24/32 are useful but not laws.

Check:
- vertical rhythm;
- container padding;
- control grouping;
- text-to-control spacing;
- section boundaries;
- alignment lines;
- density relative to task frequency;
- touch targets;
- large empty areas that are either intentional breathing room or accidental layout waste.

## 10. Surfaces

Do not default every semantic group to a rounded card.

Use in order:
1. alignment;
2. whitespace;
3. typography;
4. subtle surface shift;
5. divider;
6. border;
7. elevation;
8. strong container treatment only when needed.

## 11. Iconography — Lucide baseline

Priority:

```text
1. Existing coherent project icon system
2. Lucide Icons
3. Compatible custom SVG/vector icon
```

Lucide is the baseline when there is no established coherent system.

Use consistent viewBox, optical size, stroke behavior, currentColor inheritance, and interaction state. Common visual sizes: 16, 18, 20, 24 px depending on density.

Never use emoji or arbitrary Unicode pictograms as UI icons. Emoji are allowed only as actual content such as chat, reactions, or user-generated text.

For icon-only controls provide accessible names. For decorative icons hide redundant semantics from assistive technology where appropriate.

## 12. Motion

Every motion effect should have a job:
- state transition;
- spatial continuity;
- feedback;
- hierarchy;
- narrative/brand expression.

Do not use `transition: all` as a design strategy. Do not stack parallax, pinned scroll, WebGL, page wipes, cursor effects, and text reveals just to look “award-winning”.

Respect reduced motion.

## 13. Backgrounds and imagery

Treat images as composition, not wallpaper.

Define:
- focal point;
- crop;
- local contrast zones;
- text-safe zones;
- desktop/mobile crop behavior;
- overlay direction and strength;
- fallback/loading behavior.

Do not uniformly crush a meaningful image under an opaque dark layer unless that is intentionally the visual thesis.

## 14. Forms

Use persistent labels when identity must survive typing. Validate at useful time. Preserve valid user input after failure. Prevent duplicate submits. Show processing, success, failure, disabled, dependency, and unsaved states. Prefer reversible undo over unnecessary confirmation when safe.

## 15. States

For relevant components verify:

```text
DEFAULT
HOVER
FOCUS-VISIBLE
PRESSED
SELECTED
DISABLED
LOADING
SUCCESS
WARNING
ERROR
EMPTY
PARTIAL
OFFLINE
STALE
PERMISSION-DENIED
```

Not every component needs every state, but missing necessary states is a product defect.

## 16. Responsive and adaptive design

Responsive design is not “stack desktop vertically”. Reprioritize.

Check:
- reading order;
- action order;
- navigation transformation;
- tables/data density;
- sidebars/inspectors;
- dialogs/sheets;
- media crop;
- keyboard vs touch;
- safe areas;
- high DPI;
- large text;
- split-screen/multi-window where relevant.

## 17. Accessibility

Accessibility is part of design quality, not a final compliance sticker.

Check semantics, names/roles/states, keyboard navigation, focus visibility, target size, contrast, text scaling, reduced motion, screen-reader order, non-color cues, error explanation, form labeling, zoom, and platform accessibility APIs.

## 18. Localization and internationalization

Design for text expansion, pluralization, variable date/number formats, RTL, mixed-script text, long names, different address formats, different decimal/group separators, and locale-specific line breaking.

Do not hardcode layout assumptions around English label length.

## 19. Input methods

Design according to actual input:
- mouse;
- keyboard;
- touch;
- pen;
- controller/gamepad;
- remote/TV;
- accessibility switches;
- screen readers;
- terminal keyboard-only environments.

Hover cannot be required for essential information on touch-first systems.

## 20. Performance-aware design

Performance affects perceived quality.

Avoid unnecessary blur, giant backdrop filters, huge unoptimized images, excessive shadows, layout thrash, expensive continuous animation, unnecessary WebGL, too many DOM nodes, or native view nesting when equivalent simpler structure exists.

Preserve a useful low-power/fallback experience for effect-heavy products.

## 21. Data visualization

Match palette and visual encoding to data semantics:
- categorical;
- sequential;
- diverging;
- temporal;
- geographic;
- hierarchical.

Do not use ten saturated colors when grouping, direct labels, small multiples, line styles, or interaction would communicate better.

## 22. Copy and microcopy

Prefer specific action language over generic filler. Distinguish labels, helper text, status, error, and explanatory copy. Do not add slogans to fill whitespace. Do not invent product claims, metrics, testimonials, or fake user activity.

## 23. Navigation

Navigation should answer:
- Where am I?
- What can I do here?
- How do I go back/up?
- What is persistent vs contextual?
- What happens to history/deep links?

Experimental navigation must still preserve orientation and recovery.

## 24. Design systems

Trace real ownership before editing shared tokens/components. Fix the smallest governing layer. Avoid component-local raw values that should be semantic tokens. Do not globalize a local decorative color by accident.

## 25. SVG and vector assets

Use SVG/vector assets for interface icons. Normalize viewBox, fill/stroke behavior, optical size, theme adaptation, and accessibility semantics. Prefer currentColor for reusable monochrome controls. Do not embed arbitrary hardcoded semantic colors inside reusable icons unless the icon itself is intentionally multicolor.

## 26. Programming language / toolkit rule

Design principles do not belong to one language. Implementation does.

First classify the UI architecture:

```text
WEB / DOCUMENT FLOW
RETAINED-MODE NATIVE
DECLARATIVE NATIVE
IMMEDIATE-MODE GUI
SCENE GRAPH / CANVAS
GAME ENGINE UI
TERMINAL / TUI
EMBEDDED / CONSTRAINED
REMOTE / STREAMED UI
```

Then map design tokens, layout, typography, states, icons, accessibility, motion, responsiveness/adaptivity, and QA to the toolkit's real primitives.

Read `handbook/stacks/language-toolkit-map.md` and the matching stack guide. If a language is unlisted, use the universal adapter in that file instead of guessing.

## 27. Source-of-truth rule

If the user supplied a screenshot, file, codebase, design document, or existing product, ground recommendations in it. Do not silently replace source facts with generic design advice.

## 28. Implementation safety

Do not:
- rewrite business logic for visual convenience;
- silently delete features;
- leave fake controls;
- invent data;
- refactor unrelated modules;
- break routing/state/API contracts;
- replace a functioning native convention with a fashionable but weaker custom one.

## 29. Runtime verification

After meaningful implementation:
1. build/run;
2. inspect the actual target state;
3. inspect at least one non-happy state where relevant;
4. inspect responsive/adaptive states;
5. verify keyboard/focus or platform input behavior;
6. run type/lint/tests/build checks;
7. compare before/after at equivalent state if possible.

## 30. Evidence vocabulary

Use:

```text
PASS
FAIL
NOT REVIEWED
BLOCKED
N/A
UNKNOWN
```

Unrun is not PASS. Static code cannot prove runtime interaction PASS.

## 31. Stop rule

Stop when acceptance criteria are met, must-preserve behavior remains correct, high-impact issues are resolved, verification passes or is honestly BLOCKED, and further work would mostly add churn.

## 32. Recommended reading in MAX mode

For substantial tasks, load the full relevant chain rather than only one short subskill:

### Web
- `references/web.md`
- `handbook/core/*` relevant to the task
- matching `handbook/stacks/*`
- matching `handbook/patterns/*`
- QA references

### Desktop/native
- `references/application.md`
- platform reference
- toolkit/language guide
- design-system / accessibility / QA where relevant

### Color
- `handbook/core/color-system.md`
- `references/visual-direction.md`
- exactly matching palette catalog, plus theme/accessibility QA

### Full audit
Read broad core guidance, the platform/toolkit guide, product-pattern guide, and QA suite. MAX is intentionally allowed to use large context when the task justifies it.
