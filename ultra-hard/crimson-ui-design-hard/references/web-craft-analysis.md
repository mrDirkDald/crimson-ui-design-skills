# Human-Crafted Web vs AI-Default Web

## Contents

- Purpose
- Evidence base
- Core conclusion
- Human-crafted strengths
- AI-default failure signatures
- Human art-direction workflow
- Page grammar
- Narrative rhythm
- Typography craft
- Media and asset direction
- Composition and controlled irregularity
- Motion and interaction craft
- Responsive recomposition
- Conversion without template collapse
- Copy and proof quality
- Performance, accessibility and resilience
- Human-vs-AI comparison matrix
- Beautiful-site acceptance gates
- Reference-study protocol
- Research source notes

## Purpose

Use this reference when the user asks for a **beautiful**, **distinctive**, **premium**, **award-level**, **portfolio**, **brand**, **campaign**, **creative**, or strongly art-directed website.

The goal is not to imitate a human designer's taste superficially.

The goal is to reproduce the **decision process** that makes strong human-designed websites feel intentional instead of generated from a universal section template.

This reference should strengthen `references/web.md` and `references/expressive-web.md`.

It does not replace usability, browser semantics, accessibility, performance, or conversion requirements.

---

# 1. Evidence base

This guidance synthesizes two different evidence groups.

## Human-crafted / studio-led examples

Recent award-recognized work and studio case studies show a repeated pattern: strong sites start from a specific brand/product idea and build a web language around it.

Examples used during this synthesis include:

- **Hyperbolic — Studio Freight** — Awwwards Site of the Day + Developer Award, May 2025;
- **The Best You by Klook — Unseen Studio** — Awwwards Site of the Day + Developer Award, June 2025;
- **Vooban — Locomotive** — Awwwards Site of the Day + Developer Award, July 2025;
- **Clément Grellier portfolio / ONTO / Lens work** — award-recognized custom front-end work with strong grids, transitions, typography and interaction;
- **Editorial New — Locomotive** — typography itself used as the experience subject;
- **Baillat Studio / Populous / Structured — Locomotive** — different products receive different visual languages rather than one studio template.

The important point is not that award galleries are universally correct.

The important point is that these case studies repeatedly describe **subject-specific art direction**, custom systems, typography, media, transitions, motion, grids, and interaction that are tied to what the client actually is.

## AI-first website evidence

Current AI website builders themselves describe generated output as a **first direction / editable draft**, not a finished design endpoint.

Framer's 2026 materials describe AI-generated structures, sections, copy and page directions as content that should be refined on the canvas until the site feels custom rather than template-made.

Wix's 2026 State of Websites report says that most Harmony users still manually edit brand-sensitive details; reported edit rates include text and imagery in particular.

Framer's template guidance also notes that low-effort generic templates are easier for AI to reproduce, while strong templates with clear art direction, structure and reusable systems become more valuable.

Academic work on LLM-generated web accessibility likewise shows that default generated code can miss complex accessibility requirements and benefits from feedback, visual context and additional verification.

## Interpretation

The useful conclusion is not:

```text
human = good
AI = bad
```

The useful conclusion is:

```text
AI is good at producing a plausible first structure quickly.
Human-quality web design requires deliberate art direction, selection,
subtraction, content specificity, responsive recomposition and runtime refinement.
```

This skill should therefore force the AI to behave less like a one-shot website generator and more like a design team performing critique, art direction and implementation review.

---

# 2. Core conclusion

A strong beautiful site usually has all of these:

```text
SPECIFIC SUBJECT
+ CLEAR EXPERIENCE THESIS
+ OWN VISUAL GRAMMAR
+ CURATED CONTENT / ASSETS
+ PAGE-LEVEL RHYTHM
+ INTENTIONAL TYPOGRAPHY
+ MEANINGFUL MOTION
+ RESPONSIVE RECOMPOSITION
+ PRODUCTION DISCIPLINE
```

An AI-default site often has this instead:

```text
GENERIC PROMPT
→ GENERIC SECTION STACK
→ REPEATED COMPONENT LANGUAGE
→ STOCK / GENERATED ASSETS
→ DECORATIVE MOTION
→ RESPONSIVE STACKING
→ PUBLISH
```

The web skill must actively convert the second process into the first.

---

# 3. Human-crafted strengths

