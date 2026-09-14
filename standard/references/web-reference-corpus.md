# Web Reference Corpus — Cross-Source Synthesis

## Contents

- Purpose
- Corpus reviewed
- Source-family bias map
- Cross-source findings
- Reference triangulation protocol
- Reference-to-decision mapping
- Gallery pattern vs product pattern
- Human-craft signals strengthened by the corpus
- Anti-AI reference failure modes
- Web corpus design gates
- Short operating procedure
- Research source notes

## Purpose

Use this reference when a web task would benefit from external design research rather than a single inspiration image.

This file synthesizes patterns from multiple kinds of public web-design reference sources so the agent can use references without copying a gallery trend or treating an award site as universal product UX guidance.

It complements:
- `references/web-craft-analysis.md` for human-crafted vs AI-default web quality;
- `references/expressive-web.md` for high-expression browser experiences;
- `references/web.md` for production web/product rules;
- `references/design-deliberation.md` for candidate selection;
- `references/visual-qa.md` for verification.

The goal is **reference triangulation**: learn different things from different source families, then adapt the useful mechanism to the current product.

---

# 1. Corpus reviewed

The synthesis uses fourteen source families:

1. Awwwards — award/experimental websites and interaction-heavy work.
2. CSS Design Awards — judged UI, UX and innovation work.
3. FWA — interactive, campaign, storytelling and technology-forward work.
4. Godly — highly selective creative/interactive web curation.
5. SiteInspire — broad design curation with strong typographic, minimal, grid and art-direction categories.
6. Land-book — broad landing/site curation with industry/style/type/typography filtering.
7. Lapa Ninja — large landing-page corpus with full-page examples, categories and historical variants.
8. One Page Love — single-page and landing-page sequencing with feature/design notes.
9. Mobbin — shipped app/site screens, UI elements and complete product flows.
10. Page Flows — recorded product flows and screen sequences for real web products.
11. Behance — case studies that expose concept, process, rationale, brand and presentation choices.
12. Typewolf — typography-in-the-wild, font pairings and real website examples.
13. Fonts In Use — broad real-world typography corpus across web and other media.
14. Made in Webflow / Webflow Showcase — implemented community sites, interaction patterns and cloneable/buildable examples.

Do not treat this list as a ranking.

Each source has a different bias and should answer a different design question.

---

# 2. Source-family bias map

## Award / spectacle sources

Sources:
- Awwwards
- CSS Design Awards
- FWA
- parts of Godly

Best for:
- art direction;
- memorable interaction;
- motion choreography;
- WebGL/3D as narrative or product proof;
- non-standard navigation;
- page transitions;
- portfolio/campaign storytelling;
- strong visual thesis.

Bias:
- novelty and spectacle are over-represented;
- production constraints can be secondary;
- complex motion may be inappropriate for ordinary SaaS/product work;
- awards can reward a memorable experience that would be too slow or distracting in a daily-use tool.

Use these sources to answer:

```text
HOW CAN THIS EXPERIENCE BECOME MEMORABLE?
WHAT VISUAL OR INTERACTION THESIS COULD BE UNIQUE TO THIS SUBJECT?
```

Do not use them alone to answer:

```text
WHAT IS THE SAFEST DEFAULT UX FOR A REPEATED TASK?
```

## Curated web galleries

Sources:
- Godly
- SiteInspire
- Land-book
- Lapa Ninja
- One Page Love

Best for:
- page silhouette;
- section rhythm;
- layout variation;
- landing-page sequence;
- editorial composition;
- category-specific references;
- current visual language;
- seeing how common patterns are adapted across industries.

Bias:
- visually attractive sites are over-represented;
- screenshots can hide interaction, performance and accessibility problems;
- trend repetition can make a pattern look more justified than it is.

Use these sources to answer:

```text
HOW DO STRONG CURRENT SITES ORGANIZE VISUAL MASS AND RHYTHM?
WHAT LAYOUT OPTIONS EXIST BEYOND THE DEFAULT TEMPLATE?
```

## Product-flow sources

Sources:
- Mobbin
- Page Flows

Best for:
- onboarding;
- authentication;
- checkout;
- subscriptions/paywalls;
- settings;
- account/workspace switching;
- progressive disclosure;
- state transitions;
- error/success ownership;
- step order;
- real copy patterns;
- interaction continuity across screens.

Bias:
- shipped does not automatically mean optimal;
- large products may contain legacy compromises;
- a flow from a different business model can be misleading.

Use these sources to answer:

```text
HOW DO REAL PRODUCTS HANDLE THIS TASK END TO END?
WHAT STATES AND TRANSITIONS AM I FORGETTING?
```

## Case-study sources

Source:
- Behance

Best for:
- rationale;
- brand-to-interface translation;
- concept development;
- visual system presentation;
- showing how typography, imagery and layout derive from a theme.

