# Design Deliberation

Use this reference for meaningful `REDESIGN`, new-product UI direction, or any task where several materially different structures could plausibly solve the same problem.

Do not use it to manufacture variants for tiny fixes.

## Contents

- Purpose
- When deliberation is required
- When to skip it
- Problem framing
- Candidate-generation rules
- Structural divergence axes
- Evidence-driven comparison
- Decision matrix
- Strongest-alternative test
- Design rationale contract
- Product-specificity test
- Attention-budget test
- Implementation-risk test
- Runtime proof
- Reference extraction
- Anti-patterns
- Output contract

## Purpose

The goal is not “generate three pretty designs.”

The goal is to avoid prematurely committing to the first acceptable layout.

A strong design agent should:
1. understand the product problem;
2. generate a small set of genuinely different solution models;
3. compare them using the product's real constraints;
4. choose one;
5. explain why it is the best fit;
6. acknowledge the strongest rejected alternative and the tradeoff accepted;
7. implement and verify the selected direction.

Design quality comes from **selection among good alternatives**, not from polishing the first idea.

## When deliberation is required

Use deliberate alternatives when:
- the user asks for redesign rather than a local refinement;
- information architecture is weak or unclear;
- several workflow structures are plausible;
- the product lacks a clear visual/product thesis;
- the existing layout is generic and a stronger product-specific structure is needed;
- navigation, density, composition, or primary action hierarchy may materially change;
- an expressive/brand-led surface could be built around several different experience concepts;
- the agent is creating a new important surface from scratch.

## When to skip it

Skip broad alternatives when:
- the user already selected/approved a direction;
- acceptance criteria define the layout tightly;
- the task is one localized bug or state fix;
- a platform convention clearly determines the correct structure;
- exploration would only produce cosmetic variants;
- the extra decision work would not change implementation.

Do not argue against an explicitly accepted direction unless it creates a material usability, accessibility, security, or preservation failure.

## Problem framing

Before candidates:

```text
PRODUCT:
TARGET USERS:
PRIMARY JOB:
HIGH-FREQUENCY ACTION:
CURRENT FAILURE:
EVIDENCE:
MUST PRESERVE:
ALLOWED TO CHANGE:
PLATFORM:
CONTENT / DATA SHAPE:
INPUT METHODS:
RESPONSIVE / WINDOW CONSTRAINTS:
IDENTITY TO PRESERVE:
UNKNOWN:
BLOCKED:
```

Then state the actual design question in one sentence.

Bad:
> Make the dashboard look more modern.

Better:
> How should a repeated-use controller utility expose live input state, high-frequency tuning controls, and advanced mapping without turning the dashboard into a generic card grid?

The question should constrain candidate generation.

## Candidate-generation rules

Generate **2–4 serious candidates**.

Two is enough when the design space is narrow.
Three is usually ideal.
Four is acceptable for a genuinely open problem.

Do not generate more merely to appear thorough.

Every candidate must be valid enough that it could realistically be chosen.

Do not include one intentionally bad option to make the preferred option look stronger.

## Cosmetic variation is not structural divergence

These are NOT separate directions:

```text
Direction A = blue
Direction B = purple
Direction C = orange
```

or:

```text
A = 12px radius
B = 16px radius
C = glass cards
```

They share the same product model.

Candidates should differ in one or more governing dimensions.

## Structural divergence axes

Useful axes include:

### Information architecture
- task-first;
- object-first;
- mode-first;
- timeline/history-first;
- workspace + inspector;
- command-first.

### Navigation
- sidebar;
- top-level tabs;
- drill-down hierarchy;
- command palette + contextual navigation;
- split navigation/workspace;
- single-surface progressive disclosure.

### Density
- compact professional workspace;
- balanced application UI;
- spacious guided experience.

### Primary work model
- list + details;
- canvas + inspector;
- queue + contextual controls;
- dashboard + drill-down;
- direct manipulation;
- wizard/step flow;
- persistent workspace.

### Action hierarchy
- one persistent primary action;
- contextual actions by selection;
- command bar;
- bottom action shelf;
- inline actions;
- keyboard/shortcut-led workflow.

### Product identity
- typography-led;
- data/instrument-led;
- material/media-led;
- domain-diagram-led;
- motion-led;
- restrained native/productivity identity.

### Motion
- nearly static;
- functional transitions only;
- moderate spatial continuity;
- expressive narrative motion.

### Responsive adaptation
- reflow;
- collapse;
- mode switch;
- inspector-to-sheet transformation;
- table-to-list;
- multi-pane-to-stack.

Use only axes that fit the product.

## Candidate card

For each direction record:

```text
DIRECTION:
ONE-SENTENCE THESIS:
STRUCTURE:
PRIMARY ACTION MODEL:
PRIMARY CONTENT MODEL:
NAVIGATION:
DENSITY:
IDENTITY DEVICE:
MOTION LEVEL:
RESPONSIVE / WINDOW STRATEGY:
WHAT STAYS QUIET:
WHY IT FITS:
MAIN RISK:
IMPLEMENTATION COST / RISK:
```

This prevents vague “mood board” concepts with no workflow.

## Evidence-driven comparison

Compare candidates against the actual product, not personal taste.

Recommended dimensions:

```text
TASK FIT
WORKFLOW EFFICIENCY
STATE CLARITY
INFORMATION HIERARCHY
PRODUCT SPECIFICITY
DISCOVERABILITY
SCALABILITY
RESPONSIVE / WINDOW FIT
ACCESSIBILITY
PLATFORM FIT
IMPLEMENTATION RISK
PRESERVATION RISK
IDENTITY STRENGTH
MOTION / ATTENTION COST
```

Not every dimension needs equal weight.

For repeated-use utilities, weight:
- task fit;
- efficiency;
- state clarity;
- density;
- platform fit.

For marketing/expressive surfaces, identity and narrative may receive more weight.

## Decision matrix

A lightweight scoring table may use:

```text
1 = poor
2 = weak
3 = acceptable
4 = strong
5 = excellent
```

But do not pretend numeric scoring is objective proof.

Use scores only to expose tradeoffs.

Always accompany a score with evidence or rationale.

Example:

```text
Direction A
Task fit: 5 — high-frequency actions stay visible.
Product specificity: 4 — controller diagram becomes the governing workspace.
Responsive fit: 3 — inspector requires a mobile/small-window transformation.
Implementation risk: 3 — moderate SVG interaction complexity.
```

## Strongest-alternative test

After selecting a direction, identify the **strongest rejected alternative**.

Ask:
- What did it do better?
- Why is that advantage less important here?
- What tradeoff are we accepting?
- Is there one useful principle from it that can be safely incorporated without collapsing the distinction?

This reduces confirmation bias.

Do not merge every good idea from every direction.
That usually creates a hybrid with no thesis.

## Design rationale contract

Before implementation:

```text
SELECTED DIRECTION:
WHY THIS ONE:
WHY IT FITS THIS PRODUCT:
WHY IT FITS THESE USERS:
WHY IT FITS THIS PLATFORM:
WHY NOT THE STRONGEST ALTERNATIVE:
TRADEOFF ACCEPTED:
WHAT CREATES IDENTITY:
WHAT MUST STAY QUIET:
WHAT MUST BE PRESERVED:
WHAT MUST BE PROVEN IN RUNTIME:
```

If these answers are vague, the direction is not ready.

## Product-specificity test

Hide or mentally remove:
- logo;
- product name;
- hero art;
- branded slogans.

Ask:

> Could this exact structure be relabeled for several unrelated products with almost no change?

If yes, improve specificity through:
- workflow;
- domain controls;
- real data/state;
- diagrams/instruments;
- terminology;
- content hierarchy;
- action model;
- meaningful product media.

Do not solve genericity with random texture or decoration.

## Attention-budget test

Every moving/bright/persistent element spends attention.

Count attention-demanding mechanisms:
- autoplay media;
- marquee;
- blinking live state;
- pulsing CTA;
- animated counters;
- large motion;
- parallax;
- auto-advancing carousel;
- sticky CTA;
- high-chroma accents.

A composition may contain several mechanisms, but they cannot all be co-primary.

For each viewport/state identify:

```text
PRIMARY ATTENTION TARGET:
SECONDARY MOTION:
BACKGROUND / QUIET MOTION:
SUPPRESSED / PAUSED WHEN:
```

If several elements compete continuously, reduce or pause some of them.

## Implementation-risk test

A visually stronger direction may still be wrong if it:
- breaks existing behavior;
- requires rewriting unrelated business logic;
- cannot adapt to required window sizes;
- has weak accessibility;
- relies on fragile custom controls;
- requires heavy motion/WebGL with no fallback;
- depends on fake/unavailable data.

Implementation risk is part of design quality.

Do not evaluate design in a vacuum.

## Runtime proof

After implementation, compare the selected direction in the actual product.

Verify:
- equivalent content/state;
- primary task;
- hierarchy;
- action clarity;
- keyboard/touch/pointer behavior as relevant;
- multiple important states;
- overflow;
- real text length;
- responsive/window size;
- theme;
- reduced motion if applicable.

A design rationale is a hypothesis until runtime evidence supports it.