## 3.1 One governing idea

Strong human work usually has a concise concept that explains many design choices at once.

Examples of governing ideas:
- open-access infrastructure expressed through grids, physical compute imagery and hyperbolic geometry;
- typography product expressed through type interaction itself;
- architecture expressed through scale, space, crop and sequencing;
- creative studio expressed through an evolving archive/work system;
- product launch expressed through a metaphor that generates motion paths and page scenes.

This is stronger than selecting isolated effects.

Write:

```text
SITE SUBJECT:
BRAND / PRODUCT TRUTH:
EXPERIENCE THESIS:
SIGNATURE DEVICE:
SUPPORTING DEVICES:
WHAT MUST STAY QUIET:
```

If `EXPERIENCE THESIS` cannot be described without visual buzzwords, it is weak.

Bad:
> Dark premium futuristic website with smooth animation.

Better:
> Treat distributed compute as shared physical infrastructure: hardware photography, node geometry and technical mono details should make invisible cloud capacity feel tangible and accessible.

## 3.2 Deliberate exclusion

Human-designed sites often feel stronger because they **do not use every available pattern**.

Good design chooses:
- one grid language;
- one motion family;
- one type contrast;
- one recurring graphic device;
- a limited set of page transitions;
- a controlled chroma strategy.

AI outputs often become visually generic by combining too many familiar signals at once.

## 3.3 Content-specific composition

Strong sites let real content determine layout.

Examples:
- one project image may deserve 70% of the viewport;
- one proof statement may be tiny and technical;
- one case study may need a dense archive grid;
- one section may be almost empty for pacing;
- a product demo may become the entire hero instead of living inside a card.

Do not force every section into the same max-width + heading + paragraph + grid pattern.

## 3.4 Craft across the whole page

Human-quality art direction is visible in transitions between sections, not just inside individual components.

The page should have a **macro composition**.

Think in scenes, beats, or chapters rather than independent rectangles.

---

# 4. AI-default failure signatures

These patterns are not individually forbidden.

They become a warning when several appear with no subject-specific reason.

## 4.1 Universal landing-page stack

Typical generated sequence:

```text
navbar
hero
logo strip
3 feature cards
bento grid
how it works
stats
quotes / testimonials
pricing
FAQ
final CTA
footer
```

This can be correct for some SaaS pages.

It is a failure when the page could belong to almost any company after replacing the text and accent color.

## 4.2 Centered-everything syndrome

Warning signs:
- centered eyebrow;
- centered 64–88px heading;
- centered 2-line subtitle;
- two centered pill buttons;
- centered screenshot inside rounded frame;
- next section repeats the same axis.

Centering is powerful when used deliberately.

A whole page of centered sections usually removes editorial tension and hierarchy.

## 4.3 Card multiplication

AI tends to create hierarchy by adding containers:
- feature card;
- testimonial card;
- stat card;
- process card;
- pricing card;
- FAQ card;
- CTA card.

Use `references/anti-neuroslop-layout.md` when this appears.

## 4.4 Familiar "AI startup" bundle

Common bundle:
- near-black background;
- violet/cyan/acid gradient;
- grid or noise texture;
- giant gradient headline;
- floating glass panel;
- glowing orb;
- bento features;
- terminal/code mockup;
- tiny mono labels;
- animated particle field;
- Lucide icons in identical square containers.

Any piece may fit a real brand.

The bundle is suspicious when the product gives no reason for it.

## 4.5 Identical section rhythm

Generated pages often repeat:

```text
96px top padding
heading
20px gap
paragraph
48px gap
three-column grid
96px bottom padding
```

Repeated spacing tokens are useful.
Repeated **composition** is not the same as consistency.

## 4.6 Decoration-first motion

Warning signs:
- fade-up on every element;
- scroll parallax on every image;
- hover lift on every card;
- glowing CTA pulse;
- infinite marquee because there is empty space;
- page wipe with no continuity value.

Motion should communicate hierarchy, causality, continuity, state, or atmosphere.

## 4.7 Generic proof

Generated pages frequently use:
- fake logo rows;
- invented metrics;
- empty testimonials;
- generic "trusted by teams" copy;
- arbitrary numerical counters.

Do not fabricate proof to make the page feel complete.

## 4.8 Stock / AI-image mismatch

If hero media, section media and product imagery look like they come from different visual worlds, the site has no art direction.