Bias:
- presentation can be more polished than implementation;
- case-study screens may be concepts rather than production surfaces;
- long mockups can hide responsive or state complexity.

Use Behance to understand **design reasoning**, then verify feasibility elsewhere.

## Typography sources

Sources:
- Typewolf
- Fonts In Use

Best for:
- real font pairings;
- body/display role separation;
- mood through type rather than decoration;
- hierarchy through scale, width, weight and spacing;
- seeing a typeface in real context instead of specimen text.

Bias:
- typography can dominate the analysis and make the agent ignore product task fit;
- licensing and performance still need separate checks.

Use these sources to answer:

```text
WHAT TYPOGRAPHIC VOICE SUPPORTS THIS SUBJECT?
HOW CAN TYPE CREATE HIERARCHY BEFORE I ADD MORE CONTAINERS?
```

## Implementation/community sources

Source:
- Made in Webflow / Webflow Showcase

Best for:
- proving an interaction can be built;
- implementation patterns;
- scroll/sticky/composition mechanics;
- CMS and portfolio structures;
- seeing how visual ideas survive in real browser implementations.

Bias:
- cloneable patterns can encourage imitation;
- community popularity does not equal product fit;
- trend demos may exist only to demonstrate a technique.

Use implementation references to validate a mechanism, not to inherit an entire site identity.

---

# 3. Cross-source findings

## 3.1 Strong work has a small grammar, not one repeated component

Across curated and award sources, strong sites often change scale, density, alignment and media dominance from scene to scene.

What remains consistent is not necessarily the same card or section layout.

Consistency usually comes from a small grammar:
- type roles;
- edge treatment;
- spacing logic;
- image treatment;
- motion physics;
- color roles;
- recurring alignment or line device;
- one or two signature motifs.

Therefore:

```text
CONSISTENCY != SAME SECTION REPEATED
CONSISTENCY = SAME DESIGN LANGUAGE ACROSS DIFFERENT COMPOSITIONS
```

This is a direct defense against AI pages where every section has the same max-width, radius, spacing and reveal animation.

## 3.2 Macro rhythm matters more than local polish

Curated one-page sources repeatedly expose a page-level property that component generation misses: **rhythm**.

A strong page can move through:
- dense → quiet;
- text-led → image-led;
- narrow → full-bleed;
- explanatory → experiential;
- static → interactive;
- high contrast → low contrast.

The transitions should feel intentional.

Do not equalize every section after implementation.

## 3.3 Typography is structural

Typewolf and Fonts In Use reinforce a useful rule: a font choice is not merely a brand token.

Typography can own:
- hierarchy;
- pacing;
- editorial tension;
- personality;
- navigation emphasis;
- technical vs expressive voice;
- density.

Before adding a card, border or decorative object, ask whether type scale, measure, alignment or font-role contrast can solve the hierarchy.

Do not default every premium site to the same geometric sans + mono combination.

## 3.4 Product flows expose missing states that galleries hide

Mobbin and Page Flows make a different weakness visible: screenshot-first inspiration hides transitions.

A production web surface must account for:
- entry state;
- loading;
- empty;
- populated;
- validation;
- error;
- success;
- retry/recovery;
- permission/role differences;
- cancellation/backtracking;
- destructive confirmation;
- return visits.

For product work, a beautiful happy-path screenshot is incomplete evidence.

## 3.5 One-page quality comes from compression, not section count

One Page Love and landing-page galleries show that effective single-page work often compresses information into a few strong beats.

Do not assume a landing page becomes more convincing as sections are added.

Each major section should do at least one job:

```text
ORIENT
PROVE
EXPLAIN
DEEPEN
CONVERT
```

If a section does none of these, remove or merge it.

If three adjacent sections all merely explain, redesign the sequence.

## 3.6 Award work uses technology as part of the idea when it succeeds

Recent award/FWA examples frequently use WebGL, GSAP, 3D, sound, point clouds or non-standard scroll.

The transferable lesson is **not** “use WebGL”.

The lesson is:

```text
TECHNIQUE SHOULD EXPRESS THE SUBJECT OR ENABLE THE EXPERIENCE THESIS.
```

A real-time 3D scene can be appropriate when the product is spatial, automotive, musical, architectural or itself interactive.

The same technique is often noise on a pricing page or settings workflow.

## 3.7 Real-world references beat imagined best practice for detailed flows

Mobbin exposes hundreds of thousands of shipped screens/flows and Page Flows records complete task sequences.

When a task is common but state-heavy, inspect real patterns before inventing a novel flow.

Innovation should happen where it creates value, not where conventional behavior already reduces cognitive load.

## 3.8 Case studies are useful for concept lineage

