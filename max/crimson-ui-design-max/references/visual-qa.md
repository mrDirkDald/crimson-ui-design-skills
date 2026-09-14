# Visual & Interaction QA Core

## Contents
- Evidence protocol
- Severity
- Runtime packet
- Deterministic-first checks
- Workflow/hierarchy
- Controls/states
- Real content
- Overflow/layers
- Input/responsive smoke checks
- QA report/stop

## Evidence protocol

A PASS requires observed evidence appropriate to the claim.
For meaningful visual changes prefer before/after at the same state and viewport/window size when practical.
For interaction use `before state → action → after state`.
Static code cannot prove interaction PASS.

## Severity

Every FAIL receives:
- `BLOCKER` — primary task impossible, unsafe destructive/data-loss flow, critical inaccessible state, trapped modal, required viewport unusable.
- `HIGH` — major workflow/accessibility/navigation/state/responsive defect.
- `MEDIUM` — meaningful friction/inconsistency while task remains usable.
- `LOW` — minor polish/detail issue.

BLOCKER must be fixed or explicitly accepted.
In-scope HIGH normally blocks completion.
MEDIUM blocks only when acceptance criteria/accumulation makes it material.
LOW does not block by default.

## Runtime packet

Record relevant:

```text
RUNTIME: AVAILABLE / BLOCKED
PLATFORM:
VIEWPORT/WINDOW:
STATE/DATA:
INPUT METHOD:
THEME:
LIMITATIONS:
```

Unavailable runtime checks are BLOCKED, not PASS.

## Deterministic-first

Before subjective polish, check falsifiable failures:
- runtime/console errors;
- missing assets;
- clipping/overflow;
- hidden controls;
- broken focus/disabled behavior;
- route/state failures;
- build/type/test failures connected to the change.

Then judge composition/aesthetics.

## Workflow

Check:
- primary task obvious;
- first action discoverable;
- next state guides next action;
- recovery discoverable;
- secondary controls remain secondary.

## Hierarchy tests

### Squint
Primary action/content/state remain obvious at reduced detail.

### Silhouette
Major region proportions make sense without reading labels.

### Grayscale
Hierarchy survives without accent.

### Border removal
Grouping should not collapse if non-essential boxes disappear.

### Density
Look for giant accidental gaps, cramped clusters, oversized title, tiny metadata, underused work area.
Intentional whitespace is valid.

## Text/reduction/over-cleanup

Look for floating short phrases, redundant labels, permanent helper copy, duplicate status and filler cards.
Then run the inverse check: did cleanup remove useful state, navigation, accessibility, recovery, or identity?

## Controls/actions

For each control ask:
- what does it affect?
- is placement/context obvious?
- does appearance match behavior?
- active vs disabled clear?
- primary/secondary/destructive hierarchy correct?

## State matrix

Review relevant empty, populated, loading, queued, running, paused, selected, disabled, success, failure, retry, offline/degraded, permission denied, session expired/forbidden.
Check state clarity and avoidable layout jumps.

## Real content / many items

Test relevant 0, 1–2, 10–20+ items, long labels/paths, missing metadata, mixed states and localization expansion.
Do not validate only fixture-perfect content.

## Overflow / clipping

Inspect text/icon clipping, control overlap, horizontal overflow, unexpected scroll, content hidden by fixed/sticky UI and truncation without recovery.

## Layers / z-order

Check dialogs, menus, dropdowns, popovers, tooltips, sticky regions, toasts and overlays.
Nothing critical should render behind obstructive layers.

## Input smoke checks

When relevant, confirm essential actions are reachable through supported input methods.
Do not infer hover capability on touch-only surfaces.
Detailed keyboard/screen-reader/native accessibility belongs in `references/accessibility-qa.md`.

## Responsive smoke check

FAIL when a required layout merely stacks desktop without reprioritization, primary action becomes unreachable, table/list becomes unusable, navigation loses state, or density becomes arbitrary.

Cross-browser/platform matrices and screenshot diff belong in `references/visual-regression.md`.

## Anti-neuroslop / anti-polish

Fail only when generic effects, fake hierarchy, detached controls, active-looking-disabled, drift, fixture-only layout, over-cleanup, whitespace panic or showroom polish create a real product problem.
Do not fail expressive UI merely for being expressive when it fits the product.

## Color harmony gate

Evaluate color as a system, not as isolated swatches.

Check:
- dominant base and accent family are intentional;
- supporting hues relate to the visual direction;
- no accidental hue competition;
- strong saturation is proportional to importance;
- semantic state colors do not overpower normal workflow;
- hierarchy survives in grayscale;
- active/selected state does not disappear when hue is removed;
- supported themes preserve identity and semantic meaning;
- critical distinctions remain color-blind safe.

Harmony and accessibility are separate requirements. A palette does not PASS merely because contrast ratios pass, and it does not PASS merely because it looks harmonious.

Typical FAIL examples:
- several equally saturated accents fight for attention;
- unrelated warm/cool accents have no semantic reason;
- dark theme accent becomes neon while the rest of the palette is restrained;
- status colors are visually stronger than the primary action everywhere;
- active state disappears in grayscale;
- light/dark themes use unrelated accent families;
- chart series are attractive but visually indistinguishable.