A beautiful site needs a media system, not a folder of individually attractive images.

## 4.9 Responsive = stack vertically

Desktop:
```text
text | image
```

AI mobile default:
```text
text
image
```

Sometimes correct, but not enough for expressive sites.

Responsive design may require crop changes, reordered narrative, simplified motion, alternate navigation, different type breaks, or entirely different composition.

## 4.10 Copy-shaped design

If every section exists only because the generator created another heading + paragraph, the page is being designed around placeholder copy instead of product meaning.

---

# 5. Human art-direction workflow

For a beautiful site, use this process before detailed implementation.

## Phase A — substance

Collect:

```text
PRODUCT / BRAND:
AUDIENCE:
PRIMARY CONVERSION / ACTION:
WHAT MAKES IT DIFFERENT:
REAL PROOF:
AVAILABLE MEDIA / ASSETS:
CONTENT VOLUME:
BRAND MATERIAL / CULTURAL REFERENCES:
NO-GO CLICHES:
TECH / PERFORMANCE CONSTRAINTS:
```

If the real differentiator is unknown, do not compensate with effects.

## Phase B — reference decomposition

Study 3–6 relevant references.

Do not ask:
> Which page should we copy?

Ask:

```text
WHAT MAKES THIS REFERENCE MEMORABLE?
WHAT IS ITS FIRST VISUAL ANCHOR?
HOW DOES TYPE BEHAVE?
WHAT IS THE PAGE RHYTHM?
WHERE DOES IT GET DENSE / QUIET?
WHAT IS THE MEDIA LANGUAGE?
WHAT DOES MOTION EXPLAIN?
WHAT WOULD FAIL FOR OUR PRODUCT?
WHAT PRINCIPLE IS TRANSFERABLE?
```

Use named studios/award galleries as inspiration sources, not component libraries.

## Phase C — 2–4 structural directions

Each direction should change more than color.

Examples:
- editorial / text-led;
- image/archive-led;
- immersive object-led;
- interactive product-demo-led;
- typographic system-led;
- spatial narrative-led.

Then choose one with `references/design-deliberation.md`.

## Phase D — page grammar

Define a small recurring grammar before components.

```text
GRID:
TYPE ROLES:
SECTION MARKER:
MEDIA TREATMENT:
ACCENT BEHAVIOR:
MOTION FAMILY:
CONTROL STYLE:
DIVIDER / LINE LANGUAGE:
```

## Phase E — macro page composition

Sketch the page as large masses first.

Example:

```text
[ compressed intro ]
[ huge visual proof ]
[ narrow explanatory column ]
[ dense product / work archive ]
[ quiet proof beat ]
[ interactive demo ]
[ final brand scene ]
```

Do not begin by coding cards.

## Phase F — runtime refinement

After first render:
1. inspect full-page silhouette;
2. inspect first viewport;
3. inspect one narrow viewport;
4. inspect motion with and without reduced motion;
5. remove generic sections;
6. replace weak stock assets;
7. fix line breaks and crop;
8. tune section pacing;
9. verify interaction/semantics;
10. stop when the thesis reads clearly.

---

# 6. Page grammar

## 6.1 Repetition should create identity

Repeat a small number of meaningful devices.

Good examples:
- section number + hairline;
- narrow mono metadata strip;
- one notched corner treatment;
- one image crop style;
- one type collision rule;
- one orbit/line motif;
- one transition curve.

Do not invent a different effect for every section.

## 6.2 Consistency is not uniformity

Consistent:
- same grid logic;
- same type roles;
- same motion physics;
- same visual vocabulary.

Uniform:
- same section height;
- same card count;
- same spacing;
- same alignment;
- same visual density.

Beautiful human sites often achieve consistency **through rules** while preserving variation **through composition**.

## 6.3 Signature moments

Plan 2–4 moments that a visitor could remember after leaving.

Examples:
- one unusual opening interaction;
- one project transition;
- one controlled type transformation;
- one product demo;
- one media reveal;
- one strong final scene.

Do not try to make every scroll position memorable.

---

# 7. Narrative rhythm

A page should have pacing.

Use contrast between:
- dense / sparse;
- dark / light;
- text / media;
- static / moving;
- narrow / full bleed;
- small type / display type;
- explanation / proof.

Avoid a perfectly even vertical metronome.