## Reference extraction

When studying a reference site/app, separate:

```text
REFERENCE-SPECIFIC STYLING
TRANSFERABLE PRINCIPLE
PRODUCT FIT
ADAPTATION
WHAT NOT TO COPY
```

Example:

```text
Reference-specific:
black + orange + grayscale fitness imagery

Transferable:
normalize heterogeneous media into one art direction,
use local overlays for text-safe zones,
repeat a small visual grammar across sections

Adaptation:
apply those principles using the target product's own palette and subject matter
```

Do not turn one attractive reference into a universal style template.

## Recurrent visual grammar

Strong interfaces often repeat a small number of recognizable rules:
- section marker;
- metadata treatment;
- one image treatment;
- one accent behavior;
- one corner/line motif;
- one easing family;
- one typographic contrast;
- one diagram/instrument language.

Prefer 1–3 recurrent signature rules over a new visual trick in every section.

Repetition creates identity.
Variety without hierarchy creates noise.

## Contextual persistence

Persistent controls should appear because context makes them useful.

A sticky CTA/action is stronger when:
- the original CTA has left view;
- the target action is still relevant;
- the user is not already at the target;
- it does not cover essential content;
- it yields near the destination.

Do not make every primary action permanently sticky by default.

## Autonomous media contract

Any autoplay reel/carousel/video/audio should explicitly define:
- current state/chapter;
- progress where useful;
- pause/mute;
- manual navigation where useful;
- what happens during user interaction;
- whether autoplay resumes;
- reduced-motion behavior;
- keyboard/touch/pointer access;
- failure/loading fallback.

Autonomy without user control is not polish.

## Success integrity

Never communicate successful completion before the real operation succeeds.

For forms/actions:

```text
IDLE
→ VALIDATING
→ SUBMITTING
→ SUCCESS or FAILURE
```

Do not show a success toast merely because a local `submit` event fired.

If the example is a static prototype, label the success as simulated rather than treating it as production behavior.

## Semantic controls

Visual role and semantic role must agree.

Use:
- button for action;
- link for navigation;
- checkbox/switch for binary preference;
- radio/listbox/select for exclusive choice;
- tab for switching peer panels.

Do not turn `span`/`div` into fake controls when native/semantic controls fit.

If a custom control is required, implement keyboard, focus, role, state, and accessible naming explicitly.

## Cross-input equivalence

Hover cannot be the only way to reveal essential information or perform a required action.

For every hover interaction ask:
- keyboard equivalent?
- touch equivalent?
- controller/remote equivalent if relevant?
- visible discoverability without hover?

A flip/reveal card may keep hover as enhancement, but essential content must remain reachable by other inputs.

## Anti-patterns

Do not:
- present cosmetic variations as different concepts;
- choose a direction because it is the most fashionable;
- use “premium” as evidence;
- score candidates without rationale;
- merge all concepts into one overloaded hybrid;
- continue exploring after the user has clearly approved a direction;
- copy a reference site's palette/effects without product grounding;
- use autoplay, marquee, pulses, counters, and parallax simultaneously with no attention hierarchy;
- claim success without real backend success;
- rely on hover-only essential interaction;
- use fake semantic controls.

## Output contract

For meaningful redesign:

```text
PROBLEM FRAME:
CANDIDATES CONSIDERED:
COMPARISON:
SELECTED DIRECTION:
RATIONALE:
STRONGEST REJECTED ALTERNATIVE:
TRADEOFF:
PRESERVATION CONTRACT:
IMPLEMENTATION PLAN:
RUNTIME PROOF PLAN:
```

Keep the final user-facing explanation proportionate to the request.
The internal design process may be deeper than the final prose.


## Surface-model comparison

When comparing redesign directions, explicitly compare:
- number of persistent surfaces;
- independent rectangular enclosures;
- workspace area;
- chrome-to-content ratio;
- whether cards represent semantic boundaries;
- whole-screen silhouette;
- whether product-specific objects dominate over generic UI chrome.

Fewer containers are not automatically better.
More containers are not automatically worse.

The criterion is whether each surface helps explain or operate the product.


## Beautiful-web direction comparison

For brand/portfolio/campaign sites where visual quality is a primary goal, compare candidates on:
- governing idea clarity;
- page rhythm;
- product/brand specificity;
- media system strength;
- typographic identity;
- signature-moment quality;
- motion necessity;
- responsive recomposition potential;
- proof/conversion clarity;
- performance/accessibility cost;
- risk of falling into common AI-generated section patterns.

A more visually complex direction does not automatically score higher.

Prefer the direction with the strongest **coherent thesis per unit of complexity**.
