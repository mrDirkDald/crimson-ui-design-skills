# Visual Direction

## Contents
- Subject grounding
- Aesthetic intensity
- Design thesis
- Typography
- Color and surfaces
- Color harmony
- Spatial composition
- Motion
- Real content
- Generic-default self-critique
- Complexity budget
- Refinement rule

## Subject grounding

Before choosing a look, identify:
- concrete subject/product;
- audience;
- single primary job;
- context of use;
- emotional/brand tone.

Derive visual ideas from the subject's real world:
- tools;
- materials;
- media;
- workflows;
- vocabulary;
- artifacts;
- physical environment;
- cultural/technical context.

Do not begin from “SaaS”, “premium”, “modern”, or a trend name alone.

## Aesthetic intensity

Choose one:

### Quiet
For utilities, admin/system tools, repeated productivity workflows.
Prioritize directness, density, platform fit, restrained motion.

### Balanced
For most product UI.
Allow clear identity while keeping task hierarchy dominant.

### Expressive
For consumer, media, creative, entertainment, branded launches, or briefs that explicitly value delight/identity.
Allow richer typography, motion, imagery, and composition when justified.

Anti-polish must not force an expressive product into Quiet.

## Design thesis

For meaningful REDESIGN, write a compact plan before code:

```text
SUBJECT:
AUDIENCE:
PRIMARY JOB:
INTENSITY:
VISUAL THESIS:
TYPE:
COLOR:
LAYOUT:
MOTION:
ONE IDENTITY MOVE:
```

If structural comparison is useful, sketch one or more tiny ASCII wireframes.

Do not turn the plan into a design essay.

## Typography

Choose type based on product tone and reading/workload needs.

Define roles:
- display/title;
- section;
- item/content;
- control;
- metadata;
- technical/numeric.

Avoid habitual tells unless brief justifies them:
- tracked ALL-CAPS eyebrow labels above every heading;
- monospace for every tiny data label;
- accenting one random word in every headline;
- decorative middle-dot metadata strings everywhere;
- arrow glyph appended to every CTA.

Do not ban system fonts when platform familiarity/readability is the better choice.

## Color and surfaces

Define:
- base surface;
- raised/interactive surface;
- text primary/secondary;
- accent;
- semantic danger/success/warning.

Use dominant/secondary/accent relationships deliberately.

Effects such as gradients, texture, blur, glass, or shadows are tools, not identity by themselves.

A surface should not need border + shadow + glow + gradient + hover treatment simultaneously without a strong reason.

## Color harmony system

Color harmony is a design constraint, not decoration.

Before choosing individual values, define palette roles and relationships.

### Brief-grounded palette planning

Before coding a new visual direction, draft a compact palette plan with roughly `4–6 named hex values` for the actual token system, even when the harmony is based on only 2–3 chromatic hue families.

Derive choices from:
- subject matter;
- audience;
- materials and vernacular;
- workflow;
- brand character.

Then challenge the palette:

**Would I choose this same palette for several unrelated products?**

If yes, revise it unless the brief explicitly asks for that visual language.

Common generated-design defaults that require justification include:
- warm cream + terracotta/clay;
- near-black + acid green;
- near-black + vermilion;
- generic SaaS indigo/cyan;
- many equally polished pastel cards.

These combinations are not forbidden. They must be choices grounded in the brief rather than automatic defaults.

Spend chromatic boldness in one place and keep surrounding UI disciplined.

### Palette roles

Use semantic roles first:

```text
BACKGROUND / CANVAS:
SURFACE:
SURFACE-ELEVATED:
TEXT-PRIMARY:
TEXT-SECONDARY:
BORDER / DIVIDER:
ACCENT-PRIMARY:
ACCENT-SECONDARY (optional):
SUCCESS:
WARNING:
DANGER:
INFO:
FOCUS:
```

A color should have a reason to exist. Do not introduce a new hue merely because one component “needs more life”.

### Palette recipe references

When concrete palette candidates are needed, load only the matching catalog:

- exactly 2 principal chromatic colors → `references/color-pairs.md`
- exactly 3 principal chromatic colors → `references/color-trios.md`
- 4 or more principal chromatic colors → `references/color-palettes-4plus.md`

These catalogs are starting recipes, not mandatory brand palettes.

Always adapt them to the subject, semantic roles, theme, contrast requirements, and existing product identity.

Do not browse all three files by default.

### Hue relationship

