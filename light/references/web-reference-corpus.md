# Web Reference Corpus — Light

Use this only for meaningful website redesign, explicit requests for a beautiful/premium/studio-quality site, or when external references are being used to choose a direction. It is a compact decision layer, not a gallery catalog.

## Purpose

Strong references help when they answer a specific design question. They become harmful when the page turns into a collage of popular motifs.

Light keeps the transferable rules from broader web-reference analysis while avoiding a large catalog of examples.

The goal is:

```text
REFERENCE -> MECHANISM -> PRODUCT MAPPING -> IMPLEMENTATION -> QA
```

not:

```text
REFERENCE -> COPY THE LOOK
```

## Reference roles

Use different source types for different questions.

### 1. Award / spectacle references

Useful for:
- art direction;
- motion language;
- spatial composition;
- expressive storytelling;
- unusual transitions;
- high-impact visual identity.

Bias:
- they over-represent promotional experiences;
- spectacle may outrank repeated-task usability;
- advanced motion/3D can hide weak information architecture.

Do not treat award frequency as proof that a pattern fits a product.

### 2. Curated web galleries

Useful for:
- page silhouette;
- section rhythm;
- typography;
- image treatment;
- landing-page sequencing;
- current visual conventions.

Bias:
- screenshot selection hides interaction quality and failure states;
- repeated motifs may indicate saturation rather than correctness.

### 3. Product-flow references

Useful for:
- onboarding;
- authentication;
- settings;
- checkout;
- filtering;
- search;
- empty/error/loading states;
- repeated workflows.

These are stronger evidence than gallery screenshots for operational UX.

### 4. Case studies

Useful for tracing:
- brand idea -> grid;
- product story -> page grammar;
- content model -> layout;
- identity concept -> type/color/motion system.

Prefer the reasoning chain over the final styling.

### 5. Typography references

Useful for:
- display/body role contrast;
- line length;
- scale;
- editorial rhythm;
- font pairing;
- type-led identity.

Typography should solve hierarchy before extra containers and decoration are added.

### 6. Implementation references

Useful for checking whether an idea can be built with acceptable:
- performance;
- accessibility;
- responsive behavior;
- browser compatibility;
- maintenance cost.

A visually impressive reference is not implementation proof.

## Four-role triangulation

For a substantial web redesign, try to cover the needed roles rather than collecting many similar examples:

```text
ART DIRECTION  -> what should the page feel like?
PRODUCT FLOW   -> how should the task/state behave?
TYPOGRAPHY     -> how should hierarchy and voice work?
IMPLEMENTATION -> can the mechanism survive production?
```

Not every task needs all four. Use the smallest set that resolves real uncertainty.

## Reference card

For each useful reference record mentally or explicitly:

```text
ROLE:
WHAT IS STRONG:
TRANSFERABLE MECHANISM:
REFERENCE-SPECIFIC STYLING:
PRODUCT MAPPING:
COST / RISK:
```

If the transferable mechanism cannot be stated separately from the styling, do not copy it.

## Human-crafted signals worth preserving

### Small grammar, not one repeated component

Strong pages usually have a limited visual grammar but vary composition within it.

Consistency can come from:
- grid logic;
- typography roles;
- recurring image treatment;
- spacing cadence;
- motion physics;
- accent behavior.

Consistency does not require every section to use the same card, width, alignment or height.

### Macro rhythm over local polish

A page should work as a sequence, not merely as individually polished blocks.

Vary deliberately when useful:
- density;
- scale;
- media dominance;
- alignment;
- whitespace;
- interaction intensity.

Avoid the common AI rhythm:

```text
hero -> cards -> cards -> screenshot -> cards -> CTA
```

unless the content genuinely demands it.

### Typography is structural

Before adding boxes, borders or decorative surfaces, test whether hierarchy can be solved through:
- size;
- weight;
- width;
- measure;
- alignment;
- spacing;
- role contrast.

### Product flows reveal what screenshots hide

Beautiful screenshots rarely prove:
- loading;
- failure;
- validation;
- return visits;
- back navigation;
- destructive actions;
- long content;
- permission states.

Use flow references when these states matter.

### One-page quality comes from compression

Do not add a section just because a landing-page template usually has one.

Each major section should primarily do one job:

```text
ORIENT / PROVE / EXPLAIN / DEEPEN / CONVERT
```

Combine or remove sections that repeat the same job without adding useful evidence.

### Technology should support the idea

WebGL, GSAP, video, scroll choreography, custom cursors and page transitions are strongest when they express the subject or demonstrate product capability.

Do not add advanced technology merely to imitate an award site.

### Trend frequency is a saturation signal

If the same motif appears everywhere, require stronger product justification for using it.

Common examples include:
- generic bento grids;
- giant gradient blobs;
- endless marquees;
- floating 3D objects;
- identical SaaS hero compositions;
- pill-heavy navigation;
- stacked rounded cards.

A trend may still be correct. It just cannot be the reason by itself.

## Reference-to-decision workflow

1. State the unresolved design question.
2. Choose the reference role that can answer it.
3. Inspect a small number of materially useful examples.
4. Extract the mechanism, not the appearance.
5. Map it to product content, workflow or identity.
6. Compare against at least one credible alternative for meaningful REDESIGN.
7. Implement the smallest coherent grammar.
8. Verify the whole page and relevant runtime states.

Do not browse references indefinitely after the decision is already supported.

## Reference diversity gate

A reference set is weak when every example comes from the same visual niche.

For a major redesign, avoid using only:
- award winners;
- only SaaS landing pages;
- only dark sites;
- only one studio;
- only one framework showcase.

Diversity is useful because it separates durable principles from scene-specific fashion.

## Reference collage failure

FAIL when the direction can be described as:
- hero from site A;
- cards from site B;
- marquee from site C;
- cursor from site D;
- colors from site E.

Instead define one page grammar and adapt references into it.

## Product-specificity tests

### Logo-removal test

Temporarily imagine the brand name/logo removed. If the same page could sell an unrelated AI tool, VPN, crypto app, agency or productivity SaaS with only copy changes, identity is too generic.

### Section-shuffle test

If most sections can be reordered without damaging the story, the page may lack narrative structure.

### Asset-substitution test

If replacing the imagery with generic stock art changes almost nothing, the media system is not carrying enough identity or proof.

### Five-second memory test

After a short glance, identify what a user is likely to remember besides the logo. A strong page usually has at least one product-grounded visual or structural idea.

## Responsive reference rule

Do not copy desktop coordinates into mobile. Preserve the hierarchy and thesis.

Responsive art direction may require changing:
- crop;
- order;
- line breaks;
- overlap;
- navigation;
- motion intensity;
- amount of supporting media.

## QA gate

When this reference is active, verify:

```text
[ ] each reference answered a stated question
[ ] source bias was considered
[ ] transferable mechanism is separated from styling
[ ] page has one coherent grammar
[ ] section rhythm is not mechanically repetitive
[ ] typography contributes to structure
[ ] operational flows use flow evidence when needed
[ ] saturated motifs have product-specific justification
[ ] page survives logo-removal / section-shuffle / asset-substitution checks
[ ] responsive behavior preserves hierarchy rather than coordinates
[ ] implementation/performance/accessibility costs are acceptable
```

## Stop condition

Stop reference exploration when the design decision is supported, the strongest alternative is understood, and further examples are unlikely to change the direction.
