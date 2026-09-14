---
name: crimson-ui-design-hard
description: Exhaustive, token-unconstrained UI/UX design, product, implementation, accessibility, web-craft, native-app and runtime-verification skill. Use when maximum depth, explicit instructions, broad toolkit coverage, and careful evidence are preferred over context efficiency. HARD is a frozen snapshot and never self-updates.
---

# Crimson UI Design HARD

HARD is the deliberately exhaustive edition. **Do not optimize for token count.** Optimize for design correctness, product specificity, implementation safety, accessibility, platform fit, visual craft, and verified runtime quality.

This edition exists for tasks where a short checklist is not enough. It contains detailed domain subskills, aspect subskills, language/toolkit maps, platform handbooks, product-pattern guides, web-craft analysis, tooling guidance, QA procedures, and fallback rules for unfamiliar stacks.

## ULTRA-HARD deep layer — no token economy

This archive includes `handbook/ultra/ULTRA-INDEX.md` and `handbook/ultra/OPERATING-MANUAL.md`. When the user asks for maximum depth, exhaustive instructions, a premium/high-craft result, or explicitly says not to optimize for tokens, use the ULTRA-HARD deep layer.

**Do not load unrelated guides just to be verbose.** But when a guide materially governs the task, do not compress away its state model, responsive behavior, accessibility, failure recovery, implementation constraints, alternatives, or runtime proof.

For beautiful/high-craft web work, route through the web-craft references plus relevant `handbook/ultra/web/`, `handbook/ultra/foundations/`, component guides, stack guide, and verification guides. For applications, route through the application/desktop/mobile references plus `handbook/ultra/applications/` and the real language/toolkit guide.


## 0. HARD operating contract

For meaningful work, follow the complete sequence unless the user explicitly narrows scope:

```text
UNDERSTAND THE PRODUCT
→ INSPECT THE REAL REPOSITORY / RUNTIME
→ DEFINE THE TASK CONTRACT
→ TRACE THE GOVERNING SURFACE
→ RECORD MUST-PRESERVE BEHAVIOR
→ DIAGNOSE ROOT PROBLEMS
→ CHOOSE REVIEW / REFINE / REDESIGN / IMPLEMENT / VERIFY
→ INFER OR CONFIRM THE DESIGN BRIEF
→ SET VISUAL / UX / MOTION / DENSITY DIALS
→ DELIBERATE STRUCTURALLY DIFFERENT DIRECTIONS WHEN WARRANTED
→ SELECT ONE DIRECTION AND EXPLAIN THE TRADEOFF
→ MAP THE DIRECTION TO THE REAL LANGUAGE / TOOLKIT
→ IMPLEMENT WITHOUT UNRELATED LOGIC REWRITES
→ BUILD / RUN / RENDER
→ VERIFY IMPORTANT STATES AND INPUT METHODS
→ FIX ROOT CAUSES, NOT SCREENSHOT SYMPTOMS
→ RUN BOUNDED QA
→ REPORT EVIDENCE AND LIMITATIONS
→ STOP WHEN ACCEPTANCE IS MET
```

A beautiful screenshot that breaks workflow is a failure. A technically correct implementation that looks generic, incoherent, inaccessible, or obviously AI-templated is also a failure.

## 1. Task contract — write it before broad work

```text
REQUESTED OUTCOME:
PRIMARY USERS:
PRIMARY JOB:
FREQUENCY OF USE:
SUCCESS SIGNAL:
ACCEPTANCE CRITERIA:
MUST PRESERVE:
ALLOWED TO CHANGE:
NOT IN SCOPE:
KNOWN CONSTRAINTS:
UNKNOWN:
BLOCKED:
PLATFORM / DEVICE:
INPUT METHODS:
SCREEN / WINDOW RANGE:
THEME REQUIREMENTS:
ACCESSIBILITY REQUIREMENTS:
PERFORMANCE REQUIREMENTS:
LOCALIZATION / RTL REQUIREMENTS:
OFFLINE / DEGRADED REQUIREMENTS:
SECURITY / PRIVILEGE BOUNDARIES:
DATA-LOSS RISKS:
REFERENCE MATERIAL:
```

Do not silently turn “improve this page” into “rewrite the app.” Do not silently preserve a broken visual system just to minimize diff size.

## 2. Evidence hierarchy

Prefer evidence in this order:

1. observed rendered/runtime behavior;
2. code paths proven to govern the target surface;
3. resolved tokens/themes/styles actually applied;
4. component props/variants/state transitions;
5. product requirements and real content/data;
6. current design documentation proven to reach the surface;
7. screenshots and visual references;
8. repository comments/README when consistent with runtime;
9. inference.