When more than one chromatic hue is used, choose an intentional relationship such as:
- analogous;
- complementary;
- split-complementary;
- restrained triadic;
- monochromatic / near-monochromatic;
- neutral-dominant + one accent.

The model is a guide, not a rigid formula. Prefer fewer well-related hues over many weakly-related accents.

### Dominance and accent discipline

Establish a clear dominance relationship:

`dominant neutral/base → supporting surfaces → one primary accent → semantic state colors`

Reserve strong chroma for genuinely important action, selection, live state or brand signature. Secondary controls and metadata should normally recede.

If everything is accent, nothing is accent.

### Lightness structure

Harmony also depends on lightness.

Ensure:
- adjacent surfaces remain distinguishable;
- text hierarchy survives without relying on hue;
- active/selected state remains understandable in grayscale;
- dark themes do not collapse into near-identical blacks;
- light themes do not collapse into washed-out gray-on-white.

### Temperature balance

Use warm/cool relationships deliberately.

A contrasting temperature can be useful emphasis, but random warm/cool accents create palette noise. Semantic colors may legitimately break the dominant temperature when their meaning requires it.

### Brand color adaptation

Do not paste the raw brand color everywhere. Derive usable UI variants for:
- default accent;
- hover/pressed;
- subtle tint;
- low-emphasis tint;
- focus/selection;
- supported themes.

Preserve brand identity while adapting lightness/chroma for readability and hierarchy.

### Contrast and harmony are separate gates

A high-contrast pair can still be disharmonious. A harmonious pair can still fail accessibility.

A valid palette must satisfy both:
1. coherent visual relationship;
2. required readability/accessibility contrast.

Never reduce required contrast merely to make colors feel softer.

### Semantic state colors

Success, warning, danger and info must:
- remain semantically distinct;
- not constantly compete with the primary brand accent;
- work in all supported themes;
- remain understandable without color alone.

Do not use the brand accent as success/danger unless the semantic meaning remains unmistakable.

### Theme harmony

Light and dark themes should feel like the same product, not unrelated palettes. Preserve accent identity, semantic meaning, temperature and relative emphasis.

Do not mechanically invert colors. Rebalance lightness/chroma per theme.

### Color-blind safety

For critical distinctions:
- never rely only on red vs green;
- add label, icon, shape, pattern, position or value difference;
- avoid low-separation hue pairs in dense data.

Color harmony must not reduce semantic distinguishability.

### Color-count budget

Most product surfaces should prefer:
- neutral system;
- one primary accent;
- optional one supporting accent;
- semantic state colors.

More chromatic families require explicit product/visual-direction justification. Tonal variants of one hue are not separate families.

### Color harmony self-check

Before implementation ask:
1. What is the dominant hue/temperature?
2. What is the primary accent?
3. Which colors are semantic rather than decorative?
4. Are accents competing at equal strength?
5. Does hierarchy remain coherent in grayscale?
6. Do state colors remain distinct across themes?
7. Are critical distinctions color-blind safe?
8. Would removing one chromatic family improve clarity?

If the answers expose accidental variety, simplify the palette.

## Structural harmony gates

Visual harmony includes relationships between actions, content, support surfaces and imagery—not only color.

### Duplicate Action Gate

Detect the same destination/action appearing multiple times in one viewport.

Duplicates are acceptable when they serve genuinely different contexts, such as:
- persistent global action + local contextual action;
- desktop + mobile alternative presentation;
- repeated CTA after a long informational journey.

FAIL when two or more equally prominent controls perform the same action without a contextual reason.

Preferred correction:
- keep one primary entry point;
- demote secondary references to explanatory/link-level treatment;
- or merge duplicate action and explanation into one coherent control.

Do not create multiple equal CTAs merely to fill composition.

### Product-Specificity Gate

Test whether the visual system is meaningfully grounded in the actual product.

Temporarily ignore:
- logo;
- product name;
- hero/background image;
- branded copy.

Ask:

**Could this exact composition, component hierarchy and styling be reused almost unchanged for several unrelated products?**

If yes, strengthen product specificity through relevant:
- workflow structure;
- content organization;
- domain controls;
- typography character;
- imagery treatment;
- iconography;
- interaction behavior;
- data/state presentation.

Do not solve generic structure by adding decorative brand noise.

Product specificity should come from how the product works and communicates, not only from a logo/accent.

### Support-Surface Competition Gate