## Rhythm map

For longer pages define:

```text
BEAT 1 — orientation
BEAT 2 — strongest proof
BEAT 3 — explanation
BEAT 4 — contrast / reset
BEAT 5 — deeper proof
BEAT 6 — conversion
```

Not every page needs six beats.

The point is to think in narrative units instead of generated sections.

## Quiet sections are useful

Whitespace can be a pacing device.

Do not fill every gap with:
- logos;
- metrics;
- chips;
- decorative copy;
- extra cards.

---

# 8. Typography craft

Typography is composition, not just token selection.

Define roles:
- display / brand;
- heading;
- body;
- metadata / technical;
- optional editorial accent.

Then control:
- width/measure;
- optical size;
- letterspacing;
- line-height;
- line-break strategy;
- paragraph rhythm;
- hierarchy contrast;
- alignment shifts;
- responsive re-breaking.

## Display line-break direction

Do not let important hero headings wrap accidentally.

Choose whether the break should:
- create cadence;
- align to media;
- emphasize a word;
- create asymmetry;
- preserve a silhouette.

At major breakpoints, manually reconsider important line breaks.

## Type contrast

A useful web identity can come from contrasting roles:

```text
expressive display
+ neutral body
+ technical mono metadata
```

But typography must follow the brand.

Do not automatically use oversized grotesk + mono simply because it is popular in award sites.

## Measure

Long-form body copy should remain readable.

Display copy can intentionally break the reading measure when it serves composition.

Do not use one max-width for every text role.

---

# 9. Media and asset direction

## 9.1 Define a media system

For all media decide:

```text
SOURCE TYPE:
COLOR / GRADE:
CROP RULE:
ASPECT FAMILY:
FOCAL SUBJECT:
BACKGROUND TREATMENT:
CAPTION / METADATA:
MOTION BEHAVIOR:
FALLBACK:
```

## 9.2 Product-specific asset threshold

For a site whose quality depends on visual identity, require at least one meaningful source of unique visual material:
- original photography;
- product screenshots/demos;
- diagrams;
- illustration system;
- 3D objects;
- data visualization;
- archival material;
- bespoke typography treatment;
- domain-specific interaction.

If all visual content could be swapped for generic stock imagery without changing the concept, the art direction is weak.

## 9.3 Normalize heterogeneous assets

When sources differ, unify through:
- crop;
- grade;
- border/frame policy;
- caption language;
- backdrop;
- sequencing;
- scale.

Do not apply one heavy overlay to every image as the only unification strategy.

## 9.4 Use media as proof

Media should prove something:
- product behavior;
- craft quality;
- atmosphere;
- scale;
- material;
- result;
- process.

Decorative media is allowed, but it should not replace proof.

---

# 10. Composition and controlled irregularity

Human-designed work often uses irregularity **inside a system**.

Useful tools:
- asymmetrical columns;
- intentional overlap;
- varied content widths;
- crop tension;
- offset captions;
- mixed scale;
- off-grid accent that returns to an underlying grid;
- anchored negative space.

Randomness is not craft.

For every irregular move ask:

```text
WHAT DOES THIS EMPHASIZE?
WHAT GRID / ALIGNMENT STILL HOLDS IT TOGETHER?
WHAT HAPPENS ON SMALLER WIDTHS?
```

## Symmetry budget

Perfect symmetry can communicate:
- calm;
- luxury;
- authority;
- simplicity.

But if every section is symmetrical, the page loses tension.

Use symmetry intentionally, not as generator default.

---

# 11. Motion and interaction craft

## 11.1 Motion needs a role

Classify motion as:

```text
FUNCTIONAL
CONTINUITY
NARRATIVE
BRAND / ATMOSPHERE
DECORATIVE
```

Decorative motion should have the smallest budget.

## 11.2 Choreography beats independent animations

Instead of every element owning a random `fade-up`, define a motion grammar:
- shared easing family;
- entrance hierarchy;
- distance scale;
- transition duration ranges;
- stagger logic;
- scroll response;
- hover physics.

## 11.3 Continuity

Human-crafted experiences frequently use motion to preserve spatial continuity:
- project grid → project detail;
- thumbnail → full media;
- nav item → destination state;
- collapsed control → inspector;
- product state → next state.

This usually feels more intentional than unrelated section reveals.