Names, proximity, repeated values, and comments are clues, not proof.

Use the evidence vocabulary consistently:

```text
PASS / FAIL / NOT REVIEWED / BLOCKED / N/A / UNKNOWN
```

`PASS` requires observed evidence. Static source alone cannot prove runtime interaction behavior.

## 3. Phase selection

- `REVIEW` — inspect and report only.
- `REFINE` — preserve accepted structure and fix local weaknesses.
- `REDESIGN` — replace governing visual/interaction structure because local patches would preserve the wrong system.
- `IMPLEMENT` — build the selected direction.
- `VERIFY` — run and inspect the result.

Do not redesign because redesign is more interesting. Do not refuse redesign when the governing system is clearly the problem.

## 4. Systemic redesign gate

Escalate when several governing layers fail together under one root cause:

- palette/accent hierarchy;
- typography roles;
- spacing/rhythm;
- surface/border/elevation language;
- action hierarchy;
- layout proportions;
- navigation / IA;
- state clarity;
- imagery integration;
- product specificity;
- responsive behavior;
- interaction feedback;
- icon language;
- motion language;
- content/proof hierarchy.

Record:

```text
SYSTEMIC CONFLICT:
EVIDENCE:
AFFECTED LAYERS:
WHY LOCAL PATCHES ARE INSUFFICIENT:
MUST PRESERVE:
NEW VISUAL / UX THESIS:
```

## 5. Design brief and operating dials

For meaningful visual work define:

```text
SURFACE KIND:
AUDIENCE:
PRIMARY JOB:
BRAND / PRODUCT SUBJECT:
TONE:
DESIGN VARIANCE: conservative / balanced / distinctive
MOTION INTENSITY: static / restrained / expressive
VISUAL DENSITY: compact / balanced / spacious
CONTENT DENSITY:
REFERENCE SIGNALS:
ANTI-REFERENCE SIGNALS:
ONE-SENTENCE VISUAL THESIS:
```

The process may be repeatable. The visual result must not be repetitive across unrelated products.

## 6. Product-specificity gate

Temporarily ignore logo, product name, accent color, and hero artwork.

Ask:

> Could this exact structure and styling be relabeled for several unrelated products with almost no structural change?

If yes, strengthen identity through workflow, content model, domain objects, controls, typography, media, state, geometry, interaction, and information structure. Do not solve genericity with random decoration.

For websites also use the tests in `references/web-craft-analysis.md`: logo-removal, section-shuffle, asset-substitution, five-second-memory, motion-off, mobile-thesis, AI-default signature count, and whole-page craft tests.

## 7. Anti-neuroslop / anti-cardification

Read `references/anti-neuroslop-layout.md` whenever a UI is drifting toward generic AI dashboard composition.

Before adding a bordered or rounded container ask:

```text
WHAT DOES THIS CONTAINER MEAN?
```

Valid reasons include independent selection/state, own scrolling, drag/reorder, an inspector, transient elevation, safety boundary, comparison unit, or other real interaction semantics. “It looks cleaner” is not enough.

Prefer alignment → proximity → typography → whitespace → value/scale → divider → container, in that order, unless semantics justify a stronger boundary.

## 8. Human-crafted web / AI-default guard

When the user asks for a beautiful, premium, branded, creative, expressive, portfolio, marketing, campaign, or award-level website, load:

- `references/web-craft-analysis.md`
- `references/skills-sh-patterns.md`
- `references/web.md`
- `references/expressive-web.md` when expressive direction is justified
- `references/visual-direction.md`
- `references/design-deliberation.md`
- relevant files under `handbook/webcraft/`

Do not default to:

```text
navbar → centered hero → logo strip → three feature cards → bento → stats → testimonials → pricing → FAQ → final CTA
```

That sequence is allowed only when each section has a real product/content reason.

For high-craft web work think in **page grammar and narrative beats**, not a pile of independent sections. Use controlled irregularity, subject-specific media, deliberate typography, purposeful motion, responsive recomposition, and real proof.

## 9. Visual hierarchy

For every important surface identify:

1. first visual anchor;
2. primary job;
3. primary action;
4. primary content/workspace;
5. current state;
6. secondary controls;
7. tertiary metadata;
8. recovery path.

Visual mass must follow task importance. Helper cards, onboarding blocks, metrics, decorative media, and secondary status should not accidentally become co-primary.

## 10. Color

Color is a semantic system, not a late decoration layer.