Supporting content must not accidentally become a second primary surface.

Examples:
- onboarding steps;
- tips;
- metadata panel;
- secondary card;
- helper sidebar;
- feature explanation.

Compare:
- occupied area;
- contrast;
- border/elevation;
- saturation;
- typography;
- number of internal separators/labels.

If a support surface receives visual mass similar to the primary task without equal workflow importance, reduce its emphasis or integrate it more tightly.

Do not make helper content look like a competing application.

### Background Image Integration Gate

A background image is part of composition, not wallpaper underneath a generic dark overlay.

Define:
- focal point;
- crop behavior;
- local contrast zones;
- foreground text/control placement;
- directional gradient/overlay;
- viewport adaptation;
- mobile crop;
- loading/fallback treatment.

Prefer local/directional contrast over uniformly crushing the entire image when the image contributes identity.

FAIL when:
- the important subject is hidden;
- the image becomes indistinct texture;
- foreground legibility depends on one global opaque veil;
- crop conflicts with content;
- the image competes with controls.

Do not add a background image solely to make an otherwise generic composition feel branded.

## Harmony repair strategy

When several harmony gates fail together:

1. identify the governing causes, not individual symptoms;
2. decide whether token/component/local fixes can restore coherence;
3. if not, define a new visual thesis;
4. replace the conflicting visual system coherently rather than patching element-by-element;
5. verify the whole surface after replacement.

A systemic visual redesign may change all styling/layout layers while preserving functionality.

Do not retain mismatched legacy colors, spacing, surfaces or typography merely because they already exist in code.

## Spatial composition

Choose intentionally:
- controlled density;
- generous negative space;
- asymmetry;
- symmetry;
- split view;
- layered composition;
- editorial rhythm;
- operational grid.

Do not use unexpected composition only to look “designed”.

Workflow importance must still control visual mass.

## Motion

Match motion to aesthetic intensity and task frequency.

Prefer a few high-value moments over animation on every element.

Motion should communicate:
- continuity;
- state;
- causality;
- progress;
- hierarchy;
- product character when appropriate.

Respect reduced motion.

## Real content

Use realistic product content early.

Avoid designing around:
- Lorem Ipsum;
- ideal one-word labels;
- exactly two list items;
- perfect metadata;
- short English-only strings.

The content itself should influence layout.

## Generic-default self-critique

Before implementation, challenge the design thesis:

1. Which choices came directly from this subject/brief?
2. Which choices would I make for five unrelated products?
3. Is the identity coming from structure/type/content or only from accent/effects?
4. Did I choose a fashionable pattern because it is easy?
5. Is the design intensity appropriate for repeated daily use?
6. Would removing logo/accent leave a coherent product, even if not visually unique?

Revise only the generic parts.

## Complexity budget

Match implementation complexity to the intended aesthetic.

Quiet/refined UI:
- fewer effects;
- stronger spacing/type precision;
- lower motion complexity.

Expressive UI:
- richer implementation can be justified;
- effects still need hierarchy and performance discipline.

Do not spend implementation complexity on decoration that the product does not need.

## Refinement rule

Once a direction is accepted, stop brainstorming aesthetics.

Refine:
- hierarchy;
- spacing;
- density;
- typography;
- state treatment;
- control placement;
- consistency.

Return to REDESIGN only with evidence of structural failure.


## Visual reference process

Use references to understand design decisions, not to copy surface decoration.

When references are allowed/available, build a compact reference board of 3–6 examples covering different aspects such as:
- composition;
- typography;
- density;
- interaction;
- motion;
- imagery;
- product tone.

For each reference record:
```text
REFERENCE:
WHAT IS USEFUL:
WHAT DOES NOT FIT:
TRANSFERABLE PRINCIPLE:
```

Do not merge unrelated references into a collage of fashionable traits.

### Multi-reference synthesis

When the task uses several visual references, extract transferable principles before implementation.

Use:

```text
REFERENCE:
PATTERN:
WHY IT WORKS:
WHERE IT FAILS:
PRODUCT FIT:
TRANSFERABLE PRINCIPLE:
```

Look for patterns repeated across different domains, then separate them from trend saturation.

Do not average several references into a generic collage. Choose one coherent thesis and adapt only compatible principles.

## Competitive visual analysis

When competitive analysis is useful:
- compare task flow and information hierarchy before colors;
- note what competitors overuse;
- identify product conventions users already understand;
- separate convention from brand-specific styling;
- look for unmet clarity/density/state needs.