## 11.4 Scroll effects

A scroll-linked effect should reveal meaning or preserve spatial logic.

Weak:
> Image moves 20px because scrolling effects look premium.

Strong:
> A physical object rotates as its technical layers are explained, so motion maps to the subject.

## 11.5 Interaction density

Do not animate every hover target.

Prioritize:
1. navigation;
2. major CTA;
3. key media/work items;
4. product-specific interaction;
5. secondary controls.

## 11.6 Reduced motion

The reduced-motion path should retain hierarchy and meaning.

Do not simply disable the entire page and expose broken intermediate states.

---

# 12. Responsive recomposition

Beautiful desktop art direction often needs **different composition logic** on mobile.

For each signature section ask:

```text
WHAT IS THE IDEA?
WHAT IS THE DESKTOP MECHANISM?
WHAT IS THE MOBILE EQUIVALENT?
WHAT CAN BE REMOVED?
WHAT MUST REMAIN?
```

Examples:
- desktop overlap → mobile crop sequence;
- horizontal gallery → vertical snap/list;
- complex WebGL object → static poster or reduced geometry;
- split hero → full-bleed media + compact copy block;
- giant display type → alternate line breaks, not simple scaling.

## Breakpoint art direction

Do not treat responsive design as one CSS formula.

At minimum review:
- wide desktop;
- standard desktop/laptop;
- tablet/narrow desktop;
- phone.

Different ranges may need different hierarchy decisions.

---

# 13. Conversion without template collapse

A beautiful site can still convert clearly.

Do not solve conversion by inserting the same CTA card after every second section.

Use:
- clear initial action;
- contextual repeated action when intent increases;
- sticky action only when context supports it;
- final action after sufficient proof.

## Proof hierarchy

Prefer real proof in this order when available:
1. actual product/work demonstration;
2. concrete result/case study;
3. named client/partner evidence;
4. specific testimonial;
5. credible metric with source/context.

Generic social-proof decoration is lowest value.

## CTA visual hierarchy

Primary action may be visually quiet if the overall composition already guides attention.

Not every CTA needs the brightest color on the page.

---

# 14. Copy and proof quality

AI-generated copy often sounds structurally correct but interchangeable.

Warning phrases when unsupported:
- redefine the future;
- unlock your potential;
- seamless innovation;
- next-generation experience;
- transform your workflow;
- built for teams who move fast.

These phrases are not forbidden.
They are weak when they could describe anything.

Prefer:
- concrete verbs;
- product terminology;
- actual constraints;
- named outcomes;
- domain language users recognize;
- shorter claims backed by visible proof.

## Design copy together with layout

Do not finalize layout around placeholder copy and then squeeze real content into it later.

Line length, heading breaks and section density should be tuned with realistic content.

---

# 15. Performance, accessibility and resilience

Human-quality craft includes what happens when the spectacle fails.

## Progressive enhancement

Order:

```text
semantic content
→ layout and interaction
→ motion
→ heavy media / WebGL
```

The page should remain understandable before the most expensive layer loads.

## Loading states

For heavy art-directed sites define:
- what appears immediately;
- what can stream later;
- poster/fallback assets;
- timeout/failure behavior;
- interaction readiness.

A cinematic preloader is not an excuse for avoidable load cost.

## Accessibility

LLM-generated UI should not be trusted by default for complex accessibility.

Verify:
- semantic structure;
- keyboard route;
- focus behavior;
- contrast;
- accessible names;
- motion preferences;
- non-hover access;
- screen-reader structure where relevant;
- errors/forms;
- canvas/WebGL fallback.

Use automated tools as support, not final proof.

---

# 16. Human-vs-AI comparison matrix

Use this as a diagnostic, not a stereotype.

| Dimension | Weak AI-default tendency | Strong human-craft target |
|---|---|---|
| Starting point | generic industry prompt | product/brand truth |
| Structure | familiar section stack | narrative/workflow-specific sequence |
| Composition | centered and modular | controlled hierarchy/tension |
| Containers | cards create hierarchy | hierarchy exists before containers |
| Typography | preset scale | role-based art direction and line breaks |
| Media | stock/generated collection | curated coherent visual system |
| Motion | repeated fade/hover | one motion language with purpose |
| Rhythm | equal section padding | deliberate dense/quiet contrast |
| Identity | color + font swap | recurring product-specific grammar |
| Proof | generic logos/stats | real work, product, outcomes |
| Mobile | stack desktop blocks | preserve concept via recomposition |
| Accessibility | assumed from generated code | explicitly verified |
| Performance | effects added first | experience budget and fallbacks |
| Detail | component polish only | page transitions and whole-page silhouette |