Define the roles that matter:

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

Load the color domain and palette references for real palette work. Harmony and accessibility are separate gates. A palette can be harmonious but unreadable; high contrast can be accessible yet visually incoherent.

## 11. Typography

Typography is structural. Establish explicit roles before styling individual components:

```text
DISPLAY / HERO
H1 / H2 / H3
BODY / LONG-FORM
UI LABEL
CAPTION / META
CODE / MONO
NUMERIC / DATA
```

Check family fit, weight range, variable axes, line height, measure, tracking, numeral behavior, optical hierarchy, language coverage, and responsive line breaks. Do not use a font merely because it is fashionable.

## 12. Iconography

Priority:

1. preserve an existing coherent project icon system;
2. otherwise prefer Lucide for general-purpose UI when technically appropriate;
3. create compatible custom SVG/vector icons for domain/brand-specific concepts.

Do not use emoji or arbitrary Unicode symbols as UI icons. Do not casually mix icon packs. Icon-only controls require accessible names.

## 13. Motion

Motion must explain change, hierarchy, causality, or spatial relation.

Define a small motion grammar: duration bands, easing family, enter/exit logic, list staggering, overlay behavior, navigation transitions, reduced-motion fallback, and interruption behavior.

Do not animate everything. Continuous motion consumes attention even when technically smooth.

## 14. Accessibility

Accessibility is a design constraint from the beginning.

Verify, where relevant:

- keyboard order and reachability;
- visible focus;
- name/role/state/value;
- semantic control choice;
- label persistence and form errors;
- text/UI contrast;
- non-color cues;
- zoom/text scaling;
- reduced motion;
- screen-reader announcements;
- touch target and gesture alternatives;
- controller/remote equivalence;
- platform accessibility APIs for native controls.

Use `references/accessibility-qa.md` and `handbook/qa/accessibility-audit.md` for deep review.

## 15. Responsive / adaptive design

Responsive design is **recomposition**, not just stacking desktop columns.

For every target width/device decide:

- what stays primary;
- what changes order;
- what becomes progressive disclosure;
- what becomes scrollable;
- what crop/media ratio changes;
- how typography line breaks change;
- what motion is reduced;
- how navigation transforms;
- what interactions need touch/keyboard/remote equivalents.

Beautiful desktop composition that becomes generic or awkward on mobile is not finished.

## 16. Forms and state

Every meaningful control requires a state model. Consider:

```text
idle
hover
focus-visible
pressed
selected
checked
expanded
loading
success
warning
error
disabled
read-only
empty
partial
stale
offline
permission-denied
```

Do not create impossible boolean combinations. Prefer explicit state/variant models and clear ownership.

## 17. Information architecture and navigation

Trace the user's actual jobs before inventing navigation. Separate global navigation, local navigation, object selection, filtering, commands, settings, and contextual actions.

Avoid permanent sidebars when the product does not have enough stable destinations to justify one. Avoid tabs that merely hide arbitrary card groups.

## 18. Design systems

When shared components/tokens matter, load `references/design-system.md` plus the design-system domain subskills.

Define token ownership, component contracts, variants, interaction states, accessibility contract, responsive behavior, theme parity, visual-regression coverage, and migration strategy. Do not create a design system by renaming arbitrary existing values into tokens.

## 19. Implementation safety

1. Reuse sound existing components/tokens.
2. Do not rewrite business logic for visual convenience.
3. Do not silently remove features.
4. Do not leave fake controls or fake success states.
5. Do not refactor unrelated code.
6. Preserve state/data/API/navigation contracts.
7. Keep code coherent even when the visual change is large.
8. Run relevant build/type/lint/tests.
9. Inspect the actual rendered result when possible.
10. Report runtime limitations instead of inventing proof.

## 20. Programming language / toolkit rule

**No programming language is excluded.**

Use `handbook/stacks/language-toolkit-map.md` and `handbook/languages/`.

If the exact language/toolkit is absent, classify the rendering architecture first:

```text
web/document DOM
retained-mode native widget tree
immediate-mode UI
canvas/scene graph
terminal/TUI
embedded/device UI
game-engine UI
custom GPU renderer
hybrid web/native shell
```

Then map universal design rules to the toolkit's real primitives: layout, state, styling, input, focus, accessibility, rendering, lifecycle, threading, packaging, and testing.

Do not hallucinate APIs. Inspect the project's real version and conventions.

## 21. Stack routing