Severity:
- HIGH when color causes state/action ambiguity or accessibility failure;
- MEDIUM when harmony materially damages hierarchy/scanability;
- LOW for minor non-semantic palette drift.

## Systemic visual harmony gate

Check whether multiple local issues share one governing cause.

Signals:
- several competing accent families;
- repeated CTA duplication;
- inconsistent typography roles;
- unrelated spacing/radius systems;
- support surfaces competing with the primary task;
- generic composition weakly tied to product workflow;
- imagery treated as wallpaper rather than composed content;
- component-local patches overriding semantic tokens repeatedly.

If 3 or more related failures trace to the same governing system, classify the issue as **systemic**.

For systemic failures, do not recommend dozens of isolated tweaks by default.

Report:

```text
SYSTEMIC: YES / NO
ROOT CAUSE:
AFFECTED LAYERS:
LOCAL FIX SUFFICIENT: YES / NO
RECOMMENDED PHASE: REFINE / REDESIGN
```

If `LOCAL FIX SUFFICIENT = NO`, REDESIGN may replace the full visual layer while preserving product behavior.

### Duplicate Action QA

FAIL when duplicate controls for the same action:
- appear in the same viewport;
- have similar visual weight;
- do not serve distinct contexts;
- create uncertainty about where to act.

### Product-Specificity QA

Without relying on logo/name/background image, judge whether workflow/composition still reflects the product domain.

MEDIUM/HIGH when a supposedly distinctive product could be relabeled into an unrelated product with almost no structural change.

Do not require novelty from conventional system/admin tools where familiarity is intentionally valuable.

### Support-Surface Competition QA

FAIL when helper/onboarding/secondary surfaces compete with the primary task through comparable:
- area;
- contrast;
- elevation;
- accent;
- typography;
- internal complexity.

### Background Integration QA

When large imagery/backgrounds exist, verify:
- focal point remains useful;
- crop works at required sizes;
- overlay is local/directional when appropriate;
- image remains visually meaningful;
- foreground remains legible;
- image does not compete with controls.

A uniformly darkened image that becomes meaningless texture is a design failure when the image was intended to carry identity.

## Expressive / spectacle QA gate

Run when `references/expressive-web.md` is active.

Ask:
- can the experience thesis be stated in one sentence?
- do effects support that thesis or stack independently?
- is the primary content/task still understandable without motion/WebGL?
- does scroll advance meaning rather than merely animate entry?
- does mobile preserve the thesis through recomposition?
- do experimental navigation and page transitions preserve orientation/history?
- does a reduced-motion / fallback path preserve access?
- is the performance cost justified by communication/brand value?
- are common award patterns adapted to the subject rather than copied literally?

HIGH when spectacle blocks content, navigation, task completion, accessibility or acceptable runtime performance.
MEDIUM when the site remains usable but identity is generic effect-stacking rather than product-grounded.

## Review order

1. BLOCKER workflow/data-loss
2. accessibility blockers
3. navigation/state
4. hierarchy/composition
5. overflow/layers/responsiveness
6. density/typography
7. surfaces/color
8. icons/motion/polish

## Report

```text
PASS:
- check — evidence

FAIL:
- [HIGH] issue
  evidence:
  impact:
  fix:

BLOCKED:
- check
  reason:

NOT REVIEWED:
- ...

N/A:
- ...
```

## Stop

Stop when no unresolved BLOCKER, no unresolved in-scope HIGH unless accepted, acceptance criteria are met, BLOCKED checks are disclosed, and additional testing has low expected information value.

## SVG iconography QA gate

### Lucide consistency check

When Lucide is the baseline icon family, verify:
- no emoji icon substitutes remain;
- unrelated icon packs are not mixed without justification;
- repeated actions use the same glyph;
- sizing matches UI density;
- stroke weight and optical alignment stay coherent;
- hover/focus/disabled state comes from the control/system rather than ad-hoc SVG colors.

FAIL when interface controls use emoji or arbitrary Unicode pictograms as visual icons instead of the established SVG/vector icon system.

Check buttons, navigation, menus, toolbars, tabs, status indicators, inputs, file actions, settings, empty states, alerts and row actions.

PASS requires:
- coherent SVG/vector source;
- consistent stroke/fill language;
- consistent optical size/baseline;
- semantic token color behavior;
- accessible names for icon-only controls;
- decorative icons hidden from assistive technology when appropriate;
- correct light/dark theme rendering.

Do not fail emoji that is genuine content.

Severity:
- MEDIUM for inconsistent emoji UI iconography;
- HIGH when icon misuse creates ambiguity, accessibility problems or platform-rendering inconsistency.

# MAX Edition QA Addendum

A full MAX audit should include at least one happy state, one degraded/non-happy state, a second viewport or window size, the alternate theme when supported, keyboard/focus inspection, and verification that the icon system contains no emoji-control fallbacks. Record uncertainty explicitly.