Do not imitate a competitor merely because it looks polished.

## Imagery / illustration direction

When imagery matters, define:
- role: functional / editorial / atmospheric / instructional;
- subject matter;
- crop/aspect behavior;
- realism/stylization level;
- repetition rules;
- fallback/missing-image behavior.

Imagery should support the product thesis, not fill empty space.

## Icon direction

Define:
- stroke vs fill;
- optical size;
- corner/terminal character;
- detail level;
- brand vs utility icon distinction.

Use familiar platform/product symbols for common actions unless there is a real reason to customize.

## Accessibility constraints during direction

Do not postpone accessibility until QA.

During visual direction account for:
- contrast strategy;
- focus visibility;
- non-color-only status;
- text sizing/scaling;
- motion sensitivity;
- readable type/measure;
- accessible chart/imagery alternatives where relevant.

A visual direction that cannot meet core accessibility needs is not a valid direction.



## Measurable typography and rhythm checks

Use measurements as diagnostics, not as a style generator.

### Typography scale
For a coherent product surface:
- keep the number of simultaneously visible text roles small;
- repeated semantic roles should resolve to the same type treatment;
- body/metadata/control sizes should not drift by arbitrary 1 px differences without a reason;
- headings should create a clear rank order rather than a collection of unrelated sizes.

For long-form reading:
- verify comfortable line length and line-height in the actual font;
- avoid extremely wide text measures merely because the viewport is wide.

Do not force a mathematical modular scale when the product/platform typography already works.

### Contrast during direction
For web surfaces targeting WCAG 2.2 AA, the final implementation must be capable of meeting:
- normal text contrast: at least 4.5:1;
- large-scale text contrast: at least 3:1;
- interactive/non-text UI contrast where WCAG requires it.

Do not choose an art direction whose core palette inherently prevents the required contrast.

### Visual rhythm
Define a small spacing rhythm and verify repeated relationships:
- control internal padding;
- label → control;
- item → metadata;
- section → section;
- pane → pane.

Screen-specific composition may intentionally break the base rhythm, but repeated semantic relationships should not drift accidentally.

Use overlays/measurements when available to distinguish intended asymmetry from spacing drift.


## Optical rhythm review

After numeric spacing/type checks, review optical rhythm in the actual render.
Measure repeated semantic relationships, then correct for optical effects such as icon shape, cap height, serif display type and asymmetric controls.

Consistency means repeated intent, not blindly identical pixel gaps.

## Type-role budget

For one surface, keep simultaneously active text roles intentionally limited.
A useful default is roughly 4–6 semantic roles before special technical/status cases, not a hard limit.
If two roles differ by only 1 px/near-identical weight with no semantic purpose, merge them.

## SVG icon direction

### Lucide baseline

When the product has no established coherent icon family, use **Lucide Icons as the default baseline**.

Prefer one Lucide family across a surface, standard Lucide geometry, consistent sizing, `currentColor`, and SVG/vector rendering.

Do not mix unrelated icon packs casually, distort individual stroke widths, force Lucide into a brand mark, or replace a stronger existing product-specific icon system simply because Lucide is available.

For domain-specific or branded concepts, create a compatible custom SVG rather than forcing an inaccurate generic glyph.

UI iconography is SVG/vector-first.

Define one coherent icon language:
- source/family;
- stroke vs fill;
- stroke width;
- corner/terminal character;
- optical size;
- default/small/large size;
- active/disabled treatment.

Rules:
- prefer one icon family on the same product surface;
- reuse existing project icons first;
- use `viewBox`-based scaling;
- normalize mixed third-party SVGs before combining them;
- keep stroke weight and optical size consistent;
- do not decorate every label/action with an icon;
- do not use emoji or random Unicode pictograms as UI icons;
- if no suitable icon exists, create a simple SVG in the established language.

Icon-only controls need an accessible name and a sufficiently large interactive target.

Emoji may remain only as actual content, never as the control icon system.

# MAX Edition Addendum

In MAX mode, do not stop at a palette or typography recommendation. Connect visual direction to the product's entity model, repeated workflow, environment, and implementation constraints. For every large visual decision state what user behavior it supports, what it replaces, and how it behaves under responsive, accessibility, and theme conditions.

When choosing references, synthesize principles rather than copying surfaces. Extract the governing idea, failure boundary, product fit, and adaptation path.