Behance is especially useful when the problem is:
- “how does the brand idea become a web system?”
- “why does this art direction make sense?”
- “how do grid, type and imagery connect?”

Do not mistake presentation polish for runtime proof.

## 3.9 Implementation references are a feasibility check

Webflow Showcase contains both complete sites and small interaction demonstrations.

Use it to separate:
- a visually interesting concept;
- a browser-feasible mechanism;
- a maintainable production pattern.

An effect being cloneable does not make it necessary.

## 3.10 Trend frequency is evidence of saturation, not correctness

When the same motif appears repeatedly across multiple galleries — for example:
- giant centered headline;
- pill buttons;
- huge corner radius;
- floating browser mockup;
- bento grids;
- kinetic marquee;
- cursor follower;
- gradient blobs;
- mono metadata;
- scroll-scrubbed image sequence;

— treat frequency as a **saturation signal**.

The more common a motif becomes, the stronger the product-specific justification should be before using it.

---

# 4. Reference triangulation protocol

For a meaningful website redesign, avoid selecting all references from one gallery.

Prefer a reference set containing different evidence roles.

## Four-role reference set

```text
A. ART DIRECTION REFERENCE
B. FLOW / USABILITY REFERENCE
C. TYPOGRAPHY REFERENCE
D. IMPLEMENTATION REFERENCE
```

Not every task needs all four.

For a brand landing page:
- A is usually required;
- C is valuable;
- D may verify motion/interaction;
- B is needed when forms, purchase, sign-up or account flows matter.

For a SaaS application:
- B is usually required;
- C can support visual identity;
- A should be restrained;
- D can validate implementation patterns.

## Reference card

For each serious reference, record:

```text
REFERENCE:
SOURCE FAMILY:
WHY RELEVANT:
MECHANISM TO EXTRACT:
WHAT NOT TO COPY:
HOW IT MAPS TO THIS PRODUCT:
RISK / BIAS:
```

If `HOW IT MAPS TO THIS PRODUCT` is weak, discard the reference.

## Reference diversity gate

For a serious redesign:
- do not use one site as the entire visual answer;
- avoid taking more than two major mechanisms from one reference;
- avoid using only one source family;
- do not copy exact section order, asset treatment and motion language together from one site;
- prefer mechanism synthesis over screenshot imitation.

---

# 5. Reference-to-decision mapping

Do not collect references without a question.

Map the design uncertainty first.

Examples:

```text
UNCERTAINTY: page rhythm
SOURCE: SiteInspire / Land-book / Lapa / One Page Love

UNCERTAINTY: memorable interaction
SOURCE: Awwwards / CSSDA / FWA / Godly

UNCERTAINTY: onboarding or checkout
SOURCE: Mobbin / Page Flows

UNCERTAINTY: typographic voice
SOURCE: Typewolf / Fonts In Use

UNCERTAINTY: brand concept lineage
SOURCE: Behance

UNCERTAINTY: implementation mechanics
SOURCE: Webflow Showcase
```

This prevents “inspiration browsing” from becoming random trend accumulation.

---

# 6. Gallery pattern vs product pattern

Classify an observed pattern before adopting it.

## Gallery pattern

Optimized for:
- visual impact;
- screenshot appeal;
- novelty;
- shareability;
- award presentation.

Examples can include extreme type, full-screen media, unusual scroll, custom cursors and heavy transition systems.

## Product pattern

Optimized for:
- repeated task completion;
- predictability;
- state clarity;
- speed;
- accessibility;
- long-term use.

Examples include stable navigation, conventional form semantics, visible state, clear recovery and consistent action placement.

## Hybrid pattern

A strong marketing/product site may need both.

Use expressive language for:
- orientation;
- story;
- proof;
- brand moments.

Use conventional interaction for:
- sign-up;
- checkout;
- account management;
- forms;
- destructive actions;
- high-frequency product work.

Do not force one mode over the entire site.

---

# 7. Human-craft signals strengthened by the corpus

## 7.1 Content-driven scale

Let the importance and nature of content choose scale.

Do not make every feature equal because a component grid is convenient.

## 7.2 Intentional visual resets

A long page benefits from moments that reset attention:
- more whitespace;
- a full-bleed asset;
- a short text-only beat;
- a background/value shift;
- a different alignment;
- a restrained interactive moment.

The reset must still belong to the same visual grammar.

## 7.3 Specific proof beats generic claims

Prefer:
- live product behavior;
- real work;
- domain imagery;
- diagrams;
- quantified outcomes with context;
- actual customer evidence;

over repeated adjectives about quality, speed, trust or innovation.

## 7.4 Distinctive does not mean maximal

SiteInspire, Typewolf and typography-led examples show that memorable work can be quiet.

A distinctive page may rely on:
- excellent type;
- strong crops;
- precise spacing;
- unusual but simple alignment;
- one signature interaction.