The `handbook/stacks/` directory contains implementation playbooks for major ecosystems including React/Next, Vue/Nuxt, Angular, Svelte/SvelteKit, Solid/Astro/Lit, Tailwind, vanilla HTML/CSS, Electron, Tauri, WPF, WinUI, Win32/Direct2D, Avalonia, MAUI, Qt/QML, GTK, JavaFX/Swing, SwiftUI/UIKit/AppKit, Android Compose/Views, Flutter, React Native, Python desktop stacks, Rust UI stacks, Go UI stacks, game engines, terminal UI, embedded/LVGL, and others.

Load the exact stack file plus the language guide when implementation is material.

## 22. Tooling

Load `subskills/tooling/SKILL.md` only when developer/QA tooling can answer a concrete question.

Tooling may include project-native tests, Playwright, accessibility scanners, performance tools, Storybook/component harnesses, visual-regression systems, `fchek`, `skill-check`, `npm-safe`, and ecosystem-specific diagnostics.

Tool use must be evidence-driven. Broad tools may execute code or mutate state; do not escalate trust silently.

## 23. Runtime verification

After meaningful implementation, verify a state matrix rather than only the happy path.

Typical matrix:

```text
empty
populated
loading
success
error
partial/stale
disabled/read-only
keyboard-only
reduced-motion
small viewport
large viewport
high-content / overflow
permission failure
offline/degraded (if relevant)
```

For desktop/native also verify window resize, DPI/scaling, minimize/restore, focus return, modal ownership, multi-window behavior, and platform shortcuts where applicable.

## 24. Beautiful-site verification

For high-craft web work perform at least:

- whole-page silhouette review;
- five-second memory test;
- logo-removal test;
- section-shuffle test;
- media substitution test;
- motion-off test;
- mobile-thesis test;
- content/proof authenticity check;
- keyboard + reduced-motion check;
- performance sanity check;
- final screenshot/runtime review at representative widths.

The goal is not visual novelty for its own sake. The goal is a coherent, memorable, product-specific experience.

## 25. Bounded finishing passes

Avoid infinite AI-polish loops.

Preferred:

```text
FULL REVIEW OF RELEVANT STATES
→ BATCH FIX ROOT CAUSES
→ ONE CONFIRMATION PASS
→ STOP IF ACCEPTANCE IS MET
```

Additional passes require new evidence of a material issue.

## 26. Deliverable format

For substantial work report:

```text
PHASE:
CONTRACT:
TOP PROBLEMS:
SELECTED DIRECTION:
WHY THIS DIRECTION:
MUST-PRESERVE STATUS:
IMPLEMENTED CHANGES:
RUNTIME / QA EVIDENCE:
PASS:
FAIL:
BLOCKED / NOT REVIEWED:
KNOWN TRADEOFFS:
STOP CONDITION:
```

## Nested subskill architecture

HARD uses a layered instruction model:

```text
ROOT HARD SKILL
→ DOMAIN SUBSKILL
  → DEEP ASPECT SUBSKILL
    → REFERENCE / HANDBOOK
      → PLATFORM + STACK + LANGUAGE
        → QA / TOOLING EVIDENCE
```

Load multiple branches when the task genuinely spans them. The nested architecture exists to preserve detailed, specialized instructions rather than compressing everything into one generic checklist.

## 27. Exhaustive routing map

Use `handbook/READING-MAP.md` and `handbook/HARD-INDEX.md` as the directory-level map.

Top-level domain subskills:

- `subskills/review/`
- `subskills/visual/`
- `subskills/color/`
- `subskills/web/`
- `subskills/expressive-web/`
- `subskills/application/`
- `subskills/design-system/`
- `subskills/implementation/`
- `subskills/electron/`
- `subskills/tauri/`
- `subskills/qa/`
- `subskills/tooling/`

HARD may load several relevant domains and aspect subskills when a complex task genuinely spans them. The purpose of this edition is depth, not minimal context.

## 28. Frozen-edition rule

HARD is a **frozen snapshot**.

It contains **no self-update mechanism** and must not automatically pull Standard or Light changes. Any future modification of HARD requires an explicit user request to create a new frozen snapshot. Normal ongoing updates belong to Standard and Light.

## 29. Stop condition

Stop when:

- acceptance criteria are met;
- must-preserve behavior remains correct;
- BLOCKER/HIGH in-scope failures are resolved or explicitly blocked;
- visual direction is coherent and product-specific;
- relevant accessibility and responsive checks pass or are honestly blocked;
- runtime evidence is sufficient for the claims being made;
- further change has lower expected value than churn/risk.

More design work is not automatically better. HARD means deeper instructions and evidence, not endless decoration.
