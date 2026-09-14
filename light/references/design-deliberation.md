# Design Deliberation and Direction Selection

## Purpose

Use this reference for non-trivial redesigns or whenever several plausible visual/structural directions could solve the same problem.

The goal is not to generate many pretty concepts. The goal is to avoid committing to the first plausible idea before checking whether a better direction exists.

Do not use this process for a tiny local fix whose direction is already obvious.

## Core rule: explore before commitment

For meaningful design work, produce **2–4 materially different candidate directions** before selecting one.

The candidates must differ in governing strategy, not just color or radius.

Useful axes of difference include:
- information density;
- composition and visual anchor;
- navigation model;
- workspace vs presentation emphasis;
- typography character;
- imagery/media role;
- interaction model;
- brand intensity;
- motion intensity;
- action hierarchy;
- progressive disclosure;
- platform convention vs custom expression.

Bad concept divergence:
- Concept A = blue;
- Concept B = purple;
- Concept C = green.

Good concept divergence:
- A = dense operational workspace with quiet chrome;
- B = split-view workspace with contextual inspector;
- C = command-first interface with progressive disclosure.

## Candidate contract

For every serious candidate, state:

```text
DIRECTION NAME:
CORE IDEA:
PRIMARY VISUAL ANCHOR:
PRIMARY ACTION MODEL:
LAYOUT / IA CHANGE:
TYPOGRAPHY / COLOR CHARACTER:
MOTION / MEDIA ROLE:
WHY IT FITS THIS PRODUCT:
MAIN ADVANTAGE:
MAIN RISK:
IMPLEMENTATION COST: low / medium / high
```

A direction without a clear product reason is not a valid candidate.

## Decision criteria

Score or compare candidates against the actual task, not generic taste.

Default criteria:

1. **Product fit** — does the direction arise from the product's real workflow, subject, audience, and data?
2. **Task clarity** — can the user understand what matters and what to do next?
3. **Hierarchy** — do visual mass and action prominence match importance?
4. **Identity** — is the result recognizable without depending only on logo, color, or hero image?
5. **State clarity** — can users understand loading, selection, errors, progress, success, and disabled conditions?
6. **Accessibility** — can the direction support keyboard, focus, contrast, motion preferences, and semantic structure?
7. **Responsive/platform fit** — does it survive the required devices and conventions?
8. **Implementation risk** — does it preserve real behavior and avoid unnecessary rewrites?
9. **Maintainability** — can the design be expressed through coherent tokens/components rather than exceptions?
10. **Performance cost** — are heavy media, motion, WebGL, large assets, or runtime work justified?

Not every task needs all ten. Weight what matters to the user.

## Selection rule

Choose the direction with the strongest **overall product outcome**, not the one with the most visual novelty.

After selection, record:

```text
SELECTED DIRECTION:
WHY THIS ONE:
WHY NOT THE STRONGEST ALTERNATIVE:
TRADEOFF ACCEPTED:
WHAT MUST STAY QUIET:
WHAT CREATES IDENTITY:
WHAT MUST BE PROVEN IN RUNTIME:
```

This explanation is required for meaningful REDESIGN work unless the user already chose the direction.

## Dominant idea budget

A strong interface usually benefits from one dominant design idea and a small number of supporting ideas.

Examples:
- one dominant editorial grid + restrained accent motion;
- one immersive media treatment + conventional navigation;
- one dense command/workspace model + quiet visual identity;
- one recurring section-marker grammar + disciplined image treatment.

Do not let every section invent a new visual language.

## Recurrent visual grammar

Build identity through repeated rules, not repeated decoration.

Useful repeated grammar can include:
- consistent section markers;
- one typographic contrast pattern;
- one image treatment;
- one accent behavior;
- one corner/cut/notch motif;
- one technical metadata style;
- one motion easing family.

A repeated motif is valuable only when it reinforces product character and improves recognition or structure.

## Attention budget

Treat user attention as finite.

At a given moment, prefer:
- one dominant action;
- one dominant visual anchor;
- limited active animation;
- supporting content with lower contrast/motion.

Continuous motion, blinking indicators, marquee, animated counters, pulsing CTAs, auto-advancing media, parallax, and hover effects all spend attention.

If several are active together, require a clear hierarchy and product reason.

## Contextual persistence

Persistent UI should appear because the user's context justifies it.

A strong pattern is a CTA or control that:
- is visible while the related primary action is otherwise off-screen;
- disappears when the user reaches the destination/action surface;
- does not cover important content;
- remains dismissible/non-obstructive when appropriate.

Do not keep a sticky CTA permanently visible merely because conversion is important.

## Autonomous media contract

Auto-advancing hero reels, carousels, audio, animated stories, video, and similar autonomous media need explicit state.

When relevant provide:
- visible current position/chapter;
- progress indication if timing matters;
- pause/stop or user control;
- mute/audio state;
- manual navigation;
- input-equivalent behavior for mouse, touch, keyboard;
- reduced-motion behavior;
- fallback if media fails.

Autonomous media must never become the only way to access information.

## Cross-input equivalence

Do not design essential disclosure only for `:hover`.

If a card flips, reveals, expands, or exposes controls on hover, provide equivalent:
- click/tap behavior;
- keyboard focus/activation;
- visible affordance;
- accessible semantics.

Mouse, touch, and keyboard do not need identical mechanics, but they need equivalent access to the same information and actions.

## Semantic-control rule

If something behaves like a button, tab, radio option, disclosure, or link, use the correct semantic control or implement equivalent semantics completely.

Do not use a clickable `span`/`div` merely because it is easier to style.

This matters especially for:
- pill selectors;
- carousel controls;
- flip/reveal cards;
- custom tabs;
- mute/play controls;
- selectable filters.

## Success-state integrity

Do not show successful submission, booking, save, purchase, connection, or completion until the underlying operation actually succeeded.

UI prototypes may simulate behavior, but production guidance must distinguish simulated success from real backend success.

Do not clear user input before a real successful result unless the product contract explicitly calls for it.

## Reference extraction rule

When learning from a strong reference page, separate:

```text
TRANSFERABLE PRINCIPLE
from
REFERENCE-SPECIFIC STYLING
```

For example:
- transferable: one accent color controls interactive emphasis;
- specific: orange accent itself;
- transferable: grayscale media creates a unified content field;
- specific: gym/noir imagery;
- transferable: contextual sticky CTA appears after the hero and hides at the booking surface;
- specific: the exact conversion copy;
- transferable: role-based typography differentiates display/body/technical metadata;
- specific: the exact font families.

Never copy the subject-specific styling when only the principle is useful.

## Reference-role mapping

When references are needed, first state the uncertainty, then choose the source role that can resolve it. For web work, `web-reference-corpus.md` distinguishes art-direction, product-flow, typography, case-study and implementation evidence.

A candidate direction should cite the transferable mechanism, not merely a visual resemblance. Reject a direction whose identity depends on mixing unrelated fashionable motifs.

## Final selection check

Before implementation ask:

- Is this direction better than the strongest alternative for a stated reason?
- Can I explain why the structure fits this product?
- Is the identity carried by system-level decisions rather than decorative add-ons?
- Is there one clear attention hierarchy?
- Are interaction and responsive costs acceptable?
- Can the design be implemented without breaking product behavior?
- What evidence after implementation would prove the choice was correct?

If these cannot be answered, the design direction is not ready.