Do not equate “beautiful” with 3D, shaders, gradients or constant motion.

## 7.5 Motion needs a family

If motion is used, define shared physics:
- duration range;
- easing family;
- directionality;
- reveal logic;
- scroll relationship;
- interruption behavior.

Random per-component animation reads as generated decoration.

## 7.6 Responsive art direction must preserve hierarchy, not coordinates

When desktop composition is asymmetric or media-heavy, mobile needs a new composition.

Preserve:
- thesis;
- hierarchy;
- focal content;
- proof order;
- interaction meaning.

Do not preserve desktop overlap merely because it was visually distinctive.

---

# 8. Anti-AI reference failure modes

## Reference collage failure

Symptoms:
- hero from one site;
- cards from another;
- marquee from another;
- footer from another;
- no governing visual grammar.

Fix:
- extract principles first;
- choose one product-derived thesis;
- rebuild every mechanism inside that thesis.

## Trend laundering

Symptoms:
- a common gallery trend is described as “brand-specific” after the fact.

Fix:
- explain the product/subject reason before choosing the motif.

## Award cargo cult

Symptoms:
- smooth-scroll library, 3D, cursor effects and page transitions are added because award sites use them.

Fix:
- require a subject/interaction reason for each high-cost effect.

## Screenshot blindness

Symptoms:
- layout looks good in one viewport but flow, states and responsive behavior are incomplete.

Fix:
- pair screenshot inspiration with flow evidence and runtime QA.

## Typeface cosplay

Symptoms:
- unusual font chosen solely to look editorial/premium;
- body readability and licensing ignored.

Fix:
- define typographic roles, measures, weights and fallback behavior before committing.

## Cloneable-demo bias

Symptoms:
- interaction exists because it was easy to copy from a demo.

Fix:
- ask whether removing it would reduce understanding, proof or identity.

---

# 9. Web corpus design gates

For a meaningful beautiful-site task, ask:

### Reference-role gate

Do the references answer distinct questions, or are they all visual mood boards?

### Source-bias gate

What does each source over-represent?

### Mechanism gate

What exact mechanism is being learned?

### Product-mapping gate

Why does that mechanism fit this product?

### Saturation gate

Is this motif being selected because it is common in galleries?

### Flow gate

If the page includes product actions, have states/transitions been considered beyond the happy screenshot?

### Type gate

Is typography doing structural work, or is layout depending on containers/borders for hierarchy?

### Runtime gate

Can the proposed interaction survive keyboard, touch, reduced motion, responsive layout and performance constraints?

---

# 10. Short operating procedure

For a serious web redesign:

```text
1. DEFINE the product truth and design uncertainty.
2. PICK references by evidence role, not just visual taste.
3. EXTRACT mechanisms, not whole compositions.
4. NOTE source bias and what must not be copied.
5. SYNTHESIZE one product-specific grammar.
6. BUILD page rhythm before component polish.
7. VERIFY flows/states for interactive product work.
8. VERIFY typography as a structural layer.
9. RUN responsive/runtime/accessibility checks.
10. REMOVE any reference-derived motif that lacks a product reason.
```

This procedure should add deliberation, not create mandatory research overhead for trivial UI fixes.

---

# 11. Research source notes

Public sources reviewed for this synthesis:

- https://www.awwwards.com/ — award/experimental web reference; current archive examples show frequent use of WebGL, GSAP, storytelling, typography and interaction.
- https://www.cssdesignawards.com/ — judged work with separate UI, UX and innovation scoring.
- https://thefwa.com/ — FWA of the Day feed with interactive storytelling, WebGL, 3D, sound and campaign experiences.
- https://godly.website/ — highly selective creative web curation; also exposes technology/typeface-oriented browsing.
- https://www.siteinspire.com/ — broad curation including typographic, art-direction, minimal, grid and unusual-layout categories.
- https://land-book.com/ — curated site/landing references with industry, style, type, typography and color filters.
- https://www.lapa.ninja/ — large landing-page archive with full-page screenshots, categories, historical versions and many industry/style tags.
- https://onepagelove.com/inspiration — curated one-page/landing references with feature breakdowns and design notes.
- https://mobbin.com/ — shipped product screens, UI elements and complete flows across web/mobile products.
- https://pageflows.com/ — recorded web/product flows with screen-by-screen sequences.
- https://www.behance.net/ — design case studies useful for rationale, brand-to-interface translation and presentation of systems.
- https://www.typewolf.com/site-of-the-day — real websites indexed by font usage/pairing.
- https://fontsinuse.com/ — large real-world typography corpus with thousands of web examples plus cross-media context.
- https://webflow.com/made-in-webflow — implemented community sites and interaction/mechanism examples.

These sources are references, not authorities. Current product requirements, user needs, accessibility, performance and platform behavior remain higher priority.