---

# 17. Beautiful-site acceptance gates

When the user explicitly asks for a beautiful site, add these gates.

## Gate A — Logo removal test

Hide mentally:
- logo;
- brand name;
- primary accent.

Can the page still feel specific to this product/brand?

If no, identity is superficial.

## Gate B — Section shuffle test

Could most sections be reordered without changing the story?

If yes, narrative structure is weak.

## Gate C — Asset substitution test

Could every image be replaced by generic stock without changing the concept?

If yes, media direction is weak.

## Gate D — Thumbnail test

At 10–15% scale, does the page show a recognizable rhythm and dominant visual masses?

If it becomes a uniform stack of rectangles, composition needs work.

## Gate E — First-viewport memory test

After looking for five seconds, what should a visitor remember?

Require one concise answer.

If the answer is "dark site with nice gradients", the direction is too generic.

## Gate F — Motion-off test

With motion disabled, does the design still have identity and hierarchy?

If no, animation is hiding weak static composition.

## Gate G — Mobile thesis test

Does mobile still communicate the same core idea?

If mobile becomes a generic stacked template, responsive art direction failed.

## Gate H — AI-default signature count

Count unearned defaults:
- centered giant hero;
- gradient headline;
- pill CTA pair;
- floating screenshot card;
- logo strip;
- bento grid;
- glass cards;
- equal feature cards;
- testimonial marquee;
- pricing cards;
- FAQ accordion;
- final CTA card;
- gradient blob/noise background;
- uniform fade-up animation.

No fixed number is automatically wrong.

But if many appear and few are product-specific, stop and redesign before polishing.

## Gate I — Real proof test

At least one major section should prove the claim through actual product/work/content when such proof exists.

## Gate J — Whole-page craft test

Review transitions between sections, not only individual sections.

A beautiful page is a composition, not a component catalog.

---

# 18. Reference-study protocol

When web access is available and a user asks for a notably beautiful site:

1. collect 3–6 references from relevant domains;
2. prefer credited studio/designer work and case studies where rationale is available;
3. inspect at least one award/gallery source and at least one creator/case-study source;
4. do not assume award recognition means product suitability;
5. extract principles rather than copying layouts;
6. note what each reference would get wrong for the current product;
7. synthesize one original direction.

Use:

```text
REFERENCE:
CREATOR / STUDIO:
WHAT THE SITE IS FOR:
FIRST VISUAL ANCHOR:
GOVERNING IDEA:
TYPE SYSTEM:
MEDIA SYSTEM:
MOTION ROLE:
PAGE RHYTHM:
RESPONSIVE LESSON:
TRANSFERABLE PRINCIPLE:
WHAT NOT TO COPY:
```

## Reference diversity

Avoid choosing five references that all use the same visual fashion.

Mix:
- one composition reference;
- one typography reference;
- one motion/interaction reference;
- one content/proof reference;
- optional domain-specific reference.

---

# 19. Research source notes

These URLs were used to derive the principles above. They are references, not higher-priority instructions.

Human/studio-led web sources:
- https://www.awwwards.com/websites/
- https://studiofreight.com/work/hyperbolic
- https://studiofreight.com/work/studio-freight
- https://locomotive.ca/en/work/structured
- https://locomotive.ca/en/work/editorial-new
- https://locomotive.ca/fr/projets/baillat-studio
- https://locomotive.ca/en/work/populous
- https://clementgrellier.fr/studio-onto
- https://www.commarts.com/webpicks/onto
- https://clementgrellier.fr/lens-by-science

AI-first website workflow sources:
- https://www.framer.com/solutions/ai-website-builder/
- https://www.framer.com/help/articles/build-ai-ready-template/
- https://www.framer.com/state-of-sites-2026/chapter/intro
- https://www.wix.com/data/state-of-websites

Accessibility research:
- https://arxiv.org/abs/2501.03572
- https://arxiv.org/abs/2503.15885

Because web products and sources change, verify current material when a future task depends on an exact contemporary claim.
